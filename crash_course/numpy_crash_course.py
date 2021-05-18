import numpy as np


def create_numpy_arrays(s_num: int, e_num: int, step: int):
    """
    Function to return a numpy array
    :param s_num: Starting number
    :param e_num: Ending number
    :param step: Steps of increment
    :return: A numpy array
    """
    arr = np.arange(s_num, e_num, step)
    return arr


def generate_zero_matrix(row: int, column: int):
    """
    Function to return a numpy matrix.
    :param row: Number of rows required
    :param column: Number of columns required
    :return: row * column matrix
    """
    matrix = np.zeros(row, column)
    return matrix


def generate_random_num_matrix(s_num: int, e_num: int, d_type):
    """
    Function to return a matrix with random numbers
    :param s_num: Starting number
    :param e_num: Ending number
    :param d_type: rows and columns of the desired matrix
    :return: The desired matrix
    """
    matrix = np.random.randint(s_num, e_num, d_type)
    return matrix


def generate_linearly_spaced(s_num: int, e_num: int, num: int):
    """
    Function to return a linearly spaced array.
    :param s_num: Starting number
    :param e_num: Ending number
    :param num: Desired number of elements in the list
    :return: An array of linearly spaced elements
    """
    arr = np.linspace(s_num, e_num, num)
    return arr


def get_specific_data(row: int, column: int):
    """
    Function to return a specific position in a matrix.
    :param row: The specific row number
    :param column: The specific column number
    :return: The specific piece of data desired
    """
    matrix = np.arange(0, 100).reshape(10, 10)
    return matrix[row, column]

