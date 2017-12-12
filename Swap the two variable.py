'''
Prog02: Can you think of a way to swap the values
of two variables that does not need a third variable
as a temporary storage? In the code block below, try
to implement the swapping of the values of a and b
without using a third variable. To help you out, the
first step to do this is already given. You just need
to add two more lines of code.
'''
# a=1, b=2
a = int(input("enter value for a: "))
b = int(input("enter value for b: "))

print( "a =", a, "and b =", b )
a += b      #a=1, b=2, a=1+2= 3 (a=3, b=2)

# add two more lines of code here to cause swapping of a and b
b = a - b   #b = 3-2= 1 (a=3, b=1)
a -= b      #a = 3-1= 2 (a=2, b=1)
print( "a =", a, "and b =", b )
