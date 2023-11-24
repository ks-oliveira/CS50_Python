expression = input("Expression: ")

x, y, z = expression.split(" ")
x = float(x)
z = float(z)

match y:
    case "+":
        operation = x + z
    case  "-":
        operation = x - z
    case  "*":
        operation = x * z
    case  "/":
        operation = x / z

print(f"{operation}")