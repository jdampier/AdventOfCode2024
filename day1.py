
left = []
right = []
distances = []

f = open("day1input.txt", "r")
for x in f :
    x = x.split(" ")
    left.append(x[0].strip())
    right.append(x[-1].strip())
    left.sort()
    right.sort()

total = 0
for i, j in zip(left, right) :
    total += (abs(int(i) - int(j)))
print(total)
