'''
Real-world Example: Multiprocessing for CPU-bound tasks
Scenario: Factorial Calculation
Problem: Calculating the factorial of a large number using a single process can be computationally expensive.
Solution: Multiprocessing can be used to distribute the workload across multiple processes, allowing for faster execution.  
'''

import multiprocessing
import time 
import math
import sys

# Increase the maximum number of digits for integer conversion
sys.set_int_max_str_digits(100000)

## Fucntion to compute factorials of a given number
def compute_factorial(number):
    print(f"Computing factorial of {number}...")
    result = math.factorial(number)
    print(f"Factorial of {number} is {result}")
    return result

if __name__ == "__main__":
    numbers = [500,600,700,8000]

    start_time = time.time()

    # Create a pool of processes
    with multiprocessing.Pool() as pool:
        # Use the map function to apply the compute_factorial function to each number in the list
        results = pool.map(compute_factorial, numbers)

    end_time = time.time()

    print(f"Results: {results}")
    print(f"Time taken: {end_time - start_time} seconds")