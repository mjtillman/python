print("McNugget Problem")

nug = int(input("How many McNuggets would you like to buy? "))

num = nug

i, j, k, l, m = 0, 0, 0, 0, 0
          
if num > 0:
    i = num // 40
    num = nug - (i * 40)

if num >= 20:
    j = num // 20
    num -= j * 20

if num >= 10:
    k = num // 10
    num -= k * 10

if num >= 6:
    l = num // 6
    num -= l * 6

if num >= 4:
    m = num // 4
    num -= m * 4

if num > 0:
    print("You have", num, "nugget(s) left, you can't buy", nug, "nuggets from McDonald's")
else:
    print("For", nug, "nuggets, purchase:")

    if i > 0:
        print(i, "40-piece(s),")

    if j > 0:
        print(j, "20-piece(s),")

    if k > 0:
        print(k, "10-piece(s),")
        
    if l > 0:
        print(l, "6-piece(s),")
        
    if m > 0:
        print(m, "4-piece(s),")
        
