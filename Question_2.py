#Write a Python program to square the elements of a list using map() function.
def square_num(n):
  return n * n
nums = [1,2,3,4]
print("Original List: ",nums)
result = map(square_num, nums)
print("Square list:\n",list(result))

# sample input [1,2,3,4]
# sample output [1,4,9,16]