print("McNugget Problem")

nug = int(input("How many McNuggets would you like to buy? "))

i, j, k, l, m = 0, 0, 0, 0, 0
          
if nug // 40 > 0:
    i = nug // 40

if nug // 20 > 0:
    j = nug // 20

if nug // 10 > 0:
    k = nug // 10

if nug // 6 > 0:
    l = nug // 6

if nug // 4 > 0:
    m = nug // 4


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
        
