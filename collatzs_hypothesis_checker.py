print("""+====================================+
+ Collaz's hypothesis number checker +
+====================================+""")

c0 = int(input('Enter any non-negative and non-zero integer number:'))

steps = 0

while c0 != 1:
    steps += 1
    if c0 % 2 == 0:
        c0 //= 2
    else:
        c0 = 3 * c0 + 1
    print(c0)

print('steps =',steps)
