# cafe = {
#    'пирожное': {
#     'состав':  ['сахар','белок яичный', 'масло' , 'молоко'],
#     'цена': 5,
#     'количество': 50
#    },
#     'торт': {
#     'состав':  ['мука', 'сахар', 'яйцо', 'сливки', 'масло', 'мёд'],
#     'цена': 2.50 ,
#     'количество': 1000
#     },
#     'маффин': {
#     'состав':  ['яйцо', 'молоко', 'мука', 'сахар', 'масло', 'какао'],
#     'цена': 7,
#     'количество': 700
#
#      },
#     'безе': {
#     'состав':  ['белок яичный', 'сахарная пудра'],
#     'цена': 10,
#     'количество': 300
#     }
#
#     }
# summa = 0
# while True:
#     n = input('название - (состав, цена, количество)')
#     if n == 'q':
#         print("До свидания")
#         break
#     if n == 'купить':
#         count = input("Введите количество")
#         product = input("Введите товар")
#         summa =
#
#
#     else:
#          n = n.split(' - ')
#          if not n[0] in cafe or not n[1] in cafe[n[0]]:
#              print('такого товара нет')
#          else:
#              if isinstance(cafe[n[0]] [n[1]], list):
#                  print(n[0], n[1], ' '.join(cafe[n[0]][n[1]]))
#              else:
#                  print(n[0], cafe[n[0]][n[1]])

# n = input()
# if n == "купить":


    # count = int(input(f"enter count {n}:"))
    # summa +=
#     summa += cafe[n]['цена'] * (count/100)
#     cafe[n][2] -= count
# print(summa)

cafe = {
    "пирожное": [['сахар','белок яичный', 'масло', 'молоко'], 5, 500],
    "торт": [['мука', 'сахар', 'яйцо', 'сливки', 'масло', 'мёд'], 2.62, 1000],
    "маффин": [[ 'яйцо', 'молоко', 'мука', 'сахар', 'масло', 'какао'], 7.34, 700],
    "безе": [['белок яичный', 'сахарная пудра'], 3.51, 300],
    "кекс": [['мука', 'яйцо', 'масло', 'сахар', 'лимон', 'ванилин', 'изюм'], 5.58, 2000]
}
summa = 0
while True:
    # n = input('Введите продукт: ')
    m = input("Что вам нужно посмотреть? ")
    if m == "я хочу купить продукт":
        n = input("Введите продукт:")
        count = int(input("Введите количество в гр.:"))
        if count <= cafe[n][2]:
            summa = count * cafe[n][1]/100
            rest = cafe[n][2] - count
            print(summa)
    if m == "сколько осталось?":
        rest = cafe[n][2] - count
        print(rest)
    if m == "состав":
        print(cafe[n][0])
    if m == "цена":
        print(cafe[n][1])
    if m == "количество":
        print(cafe[n][2])
    if m == "всю информацию":
        print("Состав - ", ','.join((cafe[n][0])),'\n'"цена:", (cafe[n][1]),'\n'"количество:", (cafe[n][2]))
    if m == "выйти":
        print("до свидания")
        break









    # product = {
    #     "melon": [200, 6.22],
    #     "water": [500, 5.52],
    #     "apple": [100, 6.21],
    #     "cheese": [5, 52.52],
    #     'butter': [20, 3.61]
    # }
    # summa = 0
    # while True:
    #     name_product = input("enter name product or exit:")
    #     if name_product == "exit":
    #         break
    #     if name_product in product:
    #         count = int(input(f"enter count {name_product}:"))
    #         if count <= product[name_product][0]:
    #             summa += product[name_product][1] * count
    #             product[name_product][0] -= count
    #         else:
    #             print(f"not enoph {name_product} in shop. We have {product[name_product][0]},but you need {count}")
    #     else:
    #         print(f"no product name {name_product}")
    #
    # print(summa)
