print('***HELLO USER***')
user_num = int(input('Please enter a number: '))
num_list = []

for num in range(1, user_num + 1):
    if user_num % num == 0:
        num_list.append(num)




print(num_list)