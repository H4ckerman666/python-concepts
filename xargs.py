def my_sum(*numbers):
    result = 0
    for num in numbers:
        result += num
    print(f"The sum is {result}")

#! xargs is used when you don't know the exact number of parameters for your function
my_sum(2, 4, 6)
my_sum(2, 6)
my_sum(2, 10)
my_sum(2)
