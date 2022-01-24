import os
import pandas as pd
from numpy.random import randint
from PairFunctions import Test
from PairFunctions import Aggregate

def Classify(df, method, index):

    #Class Voting
    if method == 1:
        indices = list(range(len(df['labels'])))
        indices.remove(index)
        tmpdf = df.copy()
        tmpdf.drop(indices, inplace=True)
        tmpdf.reset_index(drop = True, inplace=True)
        tmp = list(tmpdf['labels'])[0]
        for j in range(23):
            for k in range(23):
                if j == tmp or k == tmp:
                    if j < k:
                        result = Test(j, k, tmpdf, 0)
                        if result == 0.5 or result == -0.5:
                            return True
        return False


#traindf = pd.read_csv("data/exToptimizedtrain.csv")
testdf = pd.read_csv("data/exToptimizedtest.csv")

print("Finished reading in data")

validfeatures = ['labels', 'GRHL2', 'EEF1A2', 'C2orf80', 'ZBTB41', 'GFAP', 'FAM181A', 'WDR49', 'CHI3L1', 'SOX21', 'BCAS1', 'AP1M2', 'CYTH2', 'PTPRH', 'PDCD1LG2', 'DSC2', 'IL16', 'TACR1', 'TNN', 'CLDN4', 'MARVELD3', 'CDH1', 'RAB25', 'C15orf48', 'NAP1L2', 'TUSC3', 'GPR35', 'CRB3', 'CACNA2D1', 'ATP1B2', 'HPN', 'SPINT1', 'EMX2', 'HGD', 'DLK1', 'ADGB', 'NOL3', 'SPR', 'CCDC51', 'CAMKK1', 'TPM1', 'CCND1', 'APIP', 'GC', 'ANP32B', 'SASH3', 'KLK8', 'FA2H', 'SULT2B1', 'GRB7', 'EMC10', 'GPR180', 'FAM222A', 'JPH4', 'RPL37', 'TBX15', 'ATP6V1G1', 'MYT1', 'BACE2', 'TFAP2A', 'FMN1', 'MITF', 'MMP14', 'HS6ST3', 'AGR2', 'TMC5', 'PRR15L', 'AGR3', 'LGALS4', 'CDH3', 'CLIC3', 'IGSF9', 'ST14', 'TEAD3', 'AQP4', 'MLC1', 'C1orf61', 'MT3', 'NCAN', 'LAD1', 'KIAA1324', 'PRLR', 'TMEM63C', 'LMX1B', 'LRIG1', 'GJB6', 'SFRP1', 'MRAS', 'ZFP3', 'FZD7', 'MGP', 'AIF1L', 'ZNF879', 'IRX1', 'PPARG', 'GATA3', 'MFAP3L', 'CAB39L', 'TBX3', 'TBX2', 'TBX5', 'ZFY', 'ZFR2', 'HNF1A', 'HNF4A', 'VIL1', 'DDC', 'CDX1', 'NCKAP1', 'POTEJ', 'POTEI', 'EIF3CL', 'F8A3', 'POTEE', 'MTRNR2L8', 'PTPRZ1', 'GOLT1A', 'GBP6', 'ACSF2', 'CELSR2', 'CHRM2', 'TCF21', 'MTA2', 'CDH16', 'POU3F3', 'PAX2', 'SLC3A1', 'C3orf62', 'ERBB2', 'VTN', 'SLC34A2', 'SFTA3', 'SFTPA2', 'SLC22A31', 'SFTPB', 'SFTPA1', 'ACTL6A', 'ACOX3', 'DES', 'IRX2', 'ZNF467', 'WT1', 'CRB2', 'S100P', 'FERMT1', 'FOXA3', 'SLC6A20', 'TM4SF4', 'MYRF', 'ESRP2', 'KDF1', 'EPN3', 'ERBB3', 'G6PD', 'SLC45A3', 'STEAP2', 'CREB3L4', 'ABCC4', 'ANO7', 'KLK2', 'OLFML2B', 'ZIC1', 'SLC7A14', 'TYR', 'KRT19', 'TACSTD2', 'ELF3', 'HPD', 'HOXA11', 'PHC1', 'L1TD1', 'TET1', 'CACNA2D2', 'SLC4A8', 'VRTN', 'TSHR', 'SALL1', 'ASRGL1', 'STXBP6', 'ARHGAP23', 'CSTA', 'PSCA', 'OLIG2', 'C8B', 'LSMEM2', 'SPAG16', 'MAP1B', 'APC2', 'SMAD9', 'TLN2', 'OSBPL6', 'FAM86C1', 'SCRG1', 'AMBP', 'FAM181B', 'APP', 'SCNN1A', 'OLIG1', 'MAP2', 'EIF2B5', 'MSL3', 'C11orf71', 'NEMP2', 'MCM8', 'ZBTB42', 'GRIK5', 'CLDN6', 'LAMC2', 'TXNRD3', 'CDCA4', 'SLAMF7', 'HRH1', 'SERPINB13', 'AARD', 'TRPS1', 'ID1', 'ST6GALNAC1', 'TMPRSS4', 'PCSK9', 'EPS8L3', 'IHH', 'CDX2', 'SLC22A25', 'GANAB', 'ADGRE3', 'AIRE', 'OR5K1', 'FGF19', 'GJD3', 'RPS4Y1', 'DUOXA2', 'IL1A', 'IL36G', 'C10orf99', 'PLA2G4E', 'CERS3', 'ZNF24', 'WASL', 'SCAMP1', 'WAPL', 'SS18', 'UBA3', 'WDFY4', 'OGDHL', 'SLC22A2', 'SULT1C2', 'CATSPER1', 'OR4F6', 'PTP4A2', 'ST3GAL5', 'TAZ', 'FKBP10', 'COL4A2', 'TMEM54', 'COL3A1', 'COL1A2', 'MEP1A', 'GAPDHS', 'KLK10', 'DPYSL5', 'RHBG', 'DCT', 'FOXF1', 'TBX4', 'SFTPC', 'KCNJ15', 'TSTD1', 'ARFIP2', 'DLG3', 'ERGIC1', 'SELENBP1', 'FOXE1', 'WDR72', 'MAP3K19', 'ANKRD18B', 'ST6GALNAC2', 'SLC2A10', 'IRX5', 'CCDC149', 'HID1', 'TREML4', 'WNT7A', 'ARL17A', 'CLDN16', 'KLHL14', 'UPK3B', 'SQSTM1', 'DCP1A', 'ANO10', 'TTLL8', 'SGTA', 'PPA2', 'SPINK1', 'MAK16', 'USH1C', 'SMIM24', 'FOXA2', 'HKDC1', 'HHLA2', 'PRSS8', 'UBE2R2', 'RAX', 'FAM166B', 'DDX3Y', 'TMEFF2', 'SRL', 'TBX19', 'AGBL4', 'RHAG', 'WNK3', 'PROM2', 'MMP21', 'EPB42', 'LPAR3', 'GJB1', 'DMGDH', 'ISL1', 'CDHR5', 'CTSE', 'GDF3', 'PAX8', 'MECOM', 'SOX17', 'MEIS1', 'CFI', 'FGF18', 'C5orf38', 'AZGP1', 'CLMN', 'ZCCHC12', 'WNT3A', 'ISX', 'FABP1', 'SLC39A5', 'GUCA2A', 'NR1I2', 'MATN3', 'TMEM106C', 'TMEM232', 'INPP5E', 'CTRL', 'NPIPB12', 'NLGN4Y', 'HMGN1', 'LHX8', 'E2F1', 'DSN1', 'UBE2T', 'RFC4', 'CDC25C', 'LIG1', 'TRDN', 'PRRC2A', 'PITX1', 'SERPINB3', 'KIF2C', 'WDR46', 'KDELR1', 'OVOL2', 'RND3', 'APOB', 'SCN7A', 'TMEM119', 'UTY', 'DHRS1', 'SLC25A28', 'PPDPF', 'ACTB', 'CAPZB', 'MAT2B', 'IRF6', 'BMP6', 'ADAM12', 'PLOD3', 'SP6', 'UNC119B', 'BET1', 'ZBTB20', 'DOK5', 'SERPINB4', 'BCAR1', 'LMNB1', 'MIS18A', 'AUNIP', 'NUBP1', 'ATAD3B', 'SLC33A1', 'PIP5K1C', 'ERBB4', 'TRABD', 'SPINT2', 'LSR', 'MAPK13', 'PRRG2', 'HMGA1', 'ABHD17C', 'CCDC126', 'CD22', 'DCAF12L2', 'FAM216A', 'MED1', 'USP9Y', 'CUX2', 'KDM5D', 'EIF1AY', 'PRDX5', 'PDXP', 'TG', 'ZSCAN18', 'ZNF610', 'ZNF43', 'VPS37D', 'ZNF135', 'CHST10', 'PIM1', 'ZNF541', 'SYCP2', 'SMC1B', 'ITGA2B', 'KLHL35', 'EEF1G', 'DUOX1', 'NBPF26', 'EXOC6', 'RFNG', 'LUZP2', 'RPS6KA4', 'RRP7A', 'RSPH3', 'COX10', 'HEATR5A', 'TMEM164', 'EOMES', 'MYB', 'ANKRD6', 'UBA1', 'PHGR1', 'MOGAT3', 'CLRN3', 'FUT2', 'ZPR1', 'SCGB1D2', 'YWHAB', 'SLC5A6', 'TRABD2A', 'PDSS1', 'NOX1', 'CLDN10', 'WDR34', 'RTEL1-TNFRSF6B', 'PJA2', 'GNL3L', 'LMAN2L', 'OLFM3', 'SLC25A15', 'GPA33', 'FAM83A', 'SUOX', 'DLG2', 'TUBGCP2', 'FXYD5', 'IL15RA', 'SUGT1', 'RPS6', 'SRM', 'RND2', 'TUBB4A', 'SLC7A3', 'ZNF667', 'DPPA4', 'DLX5', 'KCTD1', 'OTUD3', 'EIF4E3', 'LMTK2', 'FSD1L', 'NDUFA7', 'SIK3', 'SPDYE5', 'TRAPPC5', 'TSSK3', 'GNG12', 'GAN', 'CMIP', 'ZNF460', 'STYK1', 'SERPINB5', 'POMK', 'CTU1', 'ZFPM1', 'PLXNB1', 'NPR1', 'SPON1', 'BCAM', 'STMN2', 'TICRR', 'DYNLL2', 'ADI1', 'MAGED2', 'CBY1', 'CREB3', 'EPCAM', 'FAT2', 'DUOXA1', 'DUOX2', 'TFR2', 'IL1RL2', 'GPRC5C', 'NKX3-2', 'NKX6-1', 'TUBD1', 'SPTB', 'TTLL9', 'NOXRED1', 'DSG3', 'CLCA2', 'PHOX2B', 'GDAP1L1', 'SEL1L2', 'GH2', 'KLF16', 'PHF8', 'PELP1', 'PFN2', 'MRPS11', 'ACMSD', 'SRGAP2C', 'YBX3', 'DSC3', 'RIPK4', 'EFNB2', 'KRT5', 'TRIM46', 'OR52W1', 'GDF9', 'GUCA1C', 'TMEM130', 'DNAH14', 'OGG1', 'TP63', 'SLC22A23', 'RPL7', 'NONO', 'MRPL47', 'AMFR', 'NDUFB2', 'TRAPPC10', 'SOX4', 'NPC1L1', 'ABLIM1', 'MSLN', 'MUC1', 'GPRC5A', 'KCNN4', 'ACVR1', 'MMADHC', 'FDX1', 'LZTS1', 'SLC16A4', 'DAAM2', 'BEST1', 'TMEM238', 'DDAH1', 'SMAD6', 'PBLD', 'ADAP1', 'LIN28B', 'ANXA8', 'CTDSP1', 'ARHGAP22', 'CYB5D2', 'BRD7', 'GATC', 'MTR', 'IFT46', 'HTRA1', 'CDK19', 'CEACAM6', 'SDR16C5', 'CEACAM5', 'FAM83E', 'SAE1', 'ANKRD18A', 'GRK6', 'RELB', 'TRIM11', 'TACC3', 'CARD11', 'DHX34', 'FANCL', 'MUC16', 'KLK11', 'KLK5', 'TMEM131', 'RBM38', 'NSUN7', 'CCDC102A', 'RAB1A', 'TRIM47', 'GLCE', 'RALGAPB', 'ZNF174', 'AHCYL2', 'CUL5', 'TTC6', 'LRRC26', 'C9orf152', 'FBXL20', 'SHOX2', 'KLHDC7A', 'C1orf210', 'PLCXD1', 'SLC25A25', 'MOB1A', 'ARIH2', 'C9orf16', 'METTL17', 'ATP1A1', 'PAX3', 'GPM6B', 'CCDC140', 'EDNRB', 'RGS20', 'SGCD', 'FOXA1', 'ALDH3B2', 'RCOR2', 'LGR5', 'SIX4', 'AQP5', 'EHHADH', 'KDM4E', 'NOS3', 'GPN1', 'RBM47', 'EDNRA', 'NUPR1', 'EPS8L2', 'RASIP1', 'CD2BP2', 'MRPS23', 'CST3', 'OXA1L', 'SLC1A5', 'PCMT1', 'MASP2', 'RUNX1T1', 'ADCY5', 'USHBP1', 'KCNK3', 'NHLH2', 'MAGEB17', 'SSX3', 'SORBS2', 'RNF180', 'CADPS2', 'COL13A1', 'NES', 'RDH8', 'TMPRSS2', 'TRIM55', 'EFCAB3', 'GIPR', 'CYP8B1', 'ALLC', 'YAP1', 'SPARCL1', 'EGFR', 'TJP1', 'BGN', 'ADGRL4', 'CLMP', 'PARVA', 'FNDC4', 'S100A13', 'SELENOM', 'DLL4', 'POTEC', 'ITIH1', 'SERPINA10', 'ASGR2', 'NWD1', 'ITIH2', 'OR51E2', 'CPB2', 'ADD2', 'INA', 'RIMS4', 'DNAAF3', 'APOA1', 'ANTXR1', 'CYSTM1', 'AHSA1', 'PERP', 'PLPP1', 'ZNF613', 'PROSER2', 'PMEL', 'ZBTB7A', 'ST3GAL2', 'PLET1', 'CD300LB', 'EEF2', 'SF3A2', 'PTPN23', 'ELMO2', 'CFAP65', 'TAAR2', 'ZBTB45', 'CREBRF', 'LEFTY2', 'HOXD3', 'JMJD6', 'PLIN3', 'ACLY', 'PBX1', 'TNFRSF11A', 'CAPN5', 'PROS1', 'LRRC66', 'PDCL3', 'CD19', 'ATP2C1', 'NCF1', 'NUP153', 'FKBP7', 'FKBP9', 'LAPTM4B', 'PPIC', 'SYDE1', 'STXBP1', 'RBBP9', 'BTK', 'ARHGAP39', 'PNPLA1', 'ZNF771', 'CTXN1', 'SOX12', 'CLDN3', 'CLDN7', 'CNTN3', 'DPF2', 'TMPRSS3', 'PPP2R3A', 'ATP6V1B1', 'SRGAP3', 'ESR1', 'NUDT21', 'CMC4', 'RPL18A', 'TRAPPC8', 'GNA15', 'SBNO2', 'CCDC38', 'POTEG', 'ADGRF1', 'ADAMTSL2', 'NR5A1', 'HOXD10', 'HOXD9', 'PPY', 'CACNA1C', 'PLA2G4F', 'EVPL', 'ARHGEF16', 'DSP', 'SPDEF', 'KIRREL3', 'TSFM', 'MIA', 'PUS7', 'INSR', 'C1orf116', 'GFRA4', 'ZNF485', 'CHRNA2', 'SLC9A2', 'RAB27B', 'CDS1', 'DHRS7', 'PATE4', 'RAB5C', 'DUSP4', 'MIA-RAB4B', 'CDH19', 'S100B', 'ITIH6', 'ESAM', 'NBEAL2', 'POF1B', 'CDK5RAP3', 'ARMC3', 'DAB2', 'ALX1', 'TJP3', 'MSN', 'FGFR2', 'PKP2', 'AR', 'CD24', 'TRO', 'MAGEL2', 'ZIK1', 'SPSB4', 'RFXANK', 'CLDN18', 'ANKS3', 'SH2B1', 'RNF215', 'RHBDD3', 'PRPF6', 'NCOA4', 'POLE', 'IYD', 'KCNJ16']

#traindf = traindf.reindex(columns=validfeatures)
testdf = testdf.reindex(columns=validfeatures)

totallist = list()
multilist = list()
acclist = list()
multilistp = list()

total = 0
acc = 0
multi = 0
for i in range(23):
    for j in range(i + 1, 23):
        print("Starting pair", i, " and ", j)
        tmptotal = 0
        tmpmulti = 0
        tmpacc = 0
        tmptestdf = testdf.copy()
        labellist = tmptestdf['labels']
        elimlist = list()
        for k in range(len(labellist)):
            if labellist[k] != i and labellist[k] != j:
                elimlist.append(k)
        tmptestdf.drop(elimlist, inplace=True)
        tmptestdf.reset_index(drop = True, inplace = True)
        for k in range(len(tmptestdf['labels'])):
            result = Test(i, j, tmptestdf, k)
            total += 1
            tmptotal += 1
            if result == 0.5 or result == -0.5:
                multi += 1
                tmpmulti += 1
                tmpacc += 1
                acc += 1
            if result == 1 and list(tmptestdf['labels'])[k] == i:
                tmpacc += 1
                acc += 1
            if result == -1 and list(tmptestdf['labels'])[k] == j:
                tmpacc += 1
                acc += 1
        totallist.append(tmptotal)
        acclist.append((tmpacc / tmptotal) * 100)
        multilist.append(tmpmulti)
        multilistp.append((tmpmulti / tmptotal) * 100)

print("total:",total)
print("multi:",multi)
print("acc:",acc / total)

print("totallist:", totallist)
print("\n\nmultilist:", multilist)
print("\n\nacclist:", acclist)
print("\n\nmultilistp:", multilistp)
print("\n\n")

total = 0
multi = 0
acc = 0

acc100 = 0
acc99 = 0
acc98 = 0
acc97 = 0
acc96 = 0
acc90 = 0

multi0 = 0
multi5 = 0
multi10 = 0

for i in range(len(totallist)):
    total += totallist[i]
    acc += acclist[i]
    multi += multilist[i]
    if multilist[i] == 0:
        multi0 += 1
    if multilist[i] / totallist[i] < 0.05:
        multi5 += 1
    if multilist[i] / totallist[i] < 0.1:
        multi10 += 1
    tmpacc = acclist[i]
    if tmpacc == 100:
        acc100 += 1
    if tmpacc >= 99:
        acc99 += 1
    if tmpacc >= 98:
        acc98 += 1
    if tmpacc >= 97:
        acc97 += 1
    if tmpacc >= 96:
        acc96 += 1
    if tmpacc >= 90:
        acc90 += 1

print("\n\nAverage total:", total / 253)
print("Average acc:", acc / 253)
print("Average multi:", multi / 253)

print("Average multi divided by total:", multi / total)

print("acc100:", acc100 / 253, "   ", acc100)
print("acc99:", acc99 / 253, "   ", acc99)
print("acc98:", acc98 / 253, "   ", acc98)
print("acc97:", acc97 / 253, "   ", acc97)
print("acc96:", acc96 / 253, "   ", acc96)
print("acc90:", acc90 / 253, "   ", acc90)

print("multi0:", multi0 / 253, "   ", multi0)
print("multi5:", multi5 / 253, "   ", multi5)
print("multi10:", multi10 / 253, "   ", multi10)


#Method 1
#method = 1
#df = traindf
#labellist = list(df['labels'])
#success = 0
#duallist = list()


#for i in range(len(labellist)):
#    if (i % 100) == 0:
#        print("1/8: ", i)
#    duallist.append(Classify(df, method, i))


#df = testdf
#labellist = list(df['labels'])
#success = 0

#for i in range(len(labellist)):
#    if (i % 100) == 0:
#        print("2/8: ", i)
#    duallist.append(Classify(df, method, i))

#totalcount = len(duallist)
#truecount = 0
#for item in duallist:
#    if item == True:
#        truecount += 1
#print(truecount)
#print(totalcount)
#print(truecount / totalcount)
