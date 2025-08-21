
def table_of_number(n):
    i = 1
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")

num = int(input("Enter a number :"))
table_of_number(num)