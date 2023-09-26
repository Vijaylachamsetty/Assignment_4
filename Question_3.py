#Write a Python program to triple all numbers of a given list of integers. Use Python map.
def triple_num(n):
    return n*3
normal_list=[1,2,3,5,6]
triple_list=map(triple_num,normal_list)
print("triple list:\n",list(triple_list))

 #sample input [1,2,3,5,6]
# sample output [3,6,9,15,18]