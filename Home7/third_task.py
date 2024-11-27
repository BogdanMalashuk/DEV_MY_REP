my_list = ['chocolate', 'abccba', 'car', 'шалаш', 'dog', 'cat', 'boob']
print("Input list:")
print(my_list)

result_list = list(filter(lambda x: x == x[::-1], my_list))
print("Result list:")
print(result_list)
