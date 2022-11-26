#A four-digit integer is given. Find the sum of odd digits in it.
var_int=2797
sum_even=0
#Create a variable "var_int" and assign it a four-digit integer value
#Create a variable "sum_even" and assign it 0.
a=var_int%10
b=var_int//1000
c=(var_int//100)%10
e=((var_int//10)%10)
sum_even=(a%2)*a+(b%2)*b+(c%2)*c+(e%2)*e
print (sum_even) 
#Find the sum of the odd digits in the variable "var_int".
