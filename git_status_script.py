import os

def readLine(line):
    lineArray = line.split(",");
    return extractInfo(lineArray)

def extractInfo(lineArray):
    info = []
    for entry in lineArray:
        info.append(getInt(entry))
    if(len(lineArray) is 2):
        info.append(0)
    return info

def getInt(totalString):
    string = ""
    for char in totalString:
        if char.isdigit():
            string = string + char
    return int(string)

def informationStatus(information):
    fc, ic, dc = 0, 0, 0
    for f, i, d in information:
        fc+=f
        ic+=i
        dc+=d
    size = len(information)
    return ("Total commits: " + str(size) + "\nSum of changed files: " + str(fc) + "\nTotal insertions: " + str(ic)+ "\nTotal deletions: " + str(dc))

information = []
os.system("git log --stat > gitOutput.txt")
os.system("grep -E 'insertions' gitOutput.txt > gitStatus.txt")
os.system("rm -f gitOutput.txt")

f = open('gitStatus.txt')
for line in iter(f):
    information.append(readLine(line))
f.close()

print(informationStatus(information))

os.system("rm -f gitStatus.txt")
