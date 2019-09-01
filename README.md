# Mission
Implement Fibonacci number algorithm by using three-different type of method.

# Approaches

## Recursive
By Human-Thinkable method, calling same function recursively.
```
def get_fib_num_by_recursive_at(number):
    return get_fib_num_by_recursive_at(number - 1) + get_fib_num_by_recursive_at(number - 2)
```

## Memoization
For optimizing algorithm that kind of calling repeatedly, caching result and using when called duplicated.
```
if number in memo:
    return memo[number]
result = get_fib_num_by_memoized_with_memo_at(number - 1, memo) + get_fib_num_by_memoized_with_memo_at(number - 2, memo)
memo[number] = result
return result
```

## Bottom-up
For solving recursive problem, there is non-recursive solution like this. Using iterator for processing repetitive calculation.
```
for n in range(3, number + 1):
    fibs[n] = fibs[n - 1] + fibs[n - 2]
```

# Performance Comparison
```
Wrote profile results to Fibonacci.py.lprof
Timer unit: 1e-06 s

Total time: 114.099 s
File: Fibonacci.py
Function: test_performance_get_fib_num_by_recursive at line 56

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    56                                           @profile
    57                                           def test_performance_get_fib_num_by_recursive():
    58         1         48.0     48.0      0.0      test_get_fib_num_by_recursive_at(2, 1)
    59         1         20.0     20.0      0.0      test_get_fib_num_by_recursive_at(5, 5)
    60         1        111.0    111.0      0.0      test_get_fib_num_by_recursive_at(10, 55)
    61         1       7765.0   7765.0      0.0      test_get_fib_num_by_recursive_at(20, 6765)
    62         1  114091465.0 114091465.0    100.0      test_get_fib_num_by_recursive_at(40, 102334155)

Total time: 0.000258 s
File: Fibonacci.py
Function: test_performance_get_fib_num_by_memoized at line 64

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    64                                           @profile
    65                                           def test_performance_get_fib_num_by_memoized():
    66         1         20.0     20.0      7.8      test_get_fib_num_by_memoized_at(2, 1)
    67         1         20.0     20.0      7.8      test_get_fib_num_by_memoized_at(5, 5)
    68         1         38.0     38.0     14.7      test_get_fib_num_by_memoized_at(10, 55)
    69         1         93.0     93.0     36.0      test_get_fib_num_by_memoized_at(20, 6765)
    70         1         87.0     87.0     33.7      test_get_fib_num_by_memoized_at(40, 102334155)

Total time: 0.000224 s
File: Fibonacci.py
Function: test_performance_get_fib_num_by_bottom_up at line 72

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    72                                           @profile
    73                                           def test_performance_get_fib_num_by_bottom_up():
    74         1         14.0     14.0      6.2      test_get_fib_num_by_bottom_up_at(2, 1)
    75         1         78.0     78.0     34.8      test_get_fib_num_by_bottom_up_at(5, 5)
    76         1         28.0     28.0     12.5      test_get_fib_num_by_bottom_up_at(10, 55)
    77         1         25.0     25.0     11.2      test_get_fib_num_by_bottom_up_at(20, 6765)
    78         1         79.0     79.0     35.3      test_get_fib_num_by_bottom_up_at(40, 102334155)
```
