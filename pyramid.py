import sys

def isPrime(n): 
    if n <= 1: 
        return False
    if n <= 3: 
        return True
    if n % 2 == 0 or n % 3 == 0: 
        return False
    i = 5
    while i*i <= n: 
        if n % i == 0 or n % (i + 2) == 0: 
            return False
        i = i + 6
    return True

if len(sys.argv)!=2:
  print("Please specify input file")
  exit()
inputFile=sys.argv[1]
with open(inputFile,'r') as f:
  content=f.readlines()
content=[x.strip() for x in content]

lines=[]
for line in content:
  lines.append(line.split(' '))
numberOfLines=len(lines)

table=[[0]*len(lines) for j in range(len(lines))]

#make prime numbers -inf
for i in range(len(lines)):
  for j in range(len(lines[i])):
    if isPrime(int(lines[i][j])):
      table[i][j]=-99999999
    else:
      table[i][j]=int(lines[i][j])

for i in range(1,len(lines)):
  for j in range(i+1):
    if j==0:
      table[i][j]=table[i][j]+table[i-1][j]
    elif j==i:
      table[i][j]=table[i][j]+table[i-1][j-1]
    else:
      table[i][j]=max(table[i][j]+table[i-1][j-1],table[i][j]+table[i-1][j])
found=False
l=[]
for i in range(len(lines)-1,-1,-1):
  for j in range(i,-1,-1):
    if table[i][j]>0:
      found=True
      l.append(table[i][j])
  if found:
    break

print(max(l))