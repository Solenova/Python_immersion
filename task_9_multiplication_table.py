# Задание №9
# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.


# for i in range(0, 10):
#     for j in range(0, 11):
#         print(i, '*', j , '=', i*j)
#
#     print("")

# ------------2

for i in range(1, 10):
    for j in range(0, 5):
        print(f"{j}* {i} = {i*j}\t", end="")
    print("\t", end="")
    for j in range(6, 10):
        print(f"{j}* {i} = {i*j}\t", end="")
    print()