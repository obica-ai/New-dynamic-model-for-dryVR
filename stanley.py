import numpy as np
import matplotlib.pyplot as plt
from math import cos, sin, atan2,tan
from scipy.integrate import odeint
# resource ref  https://github.com/winstxnhdw/FullStanleyController/blob/master/stanley_controller.py
# Stanley Controller definition
dt = 0.05
t_p = []
delta_p = []
a_p = []
global counter
counter = 0
class StanleyController:
    def __init__(self, control_gain=0.5, softening_gain=1.0,integral_gain=0.5, max_steer=np.deg2rad(24), wheelbase=2.58):
        self.k = control_gain
        self.kp = softening_gain
        self.max_steer = max_steer
        self.wheelbase = wheelbase
        self.ki = integral_gain 
        self.integral_error = 0

    def control_law(self, state, ref_x, ref_y, ref_theta, ref_v):
        x, y, theta, v = state
        #TODO Do we need integral error?
        cross_track_error = np.hypot(ref_x - x, ref_y - y) * np.sign(sin(ref_theta) * (x - ref_x) - cos(ref_theta) * (y - ref_y))
        #self.integral_error += cross_track_error * dt
        
        heading_error = atan2(sin(ref_theta - theta), cos(ref_theta - theta))
        delta = heading_error + atan2(self.k * cross_track_error, self.kp + v)
        a = ref_v - v
        return delta, a

# Bicycle model dynamics
def bicycle_model_dynamics(state, t, controller, ref_path):
    x, y, theta, v = state
    ref_x, ref_y, ref_theta, ref_v = ref_path(t) 
    delta, a = controller.control_law(state, ref_x, ref_y, ref_theta, ref_v)
    x_dot = (v * cos(theta) - controller.wheelbase/2 * sin(theta) * v * tan(delta) / controller.wheelbase) *dt
    y_dot = (v * sin(theta) + controller.wheelbase/2 * cos(theta) * v * tan(delta) / controller.wheelbase)  *dt
    theta_dot = v / controller.wheelbase * tan(delta) *dt
    v_dot = a *dt
    global counter
    counter += dt
    t_p.append(counter)
    delta_p.append(delta)
    a_p.append(a)
    
    return [x_dot, y_dot, theta_dot, v_dot]

# Reference path (for example purposes)
def ref_path(t):
    return 5, 5, 0.0, 1.0  # ref_x, ref_y, ref_theta, ref_v

# Simulation function
def TC_Simulate(Mode,initialCondition, time_bound):
    time_step = dt
    controller = StanleyController()
    time_bound = float(time_bound)

    number_points = int(np.ceil(time_bound/time_step))
    t = [i*time_step for i in range(0,number_points)]
    if t[-1] != time_step:
        t.append(time_bound)
    newt = []
    for step in t:
        newt.append(float(format(step, '.2f')))
    t = newt

    sol = odeint(bicycle_model_dynamics, initialCondition, t, args=(controller, ref_path))
    trace = []
    for j in range(len(t)):
        #print t[j], current_psi
        tmp = []
        tmp.append(t[j])
        tmp.append(float(sol[j,0]))
        tmp.append(float(sol[j,1]))
        tmp.append(float(sol[j,2]))
        tmp.append(float(sol[j,3]))
        
        trace.append(tmp)
    return trace
    

# Main execution block
if __name__ == "__main__":
    initial_condition = [0.0, 0.0, 0.0, 0.0]  # x, y, theta, v
    
    trace = TC_Simulate("Default",initial_condition, 10)
    for i in range(len(trace)):
        print(trace[i])
        print()
    t = [row[0] for row in trace]
    x = [row[1] for row in trace]
    y = [row[2] for row in trace]
    theta = [row[3] for row in trace]
    v = [row[4] for row in trace]
    plt.figure()
    plt.plot(t_p, delta_p, label='Delta')
    plt.plot(t_p, a_p, label='Acceleration')
    plt.legend()
    plt.title("Stanley steer and Acceleration Over Time")
    plt.xlabel("Time (s)")
    plt.ylabel("Value")
    plt.show()
    
    plt.plot(t, x, "-r")
    plt.plot(t, y, "-g")
    plt.plot(t, theta, "-b")
    plt.plot(t, v, "-y")
    plt.title("stanley Car for Kinematic Model ")
    plt.legend(["x", "y","theta","v"])
    plt.show()
