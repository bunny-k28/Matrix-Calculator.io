"""
1. This is a matrix calculator. Just solve your matrix problems in 3 easy steps:-

    optional step: Enter the formula in which you want to solve those matrix Q.s
    step 1: Enter the order of that matrix
    step 2: Enter the elements of that matrix
    step 3: Enter the operation you want to perform on that matrices

2. All the operations are there in the form of M in MatrixOperation class.
3. The code for that MatrixOperation class is there in a different python file and
    here that class is imported using static import.
"""

import functions as M
from termcolor import cprint


def drawLine(len=int()):
    print('-'*len, end='')
    print('')
    print('-'*len, end='')

if __name__ == '__main__':

    while True:

        drawLine(len=50)
        print(M.menu)
        choice = input('Choose a Operation:- ').lower()

        if choice == '1' or choice == 'addition':

            print('\n\t\t\t\t\t\t\tMAKE YOUR MATRICES')

            counterVar1 = 1  # counter value for while loop and matrix message

            while counterVar1 <= 2:

                print(f'Matrix {counterVar1}:-\n')
                rows = int(input('Enter the no. of rows:- '))
                cols = int(input('Enter the no. columns:- '))
                print()

                if counterVar1 == 1:
                    mat1 = M.__formMatrix__(rows, cols)
                    # print(matrix1)
                    M.__printMatrix__(mat1)
                    print()

                elif counterVar1 == 2:
                    mat2 = M.__formMatrix__(rows, cols)
                    # print(matrix2)
                    M.__printMatrix__(mat2)
                    print()

                counterVar1 += 1

            POM1 = M.__getProperties__(matrix=mat1)
            POM2 = M.__getProperties__(matrix=mat2)

            if POM1['order'] == POM2['order']:

                matSum = M.add(matrix1=mat1, matrix2=mat2)
                print('The SUM of your matrices is:- \n')
                M.__printMatrix__(matrix_2b_print=matSum)

            else:
                cprint(text='PropertyError: The order of Matrix1 and Matrix2 are not same!!',
                       color='red',
                       attrs=['bold'])
                print('\nThe order of both the matrices must be same to perform addition.')

        elif choice == '2' or choice == 'subtraction':
            print('\n\t\t\t\t\t\t\tMAKE YOUR MATRICES')

            counterVar1 = 1  # counter value for while loop and matrix message

            while counterVar1 <= 2:

                print(f'Matrix {counterVar1}:-\n')
                rows = int(input('Enter the no. of rows:- '))
                cols = int(input('Enter the no. columns:- '))
                print()

                if counterVar1 == 1:

                    mat1 = M.__formMatrix__(rows, cols)
                    # print(matrix1)
                    M.__printMatrix__(mat1)
                    print()

                elif counterVar1 == 2:
                    mat2 = M.__formMatrix__(rows, cols)
                    # print(matrix2)
                    M.__printMatrix__(mat2)
                    print()

                counterVar1 += 1

            POM1 = M.__getProperties__(matrix=mat1)
            POM2 = M.__getProperties__(matrix=mat2)

            if POM1['order'] == POM2['order']:

                matDifference = M.subtract(matrix1=mat1, matrix2=mat2)
                print('The DIFFERENCE of your matrices is:- \n')
                M.__printMatrix__(matrix_2b_print=matDifference)

            else:
                cprint(text='PropertyError: The order of Matrix1 and Matrix2 are not same!!',
                       color='red',
                       attrs=['bold'])
                print('\nThe order of both the matrices must be same to perform subtraction.')

        elif choice == '3' or choice == 'multiplication':

            print('Sorry! The option is Out Of Order')
            cprint('ATTENTION!!: class is not updated. Install the latest/updated class file to use the'
                   ' multiplication operator', color='red', attrs='bold')

            '''
            print('\n\t\t\t\t\t\t\tMAKE YOUR MATRICES')

            counterVar1 = 1  # counter value for while loop and matrix message

            while counterVar1 <= 2:

                print(f'Matrix {counterVar1}:-\n')
                rows = int(input('Enter the no. of rows:- '))
                cols = int(input('Enter the no. columns:- '))
                print()

                if counterVar1 == 1:

                    mat1 = M.__formMatrix__(rows, cols)
                    # print(matrix1)
                    M.__printMatrix__(mat1)
                    print()

                elif counterVar1 == 2:
                    mat2 = M.__formMatrix__(rows, cols)
                    # print(matrix2)
                    M.__printMatrix__(mat2)
                    print()

                counterVar1 += 1

            POM1 = M.__getProperties__(matrix=mat1)
            POM2 = M.__getProperties__(matrix=mat2)

            if POM1['cols'] == POM2['rows']:

                matProduct = M.multiply(matrix1=mat1, matrix2=mat2)
                print('The PRODUCT of your matrices is:- \n')
                M.__printMatrix__(matrix_2b_print=matProduct)

            else:
                cprint(text='PropertyError: The column of matrix1 != row of matrix2',
                       color='red',
                       attrs=['bold'])
                print('\nThe column/row of Matrix1 must be == row/column of Matrix2 respectively')
        '''

        elif choice == '4' or choice == 'scalar multiplication':

            print('\n\t\t\t\t\t\t\tMAKE YOUR MATRICES')

            print(f'Matrix:-\n')
            rows = int(input('Enter the no. of rows:- '))
            cols = int(input('Enter the no. columns:- '))
            print()

            Mat = M.__formMatrix__(rows, cols)
            # print(matrix1)
            M.__printMatrix__(Mat)
            print()

            multiplyInt = int(input('Enter the integer you want to multiply with your matrix:- '))

            scalarMat = M.scalar_multiply(integer=multiplyInt, matrix=Mat)
            M.__printMatrix__(scalarMat)

        elif choice == '5' or choice == 'Find Transpose' or choice == 'Transpose':

            print('\n\t\t\t\t\t\t\tMAKE YOUR MATRICES')

            print(f'Matrix:-\n')
            rows = int(input('Enter the no. of rows:- '))
            cols = int(input('Enter the no. columns:- '))
            print()

            Mat = M.__formMatrix__(rows, cols)
            # print(matrix1)
            M.__printMatrix__(Mat)
            print()

            transpose = M.__getTranspose__(matrix=Mat)
            M.__printMatrix__(transpose)            

        else:
            cprint('OutOfMenuError: No such option in menu.', color='red', attrs=['bold'])
