from scipy.integrate import odeint
import numpy as np
# import matplotlib.pyplot as plt

def PDE_20_dynamic(y,t,u1):
    x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20 = y

    x1_dot = 4.213*x3 - 252.57*x1 - 106.6*x2 - 51.94*u1 + 13.09*x4 - 1.8157*x5 + 0.4038*x6 + 0.24558*x7 - 0.038164*x8 - 0.0034798*x9 + 0.0014783*x10 + 0.00020072*x11 - 0.00007711*x12 + 2.6519e-6*x13 + 1.5426e-6*x14 + 7.8083e-7*x15 + 4.7136e-8*x16 + 8.0559e-7*x17 + 1.0658e-6*x18 - 6.4998e-7*x19 + 3.9088e-7*x20
    x2_dot = 63.509*x3 - 106.6*x1 - 777.63*x2 - 11.124*u1 + 184.91*x4 - 26.094*x5 + 5.8051*x6 + 3.5304*x7 - 0.54862*x8 - 0.050025*x9 + 0.021252*x10 + 0.0028848*x11 - 0.0011109*x12 + 0.000038122*x13 + 0.000022175*x14 + 0.000011225*x15 + 6.776e-7*x16 + 0.000011581*x17 + 0.000015321*x18 - 9.3439e-6*x19 + 5.6191e-6*x20
    x3_dot = 21.751*x5 - 4.213*x1 - 63.509*x2 - 25.034*x3 - 251.84*x4 - 0.43288*u1 - 4.797*x6 - 2.9205*x7 + 0.45386*x8 + 0.041384*x9 - 0.017581*x10 - 0.0023864*x11 + 0.00091901*x12 - 0.000031537*x13 - 0.000018345*x14 - 9.286e-6*x15 - 5.6056e-7*x16 - 9.5805e-6*x17 - 0.000012675*x18 + 7.7299e-6*x19 - 4.6485e-6*x20
    x4_dot = 1.3463*u1 + 13.09*x1 + 184.91*x2 + 251.84*x3 - 634.37*x4 + 172.68*x5 - 39.239*x6 - 23.8*x7 + 3.698*x8 + 0.3372*x9 - 0.14325*x10 - 0.01944*x11 + 0.0075016*x12 - 0.00025697*x13 - 0.00014947*x14 - 0.000075662*x15 - 4.5674e-6*x16 - 0.000078061*x17 - 0.00010327*x18 + 0.000062983*x19 - 0.000037876*x20
    x5_dot = 172.68*x4 - 1.8157*x1 - 26.094*x2 - 21.751*x3 - 0.1867*u1 - 645.44*x5 + 337.53*x6 + 175.84*x7 - 27.114*x8 - 2.474*x9 + 1.051*x10 + 0.14261*x11 - 0.055099*x12 + 0.0018853*x13 + 0.0010967*x14 + 0.00055512*x15 + 0.00003351*x16 + 0.00057272*x17 + 0.0007577*x18 - 0.00046209*x19 + 0.00027789*x20
    x6_dot = 39.239*x4 - 0.4038*x1 - 5.8051*x2 - 4.797*x3 - 0.041519*u1 - 337.53*x5 - 213.54*x6 - 248.03*x7 + 40.541*x8 + 3.6803*x9 - 1.5635*x10 - 0.21215*x11 + 0.082021*x12 - 0.0028048*x13 - 0.0016315*x14 - 0.00082585*x15 - 0.000049853*x16 - 0.00085204*x17 - 0.0011272*x18 + 0.00068746*x19 - 0.00041342*x20
    x7_dot = 23.8*x4 - 0.24558*x1 - 3.5304*x2 - 2.9205*x3 - 0.025252*u1 - 175.84*x5 - 248.03*x6 - 1671.7*x7 + 572.29*x8 + 47.319*x9 - 20.126*x10 - 2.7307*x11 + 1.0556*x12 - 0.036102*x13 - 0.021*x14 - 0.01063*x15 - 0.00064169*x16 - 0.010967*x17 - 0.014509*x18 + 0.0088486*x19 - 0.0053213*x20
    x8_dot = 3.698*x4 - 0.038164*x1 - 0.54862*x2 - 0.45386*x3 - 0.0039241*u1 - 27.114*x5 - 40.541*x6 - 572.29*x7 - 438.0*x8 - 80.887*x9 + 33.914*x10 + 4.6041*x11 - 1.7793*x12 + 0.060871*x13 + 0.035408*x14 + 0.017923*x15 + 0.001082*x16 + 0.018492*x17 + 0.024464*x18 - 0.01492*x19 + 0.0089723*x20
    x9_dot = 0.00035781*u1 + 0.0034798*x1 + 0.050025*x2 + 0.041384*x3 - 0.3372*x4 + 2.474*x5 + 3.6803*x6 + 47.319*x7 + 80.887*x8 - 291.42*x9 + 259.2*x10 + 33.668*x11 - 12.979*x12 + 0.44416*x13 + 0.25836*x14 + 0.13078*x15 + 0.0078949*x16 + 0.13493*x17 + 0.17851*x18 - 0.10887*x19 + 0.065469*x20
    x10_dot = 0.00015201*u1 + 0.0014783*x1 + 0.021252*x2 + 0.017581*x3 - 0.14325*x4 + 1.051*x5 + 1.5636*x6 + 20.126*x7 + 33.914*x8 - 259.2*x9 - 1175.0*x10 - 304.37*x11 + 123.69*x12 - 4.2158*x13 - 2.4523*x14 - 1.2413*x15 - 0.074913*x16 - 1.2807*x17 - 1.6944*x18 + 1.0333*x19 - 0.62134*x20
    x11_dot = 0.000020635*u1 + 0.00020066*x1 + 0.0028843*x2 + 0.0023865*x3 - 0.019443*x4 + 0.14264*x5 + 0.21219*x6 + 2.731*x7 + 4.6042*x8 - 33.668*x9 - 304.37*x10 - 454.22*x11 + 382.67*x12 - 12.023*x13 - 6.993*x14 - 3.5398*x15 - 0.21245*x16 - 3.6524*x17 - 4.8346*x18 + 2.9481*x19 - 1.7686*x20
    x12_dot = 7.9431e-6*u1 + 0.000077304*x1 + 0.0011112*x2 + 0.00091766*x3 - 0.0074868*x4 + 0.054975*x5 + 0.081837*x6 + 1.054*x7 + 1.779*x8 - 12.978*x9 - 123.69*x10 - 382.67*x11 - 819.72*x12 + 55.376*x13 + 32.26*x14 + 16.328*x15 + 1.0549*x16 + 16.828*x17 + 22.121*x18 - 13.509*x19 + 8.3665*x20
    x13_dot = 5.0949e-7*u1 + 4.955e-6*x1 + 0.000071232*x2 + 0.000058928*x3 - 0.00048014*x4 + 0.0035227*x5 + 0.0052407*x6 + 0.067456*x7 + 0.11374*x8 - 0.82992*x9 - 7.8774*x10 - 22.471*x11 - 103.16*x12 - 608.02*x13 - 6.3034*x14 + 5.7862*x15 + 20.089*x16 - 44.957*x17 + 31.913*x18 + 22.145*x19 - 18.235*x20
    x14_dot = 2.2231e-7*u1 + 2.1621e-6*x1 + 0.000031081*x2 + 0.000025713*x3 - 0.00020951*x4 + 0.0015371*x5 + 0.0022868*x6 + 0.029434*x7 + 0.049629*x8 - 0.36213*x9 - 3.4372*x10 - 9.8012*x11 - 45.235*x12 + 7.783*x13 - 830.71*x14 - 30.381*x15 + 13.683*x16 + 27.495*x17 - 8.7184*x18 + 52.331*x19 - 54.187*x20
    x15_dot = 8.257e-8*u1 + 8.0303e-7*x1 + 0.000011544*x2 + 9.5501e-6*x3 - 0.000077814*x4 + 0.0005709*x5 + 0.00084934*x6 + 0.010932*x7 + 0.018433*x8 - 0.1345*x9 - 1.2767*x10 - 3.6438*x11 - 16.605*x12 + 14.326*x13 - 53.19*x14 - 661.86*x15 - 1.6516*x16 - 43.748*x17 + 27.435*x18 - 12.906*x19 - 53.819*x20
    x16_dot = 0.000057126*x4 - 5.8954e-7*x1 - 8.475e-6*x2 - 7.0111e-6*x3 - 6.0618e-8*u1 - 0.00041912*x5 - 0.00062353*x6 - 0.0080258*x7 - 0.013532*x8 + 0.098742*x9 + 0.93718*x10 + 2.6705*x11 + 12.444*x12 + 34.312*x13 + 29.652*x14 + 33.327*x15 - 754.41*x16 - 0.85524*x17 + 42.161*x18 - 3.6981*x19 - 2.2351*x20
    x17_dot = 0.000060597*x4 - 6.2536e-7*x1 - 8.9899e-6*x2 - 7.4371e-6*x3 - 6.4301e-8*u1 - 0.00044459*x5 - 0.00066142*x6 - 0.0085135*x7 - 0.014355*x8 + 0.10474*x9 + 0.9942*x10 + 2.8368*x11 + 12.977*x12 - 40.881*x13 + 9.5498*x14 - 23.104*x15 + 9.3994*x16 - 729.28*x17 - 8.4843*x18 - 32.211*x19 - 31.064*x20
    x18_dot = 1.4599e-7*u1 + 1.4199e-6*x1 + 0.000020411*x2 + 0.000016886*x3 - 0.00013758*x4 + 0.0010094*x5 + 0.0015017*x6 + 0.019329*x7 + 0.032591*x8 - 0.23781*x9 - 2.2573*x10 - 6.4396*x11 - 29.533*x12 + 23.045*x13 + 7.1886*x14 + 20.228*x15 - 5.3117*x16 - 22.178*x17 - 706.87*x18 - 30.752*x19 - 73.52*x20
    x19_dot = 1.5381e-7*u1 + 1.4958e-6*x1 + 0.000021504*x2 + 0.000017789*x3 - 0.00014495*x4 + 0.0010634*x5 + 0.0015821*x6 + 0.020364*x7 + 0.034336*x8 - 0.25054*x9 - 2.378*x10 - 6.7817*x11 - 31.254*x12 + 6.8827*x13 - 18.472*x14 + 9.8702*x15 + 22.623*x16 + 12.643*x17 + 21.048*x18 - 707.2*x19 + 53.509*x20
    x20_dot = 0.000036388*x4 - 3.7553e-7*x1 - 5.3984e-6*x2 - 4.466e-6*x3 - 3.8613e-8*u1 - 0.00026697*x5 - 0.00039718*x6 - 0.0051123*x7 - 0.0086199*x8 + 0.062897*x9 + 0.59703*x10 + 1.7044*x11 + 7.7438*x12 - 15.163*x13 - 73.759*x14 - 25.314*x15 + 41.691*x16 + 9.7273*x17 - 50.649*x18 + 16.658*x19 - 730.19*x20

    dydt = [x1_dot, x2_dot, x3_dot, x4_dot, x5_dot, x6_dot, x7_dot, x8_dot, x9_dot, x10_dot, x11_dot, x12_dot, x13_dot, x14_dot, x15_dot, x16_dot, x17_dot, x18_dot, x19_dot, x20_dot]
    return dydt

def TC_Simulate(Mode,initialCondition,time_bound):
    time_step = 0.005;
    time_bound = float(time_bound)

    number_points = int(np.ceil(time_bound/time_step))
    t = [i*time_step for i in range(0,number_points)]
    if t[-1] != time_step:
        t.append(time_bound)
    newt = []
    for step in t:
        newt.append(float(format(step, '.3f')))
    t = newt

    u1 = 0.75

    sol = odeint(PDE_20_dynamic, initialCondition, t, args=(u1,), hmax=time_step)

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
        tmp.append(float(sol[j,9]))
        tmp.append(float(sol[j,10]))
        tmp.append(float(sol[j,11]))
        tmp.append(float(sol[j,12]))
        tmp.append(float(sol[j,13]))
        tmp.append(float(sol[j,14]))
        tmp.append(float(sol[j,15]))
        tmp.append(float(sol[j,16]))
        tmp.append(float(sol[j,17]))
        tmp.append(float(sol[j,18]))
        tmp.append(float(sol[j,19]))
        trace.append(tmp)
    return trace

if __name__ == "__main__":
    sol = TC_Simulate("Default", [-0.002, 0.0, -0.001, -0.001, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.0007, 0.0, 0.0, 0.0, 0.0002, -0.001, 0.001, -0.001], 20.0)

    time = [row[0] for row in sol]

    a = [row[1] for row in sol]

    b = [row[2] for row in sol]

    plt.plot(time, a, "-r")
    plt.plot(time, b, "-g")
    plt.show()
    plt.plot(a, b, "-r")
    plt.show()
