# Multiples of 3 and 5
# If we list all the natural numbers below 10 that are multiples
# of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.


def sum_of_multiples(num):
    if num < 1:
        return 'Number must be positive'
    elif type(num) != int:
        return 'Input must be Integer'
    num_sum = 0
    for i in range(num):
        if i % 3 == 0 or i % 5 == 0:
            num_sum += i
    return num_sum


print(sum_of_multiples(1000))
