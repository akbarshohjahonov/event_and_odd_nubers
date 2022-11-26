#A four-digit integer is given. Find the sum of odd digits in it.
t=2797
#Create a variable "var_int" and assign it a four-digit integer value
#Create a variable "sum_even" and assign it 0.
a=t%10
b=t//1000
c=(t//100)%10
e=((t//10)%10)
print((a%2)*a+(b%2)*b+(c%2)*c+(e%2)*e)
#Find the sum of the odd digits in the variable "var_int".
