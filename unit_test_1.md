```python
import timeit
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

    # Sum along columns (axis 1) using Einstein summation convention
    column_sums = np.einsum('ij->i', array)

    print("Original Array:")
    print(array)

    print("\nSum Along Rows (Axis 0) using Einstein summation:")
    print(row_sums)

    print("\nSum Along Columns (Axis 1) using Einstein summation:")
    print(column_sums)


# Define the code block as a function
def timed_code():
    user_array = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]
    array_axis_summation(user_array)

# Measure the execution time with timeit
elapsed_time = timeit.timeit(timed_code, number=1)
elapsed_time_micro = elapsed_time * 1e6

# Print the elapsed time in seconds
print(f"Elapsed Time: {elapsed_time_micro:.6f} microseconds")


```

    Original Array:
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    
    Sum Along Rows (Axis 0) using Einstein summation:
    [12 15 18]
    
    Sum Along Columns (Axis 1) using Einstein summation:
    [ 6 15 24]
    Elapsed Time: 832.729042 microseconds



```python
import timeit
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

    # Sum along columns (axis 1) using Einstein summation convention
    column_sums = np.einsum('ij->i', array)

    print("Original Array:")
    print(array)

    print("\nSum Along Rows (Axis 0) using Einstein summation:")
    print(row_sums)

    print("\nSum Along Columns (Axis 1) using Einstein summation:")
    print(column_sums)


# Define the code block as a function
def timed_code():
    user_array = [[2, 9, 13,2],
                  [42, 5, 6,2],
                  [7, 8, 9,8],
                  [3,4,8,10]]
    array_axis_summation(user_array)

# Measure the execution time with timeit
elapsed_time = timeit.timeit(timed_code, number=1)
elapsed_time_micro = elapsed_time * 1e6

# Print the elapsed time in seconds
print(f"Elapsed Time: {elapsed_time_micro:.6f} microseconds")


```

    Original Array:
    [[2, 9, 13, 2], [42, 5, 6, 2], [7, 8, 9, 8], [3, 4, 8, 10]]
    
    Sum Along Rows (Axis 0) using Einstein summation:
    [54 26 36 22]
    
    Sum Along Columns (Axis 1) using Einstein summation:
    [26 55 32 25]
    Elapsed Time: 1135.191880 microseconds



```python
import timeit
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

    # Sum along columns (axis 1) using Einstein summation convention
    column_sums = np.einsum('ij->i', array)

    print("Original Array:")
    print(array)

    print("\nSum Along Rows (Axis 0) using Einstein summation:")
    print(row_sums)

    print("\nSum Along Columns (Axis 1) using Einstein summation:")
    print(column_sums)


# Define the code block as a function
def timed_code():
    user_array = [[1, 1, 1],
                  [1, 1, 1],
                  [1, 1, 1]]
    array_axis_summation(user_array)

# Measure the execution time with timeit
elapsed_time = timeit.timeit(timed_code, number=1)
elapsed_time_micro = elapsed_time * 1e6

# Print the elapsed time in seconds
print(f"Elapsed Time: {elapsed_time_micro:.6f} microseconds")


```

    Original Array:
    [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    
    Sum Along Rows (Axis 0) using Einstein summation:
    [3 3 3]
    
    Sum Along Columns (Axis 1) using Einstein summation:
    [3 3 3]
    Elapsed Time: 6468.638079 microseconds



```python

```
