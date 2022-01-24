import pandas as pd
from numpy.random import randint

#Helper function that aggregates a small number of features by adding and subtracting them
def Aggregate(df, index, featurenames, reverse):
    sum = 0
    for i in range(len(featurenames)):
        value = list(df[featurenames[i]])[index]
        if reverse[i] == 0:
            sum += value
        else:
            sum -= value
    return sum


#l1 is the first label in the pair
#l2 is the second label in the pair
#df holds the sample to be classified
#index indicates the index of the target sample in df
#Returns 1 for first label winning, -1 for second label winning

def Test(l1, l2, df, index):
    if l1 >= l2:
        print("Error, invalid labels passed in")
        return 10000
        #Should never happen, and can break logic if it does.

    if l1 == 0 and l2 == 1:
        v = list(df['GRHL2'])[index]
        if v > -1 and v < 6.5:
            return -1
        v = list(df['EEF1A2'])[index]
        if v < 0 and v > -4:
            return -1
        if v > 0 and v < 12:
            return 1

    elif l1 == 0 and l2 == 2:
        v = list(df['C2orf80'])[index]
        if v > -1.5 and v < 6.2:
            return -1
        v = list(df['ZBTB41'])[index]
        if v > 4 and v < 13:
            return -1
        features = ['GFAP', 'FAM181A', 'WDR49', 'CHI3L1', 'SOX21', 'BCAS1']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > -6 and v < 35:
            return -1
        if v < -6 and v > -23:
            return 1

    elif l1 == 0 and l2 == 3:
        v = list(df['AP1M2'])[index]
        if v > 2.1 and v < 8.5:
            return -1
        v = list(df['CYTH2'])[index]
        if v < 1 and v > -4:
            return -1
        features = ['PTPRH', 'PDCD1LG2', 'DSC2', 'IL16', 'TACR1', 'TNN']
        reverse = [0, 1, 1, 1, 1, 1]
        v = Aggregate(df, index, features, reverse)
        if v > 1 and v < 25:
            return 1
        elif v < 1 and v > -15:
            return -1

    elif l1 == 0 and l2 == 4:
        features = ['CLDN4', 'MARVELD3', 'CDH1', 'RAB25', 'C15orf48', 'NAP1L2']
        reverse = [0, 0, 0, 0, 0, 1]
        v = Aggregate(df, index, features, reverse)
        if v > 8 and v < 40:
            return -1
        elif v < 8 and v > -23:
            return 1

    elif l1 == 0 and l2 == 5:
        features = ['TUSC3', 'CLDN4', 'GPR35', 'CRB3', 'CACNA2D1', 'ATP1B2']
        reverse = [0, 1, 1, 1, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > 0 and v < 25:
            return 1
        elif v < 0 and v > -31:
            return -1

    elif l1 == 0 and l2 == 6:
        v = list(df['GRHL2'])[index]
        if v > 0 and v < 6:
            return -1
        elif v < -1 and v > -4:
            return 1

    elif l1 == 0 and l2 == 7:
        v = list(df['GRHL2'])[index]
        if v > -1 and v < 6.2:
            return -1
        if v < -1 and v > -4:
            return 1

    elif l1 == 0 and l2 == 8:
        features = ['HPN', 'CRB3', 'SPINT1', 'EMX2', 'HGD', 'DLK1']
        reverse = [0, 0, 0, 0, 0, 1]
        v = Aggregate(df, index, features, reverse)
        if v < -5 and v > -30:
            return 1
        if v > 12.5 and v < 40:
            return -1
        v = list(df['ADGB'])[index]
        if v > -2.5 and v < 3:
            return 1
        if v < -2.5 and v > -4:
            return -1

    elif l1 == 0 and l2 == 9:
        features = ['NOL3', 'SPR', 'CCDC51', 'CAMKK1', 'TPM1', 'CCND1']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > 13 and v < 30:
            return 1
        elif v < 2 and v > -24:
            return -1
        v = list(df['APIP'])[index]
        if v > -0.25 and v < 3.2:
            return -1
        if v < -0.25 and v > -4:
            return 1

    elif l1 == 0 and l2 == 10:
        v = list(df['GC'])[index]
        if v > 4.5 and v < 12.5:
            return -1
        if v < 4.5 and v > -4:
            return 1

    elif l1 == 0 and l2 == 11:
        v = list(df['GRHL2'])[index]
        if v > -1.4 and v < 6:
            return -1
        if v < -1.4 and v > -4:
            return 1

    elif l1 == 0 and l2 == 12:
        v = list(df['ANP32B'])[index]
        if v < -0.4 and v > -4:
            return -1
        if v > -0.4 and v < 6:
            return 1
        v = list(df['SASH3'])[index]
        if v > 4.5 and v < 9.5:
            return -1
        if v < 4.5 and v > -3:
            return 1

    elif l1 == 0 and l2 == 13:
        v = list(df['CLDN4'])[index]
        if v > 4 and v < 10:
            return -1
        if v < 0 and v > -4:
            return 1
        v = list(df['KLK8'])[index]
        if v < -1 and v > -4:
            return 1
        if v > -1 and v < 5.2:
            return -1

    elif l1 == 0 and l2 == 14:
        features = ['CLDN4', 'FA2H', 'SULT2B1', 'GRB7', 'HGD', 'RAB25']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v < 1 and v > -22:
            return 1
        if v > 1 and v < 36:
            return -1

    elif l1 == 0 and l2 == 15:
        v = list(df['EMC10'])[index]
        if v < -1 and v > -4:
            v = list(df['GPR180'])[index]
            if v < 3.25 and v > 0.5:
                return -1
            if v > 3.25 and v < 7:
                return 1
        elif v > -1 and v < 7:
            v = list(df['FAM222A'])[index]
            if v < 2.5 and v > -4:
                return -1
            v = list(df['JPH4'])[index]
            if v < 0 and v > -4:
                return 1
            if v > 0 and v < 8:
                return 1

    elif l1 == 0 and l2 == 16:
        v = list(df['GRHL2'])[index]
        if v > -1.5 and v < 7:
            return -1
        v = list(df['RPL37'])[index]
        if v > 1.5 and v < 8:
            return 1
        if v < 1.5 and v > -4.5:
            return -1

    elif l1 == 0 and l2 == 17:
        v = list(df['TBX15'])[index]
        if v > 1 and v < 6:
            return -1
        v = list(df['ATP6V1G1'])[index]
        if v > 4 and v < 10:
            v = list(df['MYT1'])[index]
            if v < -2 and v > -4:
                return -1
            if v > -2 and v < 5:
                return 1
        elif v < -2 and v > -4:
            return 1

    elif l1 == 0 and l2 == 18:
        features = ['BACE2', 'TFAP2A', 'FMN1', 'MITF', 'MMP14', 'HS6ST3']
        reverse = [0, 0, 0, 0, 0, 1]
        v = Aggregate(df, index, features, reverse)
        if v < 10 and v > -20:
            return 1
        if v > 10 and v < 40:
            return -1

    elif l1 == 0 and l2 == 19:
        features = ['AGR2', 'TMC5', 'PRR15L', 'AGR3', 'FA2H', 'LGALS4']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v < -10 and v > -23:
            return 1
        if v > -10 and v < 50:
            return -1

    elif l1 == 0 and l2 == 20:
        v = list(df['CDH3'])[index]
        if v > 1 and v < 6:
            return -1
        if v < 1 and v > -4:
            return 1

    elif l1 == 0 and l2 == 21:
        v = list(df['CLIC3'])[index]
        if v > 2 and v < 12:
            return -1
        if v < 2 and v > -4:
            return 1

    elif l1 == 0 and l2 == 22:
        features = ['CDH3', 'CLDN4', 'IGSF9', 'SPINT1', 'GRHL2', 'ST14']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > -1 and v < 42:
            return -1
        v = list(df['TEAD3'])[index]
        if v > 4 and v < 7:
            return -1
        if v < 4 and v > -4:
            return 1

    elif l1 == 1 and l2 == 2:
        features = ['AQP4', 'MLC1', 'C1orf61', 'MT3', 'NCAN', 'LAD1']
        reverse = [0, 0, 0, 0, 0, 1]
        v = Aggregate(df, index, features, reverse)
        if v > 0 and v < 50:
            return -1
        if v < 0 and v > -30:
            return 1

    elif l1 == 1 and l2 == 3:
        features = ['KIAA1324', 'PRLR', 'TMEM63C', 'LMX1B', 'LRIG1', 'GJB6']
        reverse = [0, 0, 0, 0, 0, 1]
        v = Aggregate(df, index, features, reverse)
        if v > 9 and v < 33:
            return -1
        if v < -7 and v > -23:
            return 1
        features = ['SFRP1', 'MRAS', 'ZFP3', 'FZD7', 'MGP', 'AIF1L']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v < -15 and v > -23:
            return -1
        v = list(df['ZNF879'])[index]
        if v < -1.5 and v > -3.2:
            return 1
        v = list(df['IRX1'])[index]
        if v > -2.2 and v < 8:
            return -1
        if v < -2.2 and v > -4:
            return 1


    elif l1 == 1 and l2 == 4:
        features = ['PPARG', 'GATA3', 'MFAP3L', 'CAB39L', 'TBX3', 'TBX2']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v < -8 and v > -21:
            return -1
        if v > 15 and v < 40:
            return 1
        v = list(df['TBX5'])[index]
        if v > -2.1 and v < 4:
            return 1
        v = list(df['ZFY'])[index]
        if v > -2.9 and v < 3.5:
            return 1
        v = list(df['ZFR2'])[index]
        if v > -2.2 and v < 3.7:
            return -1
        v = list(df['TBX5'])[index]
        if v > -2.9 and v < -2:
            return 1
        if v < -2.9 and v > -3.1:
            return -1
        if v < -3.1 and v > -3.4:
            return -1

    elif l1 == 1 and l2 == 5:
        features = ['HNF1A', 'HNF4A', 'VIL1', 'GPR35', 'DDC', 'CDX1']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > 5 and v < 40:
            return -1
        v = list(df['NCKAP1'])[index]
        if v < -0.5 and v > -4:
            return -1
        if v > -0.5 and v < 5:
            return 1


    elif l1 == 1 and l2 == 6:
        features = ['POTEJ', 'POTEI', 'EIF3CL', 'F8A3', 'POTEE', 'MTRNR2L8']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > -12 and v < 4:
            return -1
        if v < -12 and v > -20:
            return 1

    elif l1 == 1 and l2 == 7:
        features = ['PTPRZ1', 'GOLT1A', 'GBP6', 'PPARG', 'GATA3', 'ACSF2']
        reverse = [0, 1, 0, 1, 1, 1]
        v = Aggregate(df, index, features, reverse)
        if v < -13 and v > -35:
            return 1
        v = list(df['CELSR2'])[index]
        if v < -2 and v > -4:
            return -1
        v = list(df['CHRM2'])[index]
        if v > -2.8 and v < 4:
            return 1
        v = list(df['IRX1'])[index]
        if v > -2.4 and v < 6:
            return -1
        v = list(df['TCF21'])[index]
        if v > -2.25 and v < 1:
            return 1
        if v < -2.25 and v > -3.1:
            return 1
        if v < -3.1 and v > -3.5:
            return -1

    elif l1 == 1 and l2 == 8:
        v = list(df['MTA2'])[index]
        if v < 3.5 and v > -4:
            return -1
        features = ['CDH16', 'POU3F3', 'HPN', 'HGD', 'PAX2', 'SLC3A1']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > -2 and v < 44:
            return -1
        v = list(df['C3orf62'])[index]
        if v < -3 and v > -4:
            return -1
        if v > -1 and v < 4:
            return 1

    elif l1 == 1 and l2 == 9:
        v = list(df['ERBB2'])[index]
        if v > 1 and v < 12:
            return 1
        if v < 1 and v > -4:
            return -1

    elif l1 == 1 and l2 == 10:
        v = list(df['VTN'])[index]
        if v > 5.5 and v < 14:
            return -1
        if v < 5.5 and v > -4:
            return 1

    elif l1 == 1 and l2 == 11:
        features = ['SLC34A2', 'SFTA3', 'SFTPA2', 'SLC22A31', 'SFTPB', 'SFTPA1']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > -3 and v < 70:
            return -1
        v = list(df['ACTL6A'])[index]
        if v > 6 and v < 8.5:
            return -1
        v = list(df['ACOX3'])[index]
        if v > 2.9 and v < 7:
            return 1
        v = list(df['DES'])[index]
        if v > 2.5 and v < 15:
            return 1
        v = list(df['IRX2'])[index]
        if v > 3.5 and v > 6:
            return 1
        if v < 3.5 and v > -4:
            return 1

    elif l1 == 1 and l2 == 12:
        v = list(df['TEAD3'])[index]
        if v > 2 and v < 8:
            return 1
        if v < 2 and v > -4:
            return -1

    elif l1 == 1 and l2 == 13:
        features = ['ZNF467', 'WT1', 'SLC34A2', 'CRB2', 'S100P', 'FERMT1']
        reverse = [0, 0, 0, 0, 1, 1]
        v = Aggregate(df, index, features, reverse)
        if v > 1 and v < 31:
            return -1
        if v < 1 and v > -30:
            return 1

    elif l1 == 1 and l2 == 14:
        features = ['FOXA3', 'HNF1A', 'SLC6A20', 'TM4SF4', 'MYRF', 'HGD']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > 0 and v < 30:
            return -1
        if v < 0 and v > -21:
            return 1

    elif l1 == 1 and l2 == 15:
        features = ['ESRP2', 'RAB25', 'GRHL2', 'KDF1', 'EPN3', 'ERBB3']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > 0 and v < 40:
            return 1
        v = list(df['G6PD'])[index]
        if v > 6.5 and v < 10:
            return 1
        if v < -1.5 and v > -4:
            return -1
        if v > 1 and v < 6.5:
            return -1

    elif l1 == 1 and l2 == 16:
        features = ['SLC45A3', 'STEAP2', 'CREB3L4', 'ABCC4', 'ANO7', 'KLK2']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v < 55 and v > 20:
            return -1
        if v < 20 and v > -10:
            return 1
        if v < -10 and v > -25:
            return -1

    elif l1 == 1 and l2 == 17:
        v = list(df['GRHL2'])[index]
        if v > 0.5 and v < 6.2:
            return 1
        v = list(df['OLFML2B'])[index]
        if v < -1 and v > -4:
            return -1
        v = list(df['ZIC1'])[index]
        if v > -2 and v < 6:
            return -1
        v = list(df['SLC7A14'])[index]
        if v > -1 and v < 4:
            return -1
        if v < -2 and v > -4:
            return 1

    elif l1 == 1 and l2 == 18:
        v = list(df['TYR'])[index]
        if v > -0.5 and v < 12:
            return -1
        features = ['KRT19', 'RAB25', 'AP1M2', 'TACSTD2', 'KDF1', 'ELF3']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > 0 and v < 50:
            return 1
        v = list(df['HPD'])[index]
        if v > -1 and v < 5:
            return 1
        if v < -1 and v > -4:
            return -1

    elif l1 == 1 and l2 == 19:
        v = list(df['HNF1A'])[index]
        if v > 0 and v < 5:
            return -1
        v = list(df['POTEJ'])[index]
        if v > -2.65 and v < 0:
            return -1
        v = list(df['HOXA11'])[index]
        if v < -2.5 and v > -4:
            return -1
        if v > -2.5 and v < 5:
            return 1

    elif l1 == 1 and l2 == 20:
        features = ['PHC1', 'L1TD1', 'TET1', 'CACNA2D2', 'SLC4A8', 'VRTN']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > 0 and v < 40:
            return -1
        if v < 0 and v > -20:
            return 1

    elif l1 == 1 and l2 == 21:
        v = list(df['TSHR'])[index]
        if v > 2 and v < 9:
            return -1
        if v < 2 and v > -4:
            return 1

    elif l1 == 1 and l2 == 22:
        features = ['SALL1', 'ASRGL1', 'STXBP6', 'SLC34A2', 'ARHGAP23', 'CSTA']
        reverse = [0, 0, 0, 0, 1, 1]
        v = Aggregate(df, index, features, reverse)
        if v > 5 and v < 30:
            return -1
        if v < -12 and v > -24:
            return 1
        v = list(df['PSCA'])[index]
        if v > 2.5 and v < 15:
            return 1
        v = list(df['EMX2'])[index]
        if v > -2 and v < 8:
            return -1
        if v < -2 and v > -4:
            return 1

    elif l1 == 2 and l2 == 3:
        v = list(df['CLDN4'])[index]
        if v > 2 and v < 10:
            return -1
        v = list(df['C2orf80'])[index]
        if v > -2 and v < 6:
            return 1
        if v < -2 and v > -4:
            return -1


    elif l1 == 2 and l2 == 4:
        v = list(df['CLDN4'])[index]
        if v > 2 and v < 10:
            return -1
        if v < 2 and v > -4:
            return 1

    elif l1 == 2 and l2 == 5:
        v = list(df['CLDN4'])[index]
        if v > 2 and v < 10:
            return -1
        if v < 2 and v > -4:
            return 1

    elif l1 == 2 and l2 == 6:
        v = list(df['ESRP2'])[index]
        if v > -0.5 and v < 6:
            return -1
        if v < -0.5 and v > -4:
            return 1

    elif l1 == 2 and l2 == 7:
        v = list(df['OLIG2'])[index]
        if v > 2 and v < 10:
            return 1
        v = list(df['CLDN4'])[index]
        if v > 0 and v < 10:
            return -1
        v = list(df['C8B'])[index]
        if v > 2 and v < 9:
            return 1
        if v < 2 and v > -2:
            return -1
        if v < -2 and v > -4:
            return -1

    elif l1 == 2 and l2 == 8:
        v = list(df['GFAP'])[index]
        if v > 4.5 and v < 15:
            return 1
        v = list(df['LSMEM2'])[index]
        if v > 1 and v < 6:
            return 1
        if v < 1 and v > -4:
            return -1

    elif l1 == 2 and l2 == 9:
        features = ['SPAG16', 'MAP1B', 'APC2', 'SMAD9', 'TLN2', 'OSBPL6']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > 2 and v < 27:
            return 1
        v = list(df['FAM86C1'])[index]
        if v < 4 and v > -4:
            return -1
        if v > 4 and v < 9:
            return 1

    elif l1 == 2 and l2 == 10:
        features = ['SCRG1', 'PTPRZ1', 'C1orf61', 'AMBP', 'HNF4A', 'FAM181B']
        reverse = [0, 0, 0, 1, 1, 0]
        v = Aggregate(df, index, features, reverse)
        if v > 5 and v < 40:
            return 1
        if v < 5 and v > -40:
            return -1

    elif l1 == 2 and l2 == 11:
        v = list(df['CLDN4'])[index]
        if v > 0.5 and v < 10:
            return -1
        if v < 0.5 and v > -4:
            return 1

    elif l1 == 2 and l2 == 12:
        v = list(df['APP'])[index]
        if v > 5 and v < 11:
            return 1
        if v < 5 and v > -4:
            return -1

    elif l1 == 2 and l2 == 13:
        v = list(df['SCNN1A'])[index]
        if v > 0 and v < 9:
            return -1
        if v < 0 and v > -4:
            return 1

    elif l1 == 2 and l2 == 14:
        v = list(df['CLDN4'])[index]
        if v > 2 and v < 10:
            return -1
        if v < 2 and v > -4:
            return 1

    elif l1 == 2 and l2 == 15:
        features = ['C2orf80', 'OLIG1', 'C1orf61', 'MAP2', 'OLIG2', 'PTPRZ1']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v < 0 and v > -22:
            return -1
        if v > 5 and v < 50:
            return 1
        features = ['EIF2B5', 'MSL3', 'C11orf71', 'NEMP2', 'ZBTB41', 'MCM8']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v < 0 and v > -20:
            return -1
        if v > 0 and v < 60:
            return 1


    elif l1 == 2 and l2 == 16:
        features = ['SCNN1A', 'CLDN4', 'C1orf61', 'TACSTD2', 'AP1M2', 'PRR15L']
        reverse = [0, 0, 1, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > -2 and v < 40:
            return -1
        if v < -2 and v > -30:
            return 1

    elif l1 == 2 and l2 == 17:
        v = list(df['AQP4'])[index]
        if v > 4 and v < 12:
            return 1
        if v < 0.5 and v > -4:
            return -1
        v = list(df['ZBTB42'])[index]
        if v > -2.5 and v < 2:
            return 1
        if v < -2.5 and v > -4:
            return -1

    elif l1 == 2 and l2 == 18:
        features = ['AQP4', 'C1orf61', 'GRIK5', 'NCAN', 'GFAP', 'MLC1']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > 5 and v < 55:
            return 1
        if v < 5 and v > -25:
            return -1

    elif l1 == 2 and l2 == 19:
        features = ['AQP4', 'C1orf61', 'GRIK5', 'NCAN', 'GFAP', 'MLC1']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > 5 and v < 55:
            return 1
        if v < 5 and v > -25:
            return -1

    elif l1 == 2 and l2 == 20:
        v = list(df['CLDN6'])[index]
        if v > 0 and v < 10:
            return -1
        if v < 0 and v > -4:
            return 1

    elif l1 == 2 and l2 == 21:
        v = list(df['LAMC2'])[index]
        if v > 1 and v < 10:
            return -1
        if v < 1 and v > -4:
            return 1

    elif l1 == 2 and l2 == 22:
        v = list(df['PTPRZ1'])[index]
        if v > 5 and v < 11:
            return 1
        if v < 1 and v > -4:
            return -1
        v = list(df['TXNRD3'])[index]
        if v < -1.5 and v > -4:
            return -1
        if v > 3 and v < 10:
            return 1
        v = list(df['CDH3'])[index]
        if v > 1.5 and v < 7:
            return -1
        if v < 1.5 and v > -4:
            return 1

    elif l1 == 3 and l2 == 4:
        v = list(df['CDCA4'])[index]
        if v < -1.5 and v > -4:
            v = list(df['SLAMF7'])[index]
            if v < 0.5 and v > -4:
                return -1
            v = list(df['HRH1'])[index]
            if v > 0.5 and v < 5:
                return -1
            if v < 0.5 and v > -4:
                return 1
        elif v > -1.5 and v < 7:
            v = list(df['TBX5'])[index]
            if v > -2.2 and v < 3:
                return 1
            v = list(df['SERPINB13'])[index]
            if v > -0.5 and v < 10:
                return -1
            features = ['AARD', 'TRPS1', 'ID1', 'ST6GALNAC1', 'TMPRSS4', 'PCSK9']
            reverse = [0, 0, 1, 1, 1, 1]
            v = Aggregate(df, index, features, reverse)
            if v < -1 and v > -30:
                return -1
            if v > -1 and v < 30:
                return 1


    elif l1 == 3 and l2 == 5:
        features = ['HNF4A', 'EPS8L3', 'VIL1', 'HNF1A', 'IHH', 'CDX2']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > 0 and v < 41:
            return -1
        features = ['SLC22A25', 'GANAB', 'ADGRE3', 'AIRE', 'OR5K1', 'FGF19']
        reverse = [0, 1, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > 20 and v < 40:
            return -1
        if v < 20 and v > -30:
            return 1

    elif l1 == 3 and l2 == 6:
        features = ['F8A3', 'GJD3', 'EIF3CL', 'RPS4Y1', 'DUOXA2', 'ZFY']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > -11.5 and v < 15:
            return -1
        if v < -11.5 and v > -23:
            return 1

    elif l1 == 3 and l2 == 7:
        features = ['IL1A', 'IL36G', 'C10orf99', 'SERPINB13', 'PLA2G4E', 'CERS3']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > 5 and v < 47:
            return -1
        features = ['ZNF24', 'WASL', 'SCAMP1', 'WAPL', 'SS18', 'UBA3']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > -9 and v < 9:
            return -1
        if v > 9 and v < 35:
            v = list(df['ZFY'])[index]
            if v < -2.2 and v > -4:
                return 1
            if v > -2.2 and v < 3.2:
                return -1
        elif v < -9 and v > -22:
            v = list(df['WDFY4'])[index]
            if v > -2.3 and v < 4.5:
                return -1
            if v < -2.3 and v > -4:
                return 1

    elif l1 == 3 and l2 == 8:
        features = ['EMX2', 'SALL1', 'OGDHL', 'POU3F3', 'SLC22A2', 'SULT1C2']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > 17 and v < 40:
            return -1
        if v < 0 and v > -23:
            return 1
        features = ['CATSPER1', 'OR4F6', 'PTP4A2', 'ST3GAL5', 'LSMEM2', 'TAZ']
        reverse = [0, 0, 1, 1, 0, 1]
        v = Aggregate(df, index, features, reverse)
        if v > 5 and v < 25:
            return 1
        if v < 5 and v > -22:
            return -1

    elif l1 == 3 and l2 == 9:
        features = ['FKBP10', 'COL4A2', 'CLDN4', 'TMEM54', 'COL3A1', 'COL1A2']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > 15 and v < 50:
            return 1
        features = ['MEP1A', 'GAPDHS', 'KLK10', 'DPYSL5', 'RHBG', 'DCT']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > 1 and v < 30:
            return 1
        if v < 1 and v > -23:
            return -1

    elif l1 == 3 and l2 == 10:
        v = list(df['GC'])[index]
        if v > 4 and v < 12.5:
            return -1
        if v < 4 and v > -4:
            return 1

    elif l1 == 3 and l2 == 11:
        features = ['FOXF1', 'TBX4', 'SFTPA1', 'SFTPB', 'SFTPC', 'KCNJ15']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > 0 and v < 56:
            return -1
        features = ['CREB3L4', 'TSTD1', 'ARFIP2', 'DLG3', 'ERGIC1', 'SELENBP1']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > -14.5 and v < 2:
            return -1
        elif v < -14.5 and v > -23:
            return 1
        elif v > 2 and v < 42:
            v = list(df['FOXE1'])[index]
            if v > 1 and v < 8:
                return -1
            v = list(df['GATA3'])[index]
            if v > 4 and v < 10.5:
                return 1
            features = ['SFTPB', 'SFTPA1', 'SFTPA2', 'WDR72', 'MAP3K19', 'ANKRD18B']
            reverse = [0, 0, 0, 0, 0, 0]
            v = Aggregate(df, index, features, reverse)
            if v > -7.5 and v < 12:
                return -1
            if v < -7.5 and v > -21:
                return 1


    elif l1 == 3 and l2 == 12:
        features = ['ST6GALNAC2', 'SLC2A10', 'IRX5', 'CCDC149', 'GATA3', 'HID1']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > 0 and v < 40:
            return 1
        features = ['TREML4', 'WNT7A', 'DPYSL5', 'ARL17A', 'MEP1A', 'OR4F6']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v < 0 and v > -22:
            return -1
        if v > 0 and v < 30:
            return 1

    elif l1 == 3 and l2 == 13:
        features = ['EMX2', 'FAM181A', 'CLDN16', 'KLHL14', 'WNT7A', 'UPK3B']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > 5 and v < 40:
            return -1
        features = ['SQSTM1', 'DCP1A', 'ANO10', 'TTLL8', 'SGTA', 'PPA2']
        reverse = [0, 0, 0, 1, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > -13.5 and v < 9:
            return -1
        elif v < -13.5 and v > -23:
            return 1
        elif v > 12 and v < 30:
            v = list(df['F8A3'])[index]
            if v > -2.4 and v < 0.5:
                return -1
            if v < -2.4 and v > -3.5:
                return 1

    elif l1 == 3 and l2 == 14:
        v = list(df['SPINK1'])[index]
        if v > 4 and v < 14:
            return -1
        v = list(df['MAK16'])[index]
        if v < 0 and v > -4:
            return -1
        features = ['USH1C', 'SMIM24', 'FOXA2', 'HKDC1', 'LGALS4', 'HHLA2']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > 1 and v < 40:
            return -1
        if v < 1 and v > -23:
            return 1

    elif l1 == 3 and l2 == 15:
        v = list(df['PRSS8'])[index]
        if v > 0 and v < 10:
            return 1
        v = list(df['UBE2R2'])[index]
        if v > -1 and v < 3:
            return -1
        elif v < -1 and v > -4:
            v = list(df['RAX'])[index]
            if v > -2.2 and v < 1:
                return -1
            if v < -2.2 and v > -4:
                return 1
        elif v > 3 and v < 6.5:
            v = list(df['FAM166B'])[index]
            if v > -0.5 and v < 7:
                return 1
            if v < -0.5 and v > -4:
                return -1

    elif l1 == 3 and l2 == 16:
        v = list(df['KLK2'])[index]
        if v > 5 and v < 12:
            return -1
        v = list(df['DDX3Y'])[index]
        if v < -0.5 and v > -4:
            return 1
        features = ['TMEFF2', 'SRL', 'TBX19', 'AGBL4', 'RHAG', 'WNK3']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > -10 and v < 28:
            return -1
        if v < -10 and v > -22:
            return 1

    elif l1 == 3 and l2 == 17:
        v = list(df['PROM2'])[index]
        if v > 1 and v < 8:
            return 1
        v = list(df['MMP21'])[index]
        if v > 0.5 and v < 8:
            return 1
        v = list(df['EPB42'])[index]
        if v > -1 and v < 1.5:
            return 1
        v = list(df['LPAR3'])[index]
        if v > -0.5 and v < 4:
            return 1
        if v < -0.5 and v > -2.8:
            return -1
        if v < -2.8 and v > -4:
            return -1

    elif l1 == 3 and l2 == 18:
        v = list(df['KIAA1324'])[index]
        if v > 2 and v < 9:
            return 1
        v = list(df['GJB1'])[index]
        if v > 0 and v < 9:
            return -1
        v = list(df['GRHL2'])[index]
        if v > 1.5 and v < 5:
            return 1
        v = list(df['DMGDH'])[index]
        if v > 0 and v < 3:
            return 1
        if v < 0 and v > -4:
            return -1


    elif l1 == 3 and l2 == 19:
        features = ['FOXF1', 'ISL1', 'LGALS4', 'GJD3', 'CDHR5', 'CTSE']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > -5 and v < 36:
            return -1
        if v < -5 and v > -22:
            return 1

    elif l1 == 3 and l2 == 20:
        v = list(df['GDF3'])[index]
        if v > 0.5 and v < 12:
            return -1
        v = list(df['ZFY'])[index]
        if v < -1 and v > -4:
            return 1
        if v > -1 and v < 3:
            return -1

    elif l1 == 3 and l2 == 21:
        v = list(df['PAX8'])[index]
        if v < 3.5 and v > -4:
            return 1
        if v > 3.5 and v < 10:
            return -1

    elif l1 == 3 and l2 == 22:
        features = ['MECOM', 'SOX17', 'MEIS1', 'CFI', 'FGF18', 'ID1']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > 20 and v < 42:
            return -1
        elif v < 20 and v > -10:
            features = ['IRX2', 'C5orf38', 'AZGP1', 'LMX1B', 'KIAA1324', 'CLMN']
            reverse = [0, 0, 0, 0, 0, 0]
            v = Aggregate(df, index, features, reverse)
            if v > 10 and v < 45:
                return 1
            v = list(df['ZCCHC12'])[index]
            if v > 0 and v < 10:
                return -1
            v = list(df['IRX1'])[index]
            if v < -3 and v > -4:
                return -1
            if v > -3 and v < 6:
                return 1
        elif v < -10 and v > -22:
            v = list(df['WNT3A'])[index]
            if v > -1 and v < 4:
                return -1
            if v < -1 and v > -4:
                return 1

    elif l1 == 4 and l2 == 5:
        features = ['ISX', 'FABP1', 'SLC39A5', 'GUCA2A', 'NR1I2', 'CDX2']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > -5 and v < 50:
            return -1
        features = ['MATN3', 'TMEM106C', 'TMEM232', 'SLC22A25', 'INPP5E', 'CTRL']
        reverse = [0, 1, 0, 0, 1, 0]
        v = Aggregate(df, index, features, reverse)
        if v > 15 and v < 30:
            return -1
        if v > -9 and v < 15:
            return 1
        if v < -9 and v > -24:
            v = list(df['ZFY'])[index]
            if v > -2.5 and v < 3:
                return -1
            if v < -2.5 and v > -4:
                return 1

    elif l1 == 4 and l2 == 6:
        features = ['F8A3', 'EIF3CL', 'GJD3', 'POTEI', 'NPIPB12', 'RPS4Y1']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v < -12.5 and v > -23:
            return 1
        if v > -12.5 and v < 7:
            return -1

    elif l1 == 4 and l2 == 7:
        v = list(df['NLGN4Y'])[index]
        if v > -2.5 and v < 3:
            return -1
        v = list(df['HMGN1'])[index]
        if v > 2 and v < 8:
            v = list(df['LHX8'])[index]
            if v > -2.5 and v < 1:
                return -1
            features = ['E2F1', 'DSN1', 'UBE2T', 'RFC4', 'CDC25C', 'LIG1']
            reverse = [0, 0, 0, 0, 0, 0]
            v = Aggregate(df, index, features, reverse)
            if v < 17.5 and v > 0:
                return -1
            v = list(df['TRDN'])[index]
            if v > -2.5 and v < 4:
                return -1
            if v < -2.5 and v > -4:
                return 1
        elif v < -2 and v > -4:
            v = list(df['PRRC2A'])[index]
            if v > -2 and v < 5:
                return -1
            if v < -2 and v > -4:
                return 1

    elif l1 == 4 and l2 == 8:
        features = ['PITX1', 'HPN', 'KLK10', 'SERPINB3', 'KIF2C', 'EMX2']
        reverse = [0, 1, 0, 0, 0, 1]
        v = Aggregate(df, index, features, reverse)
        if v > 10 and v < 40:
            return 1
        if v < -10 and v > -30:
            return -1
        v = list(df['WDR46'])[index]
        if v < 3 and v > -4:
            return -1
        v =list(df['KDELR1'])[index]
        if v > 4 and v < 9:
            v = list(df['OVOL2'])[index]
            if v > 1 and v < 5:
                return 1
            if v < 1 and v > -4:
                return -1
        elif v < 4 and v > -4:
            v = list(df['CLDN4'])[index]
            if v > 3 and v < 8:
                return 1
            if v < 3 and v > -4:
                return -1

    elif l1 == 4 and l2 == 9:
        features = ['CLDN4', 'HRH1', 'RAB25', 'RND3', 'KLK10', 'TMPRSS4']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > 1 and v < 40:
            return 1
        if v < 1 and v > -23:
            return -1

    elif l1 == 4 and l2 == 10:
        v = list(df['APOB'])[index]
        if v < 2 and v > -4:
            return 1
        if v > 2 and v < 11:
            return -1

    elif l1 == 4 and l2 == 11:
        features = ['TBX5', 'SCN7A', 'TCF21', 'SFTPA2', 'TMEM119', 'TBX4']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > 3 and v < 40:
            return -1
        v = list(df['UTY'])[index]
        if v > -3 and v < 3:
            return -1
        features = ['DHRS1', 'SLC25A28', 'PPDPF', 'ACTB', 'CAPZB', 'MAT2B']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > -8 and v < 20:
            return -1
        if v < -8 and v > -23:
            return 1
        v = list(df['TBX5'])[index]
        if v > -2 and v < 2:
            return -1
        if v < -2 and v > -4:
            return 1

    elif l1 == 4 and l2 == 12:
        v = list(df['IRF6'])[index]
        if v > 1.5 and v < 10:
            return 1
        features = ['BMP6', 'ADAM12', 'PLOD3', 'SP6', 'UNC119B', 'MEP1A']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > 10 and v < 35:
            return 1
        if v < 10 and v > -21:
            return -1

    elif l1 == 4 and l2 == 13:
        v = list(df['BET1'])[index]
        if v > 4 and v < 8:
            return -1
        if v < -0.2 and v > -4:
            return 1
        features = ['ZBTB20', 'WT1', 'SERPINB3', 'DOK5', 'ZNF467', 'SERPINB4']
        reverse = [0, 0, 1, 0, 0, 1]
        v = Aggregate(df, index, features, reverse)
        if v < 0 and v > -30:
            return 1
        if v > 12 and v < 30:
            return -1
        v = list(df['BCAR1'])[index]
        if v < -0.5 and v > -4:
            return -1
        if v > -0.5 and v < 1.8:
            return 1
        v = list(df['LMNB1'])[index]
        if v > 4.75 and v < 6.5:
            return 1
        if v < 4.75 and v > 1.5:
            return -1
        if v < 1.5 and v > -1:
            return 1

    elif l1 == 4 and l2 == 14:
        v = list(df['MIS18A'])[index]
        if v > 0 and v < 8:
            v = list(df['AUNIP'])[index]
            if v > 0.8 and v < 4.5:
                return 1
            if v < 0.8 and v > -3:
                return -1
        elif v < -1.5 and v > -4:
            features = ['NUBP1', 'ATAD3B', 'SLC33A1', 'PIP5K1C', 'ERBB4', 'TRABD']
            reverse = [0, 0, 0, 0, 1, 1]
            v = Aggregate(df, index, features, reverse)
            if v > 5 and v < 25:
                return 1
            if v < 5 and v > -16:
                return -1

    elif l1 == 4 and l2 == 15:
        features = ['SPINT2', 'LSR', 'MAPK13', 'PRRG2', 'HMGA1', 'ABHD17C']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > 21 and v < 40:
            return 1
        if v < 21 and v > -10:
            return -1
        features = ['CCDC126', 'CD22', 'DCAF12L2', 'FAM216A', 'MED1', 'CLDN4']
        reverse = [0, 0, 0, 0, 0, 1]
        v = Aggregate(df, index, features, reverse)
        if v > -9 and v < 30:
            return -1
        if v < -9 and v > -30:
            return 1

    elif l1 == 4 and l2 == 16:
        features = ['DDX3Y', 'USP9Y', 'CUX2', 'KDM5D', 'KIF2C', 'EIF1AY']
        reverse = [0, 0, 0, 0, 1, 0]
        v = Aggregate(df, index, features, reverse)
        if v > 0.5 and v < 21:
            return -1
        if v < 0.5 and v > -25:
            return 1


    elif l1 == 4 and l2 == 17:
        v = list(df['SPINT2'])[index]
        if v > 5.5 and v < 10.5:
            return 1
        if v < 5.5 and v > -3:
            return -1
        if v < -3 and v > -4:
            return 1

    elif l1 == 4 and l2 == 18:
        v = list(df['SPINT2'])[index]
        if v > 5.5 and v < 10.5:
            return 1
        if v < 5.5 and v > -3:
            return -1
        if v < -3 and v > -4:
            return 1

    elif l1 == 4 and l2 == 19:
        v = list(df['PRDX5'])[index]
        if v < -2 and v > -4:
            return 1
        v = list(df['POTEJ'])[index]
        if v > -2.75 and v < 0.5:
            return -1
        v = list(df['DDX3Y'])[index]
        if v > -1.5 and v < 4:
            return -1
        v = list(df['PDXP'])[index]
        if v > 1 and v < 3:
            return -1
        if v < 1 and v > -4:
            return 1

    elif l1 == 4 and l2 == 20:
        v = list(df['ZFY'])[index]
        if v < -2.5 and v > -4:
            return 1
        if v > -2.5 and v < 3:
            return -1

    elif l1 == 4 and l2 == 21:
        v = list(df['TG'])[index]
        if v < 2.5 and v > -5:
            return 1
        if v > 2.5 and v < 15:
            return -1

    elif l1 == 4 and l2 == 22:
        v = list(df['SERPINB3'])[index]
        if v > 6 and v < 12:
            return 1
        features = ['ZSCAN18', 'ZNF610', 'ZNF43', 'VPS37D', 'ZNF135', 'CHST10']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v < -3 and v > -16:
            return 1
        v = list(df['PIM1'])[index]
        if v < -1 and v > -4:
            return -1
        features = ['ZNF541', 'SYCP2', 'SMC1B', 'ITGA2B', 'KLHL35', 'ZFR2']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > 10 and v < 22:
            return 1
        if v < 10 and v > -20:
            return -1

    elif l1 == 5 and l2 == 6:
        features = ['POTEI', 'EEF1G', 'DUOX1', 'F8A3', 'NBPF26', 'EIF3CL']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v < -7.5 and v > -22:
            return 1
        if v > -7.5 and v < 5:
            return -1

    elif l1 == 5 and l2 == 7:
        v = list(df['EPS8L3'])[index]
        if v > 1.5 and v < 8:
            return 1
        features = ['EXOC6', 'AIRE', 'RFNG', 'LUZP2', 'RPS6KA4', 'GANAB']
        reverse = [0, 0, 1, 0, 1, 1]
        v = Aggregate(df, index, features, reverse)
        if v > 10 and v < 30:
            return 1
        if v < 10 and v > -30:
            return -1

    elif l1 == 5 and l2 == 8:
        v = list(df['CDX1'])[index]
        if v > 2 and v < 9:
            return 1
        features = ['RRP7A', 'RSPH3', 'COX10', 'HEATR5A', 'TMEM164', 'EOMES']
        reverse = [0, 0, 0, 1, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > 17 and v < 50:
            return 1
        if v < 0 and v > -21:
            return -1
        v = list(df['MYB'])[index]
        if v > 2 and v < 5:
            return 1
        if v < 2 and v > -4:
            return -1

    elif l1 == 5 and l2 == 9:
        v = list(df['CLDN4'])[index]
        if v > 3 and v < 10:
            return 1
        if v < 3 and v > -4.2:
            return -1

    elif l1 == 5 and l2 == 10:
        v = list(df['GC'])[index]
        if v > 4 and v < 12.5:
            return -1
        if v < 4 and v > -4:
            return 1

    elif l1 == 5 and l2 == 11:
        v = list(df['ANKRD6'])[index]
        if v > 4.25 and v < 8:
            v = list(df['UBA1'])[index]
            if v > 1 and v < 11:
                return -1
            if v < 1 and v > -4:
                return 1
        elif v < 4.25 and v > -4:
            features = ['CDX1', 'CDX2', 'PHGR1', 'MOGAT3', 'CLRN3', 'FABP1']
            reverse = [0, 0, 0, 0, 0, 0]
            v = Aggregate(df, index, features, reverse)
            if v > 5 and v < 50:
                return 1
            if v < 5 and v > -23:
                return -1

    elif l1 == 5 and l2 == 12:
        v = list(df['FUT2'])[index]
        if v > 0 and v < 7.5:
            return 1
        v = list(df['ZPR1'])[index]
        if v < -0.5 and v > -4:
            return -1
        if v > -0.5 and v < 2.8:
            return 1
        if v > 2.8 and v < 5:
            return -1

    elif l1 == 5 and l2 == 13:
        features = ['EMX2', 'SLC34A2', 'SCGB1D2', 'EPS8L3', 'HNF4A', 'KLHL14']
        reverse = [0, 0, 0, 1, 1, 0]
        v = Aggregate(df, index, features, reverse)
        if v > 10 and v < 40:
            return -1
        if v < -5 and v > -30:
            return 1
        v = list(df['YWHAB'])[index]
        if v < 1 and v > -4:
            return -1
        if v > 1 and v < 8:
            return 1

    elif l1 == 5 and l2 == 14:
        v = list(df['SLC5A6'])[index]
        if v > 0 and v < 8:
            features = ['MYB', 'TRABD2A', 'CDX1', 'PDSS1', 'CDX2', 'NOX1']
            reverse = [0, 0, 0, 0, 0, 0]
            v = Aggregate(df, index, features, reverse)
            if v > 20 and v < 40:
                return 1
            v = list(df['CLDN10'])[index]
            if v > -1 and v < 7:
                return -1
            if v < -1 and v > -4:
                return 1
        if v < 0 and v > -4:
            features = ['WDR34', 'RTEL1-TNFRSF6B', 'PJA2', 'GNL3L', 'LMAN2L', 'OLFM3']
            reverse = [0, 0, 0, 0, 1, 0]
            v = Aggregate(df, index, features, reverse)
            if v > -3 and v < 30:
                return 1
            if v < -3 and v > -25:
                return -1

    elif l1 == 5 and l2 == 15:
        v = list(df['SLC25A15'])[index]
        if v > -2.25 and v < 6:
            v = list(df['GPA33'])[index]
            if v > 0 and v < 10:
                return 1
            if v < 0 and v > -4:
                return -1
        elif v < -2.25 and v > -4:
            v = list(df['FAM83A'])[index]
            if v > 0 and v < 8:
                return 1
            if v < 0 and v > -4:
                return -1

    elif l1 == 5 and l2 == 16:
        v = list(df['CDX1'])[index]
        if v > 3 and v < 9:
            return 1
        v = list(df['AIRE'])[index]
        if v > 3 and v < 8.5:
            return 1
        if v < 3 and v > -2:
            return -1
        features = ['SUOX', 'DLG2', 'TUBGCP2', 'FXYD5', 'IL15RA', 'SUGT1']
        reverse = [0, 0, 0, 1, 1, 1]
        v = Aggregate(df, index, features, reverse)
        if v < -5 and v > -11:
            return 1
        if v > -5 and v < 40:
            return -1

    elif l1 == 5 and l2 == 17:
        v = list(df['CLDN4'])[index]
        if v > 3 and v < 10:
            return 1
        if v < 3 and v > -4:
            return -1

    elif l1 == 5 and l2 == 18:
        v = list(df['GPR35'])[index]
        if v < 0 and v > -4:
            return -1
        if v > 0 and v < 7:
            return 1

    elif l1 == 5 and l2 == 19:
        v = list(df['RPS6'])[index]
        if v < -2 and v > -4:
            return 1
        v = list(df['ZBTB20'])[index]
        if v < -1.7 and v > -4:
            return 1
        v = list(df['SRM'])[index]
        if v < 4 and v > 1.5:
            return 1
        if v > 4 and v < 9:
            return -1

    elif l1 == 5 and l2 == 20:
        features = ['RND2', 'TUBB4A', 'SLC7A3', 'ZNF667', 'DPPA4', 'WNK3']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v < 0 and v > -21:
            return 1
        if v > 0 and v < 31:
            return -1


    elif l1 == 5 and l2 == 21:
        v = list(df['FOXE1'])[index]
        if v > 1 and v < 9:
            return -1
        if v < 1 and v > -4:
            return 1

    elif l1 == 5 and l2 == 22:
        features = ['EMX2', 'CDX1', 'DLX5', 'PHGR1', 'SLC34A2', 'KCTD1']
        reverse = [0, 1, 0, 1, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v < 0 and v > -35:
            return 1
        if v > 15 and v < 37:
            return -1
        features = ['OTUD3', 'EIF4E3', 'LMTK2', 'FSD1L', 'NDUFA7', 'SIK3']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > 0 and v < 50:
            return -1
        if v < 0 and v > -23:
            return 1

    elif l1 == 6 and l2 == 7:
        features = ['GJD3', 'EIF3CL', 'SPDYE5', 'TRAPPC5', 'POTEI', 'TSSK3']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > -10.5 and v < 2:
            return 1
        if v < -10.5 and v > -22:
            return -1

    elif l1 == 6 and l2 == 8:
        v = list(df['ACTB'])[index]
        if v < 3 and v > -4:
            return -1
        v = list(df['F8A3'])[index]
        if v > -2.4 and v < 0.5:
            return 1
        if v < -2.4 and v > -3.5:
            return -1

    elif l1 == 6 and l2 == 9:
        v = list(df['GNG12'])[index]
        if v > 2.5 and v < 7:
            return 1
        if v < 2.5 and v > -4:
            return -1

    elif l1 == 6 and l2 == 10:
        features = ['GAN', 'CMIP', 'ZNF460', 'STYK1', 'SERPINB5', 'POMK']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > 1 and v < 30:
            return 1
        if v < 1 and v > -21:
            return -1

    elif l1 == 6 and l2 == 11:
        features = ['GJD3', 'TRAPPC5', 'EIF3CL', 'CTU1', 'POTEI', 'ZFPM1']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > -3.5 and v < 10:
            return 1
        if v < -3.5 and v > -20:
            return -1

    elif l1 == 6 and l2 == 12:
        v = list(df['PLXNB1'])[index]
        if v > 1.5 and v < 6:
            return 1
        if v < 1.5 and v > -4:
            return -1

    elif l1 == 6 and l2 == 13:
        features = ['PAX8', 'SOX17', 'FGF18', 'NPR1', 'SPON1', 'BCAM']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > -8 and v < 17.5:
            return 1
        if v < -8 and v > -20:
            return -1
        if v > 17.5 and v < 50:
            return -1

    elif l1 == 6 and l2 == 14:
        features = ['GJD3', 'EIF3CL', 'ZNF460', 'STMN2', 'TICRR', 'TRAPPC5']
        reverse = [0, 0, 0, 1, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v < -5 and v > -23:
            return -1
        if v > -5 and v < 15:
            return 1

    elif l1 == 6 and l2 == 15:
        v = list(df['GRHL2'])[index]
        if v > 0 and v < 6:
            return 1
        if v < 0 and v > -4:
            return -1

    elif l1 == 6 and l2 == 16:
        features = ['DYNLL2', 'ADI1', 'MAGED2', 'CBY1', 'CREB3', 'ERGIC1']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > 26 and v < 40:
            return -1
        if v < 26 and v > 10:
            return 1
        if v < -10 and v > -24:
            return -1

    elif l1 == 6 and l2 == 17:
        v = list(df['GRHL2'])[index]
        if v > 0.5 and v < 6:
            return 1
        if v < 0.5 and v > -4:
            return -1

    elif l1 == 6 and l2 == 18:
        features = ['F8A3', 'GJD3', 'MARVELD3', 'EPCAM', 'GRHL2', 'POTEJ']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v < -2.5 and v > -22:
            return -1
        if v > -2.5 and v < 16:
            return 1

    elif l1 == 6 and l2 == 19:
        v = list(df['FAT2'])[index]
        if v > 0 and v < 8:
            return 1
        features = ['DUOX1', 'DUOXA1', 'DUOX2', 'TFR2', 'IL1RL2', 'GPRC5C']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v < 1 and v > -17:
            return -1
        v = list(df['NKX3-2'])[index]
        if v > 0.4 and v < 4:
            return -1
        features = ['TBX5', 'NKX6-1', 'TUBD1', 'SPTB', 'TTLL9', 'NOXRED1']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v < -12 and v > -17.5:
            return -1
        if v > -12 and v < 5:
            return -1

    elif l1 == 6 and l2 == 20:
        v = list(df['F8A3'])[index]
        if v < -2.75 and v > -3.5:
            return -1
        if v > -2.75 and v < 0.5:
            return 1

    elif l1 == 6 and l2 == 21:
        v = list(df['TG'])[index]
        if v > 2.5 and v < 15:
            return -1
        if v < 2.5 and v > -5:
            return 1

    elif l1 == 6 and l2 == 22:
        features = ['EIF3CL', 'POTEI', 'POTEJ', 'SERPINB5', 'GJD3', 'ZFY']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > -7.5 and v < 10:
            return 1
        if v < -7.5 and v > -22:
            return -1

    elif l1 == 7 and l2 == 8:
        features = ['PITX1', 'EMX2', 'DSG3', 'SERPINB13', 'KLK10', 'CLCA2']
        reverse = [0, 1, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > 10 and v < 50:
            return 1
        if v < -15 and v > -30:
            return -1
        features = ['PHOX2B', 'FAM181A', 'GDAP1L1', 'SEL1L2', 'OR4F6', 'GH2']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > -8 and v < 45:
            return 1
        features = ['PITX1', 'KLF16', 'PHF8', 'PELP1', 'PFN2', 'MRPS11']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > -5 and v < 10:
            return -1
        elif v > 10 and v < 30:
            v = list(df['ACMSD'])[index]
            if v > -2 and v < 7:
                return -1
            v = list(df['SRGAP2C'])[index]
            if v > 1.5 and v < 5:
                return -1
            if v < 1.5 and v > -3:
                return 1
        elif v < -5 and v > -25:
            v = list(df['YBX3'])[index]
            if v < -2.3 and v > -4:
                return -1
            if v > -2.3 and v < 3:
                return 1

    elif l1 == 7 and l2 == 9:
        features = ['RND3', 'DSC3', 'RIPK4', 'EFNB2', 'GNG12', 'KRT5']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > -5 and v < 50:
            return 1
        v = list(df['TRIM46'])[index]
        if v < 1.5 and v > -4:
            return -1
        v = list(df['OR52W1'])[index]
        if v > 1 and v < 3:
            return 1
        if v < 1 and v > -4:
            return -1

    elif l1 == 7 and l2 == 10:
        v = list(df['VTN'])[index]
        if v > 5 and v < 14:
            return -1
        if v < 5 and v > -4:
            return 1

    elif l1 == 7 and l2 == 11:
        features = ['SFTPA2', 'SFTPA1', 'SFTA3', 'SLC34A2', 'SFTPB', 'SFTPC']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > 10 and v < 80:
            return -1
        v = list(df['GDF9'])[index]
        if v > 1.5 and v < 6.5:
            v = list(df['GUCA1C'])[index]
            if v > 2 and v < 12:
                return -1
            if v < 2 and v > -4:
                return 1
        elif v < 1.5 and v > -4:
            features = ['TBX5', 'TCF21', 'TBX4', 'TMEM130', 'SFTPB', 'DNAH14']
            reverse = [0, 0, 0, 0, 0, 0]
            v = Aggregate(df, index, features, reverse)
            if v < -14 and v > -21:
                return 1
            if v > -14 and v < -6:
                return -1
            if v > -5 and v < 11:
                return -1

    elif l1 == 7 and l2 == 12:
        v = list(df['GRHL2'])[index]
        if v > 0 and v < 6:
            return 1
        v = list(df['OGG1'])[index]
        if v > 2 and v < 7:
            return -1
        if v < 2 and v > 0:
            return 1
        if v < 0 and v > -4:
            return 1


    elif l1 == 7 and l2 == 13:
        features = ['EMX2', 'DSG3', 'KLHL14', 'TP63', 'CLCA2', 'SCGB1D2']
        reverse = [0, 1, 0, 1, 1, 0]
        v = Aggregate(df, index, features, reverse)
        if v > 5 and v < 35:
            return -1
        if v < -15 and v > -40:
            return 1
        features = ['SLC22A23', 'RPL7', 'NONO', 'MRPL47', 'AMFR', 'NDUFB2']
        reverse = [0, 1, 1, 1, 1, 1]
        v = Aggregate(df, index, features, reverse)
        if v > -15 and v < 5:
            return 1
        elif v > 5 and v < 30:
            v = list(df['TRAPPC10'])[index]
            if v > 4 and v < 10:
                return -1
            if v < 2 and v > -2:
                return 1
        elif v < -15 and v > -40:
            v = list(df['SOX4'])[index]
            if v > 5.6 and v < 7:
                return -1
            if v < 5.6 and v > 1:
                return 1

    elif l1 == 7 and l2 == 14:
        v = list(df['CLCA2'])[index]
        if v > 3.5 and v < 10:
            return 1
        v = list(df['NPC1L1'])[index]
        if v > 0 and v < 5.5:
            return -1
        v = list(df['ABLIM1'])[index]
        if v < -1 and v > -4:
            return -1
        features = ['MSLN', 'S100P', 'MUC1', 'CTSE', 'GPRC5A', 'KCNN4']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > 25 and v < 50:
            return -1
        if v < 25 and v > -20:
            return 1

    elif l1 == 7 and l2 == 15:
        v = list(df['GRHL2'])[index]
        if v > -0.5 and v < 6:
            return 1
        if v < -0.5 and v > -4:
            return -1

    elif l1 == 7 and l2 == 16:
        v = list(df['SLC45A3'])[index]
        if v > 4 and v < 12:
            return -1
        if v < 4 and v > -2.5:
            return 1
        if v < -2.5 and v > -4:
            v = list(df['ACVR1'])[index]
            if v > 0 and v < 6:
                return -1
            if v < 0 and v > -4:
                return 1

    elif l1 == 7 and l2 == 17:
        v = list(df['DSG3'])[index]
        if v > 3 and v < 10:
            return 1
        v = list(df['MMADHC'])[index]
        if v > 2.5 and v < 6.5:
            v = list(df['KDF1'])[index]
            if v < -2 and v > -4:
                return -1
            if v > -2 and v < 5:
                return 1
        elif v < 2.5 and v > -2:
            return 1
        elif v < -2 and v > -4:
            v = list(df['FDX1'])[index]
            if v > 0.5 and v < 3:
                return 1
            if v < -2 and v > -4:
                return -1

    elif l1 == 7 and l2 == 18:
        features = ['FMN1', 'MITF', 'LZTS1', 'SLC16A4', 'DAAM2', 'BEST1']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > 6 and v < 40:
            return -1
        if v < 6 and v > -24:
            return 1

    elif l1 == 7 and l2 == 19:
        features = ['ZFPM1', 'TMEM238', 'DDAH1', 'SMAD6', 'PBLD', 'ADAP1']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > 11 and v < 30:
            return -1
        if v < -5 and v > -25:
            return 1
        v = list(df['TCF21'])[index]
        if v > -1 and v < 5:
            return -1
        if v < -1 and v > -4:
            return 1

    elif l1 == 7 and l2 == 20:
        v = list(df['LIN28B'])[index]
        if v < 0.8 and v > -4:
            return 1
        if v > 0.8 and v < 6:
            return -1

    elif l1 == 7 and l2 == 21:
        v = list(df['PAX8'])[index]
        if v > 3 and v < 10:
            return -1
        if v < 3 and v > -4:
            return 1

    elif l1 == 7 and l2 == 22:
        v = list(df['SOX17'])[index]
        if v > 3 and v < 10:
            return -1
        v = list(df['ANXA8'])[index]
        if v > 1 and v < 6.5:
            return 1
        v = list(df['CTDSP1'])[index]
        if v > 2 and v < 8:
            v = list(df['DDX3Y'])[index]
            if v > -2.5 and v < 4.5:
                return 1
            if v < -2.5 and v > -4:
                return -1
        elif v < 2 and v > -4:
            v = list(df['SGTA'])[index]
            if v > -1.8 and v < 4:
                return -1
            v = list(df['ARHGAP22'])[index]
            if v > 0.25 and v < 4.5:
                return -1
            if v < 0.25 and v > -4:
                return 1

    elif l1 == 8 and l2 == 9:
        features = ['CYB5D2', 'BRD7', 'SLC33A1', 'GATC', 'MTR', 'IFT46']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > 20 and v < 37:
            return 1
        if v < -2 and v > -25:
            return -1
        v = list(df['HTRA1'])[index]
        if v < 1 and v > -4:
            return -1
        if v > 5 and v < 12:
            return 1
        v = list(df['CDK19'])[index]
        if v > 3.6 and v < 6:
            return -1
        if v < 3.6 and v > -4:
            return 1


    elif l1 == 8 and l2 == 10:
        v = list(df['VTN'])[index]
        if v > 6 and v < 14:
            return -1
        if v < 6 and v > -4:
            return 1

    elif l1 == 8 and l2 == 11:
        features = ['CEACAM6', 'ST6GALNAC1', 'SDR16C5', 'CEACAM5', 'EMX2', 'FAM83E']
        reverse = [0, 0, 0, 0, 1, 0]
        v = Aggregate(df, index, features, reverse)
        if v > 0 and v < 50:
            return -1
        if v < -14 and v > -30:
            return 1
        v = list(df['EOMES'])[index]
        if v > 4 and v < 12.5:
            return -1
        v = list(df['SAE1'])[index]
        if v < -3 and v > -4:
            return 1
        v = list(df['CDH16'])[index]
        if v > 1 and v < 10:
            return 1
        if v < 1 and v > -4:
            return -1

    elif l1 == 8 and l2 == 12:
        v = list(df['ANKRD18A'])[index]
        if v > 4 and v < 12:
            return -1
        features = ['GRK6', 'RELB', 'TRIM11', 'TACC3', 'CARD11', 'DHX34']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > 22.5 and v < 33:
            return -1
        if v < 22.5 and v > -5:
            return 1
        v = list(df['FANCL'])[index]
        if v < -2.5 and v > -4:
            return 1
        if v > -2.5 and v < 8:
            return -1


    elif l1 == 8 and l2 == 13:
        features = ['MUC16', 'LPAR3', 'KLK11', 'FAM181A', 'KLK5', 'UPK3B']
        reverse = [0, 0, 0, 1, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > 6 and v < 36:
            return -1
        v = list(df['TMEM131'])[index]
        if v > 4 and v < 8.5:
            return -1
        if v < 1 and v > -4:
            return 1
        v = list(df['RBM38'])[index]
        if v > 5.1 and v < 8.5:
            return -1
        v = list(df['NSUN7'])[index]
        if v > 6 and v < 9:
            return -1
        if v < 6 and v > -4:
            return 1


    elif l1 == 8 and l2 == 14:
        v = list(df['POU3F3'])[index]
        if v > 0 and v < 7.5:
            return 1
        features = ['CCDC102A', 'RAB1A', 'TRIM47', 'GLCE', 'RALGAPB', 'ZNF174']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v < -7.5 and v > -23:
            return 1
        v = list(df['FOXA3'])[index]
        if v < -1 and v > -4:
            return 1
        if v > -1 and v < 8:
            return -1

    elif l1 == 8 and l2 == 15:
        v = list(df['SLC3A1'])[index]
        if v > 1 and v < 9:
            return 1
        v = list(df['AHCYL2'])[index]
        if v > -2 and v < 6.5:
            v = list(df['PAX8'])[index]
            if v > 1.5 and v < 7:
                return 1
            if v < 1.5 and v > -4:
                return -1
        elif v < -2 and v > -4:
            v = list(df['CUL5'])[index]
            if v > -1.5 and v < 2:
                return -1
            if v < -1.5 and v > -4:
                return 1

    elif l1 == 8 and l2 == 16:
        features = ['ST6GALNAC1', 'CUX2', 'TTC6', 'LRRC26', 'TMEFF2', 'C9orf152']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > 10 and v < 35:
            return -1
        if v < -5 and v > -23:
            return 1
        v = list(df['FBXL20'])[index]
        if v > 0.75 and v < 6:
            return -1
        if v < 0.75 and v > -4:
            return 1

    elif l1 == 8 and l2 == 17:
        features = ['SHOX2', 'HPN', 'CRB3', 'KLHDC7A', 'CDH16', 'C1orf210']
        reverse = [0, 1, 1, 1, 1, 1]
        v = Aggregate(df, index, features, reverse)
        if v < 0 and v > -40:
            return 1
        features = ['PLCXD1', 'SLC25A25', 'MOB1A', 'ARIH2', 'C9orf16', 'METTL17']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v < 0 and v > -22:
            return 1
        if v > 10 and v < 30:
            return -1

    elif l1 == 8 and l2 == 18:
        v = list(df['CDH16'])[index]
        if v > 0 and v < 12:
            return 1
        v = list(df['ATP1A1'])[index]
        if v < -2 and v > -4:
            return 1
        features = ['PAX3', 'GPM6B', 'CCDC140', 'EDNRB', 'RGS20', 'SGCD']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v < 0 and v > -20:
            return 1
        if v > 0 and v < 40:
            return -1

    elif l1 == 8 and l2 == 19:
        features = ['EMX2', 'PITX1', 'PAX2', 'ST6GALNAC1', 'CEACAM6', 'FOXA1']
        reverse = [0, 1, 0, 1, 1, 1]
        v = Aggregate(df, index, features, reverse)
        if v > 0 and v < 30:
            return 1
        if v < 0 and v > -35:
            return -1

    elif l1 == 8 and l2 == 20:
        v = list(df['CLDN6'])[index]
        if v < 3 and v > -4:
            return 1
        if v > 3 and v < 10:
            return -1

    elif l1 == 8 and l2 == 21:
        v = list(df['TG'])[index]
        if v > 4 and v < 15:
            return -1
        if v < 4 and v > -5:
            return 1

    elif l1 == 8 and l2 == 22:
        features = ['IGSF9', 'ALDH3B2', 'RCOR2', 'LGR5', 'SIX4', 'AQP5']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > 5 and v < 40:
            return -1
        v = list(df['EHHADH'])[index]
        if v > 2.5 and v < 8:
            return 1
        if v > -4 and v < -2:
            return 1
        v = list(df['KDM4E'])[index]
        if v > 0.5 and v < 5:
            v = list(df['NOS3'])[index]
            if v < -1.5 and v > -4:
                return 1
            v = list(df['GPN1'])[index]
            if v < -2 and v > -4:
                return -1
            if v > -2 and v < 8.2:
                return 1
        elif v < -2 and v > -4:
            v = list(df['RBM47'])[index]
            if v < 1 and v > -3:
                return -1
            v = list(df['AUNIP'])[index]
            if v > 1 and v < 3.5:
                return -1
            if v < 1 and v > -3:
                return 1

    elif l1 == 9 and l2 == 10:
        v = list(df['SPR'])[index]
        if v > 3.5 and v < 8:
            return -1
        if v < 3.5 and v > -4:
            return 1

    elif l1 == 9 and l2 == 11:
        features = ['CLDN4', 'RAB25', 'HID1', 'EDNRA', 'NUPR1', 'EPS8L2']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v < -7.5 and v > -23:
            return 1
        if v > -7.5 and v < 40:
            return -1

    elif l1 == 9 and l2 == 12:
        v = list(df['RASIP1'])[index]
        if v < -0.5 and v > -4:
            return 1
        features = ['CD2BP2', 'MRPS23', 'CST3', 'OXA1L', 'SLC1A5', 'PCMT1']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > -5 and v < 22:
            return 1
        elif v > 22 and v < 40:
            v = list(df['MASP2'])[index]
            if v > -0.25 and v < 4:
                return 1
            if v < -0.25 and v > -4:
                return -1
        elif v < -5 and v > -23:
            v = list(df['RUNX1T1'])[index]
            if v > 0 and v < 9:
                return -1
            if v < 0 and v > -4:
                return 1

    elif l1 == 9 and l2 == 13:
        v = list(df['SOX17'])[index]
        if v > 1 and v < 9:
            return -1
        features = ['ADCY5', 'USHBP1', 'KCNK3', 'NHLH2', 'MEP1A', 'MAGEB17']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > 3 and v < 35:
            return -1
        if v < -11 and v > -23:
            return 1
        if v > -11 and v < 3:
            v = list(df['SSX3'])[index]
            if v > -2.75 and v < 2.5:
                return 1
            if v < -2.75 and v > -4:
                return -1

    elif l1 == 9 and l2 == 14:
        features = ['FKBP10', 'CLDN4', 'SORBS2', 'RNF180', 'CADPS2', 'COL13A1']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > -2.5 and v < 25:
            return -1
        if v < -2.5 and v > -23:
            return 1

    elif l1 == 9 and l2 == 15:
        v = list(df['NES'])[index]
        if v > 0 and v < 8:
            return -1
        v = list(df['RDH8'])[index]
        if v > 1 and v < 5:
            return -1
        if v < 1 and v > -4:
            return 1

    elif l1 == 9 and l2 == 16:
        v = list(df['TMPRSS2'])[index]
        if v > 1 and v < 10.5:
            return -1
        features = ['TRIM55', 'EFCAB3', 'GIPR', 'SLC6A20', 'CYP8B1', 'ALLC']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > 17 and v < 35:
            return -1
        if v < 17 and v > -22:
            return 1

    elif l1 == 9 and l2 == 17:
        features = ['YAP1', 'SPARCL1', 'EGFR', 'TJP1', 'BGN', 'ADGRL4']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > 7.5 and v < 40:
            return -1
        v = list(df['CLMP'])[index]
        if v > 3 and v < 7:
            return -1
        if v < 3 and v > -4:
            return 1

    elif l1 == 9 and l2 == 18:
        v = list(df['PARVA'])[index]
        if v < 1 and v > -4:
            return 1
        if v > 1 and v < 6:
            return -1

    elif l1 == 9 and l2 == 19:
        v = list(df['PARVA'])[index]
        if v < 1 and v > -4:
            return 1
        if v > 1 and v < 6:
            return -1

    elif l1 == 9 and l2 == 20:
        v = list(df['FNDC4'])[index]
        if v > 1 and v < 8:
            return -1
        if v < 1 and v > -4:
            return 1

    elif l1 == 9 and l2 == 21:
        v = list(df['S100A13'])[index]
        if v > 3.75 and v < 10.5:
            return -1
        if v < 3.75 and v > -4:
            return 1

    elif l1 == 9 and l2 == 22:
        features = ['NUPR1', 'SELENOM', 'COL4A2', 'HID1', 'DLL4', 'PARVA']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > 5 and v < 35:
            return -1
        if v < -10 and v > -23:
            return 1
        v = list(df['POTEC'])[index]
        if v > 0.5 and v < 8.5:
            return -1
        if v < 0.5 and v > -4:
            return 1

    elif l1 == 10 and l2 == 11:
        v = list(df['ITIH1'])[index]
        if v > 3 and v < 11:
            return 1
        if v < 3 and v > -4:
            return -1

    elif l1 == 10 and l2 == 12:
        v = list(df['VTN'])[index]
        if v > 4 and v < 14:
            return 1
        if v < 4 and v > -4:
            return -1

    elif l1 == 10 and l2 == 13:
        v = list(df['SERPINA10'])[index]
        if v > -2 and v < 8:
            return 1
        if v < -2 and v > -4:
            return -1

    elif l1 == 10 and l2 == 14:
        v = list(df['ASGR2'])[index]
        if v < 2 and v > -4.2:
            return -1
        if v > 2 and v < 10.2:
            return 1

    elif l1 == 10 and l2 == 15:
        v = list(df['GC'])[index]
        if v < 4 and v > -4:
            return -1
        if v > 4 and v < 12.5:
            return 1

    elif l1 == 10 and l2 == 16:
        features = ['TMEFF2', 'NWD1', 'ITIH2', 'APOB', 'OR51E2', 'HNF4A']
        reverse = [0, 0, 1, 1, 0, 1]
        v = Aggregate(df, index, features, reverse)
        if v < -15 and v > -40:
            return 1
        if v > -15 and v < 35:
            return -1

    elif l1 == 10 and l2 == 17:
        v = list(df['GC'])[index]
        if v < 4 and v > -4:
            return -1
        if v > 4 and v < 12.5:
            return 1

    elif l1 == 10 and l2 == 18:
        v = list(df['HNF4A'])[index]
        if v > 0.5 and v < 8:
            return 1
        if v < 0.5 and v > -4:
            return -1

    elif l1 == 10 and l2 == 19:
        v = list(df['CPB2'])[index]
        if v > 2 and v < 10.5:
            return 1
        if v < 2 and v > -4:
            return -1

    elif l1 == 10 and l2 == 20:
        features = ['SLC4A8', 'ADD2', 'L1TD1', 'INA', 'RIMS4', 'CDH3']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > -5 and v < 32:
            return -1
        if v < -5 and v > -22:
            return 1

    elif l1 == 10 and l2 == 21:
        v = list(df['TG'])[index]
        if v > 2.5 and v < 15:
            return -1
        if v < 2.5 and v > -5:
            return 1

    elif l1 == 10 and l2 == 22:
        v = list(df['GC'])[index]
        if v < 4 and v > -4:
            return -1
        if v > 4 and v < 12.5:
            return 1

    elif l1 == 11 and l2 == 12:
        v = list(df['GRHL2'])[index]
        if v > 0 and v < 6:
            return 1
        v = list(df['DNAAF3'])[index]
        if v < -1.9 and v > -4:
            return -1
        if v > -1.9 and v < 1:
            return 1

    elif l1 == 11 and l2 == 13:
        features = ['PAX8', 'KLHL14', 'SOX17', 'APOA1', 'SCGB1D2', 'EMX2']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > 5 and v < 46:
            return -1
        v = list(df['ANTXR1'])[index]
        if v > -1.5 and v < 8:
            return 1
        if v < -1.5 and v > -4:
            return -1

    elif l1 == 11 and l2 == 14:
        v = list(df['SFTPA2'])[index]
        if v > 5 and v < 15:
            return 1
        v = list(df['CYSTM1'])[index]
        if v < 1.5 and v > -4:
            v = list(df['AHSA1'])[index]
            if v > -1.2 and v < 2.2:
                return 1
            if v < -1.2 and v > -4:
                return -1
        elif v > 1.5 and v < 10:
            features = ['SFTPB', 'SFTPA1', 'SFTPA2', 'SFTA3', 'TBX5', 'SLC22A31']
            reverse = [0, 0, 0, 0, 0, 0]
            v = Aggregate(df, index, features, reverse)
            if v > -5 and v < 40:
                return 1
            v = list(df['TM4SF4'])[index]
            if v < 0 and v > -4:
                return 1
            if v > 0 and v < 10.5:
                return -1


    elif l1 == 11 and l2 == 15:
        features = ['GRHL2', 'MARVELD3', 'RAB25', 'CLDN4', 'PERP', 'LAD1']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > 0 and v < 43:
            return 1
        if v < 0 and v > -21:
            return -1

    elif l1 == 11 and l2 == 16:
        features = ['CAB39L', 'PLPP1', 'ABCC4', 'SLC45A3', 'ZNF613', 'TBX3']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > 20 and v < 45:
            return -1
        if v < 20 and v > -5:
            return 1
        v = list(df['PROSER2'])[index]
        if v > 4 and v < 8:
            return 1
        if v < 4 and v > -4:
            return -1

    elif l1 == 11 and l2 == 17:
        v = list(df['GRHL2'])[index]
        if v > 0.5 and v < 6:
            return 1
        v = list(df['FAM83E'])[index]
        if v > -1 and v < 4:
            return 1
        if v < -1 and v > -4:
            return -1

    elif l1 == 11 and l2 == 18:
        v = list(df['CRB3'])[index]
        if v < 0 and v > -4:
            return -1
        v = list(df['PMEL'])[index]
        if v > 4 and v < 14:
            return -1
        if v < 4 and v > -4:
            return 1

    elif l1 == 11 and l2 == 19:
        v = list(df['ZBTB7A'])[index]
        if v < 1 and v > -4:
            return 1
        features = ['F8A3', 'EIF3CL', 'POTEJ', 'GJD3', 'MTRNR2L8', 'ZFPM1']
        reverse = [0, 0, 0, 0, 1, 0]
        v = Aggregate(df, index, features, reverse)
        if v > -6 and v < 6:
            return -1
        if v < -12.5 and v > -20:
            return 1
        v = list(df['SFTPA1'])[index]
        if v > 0 and v < 15:
            return 1
        v = list(df['PHGR1'])[index]
        if v < -2 and v > -4:
            return 1
        if v > -2 and v < 12:
            return -1


    elif l1 == 11 and l2 == 20:
        v = list(df['GDF3'])[index]
        if v > 1 and v < 12.5:
            return -1
        v = list(df['ST3GAL2'])[index]
        if v > 3.2 and v < 5:
            return -1
        if v < 3.2 and v > -3:
            return 1

    elif l1 == 11 and l2 == 21:
        v = list(df['PAX8'])[index]
        if v > 4 and v < 10:
            return -1
        if v < 4 and v > -4:
            return 1

    elif l1 == 11 and l2 == 22:
        v = list(df['SFTPA2'])[index]
        if v > 5 and v < 15:
            return 1
        v = list(df['PAX8'])[index]
        if v > 3 and v < 9:
            return -1
        features = ['ADGRE3', 'PLET1', 'CD300LB', 'EEF2', 'SF3A2', 'PTPN23']
        reverse = [0, 0, 0, 1, 1, 1]
        v = Aggregate(df, index, features, reverse)
        if v > 10 and v < 32:
            features = ['ELMO2', 'CFAP65', 'NOL3', 'TAAR2', 'ZBTB45', 'CREBRF']
            reverse = [0, 0, 0, 1, 1, 0]
            v = Aggregate(df, index, features, reverse)
            if v > -1 and v < 30:
                return 1
            if v < -1 and v > -21:
                return -1
        elif v < 0 and v > -35:
            features = ['EMX2', 'LEFTY2', 'HOXD3', 'ZCCHC12', 'MAPK13', 'DES']
            reverse = [0, 0, 0, 0, 1, 0]
            v = Aggregate(df, index, features, reverse)
            if v > -8 and v < 40:
                return -1
            if v < -8 and v > -24:
                return 1

    elif l1 == 12 and l2 == 13:
        features = ['JMJD6', 'PLIN3', 'ACLY', 'SGTA', 'ZPR1', 'TRIM11']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > -9 and v < 17:
            return -1
        elif v < -9 and v > -22:
            return 1
        elif v > 17 and v < 30:
            v = list(df['PBX1'])[index]
            if v > 0 and v < 6:
                return -1
            if v < 0 and v > -3.5:
                return 1

    elif l1 == 12 and l2 == 14:
        features = ['TNFRSF11A', 'CAPN5', 'FUT2', 'PROS1', 'HGD', 'LRRC66']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > -4 and v < 30:
            return -1
        if v < -4 and v > -23:
            return 1

    elif l1 == 12 and l2 == 15:
        v = list(df['PDCL3'])[index]
        if v < -0.75 and v > -4:
            return 1
        v = list(df['CD19'])[index]
        if v > 4 and v < 8.5:
            return 1
        if v < 4 and v > -4:
            return -1

    elif l1 == 12 and l2 == 16:
        v = list(df['ATP2C1'])[index]
        if v > 4 and v < 10:
            return -1
        if v < 1.5 and v > -4:
            return 1
        v = list(df['NCF1'])[index]
        if v > 1 and v < 8:
            return 1
        if v < 1 and v > -4.2:
            return -1

    elif l1 == 12 and l2 == 17:
        v = list(df['NUP153'])[index]
        if v < -2 and v > -4:
            return 1
        features = ['FKBP7', 'FKBP9', 'FKBP10', 'LAPTM4B', 'PPIC', 'SYDE1']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > 17.5 and v < 40:
            return -1
        if v < 17.5 and v > -10:
            return 1
        if v < -10 and v > -22:
            return -1

    elif l1 == 12 and l2 == 18:
        v = list(df['STXBP1'])[index]
        if v > 1.5 and v < 9:
            return -1
        if v < 1.5 and v > -4:
            return 1

    elif l1 == 12 and l2 == 19:
        v = list(df['NCKAP1'])[index]
        if v > 1 and v < 6:
            return -1
        if v < 1 and v > -4:
            return 1

    elif l1 == 12 and l2 == 20:
        v = list(df['CLDN6'])[index]
        if v < -2 and v > -4:
            return 1
        if v > -2 and v < 10:
            return -1

    elif l1 == 12 and l2 == 21:
        v = list(df['TG'])[index]
        if v < 2 and v > -5:
            return 1
        if v > 2 and v < 15:
            return -1

    elif l1 == 12 and l2 == 22:
        v = list(df['RBBP9'])[index]
        if v < -0.5 and v > -4:
            return 1
        v = list(df['BTK'])[index]
        if v > 3 and v < 8:
            return 1
        if v < 3 and v > -4:
            return -1

    elif l1 == 13 and l2 == 14:
        v = list(df['ARHGAP39'])[index]
        if v < -2 and v > -4:
            v = list(df['PNPLA1'])[index]
            if v < -2.5 and v > -4:
                return -1
            if v > -2.5 and v < 3:
                return 1
        elif v > -2 and v < 6.5:
            features = ['ZNF771', 'CTU1', 'SOX17', 'CTXN1', 'HNF4A', 'SOX12']
            reverse = [0, 0, 0, 0, 1, 0]
            v = Aggregate(df, index, features, reverse)
            if v > 15 and v < 35:
                return 1
            if v < 15 and v > -10:
                return -1

    elif l1 == 13 and l2 == 15:
        features = ['SLC34A2', 'CLDN3', 'CLDN7', 'SCNN1A', 'AP1M2', 'GRB7']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v < 1 and v > -22:
            return -1
        if v > 22 and v < 50:
            return 1
        if v > 1 and v < 22:
            v = list(df['CNTN3'])[index]
            if v > 3 and v < 10:
                return -1
            if v < 3 and v > -4:
                return 1


    elif l1 == 13 and l2 == 16:
        v = list(df['EIF1AY'])[index]
        if v < -2 and v > -4:
            return 1
        v = list(df['DPF2'])[index]
        if v < -2 and v > -4:
            return 1
        if v > -2 and v < 4.5:
            return -1

    elif l1 == 13 and l2 == 17:
        features = ['TMPRSS3', 'CLDN3', 'OVOL2', 'SCNN1A', 'AP1M2', 'KLK8']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > 25 and v < 41:
            return 1
        if v < 3 and v > -22:
            return -1
        v = list(df['NUP153'])[index]
        if v < -1 and v > -4:
            return 1
        v = list(df['PPP2R3A'])[index]
        if v > 1 and v < 4:
            return 1
        if v < 1 and v > -4:
            return -1

    elif l1 == 13 and l2 == 18:
        features = ['MEIS1', 'SOX17', 'EPCAM', 'ATP6V1B1', 'SRGAP3', 'ESR1']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v < -16 and v > -22:
            return 1
        if v > -16 and v < 3:
            return -1
        if v > 3 and v < 40:
            return 1

    elif l1 == 13 and l2 == 19:
        features = ['EMX2', 'WT1', 'SCGB1D2', 'EPS8L3', 'HNF4A', 'FAM181A']
        reverse = [0, 0, 0, 1, 1, 0]
        v = Aggregate(df, index, features, reverse)
        if v > -2 and v < 35:
            return 1
        if v < -2 and v > -30:
            return -1

    elif l1 == 13 and l2 == 20:
        v = list(df['UTY'])[index]
        if v < -3 and v > -4:
            return 1
        if v > -3 and v < 2.75:
            return -1

    elif l1 == 13 and l2 == 21:
        v = list(df['TG'])[index]
        if v > 2.5 and v < 15.5:
            return -1
        if v < 2.5 and v > -5:
            return 1

    elif l1 == 13 and l2 == 22:
        v = list(df['TRAPPC5'])[index]
        if v < -3 and v > -4:
            v = list(df['NUDT21'])[index]
            if v < -1.5 and v > -4:
                return 1
            if v > 1 and v < 4:
                return -1
        elif v > -3 and v < 3.5:
            features = ['TRAPPC5', 'F8A3', 'CTU1', 'CMC4', 'RPL18A', 'ZNF771']
            reverse = [0, 0, 0, 0, 0, 0]
            v = Aggregate(df, index, features, reverse)
            if v > 7 and v < 20:
                return 1
            if v < 7 and v > -6:
                return -1

    elif l1 == 14 and l2 == 15:
        v = list(df['PRR15L'])[index]
        if v > 0 and v < 8:
            return 1
        v = list(df['TRAPPC8'])[index]
        if v < -2 and v > -4:
            return 1
        if v > -2 and v < 5:
            return -1

    elif l1 == 14 and l2 == 16:
        v = list(df['KLK2'])[index]
        if v > 3 and v < 12:
            return -1
        features = ['GNA15', 'SBNO2', 'TRIM47', 'CCDC102A', 'CCDC38', 'RHAG']
        reverse = [0, 0, 0, 0, 1, 1]
        v = Aggregate(df, index, features, reverse)
        if v < 0 and v > -30:
            return -1
        v = list(df['PTPRH'])[index]
        if v > -1 and v < 7:
            return 1
        if v < -1 and v > -4:
            return -1

    elif l1 == 14 and l2 == 17:
        features = ['CLDN4', 'FUT2', 'HGD', 'FA2H', 'GRB7', 'SULT2B1']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v < -2 and v > -21:
            return -1
        if v > -2 and v < 35:
            return 1

    elif l1 == 14 and l2 == 18:
        v = list(df['HNF1A'])[index]
        if v < -2.3 and v > -4:
            return -1
        if v > -2.3 and v < 3.5:
            return 1

    elif l1 == 14 and l2 == 19:
        v = list(df['POTEG'])[index]
        if v > 1 and v < 6:
            return 1
        v = list(df['POTEE'])[index]
        if v > -2.7 and v < 2:
            return -1
        v = list(df['ADGRF1'])[index]
        if v > -2.5 and v < 4:
            return 1
        v = list(df['ADAMTSL2'])[index]
        if v < 0.5 and v > -1.2:
            return -1
        if v > 0.5 and v < 7:
            return 1

    elif l1 == 14 and l2 == 20:
        v = list(df['NR5A1'])[index]
        if v < -2.5 and v > -4:
            return 1
        if v > -2.5 and v < 5:
            return -1

    elif l1 == 14 and l2 == 21:
        v = list(df['PTPRH'])[index]
        if v < 0.5 and v > -4:
            return -1
        if v > 0.5 and v < 7:
            return 1

    elif l1 == 14 and l2 == 22:
        features = ['HOXD10', 'HOXD9', 'EMX2', 'GC', 'PPY', 'SPINK1']
        reverse = [0, 0, 0, 1, 1, 1]
        v = Aggregate(df, index, features, reverse)
        if v > 0 and v < 35:
            return -1
        if v < -15 and v > -40:
            return 1
        v = list(df['NUDT21'])[index]
        if v < 1.5 and v > -4:
            return 1
        v = list(df['CACNA1C'])[index]
        if v > -0.9 and v < 4:
            return 1
        if v < -0.9 and v > -4:
            return -1

    elif l1 == 15 and l2 == 16:
        features = ['AZGP1', 'PLA2G4F', 'EVPL', 'OVOL2', 'ARHGEF16', 'DSP']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v < 5 and v > -22:
            return 1
        v = list(df['SPDEF'])[index]
        if v > 0 and v < 11:
            return -1
        v = list(df['KIRREL3'])[index]
        if v > 5 and v < 8.5:
            return 1
        if v < 5 and v > -2:
            return -1

    elif l1 == 15 and l2 == 17:
        v = list(df['TSFM'])[index]
        if v > 4.5 and v < 8:
            return 1
        elif v < 4.5 and v > 0:
            return -1
        elif v < 0 and v > -4:
            v = list(df['CD22'])[index]
            if v < 0.5 and v > -3.5:
                return 1
            if v > 0.5 and v < 8.5:
                return -1

    elif l1 == 15 and l2 == 18:
        v = list(df['TYR'])[index]
        if v > 1 and v < 12:
            return -1
        v = list(df['MIA'])[index]
        if v > 1 and v < 10:
            return -1
        v = list(df['PUS7'])[index]
        if v < 0.5 and v > -4:
            return 1
        v = list(df['INSR'])[index]
        if v < 2 and v > 0:
            return -1
        if v > 2 and v < 6:
            return 1

    elif l1 == 15 and l2 == 19:
        v = list(df['TMC5'])[index]
        if v > -0.5 and v < 8.2:
            return -1
        v = list(df['C1orf116'])[index]
        if v > -0.5 and v < 8:
            return -1
        v = list(df['GFRA4'])[index]
        if v > -2 and v < 3:
            return -1
        if v < -2 and v > -4:
            return 1

    elif l1 == 15 and l2 == 20:
        v = list(df['CLDN6'])[index]
        if v < 1 and v > -4:
            return 1
        if v > 1 and v < 10:
            return -1

    elif l1 == 15 and l2 == 21:
        v = list(df['PRSS8'])[index]
        if v < 2 and v > -4:
            return 1
        if v > 2 and v < 8:
            return -1

    elif l1 == 15 and l2 == 22:
        v = list(df['GRHL2'])[index]
        if v > -1.5 and v < 6:
            return -1
        v = list(df['ZNF485'])[index]
        if v < -2 and v > -4:
            return 1
        if v > -2 and v < 2.5:
            return 1


    elif l1 == 16 and l2 == 17:
        v = list(df['DSP'])[index]
        if v < 2 and v > -4:
            return -1
        v = list(df['CHRNA2'])[index]
        if v > -2 and v < 8.5:
            return 1
        v = list(df['KIRREL3'])[index]
        if v > 5 and v < 8.5:
            return -1
        if v < 5 and v > 0:
            return 1
        if v < 0 and v > -4:
            return -1

    elif l1 == 16 and l2 == 18:
        features = ['SLC9A2', 'RAB27B', 'CUX2', 'OVOL2', 'CDS1', 'KIAA1324']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v < 1 and v > -22:
            return -1
        if v > 1 and v < 33:
            return 1

    elif l1 == 16 and l2 == 19:
        features = ['SLC45A3', 'CREB3L4', 'STEAP2', 'DHRS7', 'ABCC4', 'TMPRSS2']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > 30 and v < 60:
            return 1
        elif v < 30 and v > -5:
            v = list(df['PATE4'])[index]
            if v > 4 and v < 10:
                return 1
            if v < 0 and v > -4:
                return -1
        elif v < -5 and v > -23:
            return 1

    elif l1 == 16 and l2 == 20:
        v = list(df['DHRS7'])[index]
        if v > 4.75 and v < 11:
            return 1
        if v < 4.75 and v > 1:
            return -1
        if v < 1 and v > -4:
            return 1

    elif l1 == 16 and l2 == 21:
        v = list(df['TSHR'])[index]
        if v > 3.5 and v < 9:
            return -1
        if v < 3.5 and v > -4:
            return 1

    elif l1 == 16 and l2 == 22:
        v = list(df['DDX3Y'])[index]
        if v < -1 and v > -4:
            return -1
        v = list(df['RAB5C'])[index]
        if v < -2 and v > -4:
            return -1
        if v > -2 and v < 6:
            return 1

    elif l1 == 17 and l2 == 18:
        v = list(df['TYR'])[index]
        if v > 1 and v < 12:
            return -1
        features = ['DUSP4', 'MIA-RAB4B', 'CDH19', 'S100B', 'ITIH6', 'GJB1']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > 5 and v < 41:
            return -1
        v = list(df['ESAM'])[index]
        if v < -2 and v > -4:
            return 1
        v = list(df['INSR'])[index]
        if v > 1.7 and v < 6:
            return 1
        if v < 1.7 and v > 0:
            return -1

    elif l1 == 17 and l2 == 19:
        v = list(df['NBEAL2'])[index]
        if v < 0 and v > -4:
            return 1
        v = list(df['POF1B'])[index]
        if v > -0.5 and v < 8:
            return -1
        v = list(df['CDK5RAP3'])[index]
        if v < 2.6 and v > 1:
            return -1
        if v > 2.6 and v < 6.5:
            return 1

    elif l1 == 17 and l2 == 20:
        v = list(df['CLDN6'])[index]
        if v < 2 and v > -4:
            return 1
        if v > 2 and v < 10:
            return -1

    elif l1 == 17 and l2 == 21:
        v = list(df['PAX8'])[index]
        if v > 4 and v < 10:
            return -1
        if v < 4 and v > -4:
            return 1

    elif l1 == 17 and l2 == 22:
        v = list(df['ARMC3'])[index]
        if v > -1.5 and v < 6.2:
            return -1
        v = list(df['DAB2'])[index]
        if v < -2 and v > -4:
            return 1
        if v > 5 and v < 8:
            return 1
        v = list(df['ELF3'])[index]
        if v > 2 and v < 8:
            return -1
        v = list(df['PBX1'])[index]
        if v > 4.5 and v < 8:
            return -1
        v = list(df['LPAR3'])[index]
        if v > -0.5 and v < 3:
            return -1
        if v < -0.5 and v > -4:
            return 1

    elif l1 == 18 and l2 == 19:
        features = ['PAX3', 'CCDC140', 'ALX1', 'RGS20', 'TYR', 'TJP3']
        reverse = [0, 0, 0, 0, 0, 1]
        v = Aggregate(df, index, features, reverse)
        if v > -8 and v < 35:
            return 1
        if v < -8 and v > -27:
            return -1

    elif l1 == 18 and l2 == 20:
        v = list(df['CLDN6'])[index]
        if v > 2 and v < 10:
            return -1
        if v < 2 and v > -4:
            return 1

    elif l1 == 18 and l2 == 21:
        v = list(df['TSHR'])[index]
        if v > 4 and v < 9:
            return -1
        if v < 4 and v > -4:
            return 1

    elif l1 == 18 and l2 == 22:
        v = list(df['TYR'])[index]
        if v > 2.5 and v < 12:
            return 1
        v = list(df['MSN'])[index]
        if v < 4.5 and v > -4:
            return -1
        features = ['FGFR2', 'EMX2', 'PKP2', 'PAX3', 'AR', 'CD24']
        reverse = [0, 0, 0, 1, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > 0 and v < 35:
            return -1
        if v < 0 and v > -20:
            return 1

    elif l1 == 19 and l2 == 20:
        features = ['TRO', 'ZNF667', 'WNK3', 'MAGEL2', 'ZIK1', 'SPSB4']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > 1 and v < 20:
            return -1
        if v < 1 and v > -20:
            return 1

    elif l1 == 19 and l2 == 21:
        v = list(df['PAX8'])[index]
        if v > 4 and v < 10:
            return -1
        if v < 4 and v > -4:
            return 1

    elif l1 == 19 and l2 == 22:
        v = list(df['RFXANK'])[index]
        if v < 1 and v > -4:
            return -1
        features = ['EMX2', 'CLDN18', 'ESR1', 'LGALS4', 'SOX17', 'DLX5']
        reverse = [0, 1, 0, 1, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > 5 and v < 40:
            return -1
        if v < -10 and v > -30:
            return 1
        features = ['ANKS3', 'SH2B1', 'RNF215', 'RHBDD3', 'PRPF6', 'NCOA4']
        reverse = [0, 0, 0, 0, 0, 1]
        v = Aggregate(df, index, features, reverse)
        if v > 10 and v < 16:
            return -1
        if v < 10 and v > -0.5:
            return 1

    elif l1 == 20 and l2 == 21:
        v = list(df['POLE'])[index]
        if v > 1.8 and v < 5:
            return 1
        if v < 1.8 and v > -1.5:
            return -1

    elif l1 == 20 and l2 == 22:
        v = list(df['UTY'])[index]
        if v > -2.5 and v < 2.5:
            return 1
        if v < -2.5 and v > -3.8:
            return -1

    elif l1 == 21 and l2 == 22:
        features = ['TG', 'FOXE1', 'IYD', 'SFTA3', 'DUOX2', 'KCNJ16']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > 12 and v < 55:
            return 1
        if v < 12 and v > -23:
            return -1

    else:
        print("Error, invalid Test parameters")

    #This isn't usually here. Only here to mimic normal classifier by forcing it to output a class rather than leaving more options
    result = randint(0, 1)
    if result == 0:
        return -1
    return 1
