from scipy.integrate import odeint
import numpy as np
# import matplotlib.pyplot as plt

def ISS_dynamic(y,t,u1,u2,u3):
    x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25 = y

    x1_dot = 0.77508*x2 - 1.5818e-8*u2 - 4.4341e-6*u3 - 3.9874e-8*x1 - 0.000067832*u1 - 0.000042976*x3 + 1.1479e-7*x4 - 7.09e-9*x5 - 1.653e-7*x6 + 0.000082292*x7 + 1.2158e-7*x8 - 0.000019112*x9 + 1.4896e-6*x10 - 1.6821e-6*x11 + 4.1703e-8*x12 - 7.4365e-8*x13 - 8.392e-6*x14 + 3.916e-7*x15 + 1.2336e-8*x16 - 0.000013101*x17 - 9.8709e-8*x18 + 0.000015487*x19 + 1.2069e-6*x20 - 2.199e-10*x21 + 3.3026e-9*x22 - 2.2098e-6*x23 - 4.4199e-7*x24 + 5.5964e-8*x25
    x2_dot = 0.010393*x3 - 7.046e-6*u2 - 0.0021408*u3 - 0.77508*x1 - 0.0077527*x2 - 0.029896*u1 - 0.000091911*x4 + 3.0412e-6*x5 + 0.000067451*x6 - 0.030171*x7 - 0.000093795*x8 + 0.0080792*x9 - 0.00062151*x10 + 0.00056631*x11 - 0.000019791*x12 + 0.000016675*x13 + 0.0034991*x14 - 0.00016438*x15 - 3.6089e-6*x16 + 0.005483*x17 + 0.00004566*x18 - 0.0068005*x19 - 0.00054048*x20 + 9.6562e-8*x21 - 1.3965e-6*x22 + 0.00097681*x23 + 0.00019284*x24 - 0.00002451*x25
    x3_dot = 0.025889*u1 + 5.692e-6*u2 + 0.0017739*u3 + 0.000042976*x1 + 0.010393*x2 - 0.019925*x3 + 1.992*x4 - 9.64e-6*x5 - 0.00020176*x6 + 0.074349*x7 + 0.00047222*x8 - 0.02434*x9 + 0.0018562*x10 - 0.0013648*x11 + 0.000060527*x12 + 1.8555e-6*x13 - 0.009979*x14 + 0.00047011*x15 + 4.6351e-6*x16 - 0.015331*x17 - 0.00014437*x18 + 0.019924*x19 + 0.0016295*x20 - 2.8194e-7*x21 + 4.0927e-6*x22 - 0.0028698*x23 - 0.00055944*x24 + 0.000073616*x25
    x4_dot = 0.00012603*u1 + 6.3733e-9*u2 - 8.2928e-6*u3 + 1.1344e-7*x1 + 0.000091528*x2 - 1.992*x3 - 4.721e-7*x4 + 6.8864e-8*x5 + 1.3712e-6*x6 - 0.00069225*x7 + 4.1564e-7*x8 + 0.00016249*x9 - 0.000011465*x10 - 7.5669e-6*x11 - 6.2996e-7*x12 + 4.4433e-7*x13 + 0.000046164*x14 - 2.1949e-6*x15 - 6.9408e-9*x16 + 0.000089016*x17 + 5.9344e-7*x18 - 0.00011087*x19 - 7.9154e-6*x20 + 1.6152e-9*x21 - 2.0157e-8*x22 + 0.000016545*x23 + 3.2471e-6*x24 - 2.8817e-7*x25
    x5_dot = 1.6594e-6*u1 + 0.000049597*u2 - 5.5481e-6*u3 + 2.267e-9*x1 + 3.4178e-7*x2 + 1.4523e-6*x3 - 3.9616e-8*x4 - 2.0742e-7*x5 + 8.4808*x6 + 0.00019256*x7 - 8.1914e-6*x8 - 0.00027239*x9 + 4.7e-6*x10 + 0.00013794*x11 + 8.9716e-6*x12 + 3.5274e-6*x13 + 0.000060912*x14 + 0.00028304*x15 + 0.000010924*x16 - 0.000010741*x17 - 3.6403e-8*x18 + 0.00012921*x19 + 0.000011657*x20 + 4.1831e-8*x21 + 0.000022211*x22 + 0.00016752*x23 - 8.7449e-6*x24 + 0.000020849*x25
    x6_dot = 0.000050285*u1 + 0.031956*u2 - 8.8146e-6*u3 + 8.4062e-8*x1 + 0.00002251*x2 - 0.000015118*x3 - 8.7922e-7*x4 - 8.4808*x5 - 0.084954*x6 + 0.0020235*x7 + 0.00035617*x8 - 0.00040077*x9 + 0.000061347*x10 - 0.0026561*x11 - 0.0053278*x12 + 0.00017381*x13 + 0.00006795*x14 - 0.11612*x15 - 0.013235*x16 - 0.00021301*x17 - 8.9555e-6*x18 - 0.02166*x19 - 0.0041435*x20 - 0.000039199*x21 - 0.013058*x22 - 0.11134*x23 + 0.0041698*x24 - 0.018503*x25
    x7_dot = 0.074387*x3 - 0.00033453*u2 - 0.004295*u3 - 0.000082305*x1 - 0.030181*x2 - 0.06356*u1 + 0.00069032*x4 - 0.00015437*x5 + 0.00051015*x6 - 0.38083*x7 - 37.979*x8 + 0.7873*x9 - 0.060466*x10 + 0.013627*x11 - 0.00039456*x12 - 0.0012494*x13 + 0.081843*x14 - 0.0030461*x15 + 0.00022337*x16 + 0.10128*x17 + 0.0014165*x18 - 0.14414*x19 - 0.013155*x20 + 2.3002e-6*x21 + 0.000053744*x22 + 0.021269*x23 + 0.00385*x24 - 0.00049419*x25
    x8_dot = 0.00046227*u1 + 4.5013e-6*u2 - 0.000403*u3 + 4.9915e-7*x1 + 0.00023226*x2 - 0.00081483*x3 - 3.7771e-6*x4 + 6.7246e-6*x5 - 0.00034414*x6 + 37.981*x7 - 0.000035297*x8 + 0.00053662*x9 - 0.00070952*x10 + 0.0031645*x11 + 0.000023345*x12 + 0.00014887*x13 + 0.0019753*x14 - 0.000017043*x15 + 0.00002319*x16 + 0.00058362*x17 + 2.4028e-6*x18 + 0.0017122*x19 + 0.000077626*x20 - 1.6826e-8*x21 + 5.5737e-6*x22 - 0.000357*x23 - 0.000057501*x24 - 0.00001095*x25
    x9_dot = 0.0067388*u1 - 0.00010737*u2 - 0.029739*u3 + 7.2178e-6*x1 + 0.0017*x2 - 0.00019482*x3 - 0.00011165*x4 + 0.00019205*x5 + 0.00079526*x6 - 0.6624*x7 - 0.003324*x8 - 0.095564*x9 - 9.226*x10 + 0.095466*x11 - 0.00027059*x12 + 0.0076725*x13 + 0.025007*x14 - 0.00075564*x15 + 0.0020501*x16 - 0.036019*x17 - 0.00021286*x18 + 0.1367*x19 + 0.0085687*x20 - 1.8999e-6*x21 + 0.000098234*x22 - 0.026071*x23 - 0.0042174*x24 - 0.00051124*x25
    x10_dot = 0.000018473*u2 - 0.00049267*u1 + 0.0011629*u3 - 6.128e-7*x1 - 0.00015906*x2 + 0.000098378*x3 + 7.5464e-6*x4 - 2.7468e-6*x5 - 0.00014204*x6 + 0.050261*x7 + 0.00077848*x8 + 9.2327*x9 - 0.00016399*x10 + 0.0025634*x11 + 0.000093672*x12 - 0.00015995*x13 + 0.0032584*x14 - 0.0001579*x15 - 0.000091724*x16 + 0.0027424*x17 + 0.000022918*x18 - 0.0038682*x19 - 0.00035484*x20 + 2.9517e-8*x21 - 8.1575e-6*x22 + 0.00055204*x23 + 0.00010812*x24 - 0.00001302*x25
    x11_dot = 0.00021885*u1 + 0.00062742*u2 + 0.031924*u3 + 2.7668e-6*x1 + 0.0012698*x2 - 0.0034992*x3 + 0.000015077*x4 - 0.000029105*x5 - 0.002264*x6 + 0.022439*x7 + 0.0010149*x8 + 0.14925*x9 - 0.0088367*x10 - 0.21936*x11 + 21.632*x12 - 0.25645*x13 + 0.034127*x14 + 0.00009552*x15 - 0.018103*x16 + 0.0063054*x17 - 0.00090411*x18 - 0.20896*x19 - 0.014827*x20 + 6.3207e-7*x21 - 0.00069129*x22 + 0.041312*x23 + 0.0065424*x24 + 0.0010382*x25
    x12_dot = 0.00096737*u3 - 0.000013375*u2 - 0.000058839*u1 + 3.4721e-9*x1 + 6.1745e-6*x2 - 0.000019726*x3 + 1.0003e-6*x4 - 2.4488e-6*x5 + 0.0021328*x6 + 0.00024909*x7 + 0.000068107*x8 + 0.0061239*x9 - 0.00028192*x10 - 21.642*x11 - 0.00020216*x12 - 0.0056107*x13 + 0.051964*x14 - 0.020176*x15 - 0.0018275*x16 + 0.00047309*x17 - 0.000017773*x18 - 0.0037257*x19 - 0.0006547*x20 - 2.5584e-6*x21 - 0.0010621*x22 - 0.0084165*x23 + 0.0003463*x24 - 0.0011795*x25
    x13_dot = 0.0004033*u1 + 0.000010686*u2 - 0.00065516*u3 + 4.2487e-7*x1 + 0.00018325*x2 - 0.00054937*x3 - 3.3887e-6*x4 - 2.1162e-6*x5 - 0.0001258*x6 + 0.0048075*x7 - 0.00014701*x8 - 0.0080888*x9 + 0.00027094*x10 + 0.25564*x11 + 0.0056807*x12 - 0.00013242*x13 - 7.9348*x14 + 0.0015647*x15 + 0.00045894*x16 + 0.0016*x17 - 0.000012036*x18 - 0.009824*x19 - 0.00013753*x20 + 2.3288e-7*x21 + 0.000031485*x22 + 0.0022741*x23 + 0.00033705*x24 + 0.000072311*x25
    x14_dot = 0.0027745*u1 - 0.00012117*u2 + 0.018323*u3 + 4.9737e-6*x1 + 0.0019737*x2 - 0.0048551*x3 - 0.000017806*x4 - 5.4907e-6*x5 + 0.00062266*x6 + 0.013547*x7 + 0.00031714*x8 + 0.09668*x9 - 0.0055953*x10 - 0.28474*x11 - 0.057516*x12 + 7.9342*x13 - 0.076875*x14 + 0.0039301*x15 - 0.010797*x16 - 0.035397*x17 - 0.0011389*x18 - 0.074604*x19 - 0.0050782*x20 + 1.5392e-6*x21 + 0.000037342*x22 + 0.020588*x23 + 0.0023203*x24 + 0.0015583*x25
    x15_dot = 0.027752*u2 - 0.00017415*u1 - 0.00064806*u3 - 2.5688e-7*x1 - 0.00010581*x2 + 0.00028025*x3 + 1.1817e-6*x4 - 0.00030614*x5 - 0.11613*x6 + 0.000072363*x7 - 0.000052153*x8 - 0.0028552*x9 + 0.000084693*x10 + 0.0013593*x11 + 0.014547*x12 - 0.0014295*x13 + 0.0041762*x14 - 0.23692*x15 - 21.642*x16 + 0.0055381*x17 + 0.00025423*x18 - 0.052304*x19 - 0.0092281*x20 - 0.00018017*x21 - 0.033616*x22 - 0.29131*x23 + 0.014834*x24 - 0.078122*x25
    x16_dot = 2.8677e-6*u1 - 0.0016301*u2 - 0.00091042*u3 - 6.7105e-8*x1 - 0.000032256*x2 + 0.000091287*x3 - 4.6696e-7*x4 + 9.6587e-6*x5 + 0.012242*x6 - 0.00087006*x7 - 0.000074804*x8 - 0.0062897*x9 + 0.00025476*x10 + 0.025598*x11 + 0.0016471*x12 - 0.000593*x13 + 0.015226*x14 + 21.64*x15 - 0.0010733*x16 - 0.0034683*x17 + 0.00013614*x18 - 0.0138*x19 - 0.0014363*x20 - 5.8718e-6*x21 - 0.0047843*x22 - 0.037873*x23 + 0.0012477*x24 - 0.003001*x25
    x17_dot = 0.010825*u1 - 3.4097e-6*u2 + 0.0010515*u3 + 0.000013095*x1 + 0.0054813*x2 - 0.015323*x3 - 0.000088195*x4 + 7.1212e-7*x5 - 0.000017313*x6 + 0.10123*x7 - 0.0010253*x8 + 0.0026272*x9 - 7.3801e-6*x10 - 0.019566*x11 - 0.00047152*x12 - 0.0027269*x13 + 0.0018871*x14 - 0.0035121*x15 + 0.0037956*x16 - 0.039118*x17 - 3.914*x18 + 0.090916*x19 + 0.010911*x20 - 1.1703e-6*x21 + 0.000024714*x22 - 0.01333*x23 - 0.0020639*x24 + 0.00047068*x25
    x18_dot = 1.0388e-6*u2 - 0.000077295*u1 - 0.000039042*u3 - 9.0898e-8*x1 - 0.000042517*x2 + 0.00013544*x3 + 5.0431e-7*x4 - 1.4116e-8*x5 - 2.6814e-6*x6 - 0.0013553*x7 + 3.0706e-6*x8 - 0.000065427*x9 - 5.6208e-6*x10 + 0.0011314*x11 + 0.000025866*x12 + 0.000010637*x13 + 0.001187*x14 - 0.00027786*x15 - 0.00014742*x16 + 3.914*x17 - 2.4807e-6*x18 + 0.00067765*x19 + 0.000060426*x20 - 1.8575e-8*x21 - 2.1208e-6*x22 - 0.000087995*x23 - 0.000017543*x24 - 1.7299e-6*x25
    x19_dot = 0.0047731*u2 - 0.008575*u1 + 0.022953*u3 - 8.4464e-6*x1 - 0.0035032*x2 + 0.0099956*x3 + 0.000079296*x4 - 0.00002916*x5 - 0.023038*x6 - 0.066715*x7 + 0.0022769*x8 + 0.13487*x9 - 0.0058809*x10 - 0.26004*x11 - 0.0087516*x12 + 0.010976*x13 - 0.15666*x14 - 0.053282*x15 + 0.022941*x16 + 0.0081611*x17 - 0.00012685*x18 - 0.50256*x19 - 47.977*x20 - 0.002141*x21 + 0.0091633*x22 + 0.04162*x23 - 0.015503*x24 - 0.097574*x25
    x20_dot = 0.0006502*u1 + 0.0010819*u2 - 0.00093859*u3 + 6.7674e-7*x1 + 0.00030673*x2 - 0.00095773*x3 - 5.021e-6*x4 - 0.000011175*x5 - 0.0053323*x6 + 0.0085965*x7 - 0.00013735*x8 - 0.0077052*x9 + 0.00033131*x10 + 0.016492*x11 + 0.00058798*x12 - 0.00035947*x13 + 0.0083581*x14 - 0.015252*x15 + 0.0011064*x16 - 0.0084702*x17 - 0.000016497*x18 + 47.967*x19 - 0.0019974*x20 - 0.00042264*x21 + 0.015553*x22 + 0.10612*x23 + 0.023792*x24 - 0.024066*x25
    x21_dot = 1.565e-7*u1 - 6.6249e-6*u2 - 4.3483e-7*u3 + 1.5042e-10*x1 + 6.2872e-8*x2 - 1.818e-7*x3 - 1.4362e-9*x4 + 5.0012e-8*x5 + 0.000039169*x6 + 8.3919e-7*x7 - 3.8961e-8*x8 - 2.7848e-6*x9 + 1.4129e-7*x10 + 7.5826e-6*x11 + 8.1314e-7*x12 - 1.8705e-7*x13 + 2.5961e-6*x14 + 0.00017993*x15 - 4.7059e-6*x16 - 3.6462e-7*x17 + 8.7599e-9*x18 + 0.002159*x19 + 0.00042365*x20 - 3.6442e-8*x21 - 0.62345*x22 - 0.003334*x23 + 0.000063254*x24 - 0.00001974*x25
    x22_dot = 0.0027032*u2 - 2.693e-6*u1 + 9.7243e-6*u3 - 1.705e-9*x1 - 6.8697e-7*x2 + 2.048e-6*x3 + 2.4563e-8*x4 - 0.000024533*x5 - 0.013058*x6 + 0.00013932*x7 - 1.9475e-6*x8 + 0.00011061*x9 - 0.000011848*x10 - 0.00068316*x11 + 0.00028803*x12 - 0.000018109*x13 + 0.000060096*x14 - 0.033617*x15 + 0.0045011*x16 + 8.7237e-6*x17 - 8.9527e-7*x18 - 0.030152*x19 - 0.019898*x20 + 0.62345*x21 - 0.0060382*x22 - 0.053123*x23 + 0.023096*x24 - 0.074786*x25
    x23_dot = 0.0011663*u1 + 0.022883*u2 - 0.0046205*u3 + 1.0393e-6*x1 + 0.00042442*x2 - 0.0012145*x3 - 0.000011524*x4 - 0.00020902*x5 - 0.11132*x6 + 0.0093905*x7 - 0.00043252*x8 - 0.026356*x9 + 0.0010723*x10 + 0.047235*x11 + 0.0041121*x12 - 0.0022434*x13 + 0.032535*x14 - 0.29196*x15 + 0.033427*x16 - 0.00015071*x17 - 0.000042847*x18 - 0.026551*x19 - 0.14408*x20 + 0.0033305*x21 - 0.053016*x22 - 0.48812*x23 + 47.846*x24 - 1.0501*x25
    x24_dot = 0.00043865*u1 - 0.000032817*u2 - 0.0010189*u3 + 4.3979e-7*x1 + 0.00018682*x2 - 0.00054655*x3 - 3.8796e-6*x4 + 2.3139e-8*x5 - 0.00021883*x6 + 0.0040048*x7 - 0.00010906*x8 - 0.0063519*x9 + 0.00027571*x10 + 0.01239*x11 + 0.00035175*x12 - 0.00046198*x13 + 0.0072301*x14 - 0.0049019*x15 - 0.0010347*x16 - 0.0016683*x17 + 2.6283e-6*x18 + 0.058033*x19 - 0.023438*x20 - 0.000059687*x21 - 0.02119*x22 - 47.837*x23 - 0.0011008*x24 + 0.018523*x25
    x25_dot = 0.000016668*u1 - 0.0031975*u2 + 0.00011215*u3 + 2.6749e-8*x1 + 0.000012562*x2 - 0.000038366*x3 - 5.9732e-8*x4 + 0.000024786*x5 + 0.018508*x6 + 0.00013388*x7 + 0.000010744*x8 + 0.00064335*x9 - 0.00001167*x10 - 0.00089759*x11 + 0.00018382*x12 + 0.000029313*x13 - 0.0014556*x14 + 0.078125*x15 - 0.002242*x16 - 0.00035695*x17 + 6.5063e-6*x18 + 0.097741*x19 + 0.024759*x20 - 0.000018961*x21 + 0.074788*x22 + 1.0502*x23 - 0.016204*x24 - 0.010456*x25

    dydt = [x1_dot, x2_dot, x3_dot, x4_dot, x5_dot, x6_dot, x7_dot, x8_dot, x9_dot, x10_dot, x11_dot, x12_dot, x13_dot, x14_dot, x15_dot, x16_dot, x17_dot, x18_dot, x19_dot, x20_dot, x21_dot, x22_dot, x23_dot, x24_dot, x25_dot]
    return dydt

def TC_Simulate(Mode,initialCondition,time_bound):
    time_step = 0.001;
    time_bound = float(time_bound)

    number_points = int(np.ceil(time_bound/time_step))
    t = [i*time_step for i in range(0,number_points)]
    if t[-1] != time_step:
        t.append(time_bound)
    newt = []
    for step in t:
        newt.append(float(format(step, '.3f')))
    t = newt

    u1 = 0.05
    u2 = 0.9
    u3 = 0.95

    sol = odeint(ISS_dynamic, initialCondition, t, args=(u1,u2,u3), hmax=time_step)

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
        tmp.append(float(sol[j,20]))
        tmp.append(float(sol[j,21]))
        tmp.append(float(sol[j,22]))
        tmp.append(float(sol[j,23]))
        tmp.append(float(sol[j,24]))
        trace.append(tmp)
    return trace

if __name__ == "__main__":

    sol = TC_Simulate("Default", [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.1, 0.9, 0.9, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 20.0)
    #for s in sol:
	#	print(s)

    time = [row[0] for row in sol]

    a = [row[1] for row in sol]

    b = [row[2] for row in sol]

    plt.plot(time, a, "-r")
    plt.plot(time, b, "-g")
    plt.show()
    plt.plot(a, b, "-r")
    plt.show()
    