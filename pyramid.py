import sys

def isPrime(n) : 
  
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
  
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
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

def bestPath(lineNumber,index):#Traversing possible paths recursively
  global numberOfLines
  global lines
  if lineNumber==0:
    if not isPrime(int(lines[0][0])):
      return int(lines[0][0])+bestPath(lineNumber+1,index)[0],lineNumber
  elif lineNumber>=numberOfLines:
    return 0,lineNumber
  else:
    first=int(lines[lineNumber][index])
    second=int(lines[lineNumber][index+1])
    if not isPrime(first) and not isPrime(second):
      x=bestPath(lineNumber+1,index)
      y=bestPath(lineNumber+1,index+1)
      if x and y:
        if int(x[0])>int(y[0]):
          return first+bestPath(lineNumber+1,index)[0],lineNumber
        elif int(x[0])<int(y[0]):
          return second+bestPath(lineNumber+1,index+1)[0],lineNumber
        else:
          return max(first+bestPath(lineNumber+1,index)[0],second+bestPath(lineNumber+1,index+1)[0]),lineNumber
      elif x:
        return first+bestPath(lineNumber+1,index)[0],lineNumber
      elif y:
        return second+bestPath(lineNumber+1,index+1)[0],lineNumber
    elif not isPrime(first):
      return first+bestPath(lineNumber+1,index)[0],lineNumber
    elif not isPrime(second):
      return second+bestPath(lineNumber+1,index+1)[0],lineNumber
    else:
      return 0,lineNumber

print(bestPath(0,0)[0])