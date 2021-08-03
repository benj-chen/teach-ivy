
some_str = "benjamin chen"
print("The first character is",some_str[0])
nums = list(map(int,input("Enter some numbers ").split()))
print(nums)
print("The first number is", nums[0])
print("The second number is",nums[1])
print("The third number is", nums[2])
# to get the first number you use nums[0] because Python
# uses "zero-indexing"
# very few languages use one-indexing
# meaning that the first number is nums[1]
# (the only one that I can think of is maybe PHP or SQL, probably)

# circle parentheses () are used to call functions ie print, and to
# put in paramters to these functions
#, used to make objects (you don't know what that is yet) like range
#, also used like they are in math with order of operations
# ie (5+3)*2 -> 16 is different from 5+3*2 -> 11

# square parentheses [] aka brackes are used to access elements in a
# collection ie lists, tuples, dicts, strings etc
# also used to make lists

# I want to get the sum of all of the numbers in nums
size = len(nums)
sum_of_list = 0
# sum_of_list = sum_of_list + 5
for index in range(0,size):
    sum_of_list = sum_of_list + nums[index]
print("the sum is",sum_of_list)

size = len(nums)
max_in_list = 0
for index in range(0,size):
    if ():
        # something
print("the max is",max_in_list)