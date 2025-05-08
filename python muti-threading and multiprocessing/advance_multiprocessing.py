### Multiprocessing with processPoolExecutor

from concurrent.futures import ProcessPoolExecutor
import time

def square_number(number):
    time.sleep(1)
    return f"The square of {number} is {number * number}"

numbers = [1, 2, 3, 4, 5]

if __name__ == "__main__":
    with ProcessPoolExecutor() as executor:
        results = executor.map(square_number, numbers)

    for result in results:
        print(result)