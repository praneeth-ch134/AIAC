
# Using a while loop to calculate the sum of first n natural numbers
n = 10  # Define n with the desired value
sum_nums = 0
i = 1
while i <= n:
    sum_nums += i
    i += 1

print("Sum calculated using while loop:", sum_nums)

# Analysis:
# The function sum_of_n_nums uses the mathematical formula n*(n+1)//2 for efficiency.
# The while loop calculates the sum by iteratively adding each number from 1 to n.
# Both approaches give the same result, but the formula is faster for large n.