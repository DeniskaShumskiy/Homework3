for i in range(1, 101): # Проходимся i с 1 до 100
    if i % 3 == 0 and i % 5 == 0: # Если кратно 3 и 5 одновременно
        print("FizzBuzz", end=" ") # Выводит FizzBuzz, end=" " - определяет
        # символ, который будет добавлен в конце вывода строки
    elif i % 3 == 0:
        print("Fizz", end=" ") # Если кратно только 3, выводит Fizz
    elif i % 5 == 0:
        print("Buzz", end=" ") # Если кратно только 5, выводит Buzz
    else:
        print(i, end=" ") # В цикле for, else выполняется в любом случае в конце и
        # выводит i и end - символ, который добавляется в конце вывода строки.

