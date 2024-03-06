#Function that converts camel case to snake case.
def camel_to_snake(camel_case):
    snake_case=''
    for char in camel_case:
        if char.isupper():
            snake_case += '_' + char.lower() #adds an under score if current char is upper and makes it a lower case.
        else:
            snake_case += char
        return snake_case.lstrip("_") #returns snake_case with striped underscore in the beginning or the end.
def main():
    camel_case_input = input("Enter a variable name in camel case: ")

    snake_case_output = ''
    for index, char in enumerate(camel_case_input): #Enumerate helps in keeping track of the index
        if char.isupper() and index != 0: #if character is upper and not the first character
            snake_case_output += '_' + char.lower()
        else:
            snake_case_output += char

    print(snake_case_output)
main()