def get_sum_of_evens(num):
    total = 0
    for i in range(2, num + 1, 2):  
        total += i  
    return total
