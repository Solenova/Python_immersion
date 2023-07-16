# 3. Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

#
# MAXLENGTH = 100_000
# num = int(input('Введите положительное число меньшее 100 000: '))
# while num < 0 or num > MAXLENGTH:
#     num = int(input('Введите положительное число меньшее 100 000: '))
#
#
# k = 0
# for i in range(2, num // 2+1):
#     if (num % i == 0):
#         k = k+1
# if (k <= 0):
#     print("Число", num, " простое")
# else:
#     print("Число", num, "составное")

# 2 variant
def prime_num_2(num):
    if num == 2 or num < 2: return  True
    if num % 2 == 0 or num < 2: return False
    for i in range(3, int(num**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

number = int(input("Введите число: "))

if number < 0 or number > 100_000:
    print("Число должно быть положительным и не превышать 100 тыс.")
else:
    print(f"Число простое - {prime_num_2(number)}")