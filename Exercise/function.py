# A Funtion is a block of code which only runs when it is called. In python, we do not use curly brackets, we use identation with tabs or spaces


# Create a Function
def sayHello(name='sonu'):
 print(f'hello {name}')

#return value
def getSum(num1, num2) : return num1 + num2
    
    
sum = getSum(3, 4)
print(sum)

 

#A lambda function is a small anonymous function.
# a lambda function can take any number of arguments, but can only have one expression . very similar to JS arrow functions

getSum = lambda num1, num2 : num1 + num2

print(getSum(10, 5))



def mul(a,b): return a*b
multiplication = mul(2,4)
print(multiplication)



substraction = lambda a,b : a-b
print(substraction(4,2))
