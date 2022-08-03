# Создайте словарь из строки ' An apple a day keeps the doctor away' следующим
# образом: в качестве ключей возьмите символы строки, а значениями пусть будут
# числа, соответствующие количеству вхождений данной буквы в строку.

s = 'An apple a day keeps the doctor away'
s1 = ""
d = {}
for i in s:
     if i != " ":
         s1+=i
         d = {i: s1.count(i) for i in s1}
print(d)



# print(s)
# print(s1)
# print(d)