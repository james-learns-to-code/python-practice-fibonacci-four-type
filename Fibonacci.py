# Mission : Make Fibonacci number using 4 type of approaching

# MARK: Implementation

def get_fib_num_by_recursive_at(number):
    if (number == 1 or number == 2):
        return 1
    return get_fib_num_by_recursive_at(number - 1) + get_fib_num_by_recursive_at(number - 2)

def get_fib_num_by_recursive_tail_call_at(number):
    if (number == 1 or number == 2):
        return 1
    return get_fib_num_by_recursive_tail_call(number, 0, 1)

def get_fib_num_by_recursive_tail_call(number, first_number, sec_number):
    if number == 0: 
        return first_number 
    if number == 1: 
        return sec_number 
    return get_fib_num_by_recursive_tail_call(number - 1, sec_number, first_number + sec_number)

def get_fib_num_by_memoized_at(number):
    memo = {1: 1, 2: 1}
    return get_fib_num_by_memoized_with_memo_at(number, memo)

def get_fib_num_by_memoized_with_memo_at(number, memo):
    if number in memo:
        return memo[number]
    result = get_fib_num_by_memoized_with_memo_at(number - 1, memo) + get_fib_num_by_memoized_with_memo_at(number - 2, memo)
    memo[number] = result
    return result

def get_fib_num_by_bottom_up_at(number):
    if (number == 1 or number == 2):
        return 1
    fibs = [None] * (number + 1)
    fibs[1] = 1
    fibs[2] = 1
    return get_fib_num_by_bottom_up_with_fibs_at(number, fibs)

def get_fib_num_by_bottom_up_with_fibs_at(number, fibs):
    for n in range(3, number + 1):
        fibs[n] = fibs[n - 1] + fibs[n - 2]
    return fibs[number]

# MARK: Test

def test_get_fib_num_by_recursive_at(number, expect_number):
    print('test_get_fib_num_by_recursive_at number: ', number)
    fib_num = get_fib_num_by_recursive_at(number)
    print('fib_num is', fib_num)
    assert fib_num == expect_number, 'Error: Result is not expect'

def test_get_fib_num_by_recursive_tail_call_at(number, expect_number):
    print('test_get_fib_num_by_recursive_tail_call_at number: ', number)
    fib_num = get_fib_num_by_recursive_tail_call_at(number)
    print('fib_num is', fib_num)
    assert fib_num == expect_number, 'Error: Result is not expect'

def test_get_fib_num_by_memoized_at(number, expect_number):
    print('test_get_fib_num_by_memoized_at number: ', number)
    fib_num = get_fib_num_by_memoized_at(number)
    print('fib_num is', fib_num)
    assert fib_num == expect_number, 'Error: Result is not expect'

def test_get_fib_num_by_bottom_up_at(number, expect_number):
    print('test_get_fib_num_by_bottom_up_at number: ', number)
    fib_num = get_fib_num_by_bottom_up_at(number)
    print('fib_num is', fib_num)
    assert fib_num == expect_number, 'Error: Result is not expect'

# Performance

#@profile
def test_performance_get_fib_num_by_recursive():
    test_get_fib_num_by_recursive_at(2, 1)
    test_get_fib_num_by_recursive_at(5, 5)
    test_get_fib_num_by_recursive_at(10, 55)
    test_get_fib_num_by_recursive_at(20, 6765)
    test_get_fib_num_by_recursive_at(40, 102334155)

#@profile
def test_performance_get_fib_num_by_recursive_tail_call():
    test_get_fib_num_by_recursive_tail_call_at(2, 1)
    test_get_fib_num_by_recursive_tail_call_at(5, 5)
    test_get_fib_num_by_recursive_tail_call_at(10, 55)
    test_get_fib_num_by_recursive_tail_call_at(20, 6765)
    test_get_fib_num_by_recursive_tail_call_at(40, 102334155)

#@profile
def test_performance_get_fib_num_by_memoized():
    test_get_fib_num_by_memoized_at(2, 1)
    test_get_fib_num_by_memoized_at(5, 5)
    test_get_fib_num_by_memoized_at(10, 55)
    test_get_fib_num_by_memoized_at(20, 6765)
    test_get_fib_num_by_memoized_at(40, 102334155)

#@profile
def test_performance_get_fib_num_by_bottom_up():
    test_get_fib_num_by_bottom_up_at(2, 1)
    test_get_fib_num_by_bottom_up_at(5, 5)
    test_get_fib_num_by_bottom_up_at(10, 55)
    test_get_fib_num_by_bottom_up_at(20, 6765)
    test_get_fib_num_by_bottom_up_at(40, 102334155)

# MARK: Main

test_performance_get_fib_num_by_recursive()
test_performance_get_fib_num_by_recursive_tail_call()
test_performance_get_fib_num_by_memoized()
test_performance_get_fib_num_by_bottom_up()