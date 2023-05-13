import math
import matplotlib.pyplot as plt

def calculate():
    SLR = 8.0
    RLR = 2.0
    OLR = SLR + RLR
    STMR = 15.0
    LSTR = 18.0
    Ds = 3.0
    Dr = 3.0
    # TELR = 65.0
    TELR = 65
    WEPL = 110.0
    # T = 0.0
    # Tr = 0.0
    # Ta = 0.0
    sT = 1.0
    mT = 100.0
    qdu = 1.0
    Ie = 0.0
    Bpl = 4.3
    Ppl = [0.0, 1.0, 2.0, 3.0]
    BurstR = 1.0
    Nc = -70.0
    Nfor = -64.0
    Ps = 35.0
    Pr = 35.0
    A = 0.0
    T = [t for t in range(0, 501, 1)]
    # T = 0
    Ie_eff = []

    R1 = []
    R2 = []
    R3 = []
    R4 = []

    MOS1 = []
    MOS2 = []
    MOS3 = []
    MOS4 = []

    for t in T:
        Ta = t
        Tr = 2*t
        Nfo = Nfor + RLR
        Pre = Pr + 10 * math.log10(1+math.pow(10, ((10.0-LSTR)/10.0)))/math.log10(10)
        Nor = RLR - 121.0 + Pre + 0.008 * math.pow((Pre - 35.0), 2)
        Nos = Ps - SLR - Ds - 100.0 + 0.004 * math.pow((Ps - OLR - Ds - 14.0), 2)
        No = 10*math.log10(math.pow(10, (Nc/10)) + math.pow(10, (Nos/10)) + math.pow(10, (Nor/10)) + math.pow(10, (Nfo/10)))
        Ro = 15.0 - (1.5 * (SLR + No))

        if qdu < 1:
            Q = 37 - 15 * math.log10(1) / math.log10(10)
        else:
            Q = 37 - 15 * math.log10(qdu) / math.log10(10)

        G = 1.07+0.258*Q+0.0602*math.pow(Q, 2)
        Z = 46.0/30.0 - G/40.0
        Y = (Ro-100)/15+46/8.4-G/9

        Xolr = OLR + 0.2 * (64.0 + No - RLR)
        Iolr = 20*(math.pow(1.0 + math.pow(Xolr/8.0, 8), 1/8) - Xolr/8.0)
        STMRo = -10 * math.log10(math.pow(10, (-STMR/10.0))+math.exp(-t/4.0) * math.pow(10, (-TELR/10)))
        Ist = 12*math.pow(1+pow((STMRo-13)/6, 8), 1/8)-28*math.pow(1+math.pow((STMRo+1)/19.4, 35), 1/35)-13*math.pow(1+math.pow((STMRo-3)/33, 13), 1/13)+29
        Iq = 15 * math.log10(1 + math.pow(10, Y) + math.pow(10, Z))

        Is = Iolr + Ist + Iq

        Rle = 10.5 * (WEPL + 7.0) * math.pow((Tr + 1.0), -0.25)
        if Ta == 0:
            X = 0
        else:
            X = (math.log10(Ta/100))/(math.log10(2))

        if Ta <= 100:
            Idd = 0
        else:
            Idd = 25 * (math.pow(1 + math.pow(X, 6), 1 / 6) - 3 * math.pow(1 + math.pow(X / 3, 6), 1 / 6)+2)

        Idle = (Ro-Rle)/2 + math.sqrt((math.pow(Ro-Rle, 2))/4+169)
        TERV = TELR-40*math.log10((1+t/10)/(1+t/150))+6*math.exp(-0.3*math.pow(t, 2))
        TERVs = TERV + (Ist/2)


        Roe = -1.5*(No-RLR)

        if STMR < 9:
            Re = 80 + 2.5 * (TERVs-14)

        else:
            Re = 80 + 2.5 * (TERV-14)


        if t < 1:
            Idte = 0
        else:
            Idte = ((Roe-Re) / 2 + math.sqrt(math.pow(Roe-Re, 2) / 4 + 100)-1)*(1 - math.exp(-t))

        if STMR > 20:
            Idtes = math.sqrt((math.pow(Idte, 2)) + (math.pow(Ist, 2)))
            Id = Idtes + Idle + Idd
        else:
            Id = Idte + Idle + Idd

        for i in range(4):
            Ie_eff.append(Ie+(95-Ie)*(Ppl[i]/(Ppl[i]/BurstR+Bpl)))

        Rp1 = Ro - Is - Id - Ie_eff[0] + A
        # print(R)
        R1.append(Rp1)
        Rp2 = Ro - Is - Id - Ie_eff[1] + A
        # print(R)
        R2.append(Rp2)
        Rp3 = Ro - Is - Id - Ie_eff[2] + A
        # print(R)
        R3.append(Rp3)
        Rp4 = Ro - Is - Id - Ie_eff[3] + A
        # print(R)
        R4.append(Rp4)


        if Rp1 > 100:
            MOSp1 = 4.5
        else:
            if Rp1 < 0:
                MOSp1 = 1
            else:
                MOSp1 = 1 + Rp1 * 0.035 + Rp1 * (Rp1-60) * (100-Rp1) * 7 * pow(10, -6)

        MOS1.append(MOSp1)

        if Rp2 > 100:
            MOSp2 = 4.5
        else:
            if Rp2 < 0:
                MOSp2 = 1
            else:
                MOSp2 = 1 + Rp2 * 0.035 + Rp2 * (Rp2-60) * (100-Rp2) * 7 * pow(10, -6)

        MOS2.append(MOSp2)

        if Rp3 > 100:
            MOSp3 = 4.5
        else:
            if Rp3 < 0:
                MOSp3 = 1
            else:
                MOSp3 = 1 + Rp3 * 0.035 + Rp3 * (Rp3-60) * (100-Rp3) * 7 * pow(10, -6)

        MOS3.append(MOSp3)

        if Rp4 > 100:
            MOSp4 = 4.5
        else:
            if Rp4 < 0:
                MOSp4 = 1
            else:
                MOSp4 = 1 + Rp4 * 0.035 + Rp4 * (Rp4-60) * (100-Rp4) * 7 * pow(10, -6)

        MOS4.append(MOSp4)

    # plt.plot(T,R)
    # plt.show()
    # dataR = {'xOsa': T, 'yOsa': R, 'MOS': MOS}
    dataR = {'xOsa': T, 'yOsa1': R1, 'yOsa2': R2, 'yOsa3': R3, 'yOsa4': R4, 'MOS1': MOS1, 'MOS2': MOS2, 'MOS3': MOS3, 'MOS4': MOS4,}

    return dataR


# Xolr = OLR + 0.2 * (64.0 + N0 - RLR)
# Iolr = 20*(math.pow(1.0 + math.pow(Xolr/8.0, 8), 1/8) - Xolr/8.0)
# STMR0 = -10 * math.log10(math.pow(10, (-STMR/10.0))+math.exp(-T/4.0) * math.pow(10, (-TELR/10)))
# Ist = 12*(math.pow((1+math.pow((STMR0-13.0)/6.0, 8)), 1/8)) - 28*(math.pow((1+math.pow((STMR0+1.0)/19.4, 35)), 1/35)) - 13*(math.pow((1+math.pow((STMR0-3.0)/33.0, 13)), 1/13))+29.0
#
# Q = 37.0 - 15 * math.log10(qdu)
# G = 1.07 + 0.258 * Q + 0.0602 * math.pow(Q, 2)
# Y = (R0-100.0)/15.0 + 46/8.4 - G/9.0
# Z = 46.0/30.0 - G/40.0
# Iq = 15 * math.log10(1 + math.pow(10, Y) + math.pow(10, Z))
# Is = Iolr + Ist + Iq
#
# if T < 1:
#     Idte = 0.0
# else:
#     TERV = TELR - 40 * math.log10((1.0+T/10.0)/(1.0+T/150.0)) + 6*math.exp(-0.3*T*T)
#     Re = 80.0 + 2.5 * (TERV - 14.0)
#     Roe = -1.5 * (N0 - RLR)
#     Idte = ((Roe - Re)/2.0 + math.sqrt(math.pow((Roe-Re), 2)/4.0 + 100.0) - 1.0) * (1.0 - math.exp(-T))
#
# Rle = 10.5 * (WEPL + 7.0) * math.pow((Tr + 1.0), -0.25)
# Idle = (R0 - Rle)/2.0 + math.sqrt((math.pow(R0-Rle, 2))/4.0 + 169.0)
#
# if Ta <= mT:
#     Idd = 0.0      # za Ta <  mT
# else:
#     X = (math.log10(Ta/mT))/(math.log10(2))
#     Idd = 25.0*((1.0+X**6)**(1/6.0)-3*(1.0+(X/3.0)**6)**(1/6.0)+2.0)
#
# Id = Idte + Idle + Idd
#
# Ie_eff = Ie + (95.0 - Ie) * Ppl / (Ppl/BurstR + Bpl)
#
# R = R0 - Is - Id - Ie_eff + A
# print(R)
