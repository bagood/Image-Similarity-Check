from numpy import asarray
import numpy as np
from PIL import Image

pap1 = input('Input the first photo file name: ')
pap2 = input('Input the second photo file name: ')

image1 = Image.open(pap1).resize((1000, 1000))
image2 = Image.open(pap2).resize((1000, 1000))

data_pap1 = asarray(image1)
data_pap2 = asarray(image2)

def dot_product(matrix1, matrix2):
    result = 0
    for mat1, mat2 in zip(matrix1, matrix2):
        for m1, m2 in zip(mat1, mat2):
            for v1, v2 in zip(m1, m2):
                dot_prod = float(v1) * float(v2)
                result += dot_prod
    return result

def matrix_magnitude(matrix):
    sum = 0
    for mat in matrix:
        for m in mat:
            mini_sum = 0
            for v in m:
                mini_sum += (float(v))**2
            sum += mini_sum
    magnitude = sum**0.5
    return magnitude

def calc(datapap1, datapap2):
    test_dot_product = dot_product(data_pap1, data_pap2)
    test_matrix_magnitude1 = matrix_magnitude(data_pap1)
    test_matrix_magnitude2 = matrix_magnitude(data_pap2)
    calculate = test_dot_product / (test_matrix_magnitude2 * test_matrix_magnitude1)
    print(f'The similarity score between the two pictures is {round(calculate*100)}%')
    return ''

calc(data_pap1, data_pap2)