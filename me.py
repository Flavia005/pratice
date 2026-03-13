def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

def power(x, y):
    return x ** y

def modulus(x, y):
    return x % y

def floor_divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x // y

def main():
    print("Simple Calculator")
    print("Operations: +, -, *, /, ** (power), % (modulus), // (floor divide)")
    print("Enter 'quit' to exit")

    while True:
        user_input = input("Enter calculation (e.g., 2 + 3): ")
        if user_input.lower() == 'quit':
            break

        try:
            # Split the input
            parts = user_input.split()
            if len(parts) != 3:
                print("Invalid input. Use format: num1 op num2")
                continue

            num1 = float(parts[0])
            op = parts[1]
            num2 = float(parts[2])

            if op == '+':
                result = add(num1, num2)
            elif op == '-':
                result = subtract(num1, num2)
            elif op == '*':
                result = multiply(num1, num2)
            elif op == '/':
                result = divide(num1, num2)
            elif op == '**':
                result = power(num1, num2)
            elif op == '%':
                result = modulus(num1, num2)
            elif op == '//':
                result = floor_divide(num1, num2)
            else:
                print("Invalid operator")
                continue

            print(f"Result: {result}")

        except ValueError:
            print("Invalid numbers")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()