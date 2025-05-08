### Multithreading in Python
# Multithreading is a technique where multiple threads are spawned by a process to execute tasks concurrently.
# It allows a program to perform multiple tasks simultaneously, improving efficiency and responsiveness.
# Python provides built-in support for multithreading through the threading module.

## when to use multithreading?
# 1. I/O-bound tasks: When the program spends a lot of time waiting for I/O operations (e.g., file reading/writing, network requests), multithreading can help improve performance by allowing other threads to run while one thread is waiting for I/O.
# 2. GUI applications: In GUI applications, multithreading can keep the user interface responsive while performing background tasks.
# 3. CPU-bound tasks: For CPU-bound tasks, multithreading can help distribute the workload across multiple threads, potentially improving performance by leveraging multiple CPU cores.
# 4. Network applications: In network applications, multithreading can handle multiple connections simultaneously, improving responsiveness and throughput.
#5. concurrent tasks: When multiple tasks can be executed independently and do not require synchronization, multithreading can help improve performance by executing them concurrently.

import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"Number: {i}")
        
def print_letters():
    for letter in "abcde":
        time.sleep(2)
        print(f"Letter: {letter}")



## Creating threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

t = time.time()

# Starting threads
t1.start()
t2.start()

# print_numbers()
# print_letters()

# Wait for threads to complete
t1.join()
t2.join()


finished_time = time.time() - t
print(finished_time)