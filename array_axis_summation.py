def array_axis_summation(array):
    """
    Demonstrates array axis summations without using NumPy.

    Given a 2D list as input, it performs summations along rows (axis 0)
    and columns (axis 1) and prints the original list and the summation results.

    Parameters:
    array (list of lists): The input 2D list for summation.
    """

    # Function to calculate the sum along rows (axis 0)
    def sum_rows(arr):
        return [sum(row) for row in arr]

    # Function to calculate the sum along columns (axis 1)
    def sum_columns(arr):
        return [sum(arr[i][j] for i in range(len(arr))) for j in range(len(arr[0]))]

    # Calculate row sums and column sums
    row_sums = sum_rows(array)
    %time                                #this function will calculate and print the consumed time
    column_sums = sum_columns(array)
    %time                                #this function will calculate and print the consumed time

    print("Original List:")
    for row in array:
        print(row)

    print("\nSum Along Rows (Axis 0):")
    print(row_sums)

    print("\nSum Along Columns (Axis 1):")
    print(column_sums)

if __name__ == "__main__":
    # This code block will only execute when the script is run directly,
    # not when it's imported as a module into another script.
    user_array = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]
    array_axis_summation(user_array)
