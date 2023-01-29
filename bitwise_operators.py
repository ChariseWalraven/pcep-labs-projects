# Note: I have no idea what's going on here

a = 1
b = 0
c = a & b
d = a | b
e = a ^ b

# print(c,d,e)
# print( c + d + e)

z = 10
y = 0

x = y < z and z > y or y > z and z < y # x is True because the order is just left to right
# so kind of like (y < z and z > y) or (y > z and z < y)
# since the first group evaluates to True, the whole statement is True

print(x)