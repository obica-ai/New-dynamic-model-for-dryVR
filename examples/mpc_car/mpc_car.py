from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
import casadi as ca
# Source: https://thomasfermi.github.io/Algorithms-for-Automated-Driving/Control/BicycleModel.html
# MPC Car for Kinematic Model
#TODO how to eval Q and R
WB = 2.58
dt = 0.05
Q = [1,1,1,1]
R = [1,1,1,1]
t_p = []
delta_p = []
a_p = []
# Get the reference states from the trajectory
ref_x = 5
ref_y =  5
ref_theta = 0.0

ref_v = 1.0
global counter
counter = 0
def mpc_car_kinematic(init_x,int_u):
    # x, y ,theta ,v = init_x
    # acc,steer_w =   int_u

    x = init_x[0]
    y = init_x[1]
    theta =    init_x[2]
    v =     init_x[3]
    acc =   int_u[0]
    steer_w =   int_u[1]

    x_dot = x + v * np.cos(theta) * dt
    y_dot =  y + v * np.sin(theta) * dt
    theta_next = theta +  (v / WB)* np.tan(steer_w)* dt
    v_next =  v + acc*dt
    return ca.vertcat(x_dot, y_dot, theta_next, v_next)


def get_cost_function(states, controls, timebound):
    # TODO: Implement your cost function here
    # You can access the state variables x_vars, control variables u_vars,
    # and reference trajectory ref_trajectory to define your cost function
    # Use the opti object to define the cost function and any constraints
    # Return the cost function object
    cost = 0
    t = 0
    i = 0
    while t < timebound:

        x = states[0, i]
        y = states[1, i]
        theta = states[2, i]

        v = states[3,i]


        throttle = controls[0, i]
        delta = controls[1, i]
        # Penalize deviations from the reference states
        cost += Q[0]  *(x - ref_x) ** 2
        cost += Q[1]  *(y - ref_y) ** 2
        cost += Q[2] * (theta - ref_theta) ** 2

        cost += Q[3] * (v - ref_v)**2

        # Penalize large fluctuations in consecutive controls
        if i >= 1:
            cost += R[0] * throttle ** 2
            cost += R[1] * delta ** 2
            cost += R[2] * (throttle - controls[0, i - 1]) ** 2
            cost += R[3] * (delta - controls[1, i - 1]) ** 2
            
        t += dt
        i += 1
    return cost
def TC_Simulate(Mode,initialCondition,time_bound):
    time_step = dt;
    time_bound = float(time_bound)

    number_points = int(np.ceil(time_bound/time_step))
    t = [i*time_step for i in range(0,number_points)]
    if t[-1] != time_step:
        t.append(time_bound)
    newt = []
    for step in t:
        newt.append(float(format(step, '.2f')))
    total_t = newt
    # print(t)
    # Set up the optimization problem
    opti = ca.Opti()
    # kinematics model variables

    tsteps = int(time_bound/time_step)
    x_vars = opti.variable(4, tsteps + 1)  # State variables
    u_vars = opti.variable(2, tsteps) # Control variables
    
    # Set initial conditions
    x,y,theta,v = initialCondition
    opti.subject_to(x_vars[:, 0] == [x,y,theta,v])

    for t in range(int(time_bound)):
        # Model equations constraints
        #TODO objective function?
        x_next = mpc_car_kinematic(x_vars[:, t], u_vars[:, t])
        opti.subject_to(x_vars[:, t + 1] == x_next)
        # opti.subject_to(opti.bounded(-max_deceleration, u_vars[0, t], max_acceleration))
        # opti.subject_to(opti.bounded(min_wheel_angle, u_vars[1, t], max_wheel_angle))
        
    # Set the objective function
    #TODO two more var need to be consider in cost
    obj = get_cost_function(x_vars, u_vars,time_bound)
    
    opti.minimize(obj)
    # sol = odeint(mpc_car_kinematic, initialCondition, t, hmax=time_step)
    options = {
        'ipopt': {
        'max_iter': 20000,
        'tol': 1e-6,
        'dual_inf_tol': 1e-6,
        'constr_viol_tol': 1e-6,
        'acceptable_tol': 1e-5,  # Looser tolerance for accepting convergence
        'linear_solver': 'mumps',  # Robust linear solver
        'print_level': 0,  # Provides detailed output about solver progress and issues
        'hessian_approximation': 'limited-memory',  # Good for large-scale problems
        'derivative_test': 'first-order',  # Check derivatives (gradient) correctness63254
    }
}
    opti.solver('ipopt', options)
    try:
        sol = opti.solve()
        
        # Extract the optimal control inputs
        optimal_control = sol.value(u_vars)
        #print(optimal_control)
        # Extract the optimal steering angle and acceleration
        optimal_acceleration = optimal_control[0, 0]
        optimal_steering = optimal_control[1, 0]

        opt_posi = sol.value(x_vars)
        
        #print(opt_posi)
        # Convert the steering angle to the corresponding steering wheel angle
        
        trace = []
        
        for j in range(len(total_t)):
            #print t[j], current_psi
            tmp = []
            tmp.append(total_t[j])
            
            tmp.append(float(opt_posi[0,j])) # x position
            tmp.append(float(opt_posi[1,j])) # y position
            tmp.append(float(opt_posi[2,j]))    # theta
            tmp.append(float(opt_posi[3,j]))    # v
            #tmp.append(float(optimal_control[0,j])) # throttle
            #tmp.append(float(optimal_control[1,j])) # steering
            
            delta_p.append(float(optimal_control[1,j]))
            a_p.append(float(optimal_control[0,j]))
            trace.append(tmp)   
    except:
        optimal_acceleration = 0.0
        steering_wheel_angle = 0.0
    
    return trace

if __name__ == "__main__":

    sol = TC_Simulate("Default", [0.0, 0.0,0.0,0.0], 10.0)
    #                  x,y,theta,v
    for s in sol:
        print(s)

    timet = [row[0] for row in sol]

    x = [row[1] for row in sol]

    y = [row[2] for row in sol]
    theta = [row[3] for row in sol]
    v = [row[4] for row in sol]


    plt.figure()
    plt.plot(timet, delta_p, label='Delta')
    plt.plot(timet, a_p, label='Acceleration')
    plt.legend()
    plt.title("MPC steer and Acceleration Over Time")
    plt.xlabel("Time (s)")
    plt.ylabel("Value")
    plt.show()
    
    plt.plot(timet, x, "-r")
    plt.plot(timet, y, "-g")
    plt.plot(timet, theta, "-b")
    plt.plot(timet, v, "-y")
    plt.title("MPC Car for Kinematic Model with all euqal penalty")
    plt.legend(["x", "y","theta","v"])
    plt.show()
    
