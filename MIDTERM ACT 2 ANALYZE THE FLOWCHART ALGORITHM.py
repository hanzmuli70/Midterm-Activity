my_list = []

for g in range(1,10):
    my_list.append(g)
    
print('Original list:', my_list)
print('Lenght of list:', len(my_list))

b = 0  

for a in range(len(my_list)):
    if b == len(my_list):
        break
    else: 
        if my_list[a] not in my_list[:a]:
            b = b + 1
        else:
            del my_list[a]
            break

print('The list with unique elements only.')
print(my_list)