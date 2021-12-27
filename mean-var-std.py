import numpy as np

def calculate(list):
    # The list must contain 9 digits, no more nor less
    if len(list) != 9:
        raise ValueError('List must contain nine numbers.')
    mtx = np.array([tuple(list[0:3]), tuple(list[3:6]), tuple(list[6:])])
    # Calculating mean
    mean_axis1 = mtx.mean(axis=0)
    mean_axis2 = mtx.mean(axis=1)
    mean_flattened = mtx.mean()
    # Calculating variance
    var_axis1 = mtx.var(axis=0)
    var_axis2 = mtx.var(axis=1)
    var_flattened = mtx.var()
    # Calculating std dev
    std_axis1 = mtx.std(axis=0)
    std_axis2 = mtx.std(axis=1)
    std_flattened = mtx.std()
    # Finding the max
    max_axis1 = mtx.max(axis=0)
    max_axis2 = mtx.max(axis=1)
    max_flattened = mtx.max()
    # Finding the min
    min_axis1 = mtx.min(axis=0)
    min_axis2 = mtx.min(axis=1)
    min_flattened = mtx.min()
    # Calculating the sum
    sum_axis1 = mtx.sum(axis=0)
    sum_axis2 = mtx.sum(axis=1)
    sum_flattened = mtx.sum()
    calculations = {'mean': [mean_axis1.tolist(), mean_axis2.tolist(), mean_flattened],
            'variance': [var_axis1.tolist(), var_axis2.tolist(), var_flattened],
            'standard deviation': [std_axis1.tolist(), std_axis2.tolist(), std_flattened],
            'max': [max_axis1.tolist(), max_axis2.tolist(), max_flattened],
            'min': [min_axis1.tolist(), min_axis2.tolist(), min_flattened],
            'sum': [sum_axis1.tolist(), sum_axis2.tolist(), sum_flattened]}
    return calculations

print(calculate([2,6,2,8,4,0,1,5,7]))