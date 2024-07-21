first = input("Введите первое число: ")
print(first)
second = input("Введите второе число: ")
print(second)
third = input("Введите третее число: ")
print(third)
if first == second and first == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)


