##x = 25
##x1 = x % 10
##x2 = x // 10    # x2 = int(x / 10)
##print(f"{x1} + {x2} = {x1 + x2}")


x = 100
x1 = x % 10
x2 = x // 10 % 10         # x2 = x % 100 // 10
x3 = x // 100

print(f"{x1} + {x2} + {x3} = {x1 + x2 + x3}")