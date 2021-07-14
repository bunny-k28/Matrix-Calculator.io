"""
This is the class file of Matrix operations. This class file contains functions
for addition, subtraction, multiplication, scalar multiplication, formation of 
matrix and formation of identity matrix.
"""

# imported modules
from termcolor import cprint

# menu of operations available in the calc. for user
menu = """
\t\tMENU\n
\t1. Addition
\t2. Subtraction
\t3. Multiplication (not working)
\t4. Scalar Multiplication
\t5. Find Transpose
\t6. Find Determinant\n
"""

def add(matrix1=list, matrix2=list): # method for addition operator
    """
        :param: matrix1 && matrix2
        :return: list
        :argument: list && list
    """

    operational_matrix = []  # the matrix formed after applying operation

    for i in range(len(matrix1)):
        operational_matrix.append([])
    # print(operational_matrix)  # print statement for testing

    counter_index = 0  # counter value for first while loop

    """while loop for putting elements in the matrix"""

    while counter_index < len(operational_matrix):
        counter_var2 = 0  # counter value for nested while loop

        while counter_var2 < len(matrix1[0]):  # while loop to add elements as/in the columns
            sum = matrix1[counter_index][counter_var2] + matrix2[counter_index][counter_var2]
            operational_matrix[counter_index].append(sum)
            counter_var2 += 1

        counter_index += 1

    return operational_matrix

def subtract(matrix1=list, matrix2=list): # method for subtraction operator
    """
        :param: matrix1 && matrix2
        :return: list
        :argument: list && list
    """

    operational_matrix = []  # the matrix formed after applying operation

    for i in range(len(matrix1)):
        operational_matrix.append([])
    # print(operational_matrix)  # print statement for testing

    counter_index = 0  # counter value for first while loop

    """while loop for putting elements in the matrix"""

    while counter_index < len(operational_matrix):
        counter_var2 = 0  # counter value for nested while loop

        while counter_var2 < len(matrix1[0]):  # while loop to add elements as/in the columns
            difference = matrix1[counter_index][counter_var2] - matrix2[counter_index][counter_var2]
            operational_matrix[counter_index].append(difference)
            counter_var2 += 1

        counter_index += 1

    return operational_matrix

def scalar_multiply(integer=int, matrix=list): # method for scalar multiplication operator
    """
        :param: integer && matrix
        :return: list
        :argument: int && list
    """

    operational_matrix = []  # the matrix formed after applying operation

    # if matrix is None:
    #     matrix = list()
    for i in range(len(matrix)):
        operational_matrix.append([])
    # print(operational_matrix)

    counter_index = 0  # counter value for first while loop

    """while loop for putting elements in the matrix"""

    while counter_index < len(matrix):
        counter_var2 = 0  # counter value for nested while loop

        while counter_var2 < len(matrix[0]):  # while loop to add elements as/in the columns
            product = matrix[counter_index][counter_var2] * integer
            operational_matrix[counter_index].append(product)
            counter_var2 += 1

        counter_index += 1

    return operational_matrix

def multiply(matrix1=list, matrix2=list): # method for multiplication operator
    """
        :param: matrix1 && matrix2
        :return: list
        :argument: list && list
    """

    operational_matrix = []  # the matrix formed after applying operation

    pom1 = __getProperties__(matrix1)
    pom2 = __getProperties__(matrix2)

    if pom1['rows'] == pom2['cols']:
        mat2Elements = __getTranspose__(matrix2)

        """code to the product matrix"""

        for i in range(len(matrix1)):
            operational_matrix.append([])
        count_rows = 0

        while count_rows < len(matrix1):
            count_cols = 0

            while count_cols < len(mat2Elements[0]):
                pass

                
    elif pom1['rows'] != pom2['cols']:
        cprint(text='PropertyError: No. of row of matrix 1 and No. of column of matrix 2 is not equal!!.',
                color='red', 
                attrs=['bold'])
        print('The No. of row of matrix 1 and No. of column of matrix 2\n'
                'have to be equal to multiply them with each other.')


    # else:
    #     cprint('ATTENTION!!: class is not updated. Install the latest/updated class file to use the'
    #            ' multiplication operator', color='red', attrs='bold')


def __formMatrix__(rows=int, cols=int, type=None):  # method to make a matrix
    """
        :param: rows, columns & type
        :return: list
        :argument: int && int && Any
    """

    raw_matrix = []  # main matrix container

    for i in range(rows):  # for loop to make matrix of order M(rows) x N(cols)
        raw_matrix.append([])

    counter_index = 0  # counter value for first while loop
    counter_row_num = 1  # counter value for row no. in message

    """while loop for putting elements in the matrix"""

    while counter_index < rows:
        counter_var2 = 1  # counter value for nested while loop

        while counter_var2 <= cols:  # while loop to add elements as/in the columns
            col_elements = eval(input(f'Enter element a{counter_row_num}{counter_var2}: '))  # variable to store user's input element
            # col_elements = 5  # statement for testing the function
            raw_matrix[counter_index].append(col_elements)

            counter_var2 += 1

        counter_index += 1
        counter_row_num += 1

    return raw_matrix

def __printMatrix__(matrix_2b_print=list):  # method to print the matrix in a matrix format
    """
    :param: matrix
    :return: None
    :argument: list
    """

    print(f'Your Matrix:-')

    for i in matrix_2b_print:  # for loop to read the main matrix container

        for j in i:  # for loop to read and print the rows and columns
            print(f'\t{j}', end='')

        print()  # print statement to add new empty line

def __identityMatrix__(rows=int, cols=int): # method to make identity matrix
    """
        :param: rows && cols
        :return: list
        :argument: int
    """

    I_raw_matrix = []  # main matrix container for identity matrix

    for i in range(rows):  # for loop to make matrix of order M(rows) x N(cols)
        I_raw_matrix.append([])

    counter_index = 0  # counter value for first while loop

    """while loop for putting elements in the matrix"""

    while counter_index < rows:
        counter_var2 = 1  # counter value for nested while loop

        while counter_var2 <= cols:  # while loop to add elements as/in the columns
            I_raw_matrix[counter_index].append(0)
            counter_var2 += 1

        counter_index += 1

    # print(I_raw_matrix)

    """resetting the counter values"""

    counter_var2 = 1
    counter_index2 = 0

    """while loop for putting 1 in the identity matrix"""

    while counter_var2 <= cols:  # while loop to add elements as/in the columns
        I_raw_matrix[counter_index2][counter_index2] = 1
        counter_index2 += 1
        counter_var2 += 1

    return I_raw_matrix
    # print(I_raw_matrix)

def __getDeterminant__(matrix=list, row_wise=str, column_wise=str): # method to find the determinant of a matrix
    """
    :param: matrix && row_wise $$ column_wise
    :return: list
    :argument: list && boolean
    """

def __getTranspose__(matrix=list): # method to find transpose of a matrix
    """
    :param: matrix
    :return: list
    :argument: list
    """

    transpose = [] # list to store data of transpose method

    for i in range(len(matrix[0])):  # for loop to make a list to store column elements
        transpose.append([])

    # print(transpose)  # statement for testing

    """code to store column elements"""

    counter_var = 0

    while counter_var < len(transpose):
        counter_index = 0

        while counter_index < len(matrix):
            T_element = matrix[counter_index][counter_var]
            transpose[counter_var].append(T_element)
            counter_index += 1

        counter_var += 1

    return transpose

def __getProperties__(matrix=list): # method to get properties of a matrix
    """
    :param: matrix
    :return: properties of matrix in dictionary
    :argument: list as matrix
    """

    return {'rows': len(matrix), 'cols': len(matrix[0]),
            'order': f'{len(matrix)}x{len(matrix[0])}',
            'size': len(matrix) * len(matrix[0])}
