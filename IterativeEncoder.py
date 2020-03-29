import numpy as np
from math import floor

SIZE = 0    #change this in order to save data on the first SIZE iterations of the encoder
num_iteration_steps = 0
num_loops = 0
loop_counter = []

def encode(input_mat):
    """

       :param input_mat: a numpy array of size n*m of boolean values
       :return: mat: a numpy array size (n+1)*(m+1) of boolean values that holds the constraint

       """
    global num_iteration_steps, num_loops, loop_counter
    mat = np.pad(input_mat, pad_width=[(0,1),(0,1)],mode='constant', constant_values=False)
    num_rows, num_cols = mat.shape
    row_max_value = floor(num_cols / 2)
    col_max_value = floor(num_rows / 2)
    rows_value = np.array([np.sum(row,dtype=int) for row in mat])
    cols_value = np.array([np.sum(row, dtype=int) for row in mat.T])
    flipped = True
    while flipped:
        flipped = False

        prev_steps = num_iteration_steps
        for i,val in enumerate(rows_value):
            if val > row_max_value:
                np.logical_not(mat[i],out=mat[i])
                flipped = True
                change = np.array( [1 if val else -1 for val in mat[i]])
                rows_value[i] = num_cols - val
                cols_value += change
                num_iteration_steps += 1
        if len(loop_counter) < SIZE:
            loop_counter.append(num_iteration_steps-prev_steps)
        num_loops += 1
        if not flipped:
            break

        prev_steps = num_iteration_steps
        for i,val in enumerate(cols_value):
            if val > col_max_value:
                np.logical_not(mat[:,i], out=mat[:,i])
                flipped = True
                change = np.array( [1 if val else -1 for val in mat[:,i]])
                cols_value[i] = num_rows - val
                rows_value += change
                num_iteration_steps += 1
        if  len(loop_counter) < SIZE:
            loop_counter.append(num_iteration_steps - prev_steps)
        num_loops += 1
    return mat


def decode(input_mat):
    """

        :param input_mat: a numpy array size (n+1)*(m+1) of boolean values that holds the constraint
        :return: mat: the original two dim numpy array
    """
    row_size,col_size = input_mat.shape[0], input_mat.shape[1]
    res_mat = input_mat.copy()
    if res_mat[row_size - 1,col_size - 1]:
        np.logical_not(res_mat[:, col_size-1], out=res_mat[:, col_size-1])
    for i in range(row_size):
        if res_mat[i,col_size-1]:
            np.logical_not(res_mat[i], out=res_mat[i])
    for j in range(col_size):
        if res_mat[row_size-1, j]:
            np.logical_not(res_mat[:,j], out=res_mat[:,j])
    return res_mat[:row_size-1,:col_size-1]

def _check_correctness(mat, res, dec):
    """
    used for debugging
    check the correctness of the encoder and decoder:
    check that each row and col holds the constraint and that decode(encode(M)) == M
    """
    row_max = floor(res.shape[0] / 2)
    col_max = floor(res.shape[1] / 2)
    rows_value = np.array([np.sum(row, dtype=int) for row in res])
    cols_value = np.array([np.sum(row, dtype=int) for row in res.T])
    assert (np.alltrue(rows_value <= row_max))
    assert (np.alltrue(cols_value <= col_max))
    assert (np.array_equal(mat, dec))

def _get_num_steps():
    """
    used for simulations
    returns the number of iterative steps the encoder/decoder performed and resets the counter
    """
    global num_iteration_steps
    tmp = num_iteration_steps
    num_iteration_steps = 0
    return tmp


def _get_partial_steps():
    global num_iteration_steps, num_loops, loop_counter
    tmp1 = num_iteration_steps
    tmp2 = num_loops
    tmp3 = loop_counter
    tmp3 += [0] * (SIZE - len(tmp3))
    num_iteration_steps = 0
    num_loops = 0
    loop_counter = []
    return tmp1, tmp2, np.array(tmp3)
