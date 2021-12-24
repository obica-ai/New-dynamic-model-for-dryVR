from scipy.integrate import odeint
import numpy as np 

def ProxA_dynamics(x,_):
    xp, yp, xd, yd = x 
    xp_dot = xd
    yp_dot= yd
    xd_dot= -2.89995083970656*xd - 0.0576765518445905*xp + 0.00877200894463775*yd + 0.000200959896519766*yp - (1.43496e+18*xp + 6.050365344e+25)*pow(pow(yp, 2) + pow(xp + 42164000, 2), -1.5) + 807.153595726846
    yd_dot= -0.00875351105536225*xd - 0.000174031357370456*xp - 2.90300269286856*yd - 1.43496e+18*yp*pow(pow(yp, 2) + pow(xp + 42164000, 2), -1.5) - 0.0664932019993982*yp
    return [xp_dot, yp_dot, xd_dot, yd_dot]

def ProxB_dynamics(x,t):
    xp, yp, xd, yd = x 
    xp_dot= xd
    yp_dot= yd
    xd_dot= -19.2299795908647*xd - 0.576076729033652*xp + 0.00876275931760007*yd + 0.000262486079431672*yp - (1.43496e+18*xp + 6.050365344e+25)*pow(pow(yp, 2) + pow(xp + 42164000, 2), -1.5) + 807.153595726846
    yd_dot= -0.00876276068239993*xd - 0.000262486080737868*xp - 19.2299765959399*yd - 1.43496e+18*yp*pow(pow(yp, 2) + pow(xp + 42164000, 2), -1.5) - 0.575980743701182*yp
    return [xp_dot, yp_dot, xd_dot, yd_dot]

def Passive_dynamics(x,t):
    xp, yp, xd, yd = x 
    xp_dot = xd
    yp_dot = yd
    xd_dot = 0.0000575894721132000*xp+0.00876276*yd
    yd_dot = -0.00876276*xd
    return [xp_dot, yp_dot, xd_dot, yd_dot]

def simulate(init, time_bound, time_step, dynamics):
    num_step = int(time_bound/time_step)
    x = init
    trace = [[0]+x]
    t = 0
    for i in range(num_step):
        x = odeint(dynamics, x, [0,time_step])[-1].tolist()
        t += time_step 
        trace.append([t]+x)
    return np.array(trace)

def TC_Simulate(Mode,initialCondition,time_bound):
    time_step = 0.01
    init = [float(elem) for elem in initialCondition]

    if Mode == "ProxA":
        trace = simulate(init, time_bound, time_step, ProxA_dynamics)
    elif Mode == "ProxB":
        trace = simulate(init, time_bound, time_step, ProxB_dynamics)
    elif Mode == "Passive":
        trace = simulate(init, time_bound, time_step, Passive_dynamics)
    else:
        raise ValueError(f"Mode {Mode} not found")

    return trace
