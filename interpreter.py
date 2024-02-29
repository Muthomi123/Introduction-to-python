def main():
    expression=input("Enter an arithmetic expression:")
    result=get_answer(expression)
    print(result)
#Defining a function that does the calculation on the expression
def get_answer(expression):
    #splitting the expression in 3 diff parts
    x,y,z=expression.split()
    x=int(x)
    z=int(z)
    if y=='+':
        return float(x+z)
    elif y=='-':
        return float(x-z)
    elif y=='*':
        return float(x*z)
    elif y=='/':
        if z==0:
            return("Error:Number cannot divided by zero")
        else:return float(x/z)
    else:
        return("Error:invalid operator")

main()
