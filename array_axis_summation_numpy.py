import numpy as np

def array_axis_summation(array):
    """
    Demonstrates array axis summations using the Einstein summation convention.

    Given a 2D array as input, it performs summations along rows (axis 0)
    and columns (axis 1) using the Einstein summation convention and
    prints the original array and the summation results.

    Parameters:
    array (numpy.ndarray): The input 2D array for summation.
    """

    # Sum along rows (axis 0) using Einstein summation convention
    row_sums = np.einsum('ij->j', array)
    %time np.einsum('ij->j', array)

    # Sum along columns (axis 1) using Einstein summation convention
    column_sums = np.einsum('ij->i', array)
    %time np.einsum('ij->i', array)

    print("Original Array:")
    print(array)

    print("\nSum Along Rows (Axis 0) using Einstein summation:")
    print(row_sums)

    print("\nSum Along Columns (Axis 1) using Einstein summation:")
    print(column_sums)

# Example usage:
# This code block will only execute when the script is run directly,
# not when it's imported as a module into another script.
if __name__ == "__main__":
    user_array = np.array([[1, 2, 3],
                           [4, 5, 6],
                           [7, 8, 9]])
    array_axis_summation(user_array)
