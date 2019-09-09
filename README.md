# Mission
Implement Fibonacci number algorithm by using four-different type of method.

# Approaches

## Recursive
By Human-Thinkable method, calling same function recursively.
```
def get_fib_num_by_recursive_at(number):
    return get_fib_num_by_recursive_at(number - 1) + get_fib_num_by_recursive_at(number - 2)
```

## Recursive with tail-call
Recursive solution with compiler-optimized by using tail call.
```
def get_fib_num_by_recursive_tail_call(number, first_number, sec_number):
    if number == 0: 
        return first_number 
    if number == 1: 
        return sec_number 
    return get_fib_num_by_recursive_tail_call(number - 1, sec_number, first_number + sec_number)
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

Total time: 168.634 s
File: Fibonacci.py
Function: test_performance_get_fib_num_by_recursive at line 74

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    74                                           @profile
    75                                           def test_performance_get_fib_num_by_recursive():
    76         1        291.0    291.0      0.0      test_get_fib_num_by_recursive_at(2, 1)
    77         1         33.0     33.0      0.0      test_get_fib_num_by_recursive_at(5, 5)
    78         1        142.0    142.0      0.0      test_get_fib_num_by_recursive_at(10, 55)
    79         1      12575.0  12575.0      0.0      test_get_fib_num_by_recursive_at(20, 6765)
    80         1  168620850.0 168620850.0    100.0      test_get_fib_num_by_recursive_at(40, 102334155)

Total time: 0.000177 s
File: Fibonacci.py
Function: test_performance_get_fib_num_by_recursive_tail_call at line 82

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    82                                           @profile
    83                                           def test_performance_get_fib_num_by_recursive_tail_call():
    84         1         25.0     25.0     14.1      test_get_fib_num_by_recursive_tail_call_at(2, 1)
    85         1         29.0     29.0     16.4      test_get_fib_num_by_recursive_tail_call_at(5, 5)
    86         1         25.0     25.0     14.1      test_get_fib_num_by_recursive_tail_call_at(10, 55)
    87         1         42.0     42.0     23.7      test_get_fib_num_by_recursive_tail_call_at(20, 6765)
    88         1         56.0     56.0     31.6      test_get_fib_num_by_recursive_tail_call_at(40, 102334155)

Total time: 0.000224 s
File: Fibonacci.py
Function: test_performance_get_fib_num_by_memoized at line 90

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    90                                           @profile
    91                                           def test_performance_get_fib_num_by_memoized():
    92         1         18.0     18.0      8.0      test_get_fib_num_by_memoized_at(2, 1)
    93         1         22.0     22.0      9.8      test_get_fib_num_by_memoized_at(5, 5)
    94         1         37.0     37.0     16.5      test_get_fib_num_by_memoized_at(10, 55)
    95         1         51.0     51.0     22.8      test_get_fib_num_by_memoized_at(20, 6765)
    96         1         96.0     96.0     42.9      test_get_fib_num_by_memoized_at(40, 102334155)

Total time: 0.03329 s
File: Fibonacci.py
Function: test_performance_get_fib_num_by_bottom_up at line 98

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    98                                           @profile
    99                                           def test_performance_get_fib_num_by_bottom_up():
   100         1         15.0     15.0      0.0      test_get_fib_num_by_bottom_up_at(2, 1)
   101         1         29.0     29.0      0.1      test_get_fib_num_by_bottom_up_at(5, 5)
   102         1         23.0     23.0      0.1      test_get_fib_num_by_bottom_up_at(10, 55)
   103         1      33148.0  33148.0     99.6      test_get_fib_num_by_bottom_up_at(20, 6765)
   104         1         75.0     75.0      0.2      test_get_fib_num_by_bottom_up_at(40, 102334155)
```
