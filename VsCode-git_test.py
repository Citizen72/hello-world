


def main():
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the Second number: "))
    multiply(number1, number2)
    
    c = number1 * number2
    print(c)

    
def multiply(a, b):
    answer = a * b
    return answer
    
main()