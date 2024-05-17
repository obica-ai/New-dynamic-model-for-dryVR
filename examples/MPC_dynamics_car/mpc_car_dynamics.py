from scipy.integrate import odeint
import numpy as np
import casadi as ca
import matplotlib.pyplot as plt
import casadi
# reference to
# https://github.com/alexliniger/MPCC?tab=readme-ov-file

#defualt vehicle parameters
wheel_base = 2.56 #meter
lf = 1.28 
lr = 1.28
F_aero_drag = 0.01
m = 300 # kg
grav = 9.8 # N
Cf = 1 # N/rad
Cr = 1 # N/rad
wheel_rad = 0.55 # meter
# suppose a common 3000RPM , angular velcoity = 3000 RPM * 2pi /60 = 300 pi rad/s
# max acc = 10000watts, peak torque =  10000 watts / 300pi = 10.61 Nm 
peak_torque = 10.61 # nm
dt = 0.05


def car_dynamic(control, t):
    # x,y,theta,v,delta,throttle = control
    x,y,theta,vx,vy,delta,throttle = control
    x = float(x)
    y = float(y)
    theta = float(theta) # yaw angle
    # v = float(v)
    vx = float(vx) # velocity in x direction
    vy = float(vy)  # velocity in y direction
    delta = float(delta) # front wheel angle
    throttle = float(throttle) # acceleration

    v = np.sqrt(vx **2 + vy **2)
    omega = (v * np.tan(delta))/ wheel_base

    # vx = v * np.sin(theta)
    # vy = v * np.cos(theta)
    F_grav = m * grav
    F_aero = F_aero_drag * vx **2
    x_dot = x + (vx * np.sin(theta) - vy * np.cos(theta))* dt
    y_dot = y + (vx * np.cos(theta) + vy * np.sin(theta))* dt
    # Tire forces
    alpha_f = delta - np.arctan((omega * lf + vy) / (vx ))
    alpha_r = np.arctan((omega * lr - vy) /  (vx ))
    
    Fyf = Cf * alpha_f  # force on front tire
    Fyr = Cr * alpha_r  # force on rear ti
    # traction force
    traction_force = peak_torque * 1 / wheel_rad
    F_t = (traction_force  )* throttle- 0.01* m * F_grav
    
    # velocity next
    vx_dot = ((F_t - F_aero - F_grav  - Fyf * np.sin(delta)) / m + vy * omega  ) *dt
    vy_dot = ((Fyr - Fyf * np.cos(delta) ) / m - vx * omega ) * dt

    # v_dot = v + np.sqrt(vx_dot **2 + vy_dot **2)* dt
    
    # theta next
    theta_dot = omega *dt

    # combine
    dydt = [x_dot,y_dot,theta_dot,vx_dot,vy_dot,delta,throttle]
    return dydt

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
    t = newt

    sol = odeint(car_dynamic, initialCondition, t, hmax=time_step, full_output=True)
    # print(sol[1,0])
    
    # Construct the final output
    trace = []
    for j in range(len(t)):
        #print t[j], current_psi
        tmp = []
        tmp.append(t[j])
        tmp.append(float(sol[0][j,0]))
        tmp.append(float(sol[0][j,1]))
        tmp.append(float(sol[0][j,2]))
        tmp.append(float(sol[0][j,3]))
        tmp.append(float(sol[0][j,4]))
        tmp.append(float(sol[0][j,5]))
        trace.append(tmp)
    return trace

if __name__ == "__main__":

    sol = TC_Simulate("Default", [0.0,0.0,0.1,0.1,0.1,0.01,0.01], 5)
    #                   x,y,theta,v,delta,throttle
    for s in sol:
        print(s)
         
    time = [row[0] for row in sol]

    a = [row[1] for row in sol]

    b = [row[2] for row in sol]

    plt.plot(time, a, "-r")
    plt.plot(time, b, "-g")
    plt.show()
    plt.plot(a, b, "-r")
    plt.show()
