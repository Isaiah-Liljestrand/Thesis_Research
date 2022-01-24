import os
import pandas as pd
from numpy.random import randint
from PairFunctions import Test
from PairFunctions import Aggregate
import time


def Classify(df, method, index):

    #Class Voting
    if method == 1:
        labelvalues = [0] * 23
        indices = list(range(len(df['labels'])))
        indices.remove(index)
        tmpdf = df.copy()
        tmpdf.drop(indices, inplace=True)
        tmpdf.reset_index(drop = True, inplace=True)
        for j in range(23):
            for k in range(23):
                if j < k:
                    result = Test(j, k, tmpdf, 0)
                    if result == 0.5 or result == -0.5:
                        labelvalues[j] += 1
                        labelvalues[k] += 1
                    else:
                        labelvalues[j] += result
                        labelvalues[k] -= result
        result = list()
        max = 0
        for j in range(23):
            if max < labelvalues[j]:
                max = labelvalues[j]
        for j in range(23):
            if max == labelvalues[j]:
                result.append(j);
        if len(result) == 2:
            tmpresult = Test(result[0], result[1], df, index)
            if tmpresult == 1:
                result = [result[0]]
            elif tmpresult == -1:
                result = [result[1]]
        elif len(result) > 2:
            tmplength = len(result) + 1
            breakout = False
            while len(result) > 1:
                if tmplength == len(result):
                    break
                tmplength = len(result)
                for i in range(len(result) - 1):
                    for j in range(i + 1, len(result)):
                        tmpresult = Test(result[i], result[j], df, index)
                        if tmpresult == 1:
                            del result[j]
                            breakout = True
                        if tmpresult == -1:
                            del result[i]
                            breakout = True
                        if breakout:
                            break
                    if breakout:
                        break
                breakout = False
        return result

    #Eliminate Weakest
    if method == 2:
        indices = list(range(len(df['labels'])))
        indices.remove(index)
        tmpdf = df.copy()
        tmpdf.drop(indices, inplace=True)
        tmpdf.reset_index(drop = True, inplace=True)
        labels = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
        for n in range(22):
            labelvalues = [0] * 23
            for j in labels:
                for k in labels:
                    if j < k:
                        result = Test(j, k, tmpdf, 0)
                        if result == 0.5 or result == -0.5:
                            labelvalues[j] += 1
                            labelvalues[k] += 1
                        else:
                            labelvalues[j] += result
                            labelvalues[k] -= result
            min = 50
            minindex = 0
            for j in labels:
                if labelvalues[j] < min:
                    min = labelvalues[j]
                    minindex = j
            removelist = list()
            for j in labels:
                if labelvalues[j] == min:
                    removelist.append(j)
            if len(removelist) == len(labels):
                break;
            labels.remove(minindex)
        result = labels
        if len(result) == 2:
            tmpresult = Test(result[0], result[1], df, index)
            if tmpresult == 1:
                result = [result[0]]
            elif tmpresult == -1:
                result = [result[1]]
        elif len(result) > 2:
            tmplength = len(result) + 1
            breakout = False
            while len(result) > 1:
                if tmplength == len(result):
                    break
                tmplength = len(result)
                for i in range(len(result) - 1):
                    for j in range(i + 1, len(result)):
                        tmpresult = Test(result[i], result[j], df, index)
                        if tmpresult == 1:
                            del result[j]
                            breakout = True
                        if tmpresult == -1:
                            del result[i]
                            breakout = True
                        if breakout:
                            break
                    if breakout:
                        break
                breakout = False
        return result

    #Tourney
    if method == 3:
        repeatflag = 0
        labels = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
        labelsize = len(labels)
        indices = list(range(len(df['labels'])))
        indices.remove(index)
        tmpdf = df.copy()
        tmpdf.drop(indices, inplace=True)
        tmpdf.reset_index(drop = True, inplace=True)
        while 1:
            if len(labels) == 1:
                break

            if labelsize > len(labels):
                repeatflag = 0
            if labelsize == len(labels):
                repeatflag += 1
            if labelsize == len(labels) and repeatflag == 5:
                break

            labelsize = len(labels)
            nextlabels = list()

            #Randomize labels in tourney
            for j in range(labelsize):
                r = randint(len(labels))
                nextlabels.append(labels[r])
                del labels[r]
            while len(nextlabels) > 1:
                if nextlabels[0] > nextlabels[1]:
                    tmp = nextlabels[0]
                    nextlabels[0] = nextlabels[1]
                    nextlabels[1] = tmp
                result = Test(nextlabels[0], nextlabels[1], tmpdf, 0)
                if result == 0 or result == -0.5 or result == 0.5:
                    labels.append(nextlabels[0])
                    labels.append(nextlabels[1])
                elif result == 1:
                    labels.append(nextlabels[0])
                elif result == -1:
                    labels.append(nextlabels[1])
                del nextlabels[0]
                del nextlabels[0]
            if len(nextlabels) == 1:
                labels.append(nextlabels[0])
        result = labels
        if len(result) > 2:
            tmplength = len(result) + 1
            breakout = False
            while len(result) > 1:
                if tmplength == len(result):
                    break
                tmplength = len(result)
                for i in range(len(result) - 1):
                    for j in range(i + 1, len(result)):
                        tmpresult = Test(result[i], result[j], df, index)
                        if tmpresult == 1:
                            del result[j]
                            breakout = True
                        if tmpresult == -1:
                            del result[i]
                            breakout = True
                        if breakout:
                            break
                    if breakout:
                        break
                breakout = False
        return result

    #Hybrid - k = 5
    if method == 4:
        labelvalues = [0] * 23
        indices = list(range(len(df['labels'])))
        indices.remove(index)
        tmpdf = df.copy()
        tmpdf.drop(indices, inplace=True)
        tmpdf.reset_index(drop = True, inplace=True)
        for j in range(23):
            for k in range(23):
                if j < k:
                    result = Test(j, k, tmpdf, 0)
                    if result == 0.5 or result == -0.5:
                        labelvalues[j] += 1
                        labelvalues[k] += 1
                    else:
                        labelvalues[j] += result
                        labelvalues[k] -= result
        labels = list()
        for k in range(5):
            result = 0
            max = 0
            for j in range(23):
                if max < labelvalues[j]:
                    result = j
                    max = labelvalues[j]
            labelvalues[result] = -22
            labels.append(result)

        labelsize = len(labels)
        repeatflag = 0
        while 1:
            if len(labels) == 1:
                break
            #Randomize labels in tourney
            if labelsize > len(labels):
                repeatflag = 0
            if labelsize == len(labels):
                repeatflag += 1
            if labelsize == len(labels) and repeatflag == 5:
                break
            labelsize = len(labels)
            nextlabels = list()
            for j in range(labelsize):
                r = randint(len(labels))
                nextlabels.append(labels[r])
                del labels[r]
            while len(nextlabels) > 1:
                if nextlabels[0] > nextlabels[1]:
                    tmp = nextlabels[0]
                    nextlabels[0] = nextlabels[1]
                    nextlabels[1] = tmp
                result = Test(nextlabels[0], nextlabels[1], tmpdf, 0)
                if result == 0 or result == -0.5 or result == 0.5:
                    labels.append(nextlabels[0])
                    labels.append(nextlabels[1])
                elif result == 1:
                    labels.append(nextlabels[0])
                elif result == -1:
                    labels.append(nextlabels[1])
                del nextlabels[0]
                del nextlabels[0]
            if len(nextlabels) == 1:
                labels.append(nextlabels[0])
        result = labels
        if len(result) > 2:
            tmplength = len(result) + 1
            breakout = False
            while len(result) > 1:
                if tmplength == len(result):
                    break
                tmplength = len(result)
                for i in range(len(result) - 1):
                    for j in range(i + 1, len(result)):
                        tmpresult = Test(result[i], result[j], df, index)
                        if tmpresult == 1:
                            del result[j]
                            breakout = True
                        if tmpresult == -1:
                            del result[i]
                            breakout = True
                        if breakout:
                            break
                    if breakout:
                        break
                breakout = False
        return result




traindf = pd.read_csv("data/exToptimizedtrain.csv")
testdf = pd.read_csv("data/exToptimizedtest.csv")

print("Finished reading in data")


validfeatures = ['labels', 'GRHL2', 'EEF1A2', 'C2orf80', 'ZBTB41', 'GFAP', 'FAM181A', 'WDR49', 'CHI3L1', 'SOX21', 'BCAS1', 'AP1M2', 'CYTH2', 'PTPRH', 'PDCD1LG2', 'DSC2', 'IL16', 'TACR1', 'TNN', 'CLDN4', 'MARVELD3', 'CDH1', 'RAB25', 'C15orf48', 'NAP1L2', 'TUSC3', 'GPR35', 'CRB3', 'CACNA2D1', 'ATP1B2', 'HPN', 'SPINT1', 'EMX2', 'HGD', 'DLK1', 'ADGB', 'NOL3', 'SPR', 'CCDC51', 'CAMKK1', 'TPM1', 'CCND1', 'APIP', 'GC', 'ANP32B', 'SASH3', 'KLK8', 'FA2H', 'SULT2B1', 'GRB7', 'EMC10', 'GPR180', 'FAM222A', 'JPH4', 'RPL37', 'TBX15', 'ATP6V1G1', 'MYT1', 'BACE2', 'TFAP2A', 'FMN1', 'MITF', 'MMP14', 'HS6ST3', 'AGR2', 'TMC5', 'PRR15L', 'AGR3', 'LGALS4', 'CDH3', 'CLIC3', 'IGSF9', 'ST14', 'TEAD3', 'AQP4', 'MLC1', 'C1orf61', 'MT3', 'NCAN', 'LAD1', 'KIAA1324', 'PRLR', 'TMEM63C', 'LMX1B', 'LRIG1', 'GJB6', 'SFRP1', 'MRAS', 'ZFP3', 'FZD7', 'MGP', 'AIF1L', 'ZNF879', 'IRX1', 'PPARG', 'GATA3', 'MFAP3L', 'CAB39L', 'TBX3', 'TBX2', 'TBX5', 'ZFY', 'ZFR2', 'HNF1A', 'HNF4A', 'VIL1', 'DDC', 'CDX1', 'NCKAP1', 'POTEJ', 'POTEI', 'EIF3CL', 'F8A3', 'POTEE', 'MTRNR2L8', 'PTPRZ1', 'GOLT1A', 'GBP6', 'ACSF2', 'CELSR2', 'CHRM2', 'TCF21', 'MTA2', 'CDH16', 'POU3F3', 'PAX2', 'SLC3A1', 'C3orf62', 'ERBB2', 'VTN', 'SLC34A2', 'SFTA3', 'SFTPA2', 'SLC22A31', 'SFTPB', 'SFTPA1', 'ACTL6A', 'ACOX3', 'DES', 'IRX2', 'ZNF467', 'WT1', 'CRB2', 'S100P', 'FERMT1', 'FOXA3', 'SLC6A20', 'TM4SF4', 'MYRF', 'ESRP2', 'KDF1', 'EPN3', 'ERBB3', 'G6PD', 'SLC45A3', 'STEAP2', 'CREB3L4', 'ABCC4', 'ANO7', 'KLK2', 'OLFML2B', 'ZIC1', 'SLC7A14', 'TYR', 'KRT19', 'TACSTD2', 'ELF3', 'HPD', 'HOXA11', 'PHC1', 'L1TD1', 'TET1', 'CACNA2D2', 'SLC4A8', 'VRTN', 'TSHR', 'SALL1', 'ASRGL1', 'STXBP6', 'ARHGAP23', 'CSTA', 'PSCA', 'OLIG2', 'C8B', 'LSMEM2', 'SPAG16', 'MAP1B', 'APC2', 'SMAD9', 'TLN2', 'OSBPL6', 'FAM86C1', 'SCRG1', 'AMBP', 'FAM181B', 'APP', 'SCNN1A', 'OLIG1', 'MAP2', 'EIF2B5', 'MSL3', 'C11orf71', 'NEMP2', 'MCM8', 'ZBTB42', 'GRIK5', 'CLDN6', 'LAMC2', 'TXNRD3', 'CDCA4', 'SLAMF7', 'HRH1', 'SERPINB13', 'AARD', 'TRPS1', 'ID1', 'ST6GALNAC1', 'TMPRSS4', 'PCSK9', 'EPS8L3', 'IHH', 'CDX2', 'SLC22A25', 'GANAB', 'ADGRE3', 'AIRE', 'OR5K1', 'FGF19', 'GJD3', 'RPS4Y1', 'DUOXA2', 'IL1A', 'IL36G', 'C10orf99', 'PLA2G4E', 'CERS3', 'ZNF24', 'WASL', 'SCAMP1', 'WAPL', 'SS18', 'UBA3', 'WDFY4', 'OGDHL', 'SLC22A2', 'SULT1C2', 'CATSPER1', 'OR4F6', 'PTP4A2', 'ST3GAL5', 'TAZ', 'FKBP10', 'COL4A2', 'TMEM54', 'COL3A1', 'COL1A2', 'MEP1A', 'GAPDHS', 'KLK10', 'DPYSL5', 'RHBG', 'DCT', 'FOXF1', 'TBX4', 'SFTPC', 'KCNJ15', 'TSTD1', 'ARFIP2', 'DLG3', 'ERGIC1', 'SELENBP1', 'FOXE1', 'WDR72', 'MAP3K19', 'ANKRD18B', 'ST6GALNAC2', 'SLC2A10', 'IRX5', 'CCDC149', 'HID1', 'TREML4', 'WNT7A', 'ARL17A', 'CLDN16', 'KLHL14', 'UPK3B', 'SQSTM1', 'DCP1A', 'ANO10', 'TTLL8', 'SGTA', 'PPA2', 'SPINK1', 'MAK16', 'USH1C', 'SMIM24', 'FOXA2', 'HKDC1', 'HHLA2', 'PRSS8', 'UBE2R2', 'RAX', 'FAM166B', 'DDX3Y', 'TMEFF2', 'SRL', 'TBX19', 'AGBL4', 'RHAG', 'WNK3', 'PROM2', 'MMP21', 'EPB42', 'LPAR3', 'GJB1', 'DMGDH', 'ISL1', 'CDHR5', 'CTSE', 'GDF3', 'PAX8', 'MECOM', 'SOX17', 'MEIS1', 'CFI', 'FGF18', 'C5orf38', 'AZGP1', 'CLMN', 'ZCCHC12', 'WNT3A', 'ISX', 'FABP1', 'SLC39A5', 'GUCA2A', 'NR1I2', 'MATN3', 'TMEM106C', 'TMEM232', 'INPP5E', 'CTRL', 'NPIPB12', 'NLGN4Y', 'HMGN1', 'LHX8', 'E2F1', 'DSN1', 'UBE2T', 'RFC4', 'CDC25C', 'LIG1', 'TRDN', 'PRRC2A', 'PITX1', 'SERPINB3', 'KIF2C', 'WDR46', 'KDELR1', 'OVOL2', 'RND3', 'APOB', 'SCN7A', 'TMEM119', 'UTY', 'DHRS1', 'SLC25A28', 'PPDPF', 'ACTB', 'CAPZB', 'MAT2B', 'IRF6', 'BMP6', 'ADAM12', 'PLOD3', 'SP6', 'UNC119B', 'BET1', 'ZBTB20', 'DOK5', 'SERPINB4', 'BCAR1', 'LMNB1', 'MIS18A', 'AUNIP', 'NUBP1', 'ATAD3B', 'SLC33A1', 'PIP5K1C', 'ERBB4', 'TRABD', 'SPINT2', 'LSR', 'MAPK13', 'PRRG2', 'HMGA1', 'ABHD17C', 'CCDC126', 'CD22', 'DCAF12L2', 'FAM216A', 'MED1', 'USP9Y', 'CUX2', 'KDM5D', 'EIF1AY', 'PRDX5', 'PDXP', 'TG', 'ZSCAN18', 'ZNF610', 'ZNF43', 'VPS37D', 'ZNF135', 'CHST10', 'PIM1', 'ZNF541', 'SYCP2', 'SMC1B', 'ITGA2B', 'KLHL35', 'EEF1G', 'DUOX1', 'NBPF26', 'EXOC6', 'RFNG', 'LUZP2', 'RPS6KA4', 'RRP7A', 'RSPH3', 'COX10', 'HEATR5A', 'TMEM164', 'EOMES', 'MYB', 'ANKRD6', 'UBA1', 'PHGR1', 'MOGAT3', 'CLRN3', 'FUT2', 'ZPR1', 'SCGB1D2', 'YWHAB', 'SLC5A6', 'TRABD2A', 'PDSS1', 'NOX1', 'CLDN10', 'WDR34', 'RTEL1-TNFRSF6B', 'PJA2', 'GNL3L', 'LMAN2L', 'OLFM3', 'SLC25A15', 'GPA33', 'FAM83A', 'SUOX', 'DLG2', 'TUBGCP2', 'FXYD5', 'IL15RA', 'SUGT1', 'RPS6', 'SRM', 'RND2', 'TUBB4A', 'SLC7A3', 'ZNF667', 'DPPA4', 'DLX5', 'KCTD1', 'OTUD3', 'EIF4E3', 'LMTK2', 'FSD1L', 'NDUFA7', 'SIK3', 'SPDYE5', 'TRAPPC5', 'TSSK3', 'GNG12', 'GAN', 'CMIP', 'ZNF460', 'STYK1', 'SERPINB5', 'POMK', 'CTU1', 'ZFPM1', 'PLXNB1', 'NPR1', 'SPON1', 'BCAM', 'STMN2', 'TICRR', 'DYNLL2', 'ADI1', 'MAGED2', 'CBY1', 'CREB3', 'EPCAM', 'FAT2', 'DUOXA1', 'DUOX2', 'TFR2', 'IL1RL2', 'GPRC5C', 'NKX3-2', 'NKX6-1', 'TUBD1', 'SPTB', 'TTLL9', 'NOXRED1', 'DSG3', 'CLCA2', 'PHOX2B', 'GDAP1L1', 'SEL1L2', 'GH2', 'KLF16', 'PHF8', 'PELP1', 'PFN2', 'MRPS11', 'ACMSD', 'SRGAP2C', 'YBX3', 'DSC3', 'RIPK4', 'EFNB2', 'KRT5', 'TRIM46', 'OR52W1', 'GDF9', 'GUCA1C', 'TMEM130', 'DNAH14', 'OGG1', 'TP63', 'SLC22A23', 'RPL7', 'NONO', 'MRPL47', 'AMFR', 'NDUFB2', 'TRAPPC10', 'SOX4', 'NPC1L1', 'ABLIM1', 'MSLN', 'MUC1', 'GPRC5A', 'KCNN4', 'ACVR1', 'MMADHC', 'FDX1', 'LZTS1', 'SLC16A4', 'DAAM2', 'BEST1', 'TMEM238', 'DDAH1', 'SMAD6', 'PBLD', 'ADAP1', 'LIN28B', 'ANXA8', 'CTDSP1', 'ARHGAP22', 'CYB5D2', 'BRD7', 'GATC', 'MTR', 'IFT46', 'HTRA1', 'CDK19', 'CEACAM6', 'SDR16C5', 'CEACAM5', 'FAM83E', 'SAE1', 'ANKRD18A', 'GRK6', 'RELB', 'TRIM11', 'TACC3', 'CARD11', 'DHX34', 'FANCL', 'MUC16', 'KLK11', 'KLK5', 'TMEM131', 'RBM38', 'NSUN7', 'CCDC102A', 'RAB1A', 'TRIM47', 'GLCE', 'RALGAPB', 'ZNF174', 'AHCYL2', 'CUL5', 'TTC6', 'LRRC26', 'C9orf152', 'FBXL20', 'SHOX2', 'KLHDC7A', 'C1orf210', 'PLCXD1', 'SLC25A25', 'MOB1A', 'ARIH2', 'C9orf16', 'METTL17', 'ATP1A1', 'PAX3', 'GPM6B', 'CCDC140', 'EDNRB', 'RGS20', 'SGCD', 'FOXA1', 'ALDH3B2', 'RCOR2', 'LGR5', 'SIX4', 'AQP5', 'EHHADH', 'KDM4E', 'NOS3', 'GPN1', 'RBM47', 'EDNRA', 'NUPR1', 'EPS8L2', 'RASIP1', 'CD2BP2', 'MRPS23', 'CST3', 'OXA1L', 'SLC1A5', 'PCMT1', 'MASP2', 'RUNX1T1', 'ADCY5', 'USHBP1', 'KCNK3', 'NHLH2', 'MAGEB17', 'SSX3', 'SORBS2', 'RNF180', 'CADPS2', 'COL13A1', 'NES', 'RDH8', 'TMPRSS2', 'TRIM55', 'EFCAB3', 'GIPR', 'CYP8B1', 'ALLC', 'YAP1', 'SPARCL1', 'EGFR', 'TJP1', 'BGN', 'ADGRL4', 'CLMP', 'PARVA', 'FNDC4', 'S100A13', 'SELENOM', 'DLL4', 'POTEC', 'ITIH1', 'SERPINA10', 'ASGR2', 'NWD1', 'ITIH2', 'OR51E2', 'CPB2', 'ADD2', 'INA', 'RIMS4', 'DNAAF3', 'APOA1', 'ANTXR1', 'CYSTM1', 'AHSA1', 'PERP', 'PLPP1', 'ZNF613', 'PROSER2', 'PMEL', 'ZBTB7A', 'ST3GAL2', 'PLET1', 'CD300LB', 'EEF2', 'SF3A2', 'PTPN23', 'ELMO2', 'CFAP65', 'TAAR2', 'ZBTB45', 'CREBRF', 'LEFTY2', 'HOXD3', 'JMJD6', 'PLIN3', 'ACLY', 'PBX1', 'TNFRSF11A', 'CAPN5', 'PROS1', 'LRRC66', 'PDCL3', 'CD19', 'ATP2C1', 'NCF1', 'NUP153', 'FKBP7', 'FKBP9', 'LAPTM4B', 'PPIC', 'SYDE1', 'STXBP1', 'RBBP9', 'BTK', 'ARHGAP39', 'PNPLA1', 'ZNF771', 'CTXN1', 'SOX12', 'CLDN3', 'CLDN7', 'CNTN3', 'DPF2', 'TMPRSS3', 'PPP2R3A', 'ATP6V1B1', 'SRGAP3', 'ESR1', 'NUDT21', 'CMC4', 'RPL18A', 'TRAPPC8', 'GNA15', 'SBNO2', 'CCDC38', 'POTEG', 'ADGRF1', 'ADAMTSL2', 'NR5A1', 'HOXD10', 'HOXD9', 'PPY', 'CACNA1C', 'PLA2G4F', 'EVPL', 'ARHGEF16', 'DSP', 'SPDEF', 'KIRREL3', 'TSFM', 'MIA', 'PUS7', 'INSR', 'C1orf116', 'GFRA4', 'ZNF485', 'CHRNA2', 'SLC9A2', 'RAB27B', 'CDS1', 'DHRS7', 'PATE4', 'RAB5C', 'DUSP4', 'MIA-RAB4B', 'CDH19', 'S100B', 'ITIH6', 'ESAM', 'NBEAL2', 'POF1B', 'CDK5RAP3', 'ARMC3', 'DAB2', 'ALX1', 'TJP3', 'MSN', 'FGFR2', 'PKP2', 'AR', 'CD24', 'TRO', 'MAGEL2', 'ZIK1', 'SPSB4', 'RFXANK', 'CLDN18', 'ANKS3', 'SH2B1', 'RNF215', 'RHBDD3', 'PRPF6', 'NCOA4', 'POLE', 'IYD', 'KCNJ16']

traindf = traindf.reindex(columns=validfeatures)
testdf = testdf.reindex(columns=validfeatures)

falsenegative = [0] * 23
falsepositive = [0] * 23


#Method 1
method = 1
df = traindf
labellist = list(df['labels'])
success = 0
multiclass = 0

for i in range(len(labellist)):
    if (i % 100) == 0:
        print("1/8: ", i)
    result = Classify(df, method, i)
    answer = labellist[i]

    if answer in result:
        success += 1
    if len(result) > 1:
        multiclass += 1
accuracy = (success / len(labellist)) * 100
multiclass = (multiclass / len(labellist)) * 100
print("\nMethod ", method, ", Training Accuracy:", accuracy)
acc1 = accuracy
multi1 = multiclass

df = testdf
labellist = list(df['labels'])
success = 0
multiclass = 0
overalltime = 0

for i in range(len(labellist)):
    if (i % 100) == 0:
        print("2/8: ", i)
    start = time.time()
    result = Classify(df, method, i)
    end = time.time()
    overalltime += (end - start)
    answer = labellist[i]

    if answer in result:
        success += 1
    if len(result) > 1:
        multiclass += 1
accuracy = (success / len(labellist)) * 100
multiclass = (multiclass / len(labellist)) * 100
print("Method ", method, ", Testing Accuracy:", accuracy)
acc2 = accuracy
multi2 = multiclass
time2 = overalltime / len(labellist)

print("False Positives:")
print(falsepositive)
print("False Negatives:")
print(falsenegative)

labellist = list(df['labels'])
sizes = [0] * 23
for i in range(len(labellist)):
    sizes[labellist[i]] += 1
for i in range(23):
    falsepositive[i] /= sizes[i]
    falsenegative[i] /= sizes[i]

print("\n\nFalse Positive percentages:")
print(falsepositive)
print("False Negatives percentages:")
print(falsenegative)


print("False Positive Relative to instances")



#Method 2
method = 2
df = traindf
labellist = list(df['labels'])
success = 0
multiclass = 0

for i in range(len(labellist)):
    if (i % 100) == 0:
        print("3/8: ", i)
    result = Classify(df, method, i)
    answer = labellist[i]

    if answer in result:
        success += 1
    if len(result) > 1:
        multiclass += 1
accuracy = (success / len(labellist)) * 100
multiclass = (multiclass / len(labellist)) * 100
print("\nMethod ", method, ", Training Accuracy:", accuracy)
acc3 = accuracy
multi3 = multiclass

df = testdf
labellist = list(df['labels'])
success = 0
multiclass = 0
overalltime = 0

for i in range(len(labellist)):
    if (i % 100) == 0:
        print("4/8: ", i)
    start = time.time()
    result = Classify(df, method, i)
    end = time.time()
    overalltime += (end - start)
    answer = labellist[i]

    if answer in result:
        success += 1
    if len(result) > 1:
        multiclass += 1
accuracy = (success / len(labellist)) * 100
multiclass = (multiclass / len(labellist)) * 100
print("Method ", method, ", Testing Accuracy:", accuracy)
acc4 = accuracy
multi4 = multiclass
time4 = overalltime / len(labellist)


#Method 3
method = 3
df = traindf
labellist = list(df['labels'])
success = 0
multiclass = 0

for i in range(len(labellist)):
    if (i % 100) == 0:
        print("5/8: ", i)
    result = Classify(df, method, i)
    answer = labellist[i]

    if answer in result:
        success += 1
    if len(result) > 1:
        multiclass += 1
accuracy = (success / len(labellist)) * 100
multiclass = (multiclass / len(labellist)) * 100
print("\nMethod ", method, ", Training Accuracy:", accuracy)
acc5 = accuracy
multi5 = multiclass

df = testdf
labellist = list(df['labels'])
success = 0
multiclass = 0
overalltime = 0

for i in range(len(labellist)):
    if (i % 100) == 0:
        print("6/8: ", i)
    start = time.time()
    result = Classify(df, method, i)
    end = time.time()
    overalltime += (end - start)
    answer = labellist[i]

    if answer in result:
        success += 1
    if len(result) > 1:
        multiclass += 1
accuracy = (success / len(labellist)) * 100
multiclass = (multiclass / len(labellist)) * 100
print("Method ", method, ", Testing Accuracy:", accuracy)
acc6 = accuracy
multi6 = multiclass
time6 = overalltime / len(labellist)

#Method 4
method = 4
df = traindf
labellist = list(df['labels'])
success = 0
multiclass = 0

for i in range(len(labellist)):
    if (i % 100) == 0:
        print("7/8: ", i)
    result = Classify(df, method, i)
    answer = labellist[i]

    if answer in result:
        success += 1
    if len(result) > 1:
        multiclass += 1
accuracy = (success / len(labellist)) * 100
multiclass = (multiclass / len(labellist)) * 100
print("\nMethod ", method, ", Training Accuracy:", accuracy)
acc7 = accuracy
multi7 = multiclass

df = testdf
labellist = list(df['labels'])
success = 0
multiclass = 0
overalltime = 0

for i in range(len(labellist)):
    if (i % 100) == 0:
        print("8/8: ", i)
    start = time.time()
    result = Classify(df, method, i)
    end = time.time()
    overalltime += (end - start)
    answer = labellist[i]

    if answer in result:
        success += 1
    if len(result) > 1:
        multiclass += 1
accuracy = (success / len(labellist)) * 100
multiclass = (multiclass / len(labellist)) * 100
print("Method ", method, ", Testing Accuracy:", accuracy)
acc8 = accuracy
multi8 = multiclass
time8 = overalltime / len(labellist)

print("\n\nFinished running everything\n\n")

print("Method 1 Training:\nAccuracy:", acc1, "\nMulti-class:", multi1, "\n")

print("\nMethod 1 Testing\nAccuracy:", acc2, "\nMulti-class:", multi2, "\nTime:", time2, "\n")

print("\nMethod 2 Training\nAccuracy:", acc3, "\nMulti-class:", multi3, "\n")

print("\nMethod 2 Testing\nAccuracy:", acc4, "\nMulti-class:", multi4, "\nTime:", time4, "\n")

print("\nMethod 3 Training\nAccuracy:", acc5, "\nMulti-class:", multi5, "\n")

print("\nMethod 3 Testing\nAccuracy:", acc6, "\nMulti-class:", multi6, "\nTime:", time6, "\n")

print("\nMethod 4 Training\nAccuracy:", acc7, "\nMulti-class:", multi7, "\n")

print("\nMethod 4 Testing\nAccuracy:", acc8, "\nMulti-class:", multi8, "\nTime:", time8, "\n")

print("Done")


#Test the accuracies of each pairwise classifier. Used to catch typos and errors that cause high innacuracy.
#accuracy = list()
#labelpairs = list()
#df = testdf


#
#for i in range(23):
#    for j in range(i + 1,23):
#        #print("Starting pair ", i, " and ", j)
#        total = 0
#        success = 0
#        for k in range(len(df["labels"])):
#            if list(df["labels"])[k] == i:
#                result = Test(i, j, df, k)
#                if result == 1 or result == 0.5 or result == -0.5:
#                    success += 1
#                total += 1
#            elif list(df["labels"])[k] == j:
#                result = Test(i, j, df, k)
#                if result == -1 or result == 0.5 or result == -0.5:
#                    success += 1
#                total += 1
#        accuracy.append(success / total)
#        print("Labels ", i, " and ", j, ": ", success / total)
        #labelstring = str(i) + " " + str(j)
        #labelpairs.append(labelstring)

#print(labelpairs)
#print(accuracy)
#for i in range(len(labelpairs)):
#    print(labelpairs[i], " ", accuracy[i])
#print("\n\n\n\nLabel Pairs with worse than 98% accuracy")
#for i in range(len(labelpairs)):
#    if accuracy[i] < 0.98:
#        print(labelpairs[i], " ", accuracy[i])
