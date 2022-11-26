#A four-digit integer is given. Find the sum of even digits in it.
var_int=2538
sum_even=0
#Create a variable "var_int" and assign it a four-digit integer value.
a=var_int//1000
b=(var_int//100)%10
c=(var_int//10)%10
e=var_int%10

print((a+b+c+e)-((a%2)*a+(b%2)*b+(c%2)*c+(e%2)*e))
#Create a variable "sum_even" and assign it 0.
print(sum_even) 
#Find the sum of the even digits in the variable "var_int".
