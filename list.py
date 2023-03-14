nums = list(range(21))
print(f"nums: {nums}")
even_numbers = nums[::2]
print(f"even_numbers: {even_numbers}")
odd_numbers = nums[1::2]
print(f"odd_numbers: {odd_numbers}")
print("\n ---------------------------------------------------------------- \n")

print("Unzip Lists")
first_number, second_number, *other_nums = nums
print("first_number: ", first_number)
print("second_number: ", second_number)
first_number, *other_nums, last_number = nums
print("first_number: ", first_number)
print("second_number: ", last_number)
print("\n ---------------------------------------------------------------- \n")

print("Filter")
if 11 in nums:
    print("index: ", nums.index(11))
print("\n ---------------------------------------------------------------- \n")

print("Order List")
#! sorted return a new list, sort not
new_list = sorted(nums, reverse=True)
print("new_list: ", new_list)
nums.sort(reverse=True)
names = [
    ["Joss", 16],
    ["Edwards", 67],
    ["John", 24]
]


def new_order(e):
    return e[1]


print(names)
print(sorted(names, key=new_order, reverse=False))
print(sorted(names, key=new_order, reverse=True))
names.sort(key=lambda x: x[1], reverse=False)
print(names)
print("\n ---------------------------------------------------------------- \n")
print("Comprehension List")
print(f"Numbers: {[x[1] for x in names]}")
print(f"Numbers with map : {list(map(lambda x: x[1],names))}")
print(f"Numbers greater than 20 : {[x for x in names if x[1] > 20]}")
print(
    f"Numbers greater than 20 with filter : {list(filter(lambda x: x[1] if x[1]>20 else None,names))}")
print("\n ---------------------------------------------------------------- \n")
