#A four-digit integer is given. Find the number of even digits in it.
var_int=2456
#Create a variable "var_int" and assign it a four-digit integer value.
print(4-((var_int//1000)%2+((var_int//100)%10)%2+((var_int//10)%10)%2+(var_int%10)%2))
#Print the number of even digits in the variable "var_int".