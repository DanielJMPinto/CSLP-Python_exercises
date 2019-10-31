import sys

f = open(sys.argv[1], "r")
sum=0
count=0

for x in f:
    sum+=float(x)
    count+=1

print("Sum: " + str(round(sum, 2)))
print("Average: " + str(round(sum/count, 2)))