import math

def calculate():
    # Default values of parameters
    SLR = 8                 # Send loudness rating [dB]
    RLR = 2                 # Receive loudness rating [dB]
    OLR = SLR + RLR         # Overall loudness rating [dB]
    STMR = 15               # Sidetone masking rating [dB]
    LSTR = 18               # Listener sidetone rating [dB]
    Ds = 3                  # D-Value of telephone, send side
    Dr = 3                  # D-Value of telephone, receive side
    TELR = 65               # Talker echo loudness rating [dB]
    WEPL = 110              # Weighted echo path loss [dB]
    sT = 1                  # Delay sensitivity
    mT = 100                # Minimum perceivable delay [ms]
    qdu = 1                 # Number of quantization distortion units
    Ie = 0                  # Equipment impairment factor
    Bpl = 4.3               # Packet-loss robustness factor
    Ppl = [0, 1, 2, 3]      # Random packet-loss probability [%]
    BurstR = 1              # Burst ratio
    Nc = -70                # Circuit noise referred to 0 dBr-point [dBm0p]
    Nfor = -64              # Noise floor at the receive side [dBmp]
    Ps = 35                 # Room noise at the send side [dB(A)]
    Pr = 35                 # Room noise at the receive side [dB(A)]
    A = 0                   # Advantage factor

    # Calculate R and MOS for t between 0 and 1000
    T = [t for t in range(0, 1000, 1)]

    # Defube empty lists
    Ie_eff = []

    R1 = []     # for Ppl = 0%
    R2 = []     # for Ppl = 1%
    R3 = []     # for Ppl = 2%
    R4 = []     # for Ppl = 3%

    MOS1 = []   # for Ppl = 0%
    MOS2 = []   # for Ppl = 1%
    MOS3 = []   # for Ppl = 2%
    MOS4 = []   # for Ppl = 3%

    for t in T:
        Ta = t
        Tr = 2*t
        Nfo = Nfor + RLR
        Pre = Pr + 10 * math.log10(1+math.pow(10, ((10-LSTR)/10)))/math.log10(10)
        Nor = RLR - 121 + Pre + 0.008 * math.pow((Pre - 35), 2)
        Nos = Ps - SLR - Ds - 100 + 0.004 * math.pow((Ps - OLR - Ds - 14), 2)
        No = 10*math.log10(math.pow(10, (Nc/10)) + math.pow(10, (Nos/10)) + math.pow(10, (Nor/10)) + math.pow(10, (Nfo/10)))
        Ro = 15 - (1.5 * (SLR + No))

        if qdu < 1:
            Q = 37 - 15 * math.log10(1) / math.log10(10)
        else:
            Q = 37 - 15 * math.log10(qdu) / math.log10(10)

        G = 1.07+0.258*Q+0.0602*math.pow(Q, 2)
        Z = 46/30 - G/40
        Y = (Ro-100)/15+46/8.4-G/9

        Xolr = OLR + 0.2 * (64 + No - RLR)
        Iolr = 20*(math.pow(1 + math.pow(Xolr/8, 8), 1/8) - Xolr/8)
        STMRo = -10 * math.log10(math.pow(10, (-STMR/10))+math.exp(-t/4) * math.pow(10, (-TELR/10)))
        Ist = 12*math.pow(1+pow((STMRo-13)/6, 8), 1/8)-28*math.pow(1+math.pow((STMRo+1)/19.4, 35), 1/35)-13*math.pow(1+math.pow((STMRo-3)/33, 13), 1/13)+29
        Iq = 15 * math.log10(1 + math.pow(10, Y) + math.pow(10, Z))

        Is = Iolr + Ist + Iq

        Rle = 10.5 * (WEPL + 7) * math.pow((Tr + 1), -0.25)
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
        R1.append(Rp1)
        Rp2 = Ro - Is - Id - Ie_eff[1] + A
        R2.append(Rp2)
        Rp3 = Ro - Is - Id - Ie_eff[2] + A
        R3.append(Rp3)
        Rp4 = Ro - Is - Id - Ie_eff[3] + A
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

    dataR = {'xOsa': T, 'yOsa1': R1, 'yOsa2': R2, 'yOsa3': R3, 'yOsa4': R4, 'MOS1': MOS1, 'MOS2': MOS2, 'MOS3': MOS3, 'MOS4': MOS4}

    return dataR

