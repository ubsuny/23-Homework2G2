# Varying Methods to Perform Axis Array Summation

## Background
Einstein notation is a mathematical shorthand used to represent summations of tensors. In the case of covariant tensors, we use subscript indices to represent the dimensions of the tensors, and when indices are repeated
between two tensors that index is summed over. For example, $A_i$ is a 1D tensor, $B_{i,j}$ is a 2D tensor, etc. 

If we wish to sum these tensors along a our first axis, we can simply write
$$A_i B_{i,j}$$
Since
$$A_i B_{i,j} = \sum_{i} A_i B_{i,j}$$
Which effectively just eliminates the summation sign. 

This notation can be used to simplify tensor operations for any number of dimensions. For example
$$A_{i,j} B_{i,j} = \sum{i} \sum{j} A_{i,j} B_{i,j} = **A** \dot **B**$$

## Axis Array Summation

For this project, we elected to implement the operation of axis array summation. This is simply the act of summing all of the elements along a given axis. Generally speaking, for some tensor $A_{i,j,k}$, summation along
the principle axis is given by
$$\sum_{i} A_{i,j,k}$$

For example, if we have the array
$$A_i = [1,2,3]$$
$$\sum{i} A_i = A_1 + A_2 + A_3 = 1 + 2 + 3 = 6$$
Summing the elements along the principle axis would give a result of 6. As previously mentioned, this will work for tensors of any dimensions.

## Comparing Methods of Calculation

There are several ways to perform this operation in python. The two principle methods we compared are (as outlined by @Pranjal-Srivastava-2023)

### Method 1: Using Loops to "Manually" Perform the Math

The steps to this algorithm are

1) Define a function sum_rows(arr) that takes a 2D list arr as input.
2) Define a function sum_columns(arr) that takes a 2D list arr as input.
3) Calculate row sums and column sums by calling the sum_rows and sum_columns functions on the input array.
4) Print the original 2D list array.
5) Print the computed row sums using Einstein summation.
6) Print the computed column sums using Einstein summation.
7) Measure the execution time of the entire array summation operation:
8) Print the elapsed time in microseconds for the array summation operation.

Which are implemented in the code as


`def array_axis_summation(array):`
    
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


### Method 2: Using Numpy's Built in Einsum Function

The steps to this algorithm are

1) Calculate row sums and column sums using NumPy and the Einstein summation convention
2) Print the original 2D NumPy array array
3) Print the computed row sums using Einstein summation
4) Print the computed column sums using Einstein summation
5) Measure the execution time of the entire array summation operation
6) Print the elapsed time in microseconds for the array summation operation

Which are implemented as

`def array_axis_summation(array):`   
 
    Demonstrates array axis summations using the Einstein summation convention.

    Given a 2D array as input, it performs summations along rows (axis 0)
    and columns (axis 1) using the Einstein summation convention and
    prints the original array and the summation results.

    Parameters:
    array (numpy.ndarray): The input 2D array for summation.
    """

    # Sum along rows (axis 0) using Einstein summation convention
    row_sums = np.einsum('ij->j', array)
    %time np.einsum('ij->j', array)    #this function will calculate and print the consumed time

    # Sum along columns (axis 1) using Einstein summation convention
    column_sums = np.einsum('ij->i', array)
    %time np.einsum('ij->i', array)    #this function will calculate and print the consumed time

    print("Original Array:")
    print(array)

    print("\nSum Along Rows (Axis 0) using Einstein summation:")
    print(row_sums)

    print("\nSum Along Columns (Axis 1) using Einstein summation:")
    print(column_sums)


    #Define the code block as a function
    def timed_code():
     user_array = [[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]]
     array_axis_summation(user_array)

    #Measure the execution time with timeit
    elapsed_time = timeit.timeit(timed_code, number=1)
    elapsed_time_micro = elapsed_time * 1e6

    #Print the elapsed time in seconds
    print(f"Elapsed Time: {elapsed_time_micro:.6f} microseconds")


## Results

While the execution time does depend on the machine on which the code is being run, using numpy's built in einsum function is significantly faster than manually applying the algorithm.
This is likely due to the fact that einsum is a part of the numpy library, which is largely written in C. C tends to be much faster at handling calculations than Python,
so numpy algorithms can take advantage of this to offer optimized calculations.

### Sources
https://mathworld.wolfram.com/EinsteinSummation.html
https://numpy.org/doc/stable/reference/generated/numpy.einsum.html
https://github.com/ubsuny/CompPhys/blob/main/ReviewPython/EinsteinNotation.ipynb
