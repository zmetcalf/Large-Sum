txt = open("num.txt")
numList = []
total = 0

numList = str(txt.read()).split(" ", 100)

for x in range(100):
    temp = int(numList[x])
    total = total + temp

print total