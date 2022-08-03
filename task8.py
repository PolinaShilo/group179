# students = []
# with open("students.txt", "r+", encoding="utf-8")as f:
#     # for i in range(10):
#     #     s = f.write(input()+'\n')
#     for i in range(10):
#         s1 = f.readline().rstrip()
#         s1 = s1.split()
#         students.append(s1)
#
#         avg = 0
#         for j in range(len(s1)):
#             summa = 0
#             summa1 = 0
#             if s1[j].isdigit():
#
#                  summa += j
#
#                  print(summa)
#                 # summa += s1[j]
#                 #
#                 # # s1[j]= s1[j+1]
#                 # avg = summa / len(s1)
#                 # print(avg)
#
#
# print(students)
        # st = dict(students)
# В текстовый файл построчно записаны фамилия и имя учащихся класса и его
# оценка за контрольную. Вывести на экран всех учащихся, чья оценка меньше 3
# баллов и посчитать средний балл по классу
students = []
summa = 0
avg = 0
with open("students.txt", "r", encoding="utf-8") as stud:
    for i in range(10):
        s1 = stud.readline().rstrip().split()
        students.append(s1)
    for i in range(len(students)):
        for j in range(len(students[i])):
            students[i][2] = int(students[i][2])
            if students[i][2] < 3:


                print(str(students[i][j]))
                break




        summa+=students[i][2]
        avg = summa/len(students)
    print("Средний балл:",avg)






        # print(summa)
        # print(avg)

# print(students)




