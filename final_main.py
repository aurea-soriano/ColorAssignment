import numpy as np
import scipy.io as sio
import statistics


def fo_sum(min_value, max_value):
    fo_sum = []

    for i in range(0, 500):
        fo_sum.append(0)

    matlab_data = sio.loadmat('/home/aurea/Documents/MEGA/MEGA/Documento-PosDoctorado/DadosForlan/4018_days/BHP_Productivity_Deviation.mat')
    matrix = matlab_data['BHP_Productivity_Deviation']

    for i in range(0, 500):
        vector = matrix[i, :]
        for j in range(0, len(vector)):
            if min_value <= vector[j] <= max_value:
                fo_sum[i] = fo_sum[i] + 1

    matlab_data = sio.loadmat('/home/aurea/Documents/MEGA/MEGA/Documento-PosDoctorado/DadosForlan/4018_days/BT_Deviation.mat')
    matrix = matlab_data['BT_Deviation']

    for i in range(0, 500):
        vector = matrix[i, :]
        for j in range(0, len(vector)):
            if min_value <= vector[j] <= max_value:
                fo_sum[i] = fo_sum[i] + 1

    matlab_data = sio.loadmat('/home/aurea/Documents/MEGA/MEGA/Documento-PosDoctorado/DadosForlan/4018_days/Liquid_Productivity_Deviation.mat')
    matrix = matlab_data['Liquid_Productivity_Deviation']

    for i in range(0, 500):
        vector = matrix[i, :]
        for j in range(0, len(vector)):
            if min_value <= vector[j] <= max_value:
                fo_sum[i] = fo_sum[i] + 1

    matlab_data = sio.loadmat('/home/aurea/Documents/MEGA/MEGA/Documento-PosDoctorado/DadosForlan/4018_days/NQDS_Data_BHP.mat')
    matrix = matlab_data['NQDS_Data_BHP']

    for i in range(0, 500):
        vector = matrix[i, :]
        for j in range(0, len(vector)):
            if min_value <= vector[j] <= max_value:
                fo_sum[i] = fo_sum[i] + 1

    matlab_data = sio.loadmat('/home/aurea/Documents/MEGA/MEGA/Documento-PosDoctorado/DadosForlan/4018_days/NQDS_Data_Gas.mat')
    matrix = matlab_data['NQDS_Data_Gas']

    for i in range(0, 500):
        vector = matrix[i, :]
        for j in range(0, len(vector)):
            if min_value <= vector[j] <= max_value:
                fo_sum[i] = fo_sum[i] + 1

    matlab_data = sio.loadmat('/home/aurea/Documents/MEGA/MEGA/Documento-PosDoctorado/DadosForlan/4018_days/NQDS_Data_Oil.mat')
    matrix = matlab_data['NQDS_Data_Oil']

    for i in range(0, 500):
        vector = matrix[i, :]
        for j in range(0, len(vector)):
            if min_value <= vector[j] <= max_value:
                fo_sum[i] = fo_sum[i] + 1

    matlab_data = sio.loadmat('/home/aurea/Documents/MEGA/MEGA/Documento-PosDoctorado/DadosForlan/4018_days/NQDS_Data_Water.mat')
    matrix = matlab_data['NQDS_Data_Water']

    for i in range(0, 500):
        vector = matrix[i, :]
        for j in range(0, len(vector)):
            if min_value <= vector[j] <= max_value:
                fo_sum[i] = fo_sum[i] + 1

    matlab_data = sio.loadmat('/home/aurea/Documents/MEGA/MEGA/Documento-PosDoctorado/DadosForlan/4018_days/NQDS_Data_Water_Injection.mat')
    matrix = matlab_data['NQDS_Data_Water_Injection']

    for i in range(0, 500):
        vector = matrix[i, :]
        for j in range(0, len(vector)):
            if min_value <= vector[j] <= max_value:
                fo_sum[i] = fo_sum[i] + 1

    matlab_data = sio.loadmat('/home/aurea/Documents/MEGA/MEGA/Documento-PosDoctorado/DadosForlan/4018_days/Water_Injection_Productivity_Deviation.mat')
    matrix = matlab_data['Water_Injection_Productivity_Deviation']

    for i in range(0, 500):
        vector = matrix[i, :]
        for j in range(0, len(vector)):
            if min_value <= vector[j] <= max_value:
                fo_sum[i] = fo_sum[i] + 1

    return fo_sum


def mean_values():
    model_values = []

    for i in range(0, 500):
        model_values.append([])

    matlab_data = sio.loadmat('/home/aurea/Documents/MEGA/MEGA/Documento-PosDoctorado/DadosForlan/4018_days/BHP_Productivity_Deviation.mat')
    matrix = matlab_data['BHP_Productivity_Deviation']

    for i in range(0, 500):
        vector = matrix[i, :]
        for j in range(0, len(vector)):
            model_values[i].append(abs(vector[j]))

    matlab_data = sio.loadmat('/home/aurea/Documents/MEGA/MEGA/Documento-PosDoctorado/DadosForlan/4018_days/BT_Deviation.mat')
    matrix = matlab_data['BT_Deviation']

    for i in range(0, 500):
        vector = matrix[i, :]
        for j in range(0, len(vector)):
            model_values[i].append(abs(vector[j]))

    matlab_data = sio.loadmat('/home/aurea/Documents/MEGA/MEGA/Documento-PosDoctorado/DadosForlan/4018_days/Liquid_Productivity_Deviation.mat')
    matrix = matlab_data['Liquid_Productivity_Deviation']

    for i in range(0, 500):
        vector = matrix[i, :]
        for j in range(0, len(vector)):
            model_values[i].append(abs(vector[j]))

    matlab_data = sio.loadmat('/home/aurea/Documents/MEGA/MEGA/Documento-PosDoctorado/DadosForlan/4018_days/NQDS_Data_BHP.mat')
    matrix = matlab_data['NQDS_Data_BHP']

    for i in range(0, 500):
        vector = matrix[i, :]
        for j in range(0, len(vector)):
            model_values[i].append(abs(vector[j]))

    matlab_data = sio.loadmat('/home/aurea/Documents/MEGA/MEGA/Documento-PosDoctorado/DadosForlan/4018_days/NQDS_Data_Gas.mat')
    matrix = matlab_data['NQDS_Data_Gas']

    for i in range(0, 500):
        vector = matrix[i, :]
        for j in range(0, len(vector)):
            model_values[i].append(abs(vector[j]))

    matlab_data = sio.loadmat('/home/aurea/Documents/MEGA/MEGA/Documento-PosDoctorado/DadosForlan/4018_days/NQDS_Data_Oil.mat')
    matrix = matlab_data['NQDS_Data_Oil']

    for i in range(0, 500):
        vector = matrix[i, :]
        for j in range(0, len(vector)):
            model_values[i].append(abs(vector[j]))

    matlab_data = sio.loadmat('/home/aurea/Documents/MEGA/MEGA/Documento-PosDoctorado/DadosForlan/4018_days/NQDS_Data_Water.mat')
    matrix = matlab_data['NQDS_Data_Water']

    for i in range(0, 500):
        vector = matrix[i, :]
        for j in range(0, len(vector)):
            model_values[i].append(abs(vector[j]))

    matlab_data = sio.loadmat('/home/aurea/Documents/MEGA/MEGA/Documento-PosDoctorado/DadosForlan/4018_days/NQDS_Data_Water_Injection.mat')
    matrix = matlab_data['NQDS_Data_Water_Injection']

    for i in range(0, 500):
        vector = matrix[i, :]
        for j in range(0, len(vector)):
            model_values[i].append(abs(vector[j]))

    matlab_data = sio.loadmat('/home/aurea/Documents/MEGA/MEGA/Documento-PosDoctorado/DadosForlan/4018_days/Water_Injection_Productivity_Deviation.mat')
    matrix = matlab_data['Water_Injection_Productivity_Deviation']

    for i in range(0, 500):
        vector = matrix[i, :]
        for j in range(0, len(vector)):
            model_values[i].append(abs(vector[j]))

    result_vector = []
    for i in range(0, 500):
        mean_value = statistics.mean(model_values[i])
        result_vector.append(round(mean_value, 2))

    return result_vector


def categorize_value(vector):

    ''' 1-excellent, 2-good, 3-regular, 4-bad, 5-really bad'''
    result_values = []
    for i in range(0, len(vector)):
        if -1 <= vector[i] <= 1:
            result_values.append(1)
        elif -3 <= vector[i] <= 3:
            result_values.append(2)
        elif -5 <= vector[i] <= 5:
            result_values.append(3)
        elif -10 <= vector[i] <= 10:
            result_values.append(4)
        else:
            result_values.append(5)
    return result_values


def main():
    mean_strategy = mean_values()
    print(mean_strategy)
    fo_sum_strategy = fo_sum(-5, +5)
    print(fo_sum_strategy)
    categorize_strategy = categorize_value(mean_strategy)
    print(categorize_strategy)


if __name__ == "__main__":
    main()