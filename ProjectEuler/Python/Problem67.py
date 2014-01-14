

def smush(numlist):
    returnlist  = []
    for i in range(0, len(numlist)-1):
        if numlist[i] > numlist[i+1]:
            returnlist.append(numlist[i])
        else:
            returnlist.append(numlist[i+1])
    return returnlist
                

def sumlines(numlist, smashline):
    returnlist = []
    for i in range(0, len(numlist)):
        print numlist[i], "+",smashline[i]
        returnlist.append(int(numlist[i])+int(smashline[i]))
    return returnlist



line = []


with open ("triangle.txt", "r") as myfile:
    pyrdata=myfile.readlines()

for i in range(0,len(pyrdata)):
    print i
    line.append(pyrdata[i].split(' '))
print line

line.reverse()

sum = []
for i in range(0, len(line)-1):
    smushed = smush(line[i])
    line[i+1] = sumlines(line[i+1], smushed)
    print line[i+1]
