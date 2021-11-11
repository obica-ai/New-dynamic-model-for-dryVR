from scipy.integrate import odeint
import numpy as np
# import matplotlib.pyplot as plt

# Source: https://ths.rwth-aachen.de/research/projects/hypro/biological-model-ii/

def biological_model_2_dynamic(y,t):
    x1 = y[0]
    x2 = y[1]
    x3 = y[2]
    x4 = y[3]
    x5 = y[4]
    x6 = y[5]
    x7 = y[6]
    x8 = y[7]
    x9 = y[8]
    # x1, x2, x3, x4, x5, x6, x7, x8, x9 = y
    x1 = float(x1)
    x2 = float(x2)
    x3 = float(x3)
    x4 = float(x4)
    x5 = float(x5)
    x6 = float(x6)
    x7 = float(x7)

    x1_dot = 3*x3 - x1*x6
    x2_dot = x4 - x2*x6
    x3_dot = x1*x6 - 3*x3
    x4_dot = x2*x6 - x4
    x5_dot = 3*x3 + 5*x1 - x5
    x6_dot = 5*x5 + 3*x3 + x4 - x6*(x1 + x2 + 2*x8 + 1)
    x7_dot = 5*x4 + x2 - 0.5*x7
    x8_dot = 5*x7 - 2*x6*x8 + x9 - 0.2*x8
    x9_dot = 2*x6*x8 - x9

    dydt = [x1_dot, x2_dot, x3_dot, x4_dot, x5_dot, x6_dot, x7_dot, x8_dot, x9_dot]
    return dydt


def TC_Simulate(Mode,initialCondition,time_bound):
    time_step = 0.05;
    time_bound = float(time_bound)

    number_points = int(np.ceil(time_bound/time_step))
    t = [i*time_step for i in range(0,number_points)]
    if t[-1] != time_step:
        t.append(time_bound)
    newt = []
    for step in t:
        newt.append(float(format(step, '.2f')))
    t = newt

    sol = odeint(biological_model_2_dynamic, initialCondition, t, hmax=time_step)

    # Construct the final output
    trace = []
    for j in range(len(t)):
        #print t[j], current_psi
        tmp = []
        tmp.append(t[j])
        tmp.append(float(sol[j,0]))
        tmp.append(float(sol[j,1]))
        tmp.append(float(sol[j,2]))
        tmp.append(float(sol[j,3]))
        tmp.append(float(sol[j,4]))
        tmp.append(float(sol[j,5]))
        tmp.append(float(sol[j,6]))
        tmp.append(float(sol[j,7]))
        tmp.append(float(sol[j,8]))
        trace.append(tmp)
    return trace

if __name__ == "__main__":

    sol = TC_Simulate("Default", [1.0, 1,0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], 2.0)
    #for s in sol:
	#	print(s)

    time = [row[0] for row in sol]

    x1 = [row[1] for row in sol]

    x2 = [row[2] for row in sol]

    x3 = [row[3] for row in sol]

    x4 = [row[4] for row in sol]

    x5 = [row[5] for row in sol]

    x6 = [row[6] for row in sol]

    x7 = [row[7] for row in sol]

    x8 = [row[7] for row in sol]

    x9 = [row[7] for row in sol]

    plt.plot(x2, x8, "-r")
    plt.show()
