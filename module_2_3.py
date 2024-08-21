
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
counter =0
while counter<len(my_list):
    if my_list[counter]<0:
        break
    if my_list[counter]>0:
        print(my_list[counter])
    counter+=1