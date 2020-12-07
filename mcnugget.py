print("McNugget Problem")

nug = int(input("How many McNuggets would you like to buy? "))

num = nug

i, j, k, l, m = 0, 0, 0, 0, 0

sols = []
          
if num > 40:
    i = num // 40
    num = nug - (i * 40)
    print(i, "40-piece,")

if num > 20:
    j = i % 20
    num -= j * 20
    print(j, "20-piece,")

if num > 10:
    k = j % 10
    num -= k * 10
    print(k, "10-piece,")

if num > 6:
    l = k % 6
    num -= l * 6
    print(l, "6-piece,")

if num > 4:
    m = l % 4
    num -= m * 4
    print(m, "4-piece,")

if num > 0:
    print("You have", num, "nugget(s) left, you can't buy", nug, "nuggets from McDonald's")
    
    
    
