
def sum_of_n_nums(num):
    sum = 0
    for i in range(0,num+1):
        sum = sum + i
    return sum

n = int(input("Enter the number :"))
print(sum_of_n_nums(n))