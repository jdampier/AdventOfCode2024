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

simScores = []
for i in left :
    multVar = 0
    for j in right :
        if (int(i) == int(j)) :
            multVar += 1
    simScores.append(multVar * int(i))

total = 0
for i in range(len(simScores)):
    total += simScores[i]

print(total)
