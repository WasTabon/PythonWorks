_integer = 5
_float = 5.5
_bool = True
print(_integer)
print(_float)
print(_bool)

number1 = int(input("Перше число: "))
number2 = int(input("Друге число: "))

sum = number1 + number2
print("Сума:", sum)

minus = number1 - number2
print("Віднімання:", minus)

mult = number1 * number2
print("Множення:", mult)

if number2 != 0:
    dil = number1 / number2
    print("Ділення:", dil)
else:
    print("Ділення")

high = number1 > number2

if high:
    print("Перше число більше")
else: 
    print("Друге число більше")

numberToStr = str(number1)
print("Число 1 стало стрінгом: ", number1)