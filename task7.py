tup = (1,6,7,8,9)
try:
    tup[1] = 2
except TypeError:
    print('Type Error :(')
finally:
    print(tup)
#     for i in tup:

