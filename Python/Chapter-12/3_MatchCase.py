def calculator(a, b, operation):
    match operation:
        case "add":
            return a + b
        case "subtract":
            return a - b
        case "multiply":
            return a * b
        case "divide":
            if b != 0:
                return a / b
            else:
                return "Error: Division by zero"
        case _: # default case
            return "Error: Invalid operation"

result = calculator(10, 5, "add")
print(result)
result = calculator(10, 5, "divide")
print(result)