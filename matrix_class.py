"""
This is the class file of Matrix operations. This class file contains functions
for addition, subtraction, multiplication, scalar multiplication, formation of matrix and
formation of identity matrix.
"""

# imported modules
from termcolor import cprint

menu = """
\t\tMENU\n
\t1. Addition
\t2. Subtraction
\t3. Multiplication (not working)
\t4. Scalar Multiplication
\t5. Find Transpose
\t6. Find Determinant\n
"""


class MatrixOperation:

    def __init__(self):

        """global variables/lists"""

        self.raw_matrix = []  # main matrix container
        self.I_raw_matrix = []  # main matrix container for identity matrix
        self.operational_matrix = []  # the matrix formed after applying operation
        self.column_elements = []  # list to store column elements
        self.determinant = []  # list to store data of determinant method
        self.transpose = []  # list to store data of transpose method

    def add(self, matrix1=list, matrix2=list):
        """
            :param: matrix1
            :return: addition of matrix1 && matrix2
            :argument: lists as matrix
        """

        for i in range(len(matrix1)):
            self.operational_matrix.append([])
        # print(self.operational_matrix)  # print statement for testing

        counter_index = 0  # counter value for first while loop

        """while loop for putting elements in the matrix"""

        while counter_index < len(self.operational_matrix):
            counter_var2 = 0  # counter value for nested while loop

            while counter_var2 < len(matrix1[0]):  # while loop to add elements as/in the columns
                sum = matrix1[counter_index][counter_var2] + matrix2[counter_index][counter_var2]
                self.operational_matrix[counter_index].append(sum)
                counter_var2 += 1

            counter_index += 1

        return self.operational_matrix

    def subtract(self, matrix1=list, matrix2=list):
        """
            :param: matrix1
            :return: subtraction of matrix1 && matrix2
            :argument: lists as matrix
        """

        for i in range(len(matrix1)):
            self.operational_matrix.append([])
        # print(self.operational_matrix)  # print statement for testing

        counter_index = 0  # counter value for first while loop

        """while loop for putting elements in the matrix"""

        while counter_index < len(self.operational_matrix):
            counter_var2 = 0  # counter value for nested while loop

            while counter_var2 < len(matrix1[0]):  # while loop to add elements as/in the columns
                difference = matrix1[counter_index][counter_var2] - matrix2[counter_index][counter_var2]
                self.operational_matrix[counter_index].append(difference)
                counter_var2 += 1

            counter_index += 1

        return self.operational_matrix

    def scalar_multiply(self, integer=int, matrix=list):
        """
            :param: integer && matrix1
            :return: product of matrix with integer
            :argument: lists as matrix
        """

        # if matrix is None:
        #     matrix = list()
        for i in range(len(matrix)):
            self.operational_matrix.append([])
        # print(self.operational_matrix)

        counter_index = 0  # counter value for first while loop

        """while loop for putting elements in the matrix"""

        while counter_index < len(matrix):
            counter_var2 = 0  # counter value for nested while loop

            while counter_var2 < len(matrix[0]):  # while loop to add elements as/in the columns
                product = matrix[counter_index][counter_var2] * integer
                self.operational_matrix[counter_index].append(product)
                counter_var2 += 1

            counter_index += 1

        return self.operational_matrix

    def multiply(self, matrix1=list, matrix2=list):
        """
            :param: matrix1
            :return: multiplication of matrix1 && matrix2
            :argument: lists as matrix
        """

        pom1 = Matrix().__getProperties__(matrix1)
        pom2 = Matrix().__getProperties__(matrix2)

        if pom1['order'] == pom2['order']:
            col_elements = Matrix().__getColumnElements__(matrix2)

            """code to the product matrix"""

            for i in range(len(matrix1)):
                self.operational_matrix.append([])

            """while loop for column"""

            counter_index = 0  # counter value for first while loop

            while counter_index < len(self.operational_matrix):
                counter_var2 = 0  # counter value for nested while loop
                product_sum = []  # list to store values of element.ij

                while counter_var2 < len(matrix1[0]):  # while loop column elements of product matrix
                    product = matrix1[counter_index][counter_var2] * col_elements[counter_index][counter_var2]
                    product_sum.append(product)
                    counter_var2 += 1

                self.operational_matrix[counter_index].append(sum(product_sum))

                counter_index += 1

            """while loop for rows"""

            counter_index = 0  # counter value for first while loop

            while counter_index < len(self.operational_matrix):
                counter_var2 = 0  # counter value for nested while loop
                product_sum = []  # list to store values of element.ij

                while counter_var2 < len(matrix1[0]):  # while loop column elements of product matrix
                    product = matrix1[counter_index][counter_var2] * col_elements[counter_index][counter_var2]
                    product_sum.append(product)
                    counter_var2 += 1

                self.operational_matrix[counter_index].append(sum(product_sum))

                counter_index += 1

            return self.operational_matrix

        else:
            cprint('ATTENTION!!: class is not updated. Install the latest/updated class file to use all the features'
                   ' of multiplication function', color='red', attrs='bold')


class Matrix(MatrixOperation):

    def __init__(self):  # function to initialize current class

        MatrixOperation.__init__(self)  # statement to initialize MatrixOperation class

        """global variables"""

        self.raw_matrix = []  # main matrix container
        self.I_raw_matrix = []  # main matrix container for identity matrix
        self.column_elements = []  # list to store column elements
        self.counterVar1 = 1

    def __formMatrix__(self, rows=int, cols=int, type=None):  # function to make matrix with 2 integer parameters
        """
            :param: rows, columns & type
            :return: matrix of M(rows) x N(columns)
            :argument: int, int & text
        """


        for i in range(rows):  # for loop to make matrix of order M(rows) x N(cols)
            self.raw_matrix.append([])

        counter_index = 0  # counter value for first while loop
        counter_row_num = 1  # counter value for row no. in message

        """while loop for putting elements in the matrix"""

        while counter_index < rows:
            counter_var2 = 1  # counter value for nested while loop

            while counter_var2 <= cols:  # while loop to add elements as/in the columns
                col_elements = eval(input(f'Enter element a{counter_row_num}{counter_var2}: '))  # variable to store user's input element
                # col_elements = 5  # statement for testing the function
                self.raw_matrix[counter_index].append(col_elements)

                counter_var2 += 1

            counter_index += 1
            counter_row_num += 1

        return self.raw_matrix

    def __printMatrix__(self, matrix_2b_print=list):  # function to print the formed matrix in a matrix format
        """
        :param: matrix
        :return: list (final matrix) in matrix format
        :argument: list as matrix
        """

        print(f'Your Matrix:-')

        for i in matrix_2b_print:  # for loop to read the main matrix container

            for j in i:  # for loop to read and print the rows and columns
                print(f'\t{j}', end='')

            print()  # print statement to add new empty line
            

    def __identityMatrix__(self, rows=int, cols=int):
        """
            :param: rows && cols
            :return: Identity matrix
            :argument: int
        """

        for i in range(rows):  # for loop to make matrix of order M(rows) x N(cols)
            self.I_raw_matrix.append([])

        counter_index = 0  # counter value for first while loop

        """while loop for putting elements in the matrix"""

        while counter_index < rows:
            counter_var2 = 1  # counter value for nested while loop

            while counter_var2 <= cols:  # while loop to add elements as/in the columns
                self.I_raw_matrix[counter_index].append(0)
                counter_var2 += 1

            counter_index += 1

        # print(self.I_raw_matrix)

        """resetting the counter values"""

        counter_var2 = 1
        counter_index2 = 0

        """while loop for putting 1 in the identity matrix"""

        while counter_var2 <= cols:  # while loop to add elements as/in the columns
            self.I_raw_matrix[counter_index2][counter_index2] = 1
            counter_index2 += 1
            counter_var2 += 1

        return self.I_raw_matrix
        # print(self.I_raw_matrix)

    def __getColumnElements__(self, matrix=list):
        """
        :param: matrix
        :return: list of column elements
        :argument: list as matrix
        """

        for i in range(len(matrix[0])):  # for loop to make a list to store column elements
            self.column_elements.append([])
        # print(self.column_elements)  # statement for testing

        """code to store column elements"""

        counter_var = 0

        while counter_var < len(self.column_elements):
            counter_index = 0

            while counter_index < len(matrix):
                col_element = matrix[counter_index][counter_var]
                self.column_elements[counter_var].append(col_element)
                counter_index += 1

            counter_var += 1

        return self.column_elements

    def __getDeterminant__(self, matrix, row_wise=False, column_wise=False):
        """
        :param: matrix && row_wise $$ column_wise
        :return: determinant of the given matrix
        :argument: matrix && boolean value
        """


    def __getTranspose__(self, matrix=list):
        """
        :param: matrix
        :return: list
        :argument: list
        """

        for i in range(len(matrix[0])):  # for loop to make a list to store column elements
            self.transpose.append([])

        # print(self.transpose)  # statement for testing

        """code to store column elements"""

        counter_var = 0

        while counter_var < len(self.transpose):
            counter_index = 0

            while counter_index < len(matrix):
                T_element = matrix[counter_index][counter_var]
                self.transpose[counter_var].append(T_element)
                counter_index += 1

            counter_var += 1

        return self.transpose

    
    def __getProperties__(self, matrix):
        """
        :param: matrix
        :return: properties of matrix in dictionary
        :argument: list as matrix
        """

        return {'rows': len(matrix), 'cols': len(matrix[0]),
                'order': f'{len(matrix)}x{len(matrix[0])}',
                'size': len(matrix) * len(matrix[0])}
