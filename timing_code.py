import time
import timeit

def func_one(n):
    return [str(num) for num in range(n)]

def func_two(n):
    return list(map(str,range(n)))

# Current time
start_time = time.time()

# Run code
result = func_one(1000000)

# Current time after running code
end_time = time.time()

# Elapsed time
elapsed_time = end_time - start_time
print(elapsed_time)

# Current time
start_time = time.time()

# Run code
result = func_two(1000000)

# Current time after running code
end_time = time.time()

# Elapsed time
elapsed_time = end_time - start_time
print(elapsed_time)

stmt = '''
func_one(100)
'''

setup = '''
def func_one(n):
    return [str(num) for num in range(n)]
'''

time_taken= timeit.timeit(stmt,setup,number=1000000)

print(time_taken)

stmt2 = '''
func_two(100)
'''

setup2 = '''
def func_two(n):
    return list(map(str,range(n)))
'''

time_taken2= timeit.timeit(stmt2,setup2,number=1000000)

print(time_taken2)
