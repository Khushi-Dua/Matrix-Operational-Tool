import numpy as np

def inp_mat(prompt):
    print(prompt)
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    print("Enter the values of the matrix row by row: ")
    matrix = []
    for i in range(rows):
        row = list(map(float, input(f"Row {i+1}: ").split()))
        if len(row) != cols:
            print("Error: Number of columns must match the input.")
            return None
        matrix.append(row)
    return np.array(matrix)

def display_menu():
    print("\n====================== MATRIX OPERATIONS MENU ======================")
    print(" 1. Addition")
    print(" 2. Subtraction")
    print(" 3. Multiplication")
    print(" 4. Transpose")
    print(" 5. Determinant")
    print(" 6. Inverse")
    print(" 0. Exit")
    print("===================================================================\n")

def operations():
    while True:
        display_menu()
        choice = int(input("Enter your choice: "))

        if choice == 0:
            print("Exiting... Thank you for using the Matrix Operations Tool!")
            break

        elif choice in [1, 2, 3]:
            mat1 = inp_mat("Matrix 1:")
            mat2 = inp_mat("Matrix 2:")
            if mat1 is None or mat2 is None:
                continue

            if choice == 1:
                if mat1.shape == mat2.shape:
                    print("Result: \n", np.add(mat1, mat2))
                else:
                    print("Error: Matrices must be of the same size for addition.")

            elif choice == 2:
                if mat1.shape == mat2.shape:
                    print("Result: \n", np.subtract(mat1, mat2))
                else:
                    print("Error: Matrices must be of the same size for subtraction.")

            elif choice == 3:
                if mat1.shape[1] == mat2.shape[0]:
                    print("Result: \n", np.matmul(mat1, mat2))
                else:
                    print("Error: Number of columns in Matrix 1 must equal the number of rows in Matrix 2 for multiplication.")

        elif choice == 4:
            mat = inp_mat("Matrix:")
            if mat is not None:
                print("Result: \n", np.transpose(mat))

        elif choice == 5:
            mat = inp_mat("Square Matrix:")
            if mat is not None:
                if mat.shape[0] != mat.shape[1]:
                    print("Error: Determinant can only be calculated for square matrices.")
                else:
                    print("Determinant: \n", np.linalg.det(mat))

        elif choice == 6:
            mat = inp_mat("Square Matrix:")
            if mat is not None:
                if mat.shape[0] != mat.shape[1]:
                    print("Error: Inverse can only be calculated for square matrices.")
                elif np.linalg.det(mat) == 0:
                    print("Error: Matrix is singular and cannot be inverted.")
                else:
                    print("Inverse: \n", np.linalg.inv(mat))

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    print("Welcome to the Matrix Operations Tool!")
    operations()
