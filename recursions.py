def split (n):
    return n // 10, n % 10
def digit_sum (n): 
    if n < 10:
        return n 
    else:
        all_but_last_digit, last_digit= split(n)
        return digit_sum(all_but_last_digit) + last_digit
# print(digit_sum(12345))
# print(split(12))


# def factorial (n): 
#     if n == 0:
#         return 1 
#     else: 
#         return n * factorial(n-1)
    
# print(factorial(4)) ## 24 

# def factorial_v2 (n):
#     total, k = 1,1 
#     if n == 0:
#         return 1
#     while k <= n:
#         total, k = k * total, k+1
#     return total

# print(factorial_v2(4))

def luhn_sum(n):
    if n < 10: 
        return n
    else: 
        all_but_last_digit, last_digit = split(n)
    return luhn_sum_double(all_but_last_digit) + last_digit

def luhn_sum_double(n): 
    all_but_last_digit, last_digit = split(n)
    luhn_sum_digit = digit_sum(last_digit * 2)
    if n < 10: 
        return luhn_sum_digit
    else: 
        return luhn_sum(all_but_last_digit) + luhn_sum_digit
    
print(luhn_sum(138743))
print(luhn_sum(5105105105105100))
        