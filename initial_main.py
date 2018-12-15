import numpy as np
import scipy.io as sio
import statistics


def fo_sum(min_value, max_value):
    fo_sum = []

    for i in range(0, 500):
        fo_sum.append(0)

    matlab_data = sio.loadmat('/home/aurea/Documents/MEGA/MEGA/Documento-PosDoctorado/DadosForlan/Initial_Diagnosis/NQDS_Data_BHP.mat')
    matrix = matlab_data['NQDS_Data_BHP']

    for i in range(0, 500):
        vector = matrix[i, :]
        for j in range(0, len(vector)):
            if min_value <= vector[j] <= max_value:
                fo_sum[i] = fo_sum[i] + 1

    matlab_data = sio.loadmat('/home/aurea/Documents/MEGA/MEGA/Documento-PosDoctorado/DadosForlan/Initial_Diagnosis/NQDS_Data_Gas.mat')
    matrix = matlab_data['NQDS_Data_Gas']

    for i in range(0, 500):
        vector = matrix[i, :]
        for j in range(0, len(vector)):
            if min_value <= vector[j] <= max_value:
                fo_sum[i] = fo_sum[i] + 1

    matlab_data = sio.loadmat('/home/aurea/Documents/MEGA/MEGA/Documento-PosDoctorado/DadosForlan/Initial_Diagnosis/NQDS_Data_Oil.mat')
    matrix = matlab_data['NQDS_Data_Oil']

    for i in range(0, 500):
        vector = matrix[i, :]
        for j in range(0, len(vector)):
            if min_value <= vector[j] <= max_value:
                fo_sum[i] = fo_sum[i] + 1

    matlab_data = sio.loadmat('/home/aurea/Documents/MEGA/MEGA/Documento-PosDoctorado/DadosForlan/Initial_Diagnosis/NQDS_Data_Water.mat')
    matrix = matlab_data['NQDS_Data_Water']

    for i in range(0, 500):
        vector = matrix[i, :]
        for j in range(0, len(vector)):
            if min_value <= vector[j] <= max_value:
                fo_sum[i] = fo_sum[i] + 1

    matlab_data = sio.loadmat('/home/aurea/Documents/MEGA/MEGA/Documento-PosDoctorado/DadosForlan/Initial_Diagnosis/NQDS_Data_Water_Injection.mat')
    matrix = matlab_data['NQDS_Data_Water_Injection']

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

    matlab_data = sio.loadmat('/home/aurea/Documents/MEGA/MEGA/Documento-PosDoctorado/DadosForlan/Initial_Diagnosis/NQDS_Data_BHP.mat')
    matrix = matlab_data['NQDS_Data_BHP']

    for i in range(0, 500):
        vector = matrix[i, :]
        for j in range(0, len(vector)):
            model_values[i].append(abs(vector[j]))

    matlab_data = sio.loadmat('/home/aurea/Documents/MEGA/MEGA/Documento-PosDoctorado/DadosForlan/Initial_Diagnosis/NQDS_Data_Gas.mat')
    matrix = matlab_data['NQDS_Data_Gas']

    for i in range(0, 500):
        vector = matrix[i, :]
        for j in range(0, len(vector)):
            model_values[i].append(abs(vector[j]))

    matlab_data = sio.loadmat('/home/aurea/Documents/MEGA/MEGA/Documento-PosDoctorado/DadosForlan/Initial_Diagnosis/NQDS_Data_Oil.mat')
    matrix = matlab_data['NQDS_Data_Oil']

    for i in range(0, 500):
        vector = matrix[i, :]
        for j in range(0, len(vector)):
            model_values[i].append(abs(vector[j]))

    matlab_data = sio.loadmat('/home/aurea/Documents/MEGA/MEGA/Documento-PosDoctorado/DadosForlan/Initial_Diagnosis/NQDS_Data_Water.mat')
    matrix = matlab_data['NQDS_Data_Water']

    for i in range(0, 500):
        vector = matrix[i, :]
        for j in range(0, len(vector)):
            model_values[i].append(abs(vector[j]))

    matlab_data = sio.loadmat('/home/aurea/Documents/MEGA/MEGA/Documento-PosDoctorado/DadosForlan/Initial_Diagnosis/NQDS_Data_Water_Injection.mat')
    matrix = matlab_data['NQDS_Data_Water_Injection']

    for i in range(0, 500):
        vector = matrix[i, :]
        for j in range(0, len(vector)):
            model_values[i].append(abs(vector[j]))

    result_vector = []
    for i in range(0, 500):
        mean_value = statistics.mean(model_values[i])
        result_vector.append(round(mean_value, 2))

    return result_vector


def categorize_mean_value(vector):

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


def categorize_sumfo_value(vector):

    ''' 1-excellent, 2-good, 3-regular, 4-bad, 5-really bad'''
    result_values = []
    for i in range(0, len(vector)):
        if 70 <= vector[i]:
            result_values.append(0)
        elif 65 <= vector[i] < 70:
            result_values.append(1)
        elif 60 <= vector[i] < 65:
            result_values.append(2)
        elif 55 <= vector[i] < 60:
            result_values.append(3)
        else:
            result_values.append(4)
    return result_values


def main():
    mean_strategy = mean_values()
    print(mean_strategy)
    fo_sum_strategy = fo_sum(-10, +10)
    print(fo_sum_strategy)
    categorize_strategy = categorize_mean_value(mean_strategy)
    print(categorize_strategy)
    fo_categorize_strategy = categorize_sumfo_value(fo_sum_strategy)
    print(fo_categorize_strategy)


if __name__ == "__main__":
    main()