import pandas as pd

def Aggregate(df, index, featurenames, reverse):
    sum = 0
    for i in range(len(featurenames)):
        value = list(df[featurenames[i]])[index]
        if reverse[i] == 0:
            sum += value
        else:
            sum -= value
    return sum

#Returns 1 for first label winning, -1 for second label winning
def Test(l1, l2, df, index):

    if l1 == 0 and l2 == 1:
        v = list(df['2654'])[index]
        if v > -3.25 and v < 4:
            return -1
        if v <= -3.25 and v > -10:
            return 1

    elif l1 == 0 and l2 == 2:
        v = list(df['4366'])[index]
        if v >= -6.5 and v < 0:
            return -1
        if v < -6.5 and v > -10:
            v = list(df['5979'])[index]
            if v > -1.5 and v < 2:
                return -1
            if v < -1.5 and v > -10:
                return 1


    elif l1 == 0 and l2 == 3:
        v = list(df['4366'])[index]
        if v >= -5.5 and v < -0.5:
            return -1
        if v < -5.5 and v > -10:
            return 1

    elif l1 == 0 and l2 == 4:
        features = ['11658', '8543', '3066', '8177', '3076', '6598']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v >= -27 and v < 10:
            return -1
        if v < -27 and v > -53:
            return 1

    elif l1 == 0 and l2 == 5:
        v = list(df['2901'])[index]
        if v >= -2 and v < 2:
            return -1
        if v < -2 and v > -7.5:
            return 1

    elif l1 == 0 and l2 == 6:
        v = list(df['6075'])[index]
        if v >= -3 and v < 4:
            return -1
        if v < -3 and v > -10:
            return 1

    elif l1 == 0 and l2 == 7:
        v = list(df['11405'])[index]
        if v >= -4 and v < 2.5:
            return -1
        if v < -4 and v > -10:
            return 1

    elif l1 == 0 and l2 == 8:
        features = ['6075', '9186', '4929', '12127', '8061', '12181']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v >= -26 and v < 10:
            return -1
        if v < -26 and v > -53:
            return 1

    elif l1 == 0 and l2 == 9:
        v = list(df['11405'])[index]
        if v >= -4.25 and v < 2.5:
            return -1
        if v < -4.25 and v > -10:
            return 1

    elif l1 == 0 and l2 == 10:
        v = list(df['1314'])[index]
        if v >= -5.5 and v < 1:
            return -1
        if v < -5.5 and v > -10:
            return 1

    elif l1 == 0 and l2 == 11:
        v = list(df['4366'])[index]
        if v >= -6 and v < 5:
            return -1
        if v <= -5.5 and v > -10:
            return 1

    elif l1 == 0 and l2 == 12:
        features = ['10572', '6762', '6908', '668', '9186', '12385']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v >= -6 and v < 10:
            return -1
        if v <= -13 and v > -40:
            return 1
        if v < -6 and v > -13:
            features = ['6431', '2975', '10602', '5681', '3463', '5503']
            reverse = [0, 1, 1, 1, 1, 1]
            v = Aggregate(df, index, features, reverse)
            if v >= 6 and v < 34:
                return -1
            if v < 6 and v > -30:
                return 1

    elif l1 == 0 and l2 == 13:
        v = list(df['4366'])[index]
        if v >= -6.5 and v < 0.5:
            return -1
        if v < -6.5 and v > -10:
            v = list(df['11059'])[index]
            if v >= -4 and v < 4:
                return 1
            if v < -4 and v > -10:
                return -1

    elif l1 == 0 and l2 == 14:
        v = list(df['923'])[index]
        if v > -4 and v < 4:
            return -1
        if v <= -4 and v > -10:
            return 1

    elif l1 == 0 and l2 == 15:
        v = list(df['5703'])[index]
        if v > -2 and v < 4.5:
            return -1
        if v <= -2 and v > -10:
            return 1

    elif l1 == 0 and l2 == 16:
        v = list(df['2625'])[index]
        if v > -2.5 and v < 2.5:
            return -1
        if v <= -2.5 and v > -10:
            return 1

    elif l1 == 0 and l2 == 17:
        v = list(df['11019'])[index]
        if v > -2 and v < 2.5:
            return -1
        if v <= -2 and v > -10:
            return 1

    elif l1 == 0 and l2 == 18:
        v = list(df['4366'])[index]
        if v > -6.5 and v < 0:
            return -1
        if v <= -6.5 and v > -10:
            v = list(df['2981'])[index]
            if v > 0.5 and v < 2.5:
                return -1
            if v <= 0.5 and v > -5:
                return 1

    elif l1 == 1 and l2 == 2:
        v = list(df['9935'])[index]
        if v > -2 and v < 2.5:
            return 1
        if v <= -2 and v > -8.5:
            return -1

    elif l1 == 1 and l2 == 3:
        v = list(df['13300'])[index]
        if v > -3 and v < 2.5:
            return -1
        if v <= -3 and v > -10:
            return 1

    elif l1 == 1 and l2 == 4:
        v = list(df['12868'])[index]
        if v > 0.5 and v < 8.5:
            return 1
        if v <= 0.5 and v > -10:
            return -1

    elif l1 == 1 and l2 == 5:
        v = list(df['1742'])[index]
        if v > -3.5 and v < 2:
            return 1
        if v <= -3.5 and v > -8:
            return -1

    elif l1 == 1 and l2 == 6:
        v = list(df['9131'])[index]
        if v > -3 and v < 2:
            return 1
        if v <= -3 and v > -10:
            return -1

    elif l1 == 1 and l2 == 7:
        v = list(df['5522'])[index]
        if v > -2.5 and v < 2.5:
            return -1
        if v <= -2.5 and v > -10:
            return 1

    elif l1 == 1 and l2 == 8:
        features = ['4401', '12868', '11003', '13621', '8893', '1742']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > -11 and v < 20:
            return 1
        if v <= -11 and v > -51:
            return -1

    elif l1 == 1 and l2 == 9:
        v = list(df['2797'])[index]
        if v > -2 and v < 3:
            return -1
        if v <= -2 and v > -8.5:
            return 1

    elif l1 == 1 and l2 == 10:
        v = list(df['4366'])[index]
        if v > -6 and v < -1.5:
            return -1
        if v <= -6 and v > -10:
            return 1

    elif l1 == 1 and l2 == 11:
        v = list(df['8956'])[index]
        if v > 0.5 and v < 6:
            return -1
        if v <= 0.5 and v > -6:
            return 1

    elif l1 == 1 and l2 == 12:
        features = ['12868', '2638', '2654', '6566', '4401', '8173']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > -7 and v < 30:
            return 1
        if v <= -7 and v > -51:
            return -1

    elif l1 == 1 and l2 == 13:
        features = ['12868', '9804', '1543', '4223', '9131', '5522']
        reverse = [0, 1, 0, 1, 0, 1]
        v = Aggregate(df, index, features, reverse)
        if v > 15 and v < 40:
            return 1
        if v <= 15 and v > -30:
            return -1

    elif l1 == 1 and l2 == 14:
        v = list(df['12868'])[index]
        if v > 0 and v < 8.5:
            return 1
        if v <= 0 and v > -10.5:
            return -1

    elif l1 == 1 and l2 == 15:
        v = list(df['12868'])[index]
        if v > 0 and v < 8.5:
            return 1
        if v <= 0 and v > -10.5:
            return -1

    elif l1 == 1 and l2 == 16:
        v = list(df['11450'])[index]
        if v > -4 and v < 1.25:
            return 1
        if v <= -4 and v > -10.5:
            return -1

    elif l1 == 1 and l2 == 17:
        v = list(df['2090'])[index]
        if v > -2 and v < 2.5:
            return -1
        if v <= -2 and v > -10.5:
            return 1

    elif l1 == 1 and l2 == 18:
        features = ['9935', '1543', '5384', '1780', '12868', '10439']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > -10 and v < 20:
            return 1
        if v <= -10 and v > -51:
            return -1

    elif l1 == 2 and l2 == 3:
        v = list(df['3578'])[index]
        if v > -0.25 and v < 6:
            return -1
        if v <= -0.25 and v > -10.5:
            return 1

    elif l1 == 2 and l2 == 4:
        features = ['268', '2215', '12071', '9272', '13328', '7758']
        reverse = [0, 0, 0, 0, 1, 1]
        v = Aggregate(df, index, features, reverse)
        if v > -5 and v < 25:
            return -1
        if v <= -5 and v > -31:
            return 1

    elif l1 == 2 and l2 == 5:
        v = list(df['6931'])[index]
        if v > -4 and v < 0.25:
            return 1
        if v <= -4 and v > -10.5:
            return -1

    elif l1 == 2 and l2 == 6:
        features = ['3800', '540', '11582', '9254', '8973', '2745']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > -16 and v < 21:
            return -1
        if v <= -16 and v > -48:
            return 1

    elif l1 == 2 and l2 == 7:
        features = ['11864', '13255', '8091', '2600', '2215', '10002']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > -20 and v < 23:
            return -1
        if v <= -20 and v > -56:
            return 1

    elif l1 == 2 and l2 == 8:
        features = ['3387', '11347', '4366', '6735', '2604', '7134']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > -16 and v < 6:
            return 1
        if v <= -16 and v > -56:
            v = list(df['6629'])[index]
            if v > -0.75 and v < 2.5:
                return 1
            if v <= -0.75 and v > -7:
                return -1

    elif l1 == 2 and l2 == 9:
        features = ['12160', '5547', '1226', '3161', '7213', '4848']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > -12 and v < 10:
            return -1
        if v <= -12 and v > -43:
            return 1

    elif l1 == 2 and l2 == 10:
        v = list(df['3578'])[index]
        if v > -0.25 and v < 5.5:
            return -1
        if v <= -0.25 and v > -10.5:
            return 1

    elif l1 == 2 and l2 == 11:
        features = ['11311', '4322', '200', '4505', '9384', '9547']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > -9 and v < 20:
            return -1
        if v <= -9 and v > -43:
            return 1

    elif l1 == 2 and l2 == 12:
        features = ['1656', '4366', '2090', '8720', '2929', '4239']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > -21 and v < 0:
            return 1
        if v <= -21 and v > -55:
            v = list(df['12936'])[index]
            if v > 1.5 and v < 4.5:
                return 1
            if v <= 1.5 and v > -10.5:
                return -1


    elif l1 == 2 and l2 == 13:
        features = ['7930', '1157', '3489', '6061', '13559', '9567']
        reverse = [0, 0, 0, 0, 1, 0]
        v = Aggregate(df, index, features, reverse)
        if v < -23 and v > -50:
            return -1
        if v >= -10 and v < 17:
            return 1
        features = ['9754', '5778', '212', '4848', '3363', '9530']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > -20 and v < 7:
            return -1
        if v < -20 and v > -53:
            return 1


    elif l1 == 2 and l2 == 14:
        features = ['846', '3578', '13328', '7113', '2597', '10002']
        reverse = [0, 0, 1, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v < -10 and v > -42:
            return 1
        if v >= -10 and v < 22:
            return -1

    elif l1 == 2 and l2 == 15:
        v = list(df['5703'])[index]
        if v > 0 and v < 4.5:
            return -1
        if v <= 0 and v > -10.5:
            return 1

    elif l1 == 2 and l2 == 16:
        features = ['3873', '10631', '11177', '5271', '1646', '12257']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v < -4.5 and v > -30:
            return 1
        if v >= -4.5 and v < 16:
            return -1

    elif l1 == 2 and l2 == 17:
        v = list(df['9802'])[index]
        if v > -0.5 and v < 6:
            return -1
        if v < -0.5 and v > -11:
            return 1

    elif l1 == 2 and l2 == 18:
        features = ['8484', '13634', '9567', '2600', '12160', '12294']
        reverse = [0, 0, 0, 1, 1, 0]
        v = Aggregate(df, index, features, reverse)
        if v < -6 and v > -40:
            return -1
        if v >= -6 and v < 25:
            return 1

    elif l1 == 3 and l2 == 4:
        features = ['6438', '12489', '12766', '4011', '8721', '8943']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v < -15 and v > -55:
            return -1
        if v >= -15 and v < 20:
            return 1

    elif l1 == 3 and l2 == 5:
        v = list(df['1946'])[index]
        if v > -2 and v < 4.5:
            return 1
        if v <= -2 and v > -10.5:
            return -1

    elif l1 == 3 and l2 == 6:
        v = list(df['8973'])[index]
        if v > 0 and v < 7.5:
            return -1
        if v < 0 and v > -10:
            return 1

    elif l1 == 3 and l2 == 7:
        v = list(df['5159'])[index]
        if v < -1 and v > -8.5:
            return 1
        if v >= -1 and v < 5:
            features = ['7161', '8408', '11864', '6794', '13255', '8091']
            reverse = [0, 0, 1, 0, 1, 1]
            v = Aggregate(df, index, features, reverse)
            if v < 1 and v > -45:
                return -1
            if v >= 1 and v < 30:
                return 1

    elif l1 == 3 and l2 == 8:
        v = list(df['11958'])[index]
        if v > -1 and v < 4:
            return 1
        if v <= -1 and v > -10.5:
            return -1

    elif l1 == 3 and l2 == 9:
        v = list(df['8721'])[index]
        if v > -0.5 and v < 6:
            return 1
        if v <= -0.5 and v > -10.5:
            return -1

    elif l1 == 3 and l2 == 10:
        features = ['5232', '2752', '5486', '6296', '179', '5159']
        reverse = [0, 0, 0, 1, 1, 0]
        v = Aggregate(df, index, features, reverse)
        if v < -6 and v > -31:
            return 1
        if v >= -6 and v < 15:
            return -1

    elif l1 == 3 and l2 == 11:
        v = list(df['8956'])[index]
        if v > 1 and v < 6.5:
            return -1
        if v < 1 and v > -10.5:
            return 1

    elif l1 == 3 and l2 == 12:
        v = list(df['2090'])[index]
        if v > -1 and v < 3.5:
            return 1
        if v < -1 and v > -10.5:
            return -1

    elif l1 == 3 and l2 == 13:
        v = list(df['3578'])[index]
        if v < -1 and v > -10.5:
            return -1
        if v > -1 and v < 6.5:
            features = ['274', '5486', '4359', '5201', '8078', '13477']
            reverse = [0, 0, 0, 0, 0, 0]
            v = Aggregate(df, index, features, reverse)
            if v < -24 and v > -51:
                return 1
            if v >= -24 and v < -5:
                return -1

    elif l1 == 3 and l2 == 14:
        v = list(df['7267'])[index]
        if v < -8 and v > -10:
            return 1
        if v >= -8 and v < 2.5:
            features = ['7267', '4419', '12704', '13336', '13519', '3745']
            reverse = [0, 0, 0, 1, 1, 1]
            v = Aggregate(df, index, features, reverse)
            if v > -1 and v < 11:
                return -1
            if v <= -6 and v > -20:
                return 1
            features = ['1106', '13470', '12489', '9592', '10376', '9908']
            reverse = [0, 0, 0, 0, 0, 1]
            v = Aggregate(df, index, features, reverse)
            if v > -15 and v < 5:
                return 1
            if v <= -15 and v > -36:
                return -1

    elif l1 == 3 and l2 == 15:
        v = list(df['9929'])[index]
        if v > -1.5 and v < 3:
            return -1
        if v <= -1.5 and v > -8.5:
            return 1

    elif l1 == 3 and l2 == 16:
        v = list(df['3578'])[index]
        if v > -1 and v < 6:
            return 1
        if v <= -1 and v > -6.5:
            return -1

    elif l1 == 3 and l2 == 17:
        v = list(df['3578'])[index]
        if v > -1 and v < 6:
            return 1
        if v < -1 and v > -10.5:
            return -1

    elif l1 == 3 and l2 == 18:
        v = list(df['3578'])[index]
        if v > 0 and v < 6:
            return 1
        if v <= 0 and v > -11:
            return -1

    elif l1 == 4 and l2 == 5:
        features = ['8543', '9792', '5891', '3066', '8177', '12071']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > -21 and v < 11:
            return 1
        if v <= -21 and v > -62:
            return -1

    elif l1 == 4 and l2 == 6:
        features = ['12071', '5547', '1864', '8973', '801', '4847']
        reverse = [0, 0, 1, 1, 1, 1]
        v = Aggregate(df, index, features, reverse)
        if v > -5 and v < 40:
            return 1
        if v <= -5 and v > -42:
            return -1

    elif l1 == 4 and l2 == 7:
        features = ['5999', '6438', '2821', '13397', '13237', '12071']
        reverse = [0, 0, 0, 0, 0, 1]
        v = Aggregate(df, index, features, reverse)
        if v > -18 and v < 30:
            return -1
        if v <= -18 and v > -52:
            return 1

    elif l1 == 4 and l2 == 8:
        features = ['2874', '11658', '8543', '960', '6598', '2604']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > -16 and v < 12:
            return 1
        if v <= -16 and v > -60:
            return -1

    elif l1 == 4 and l2 == 9:
        features = ['1564', '3881', '6712', '8444', '3093', '5759']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > -10.5 and v < 20:
            return -1
        if v <= -10.5 and v > -60:
            return 1

    elif l1 == 4 and l2 == 10:
        features = ['6438', '13076', '13237', '5999', '2821', '12071']
        reverse = [0, 0, 0, 0, 0, 1]
        v = Aggregate(df, index, features, reverse)
        if v > -20 and v < 21:
            return -1
        if v <= -20 and v > -52:
            return 1

    elif l1 == 4 and l2 == 11:
        v = list(df['8956'])[index]
        if v > 0.5 and v < 6.5:
            return -1
        if v <= 0.5 and v > -8.5:
            return 1

    elif l1 == 4 and l2 == 12:
        features = ['268', '11658', '4979', '8177', '2797', '8543']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > -20 and v < 10:
            return 1
        if v <= -20 and v > -52:
            return -1

    elif l1 == 4 and l2 == 13:
        v = list(df['13076'])[index]
        if v > -3 and v < 4:
            return -1
        v = list(df['12071'])[index]
        if v < -5 and v > -10.5:
            return -1
        if v >= -5 and v < 4:
            return 1

    elif l1 == 4 and l2 == 14:
        features = ['12071', '5547', '13076', '13237', '6438', '8721']
        reverse = [0, 0, 1, 1, 1, 1]
        v = Aggregate(df, index, features, reverse)
        if v > 12 and v < 41:
            return 1
        if v <= 12 and v > -31:
            return -1

    elif l1 == 4 and l2 == 15:
        v = list(df['6502'])[index]
        if v > -2.75 and v < 1.2:
            return -1
        if v <= -2.75 and v > -8.2:
            return 1

    elif l1 == 4 and l2 == 16:
        v = list(df['977'])[index]
        if v > 1 and v < 7:
            return -1
        if v <= 1 and v > -10.5:
            return 1

    elif l1 == 4 and l2 == 17:
        features = ['9802', '12925', '6367', '10391', '9856', '12071']
        reverse = [0, 0, 0, 0, 0, 1]
        v = Aggregate(df, index, features, reverse)
        if v > -5 and v < 27:
            return -1
        if v <= -5 and v > -51:
            return 1

    elif l1 == 4 and l2 == 18:
        features = ['7758', '10683', '3363', '6712', '12160', '13199']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > -25 and v < 10:
            return -1
        if v <= -25 and v > -56:
            return 1

    elif l1 == 5 and l2 == 6:
        v = list(df['618'])[index]
        if v > -2.5 and v < 3:
            return -1
        if v <= -2.5 and v > -10.5:
            return 1

    elif l1 == 5 and l2 == 7:
        v = list(df['2642'])[index]
        if v > -1.5 and v < 4.2:
            return -1
        if v <= -1.5 and v > -10.5:
            return 1

    elif l1 == 5 and l2 == 8:
        features = ['93', '7460', '5651', '12801', '2661', '12127']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > -18 and v < 11:
            return -1
        if v <= -18 and v > -44:
            return 1

    elif l1 == 5 and l2 == 9:
        v = list(df['1564'])[index]
        if v > -3 and v < 5:
            return -1
        if v <= -3 and v > -10.5:
            return 1

    elif l1 == 5 and l2 == 10:
        v = list(df['3578'])[index]
        if v > -0.5 and v < 5:
            return -1
        if v <= -0.5 and v > -8:
            return 1

    elif l1 == 5 and l2 == 11:
        v = list(df['13199'])[index]
        if v > -1 and v < 4.5:
            return -1
        if v <= -1 and v > -10.5:
            return 1

    elif l1 == 5 and l2 == 12:
        v = list(df['1980'])[index]
        if v > -3.4 and v < 0.5:
            return -1
        if v <= -3.4 and v > -10.5:
            return 1

    elif l1 == 5 and l2 == 13:
        features = ['4734', '3983', '187', '5487', '4151', '1991']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > -24 and v < 4:
            return -1
        if v <= -24 and v > -61:
            return 1

    elif l1 == 5 and l2 == 14:
        v = list(df['12127'])[index]
        if v > -2.6 and v < 2.75:
            return -1
        if v <= -2.6 and v > -9:
            return 1

    elif l1 == 5 and l2 == 15:
        v = list(df['11117'])[index]
        if v > -3 and v < 2:
            return -1
        if v <= -3 and v > -10:
            return 1

    elif l1 == 5 and l2 == 16:
        v = list(df['9277'])[index]
        if v > -1 and v < 8:
            return -1
        if v <= -1 and v > -10.5:
            return 1

    elif l1 == 5 and l2 == 17:
        v = list(df['11019'])[index]
        if v > -1.5 and v < 2.1:
            return -1
        if v <= -1.5 and v > -10.5:
            return 1

    elif l1 == 5 and l2 == 18:
        v = list(df['1004'])[index]
        if v > -2.5 and v < 1:
            return 1
        if v <= -2.5 and v > -9:
            return -1

    elif l1 == 6 and l2 == 7:
        features = ['1864', '8973', '540', '2821', '13255', '13539']
        reverse = [0, 0, 0, 1, 1, 0]
        v = Aggregate(df, index, features, reverse)
        if v > 1 and v < 35:
            return 1
        if v <= 1 and v > -32:
            return -1

    elif l1 == 6 and l2 == 8:
        v = list(df['5742'])[index]
        if v > -4.5 and v < 0.5:
            return 1
        if v <= -4.5 and v > -10.5:
            return -1

    elif l1 == 6 and l2 == 9:
        v = list(df['12160'])[index]
        if v > 0 and v < 4.5:
            return -1
        if v <= 0 and v > -6.5:
            return 1

    elif l1 == 6 and l2 == 10:
        features = ['3363', '6597', '10741', '2245', '2821', '5495']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > -25 and v < 5:
            return -1
        if v <= -25 and v > -60:
            return 1

    elif l1 == 6 and l2 == 11:
        v = list(df['4322'])[index]
        if v > -2.4 and v < 6.5:
            return -1
        if v <= -2.4 and v > -10.5:
            return 1

    elif l1 == 6 and l2 == 12:
        v = list(df['6075'])[index]
        if v > -1.5 and v < 4.5:
            return 1
        if v <= -1.5 and v > -10.5:
            return -1

    elif l1 == 6 and l2 == 13:
        features = ['3800', '11582', '8973', '540', '2745', '4584']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > -10 and v < 30:
            return 1
        if v <= -10 and v > -47:
            return -1

    elif l1 == 6 and l2 == 14:
        features = ['4102', '6366', '13539', '8973', '540', '2745']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > -11 and v < 24:
            return 1
        if v <= -11 and v > -50:
            return -1

    elif l1 == 6 and l2 == 15:
        v = list(df['4218'])[index]
        if v > 0.5 and v < 6:
            return 1
        if v <= 0.5 and v > -10.5:
            return -1

    elif l1 == 6 and l2 == 16:
        v = list(df['6597'])[index]
        if v > -2.75 and v < 2.75:
            return -1
        if v <= -2.75 and v > -10.5:
            return 1

    elif l1 == 6 and l2 == 17:
        v = list(df['9802'])[index]
        if v > 0 and v < 6:
            return -1
        if v <= 0 and v > -10.5:
            return 1

    elif l1 == 6 and l2 == 18:
        v = list(df['8973'])[index]
        if v > 0 and v < 7:
            return 1
        if v <= 0 and v > -10.5:
            return -1

    elif l1 == 7 and l2 == 8:
        v = list(df['2604'])[index]
        if v > -1 and v < 3.2:
            return 1
        if v <= -1 and v > -8:
            return -1

    elif l1 == 7 and l2 == 9:
        features = ['12160', '5547', '3161', '28', '13028', '443']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > -15 and v < 11:
            return -1
        if v <= -15 and v > -50:
            return 1

    elif l1 == 7 and l2 == 10:
        features = ['7758', '8091', '1497', '13255', '11864', '10602']
        reverse = [0, 1, 0, 1, 1, 0]
        v = Aggregate(df, index, features, reverse)
        if v > 2 and v < 30:
            return -1
        if v <= 2 and v > -48:
            return 1

    elif l1 == 7 and l2 == 11:
        v = list(df['8956'])[index]
        if v > 1.5 and v < 6.2:
            return -1
        if v <= 1.5 and v > -5.5:
            return 1

    elif l1 == 7 and l2 == 12:
        v = list(df['2090'])[index]
        if v > -1.2 and v < 3:
            return 1
        if v <= -1.2 and v > -10.5:
            return -1

    elif l1 == 7 and l2 == 13:
        v = list(df['977'])[index]
        if v > 4 and v < 8.5:
            return -1
        features = ['13255', '8091', '11864', '240', '13397', '13088']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v < -20 and v > -52:
            return -1
        features = ['11532', '977', '8078', '5718', '1200', '5076']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > -5 and v < 11:
            return -1
        if v <= -5 and v > -48:
            return 1

    elif l1 == 7 and l2 == 14:
        features = ['4440', '13255', '8091', '13397', '1732', '7721']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > -10 and v < 30:
            return 1
        if v <= -10 and v > -46:
            return -1

    elif l1 == 7 and l2 == 15:
        v = list(df['408'])[index]
        if v > -4 and v < 1.2:
            return 1
        if v <= -4 and v > -7.2:
            return -1

    elif l1 == 7 and l2 == 16:
        features = ['11760', '966', '2797', '12122', '13082', '9408']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > -17.5 and v < 5:
            return 1
        if v <= -17.5 and v > -42:
            return -1

    elif l1 == 7 and l2 == 17:
        v = list(df['268'])[index]
        if v > -1.8 and v < 4.2:
            return -1
        if v <= -1.8 and v > -10:
            return 1

    elif l1 == 7 and l2 == 18:
        features = ['268', '2118', '5547', '12160', '8091', '5443']
        reverse = [0, 1, 0, 0, 1, 1]
        v = Aggregate(df, index, features, reverse)
        if v > 1 and v < 33:
            return -1
        if v <= 1 and v > -30:
            return 1

    elif l1 == 8 and l2 == 9:
        v = list(df['4482'])[index]
        if v > -1.7 and v < 4.2:
            return -1
        if v <= -1.7 and v > -10.5:
            return 1

    elif l1 == 8 and l2 == 10:
        v = list(df['923'])[index]
        if v > -2.2 and v < 3:
            return -1
        if v <= -2.2 and v > -10.5:
            return 1

    elif l1 == 8 and l2 == 11:
        v = list(df['13199'])[index]
        if v > -1 and v < 4.5:
            return -1
        if v <= -1 and v > -10.5:
            return 1

    elif l1 == 8 and l2 == 12:
        features = ['6118', '12127', '2137', '5651', '9822', '3254']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > -11.5 and v < 21:
            return 1
        if v <= -11.5 and v > -42:
            return -1

    elif l1 == 8 and l2 == 13:
        v = list(df['2604'])[index]
        if v > -1.3 and v < 4:
            return -1
        if v <= -1.3 and v > -8.5:
            return 1

    elif l1 == 8 and l2 == 14:
        v = list(df['923'])[index]
        if v > -3 and v < 4.5:
            return -1
        if v <= -3 and v > -10.5:
            return 1

    elif l1 == 8 and l2 == 15:
        v = list(df['5703'])[index]
        if v > -1 and v < 4.5:
            return -1
        if v <= -1 and v > -10.5:
            return 1

    elif l1 == 8 and l2 == 16:
        v = list(df['2625'])[index]
        if v > -1.6 and v < 2.2:
            return -1
        if v <= -1.6 and v > -10.5:
            return 1

    elif l1 == 8 and l2 == 17:
        v = list(df['11019'])[index]
        if v > -1 and v < 2.2:
            return -1
        if v <= -1 and v > -10.5:
            return 1

    elif l1 == 8 and l2 == 18:
        features = ['11928', '12160', '8510', '4366', '12662', '11958']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > -25 and v < 12:
            return -1
        if v <= -25 and v > -55:
            return 1

    elif l1 == 9 and l2 == 10:
        v = list(df['8721'])[index]
        if v > -0.5 and v < 5.5:
            return -1
        if v <= -0.5 and v > -10.5:
            return 1

    elif l1 == 9 and l2 == 11:
        v = list(df['9547'])[index]
        if v > -4.5 and v < 2:
            return -1
        if v <= -4.5 and v > -10.5:
            return 1

    elif l1 == 9 and l2 == 12:
        v = list(df['6136'])[index]
        if v > 1 and v < 6.2:
            return 1
        if v <= 1 and v > -10.5:
            return -1

    elif l1 == 9 and l2 == 13:
        v = list(df['12160'])[index]
        if v < 0 and v > -8.5:
            return -1
        features = ['5335', '9592', '7494', '5093', '11932', '1226']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > -17.5 and v < 6:
            return 1
        if v <= -17.5 and v > -32:
            return -1

    elif l1 == 9 and l2 == 14:
        features = ['12160', '5547', '1226', '5335', '443', '8721']
        reverse = [0, 0, 0, 0, 0, 1]
        v = Aggregate(df, index, features, reverse)
        if v > -2 and v < 21:
            return 1
        if v <= -2 and v > -40:
            return -1

    elif l1 == 9 and l2 == 15:
        v = list(df['9547'])[index]
        if v > -4 and v < 2.5:
            return -1
        if v <= -4 and v > -10.5:
            return 1

    elif l1 == 9 and l2 == 16:
        v = list(df['9277'])[index]
        if v > 0 and v < 8:
            return -1
        if v <= 0 and v > -10.5:
            return 1

    elif l1 == 9 and l2 == 17:
        v = list(df['5183'])[index]
        if v > -4 and v < 0.5:
            return -1
        if v <= -4 and v > -10.5:
            return 1

    elif l1 == 9 and l2 == 18:
        features = ['1112', '7749', '8408', '9534', '13028', '11271']
        reverse = [0, 0, 1, 0, 0, 1]
        v = Aggregate(df, index, features, reverse)
        if v < -3 and v > -25:
            return -1
        features = ['4419', '12704', '7267', '6775', '5780', '7729']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v < -12 and v > -33:
            return -1
        if v >= -12 and v < 11:
            return 1

    elif l1 == 10 and l2 == 11:
        v = list(df['8956'])[index]
        if v > 0.5 and v < 6.5:
            return -1
        if v <= 0.5 and v > -5.5:
            return 1

    elif l1 == 10 and l2 == 12:
        v = list(df['3405'])[index]
        if v > -2.75 and v < 2:
            return 1
        if v <= -2.75 and v > -10.5:
            return -1

    elif l1 == 10 and l2 == 13:
        features = ['13556', '9162', '8490', '7964', '3578', '2752']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v < -15 and v > -51:
            return -1
        if v >= -15 and v < 3:
            v = list(df['11681'])[index]
            if v > -2.5 and v < 0:
                return -1
            if v <= -2.5 and v > -6:
                return 1
            if v < -6 and v > -7.5:
                return -1

    elif l1 == 10 and l2 == 14:
        features = ['3853', '7708', '4419', '7267', '12704', '3847']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v < -16.5 and v > -42:
            return 1
        if v >= -16.5 and v < 7:
            return -1

    elif l1 == 10 and l2 == 15:
        v = list(df['9929'])[index]
        if v > -1.2 and v < 3.5:
            return -1
        if v <= -1.2 and v > -6.5:
            return 1

    elif l1 == 10 and l2 == 16:
        v = list(df['3597'])[index]
        if v > -1.75 and v < 3:
            return 1
        if v <= -1.75 and v > -7:
            return -1

    elif l1 == 10 and l2 == 17:
        v = list(df['3405'])[index]
        if v > -3 and v < 2:
            return 1
        if v <= -3 and v > -10.5:
            return -1

    elif l1 == 10 and l2 == 18:
        features = ['8723', '3578', '2118', '7179', '1358', '3234']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v < -19 and v > -52:
            return -1
        if v >= -19 and v < 3:
            return 1

    elif l1 == 11 and l2 == 12:
        v = list(df['13199'])[index]
        if v > -1 and v < 4:
            return 1
        if v <= -1 and v > -10.5:
            return -1

    elif l1 == 11 and l2 == 13:
        v = list(df['200'])[index]
        if v > -0.3 and v < 5:
            return 1
        if v <= -0.3 and v > -7:
            return -1

    elif l1 == 11 and l2 == 14:
        v = list(df['8956'])[index]
        if v > 1 and v < 6:
            return 1
        if v <= 1 and v > -7.5:
            return -1

    elif l1 == 11 and l2 == 15:
        v = list(df['13199'])[index]
        if v > -1 and v < 4:
            return 1
        if v <= -1 and v > -10.5:
            return -1

    elif l1 == 11 and l2 == 16:
        v = list(df['200'])[index]
        if v > -1 and v < 5:
            return 1
        if v <= -1 and v > -6.5:
            return -1

    elif l1 == 11 and l2 == 17:
        v = list(df['8956'])[index]
        if v > 1 and v < 6.5:
            return 1
        if v <= 1 and v > -6.5:
            return -1

    elif l1 == 11 and l2 == 18:
        v = list(df['9547'])[index]
        if v > -4 and v < 2:
            return 1
        if v <= -4 and v > -10.5:
            return -1

    elif l1 == 12 and l2 == 13:
        features = ['9804', '4812', '2090', '4223', '1394', '3353']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v < -15 and v > -58:
            return 1
        if v >= -15 and v < 11:
            return -1

    elif l1 == 12 and l2 == 14:
        v = list(df['8721'])[index]
        if v > -2 and v < 6.5:
            return -1
        if v <= -2 and v > -10.5:
            return 1

    elif l1 == 12 and l2 == 15:
        v = list(df['5703'])[index]
        if v > -0.5 and v < 4.5:
            return -1
        if v <= -0.5 and v > -10.5:
            return 1

    elif l1 == 12 and l2 == 16:
        features = ['5497', '2625', '12171', '1600', '8962', '1656']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v < -12 and v > -42:
            return 1
        if v >= -12 and v < 13:
            return -1

    elif l1 == 12 and l2 == 17:
        v = list(df['2090'])[index]
        if v > -1.3 and v < 2.5:
            return -1
        if v <= -1.3 and v > -10.5:
            return 1

    elif l1 == 12 and l2 == 18:
        features = ['11928', '443', '8720', '2090', '6712', '4366']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v < -26 and v > -62:
            return 1
        if v >= -26 and v < 12:
            return -1

    elif l1 == 13 and l2 == 14:
        v = list(df['2597'])[index]
        if v < -4 and v > -10.5:
            return 1
        v = list(df['5791'])[index]
        if v > -2 and v < 0.5:
            return 1
        features = ['4317', '4366', '4224', '9578', '3692', '6712']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v > -1 and v < 11:
            return 1
        if v <= -1 and v > -50:
            return -1

    elif l1 == 13 and l2 == 15:
        v = list(df['5703'])[index]
        if v > 0 and v < 4:
            return -1
        if v <= 0 and v > -10:
            return 1

    elif l1 == 13 and l2 == 16:
        v = list(df['8962'])[index]
        if v > 1 and v < 8:
            return -1
        if v <= 1 and v > -10.5:
            return 1

    elif l1 == 13 and l2 == 17:
        features = ['268', '10045', '178', '10160', '13076', '5651']
        reverse = [0, 1, 0, 0, 1, 1]
        v = Aggregate(df, index, features, reverse)
        if v > 8 and v < 30:
            return -1
        if v <= 8 and v > -25:
            return 1

    elif l1 == 13 and l2 == 18:
        features = ['12160', '11532', '13196', '1862', '6288', '443']
        reverse = [0, 1, 0, 0, 1, 1]
        v = Aggregate(df, index, features, reverse)
        if v < -5 and v > -30:
            return 1
        features = ['5547', '12160', '268', '8489', '2266', '2139']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v < -15 and v > -45:
            return 1
        if v > -15 and v < 12:
            return -1

    elif l1 == 14 and l2 == 15:
        v = list(df['5703'])[index]
        if v > 0 and v < 4.5:
            return -1
        if v <= 0 and v > -9:
            return 1

    elif l1 == 14 and l2 == 16:
        v = list(df['7756'])[index]
        if v > 1 and v < 3.5:
            return -1
        if v <= 1 and v > -2.5:
            return 1

    elif l1 == 14 and l2 == 17:
        v = list(df['268'])[index]
        if v > -1.6 and v < 4:
            return -1
        if v <= -1.6 and v > -8:
            return 1

    elif l1 == 14 and l2 == 18:
        features = ['268', '5547', '1500', '9274', '8661', '9884']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v < -14.5 and v > -36:
            return 1
        if v > -14.5 and v < 10:
            return -1

    elif l1 == 15 and l2 == 16:
        v = list(df['5703'])[index]
        if v > -1 and v < 4.5:
            return 1
        if v <= -1 and v > -6.5:
            return -1

    elif l1 == 15 and l2 == 17:
        v = list(df['1058'])[index]
        if v > -2.5 and v < 1.5:
            return 1
        if v <= -2.5 and v > -7.5:
            return -1

    elif l1 == 15 and l2 == 18:
        v = list(df['9547'])[index]
        if v > -4 and v < 2:
            return 1
        if v <= -4 and v > -10.5:
            return -1

    elif l1 == 16 and l2 == 17:
        v = list(df['268'])[index]
        if v > -2 and v < 4:
            return -1
        if v <= -2 and v > -10.5:
            return 1

    elif l1 == 16 and l2 == 18:
        features = ['5497', '8289', '584', '4085', '8285', '5843']
        reverse = [0, 0, 0, 0, 0, 0]
        v = Aggregate(df, index, features, reverse)
        if v < -13 and v > -36:
            return -1
        if v > -13 and v < 2:
            return 1

    elif l1 == 17 and l2 == 18:
        features = ['9802', '4197', '5183', '13199', '2266', '7414']
        reverse = [0, 0, 0, 1, 1, 1]
        v = Aggregate(df, index, features, reverse)
        if v < 10 and v > -32:
            return -1
        if v > 10 and v < 35:
            return 1
    else:
        print("Error, invalid Test parameters")
        print(l1, " ", l2)

    return 0
