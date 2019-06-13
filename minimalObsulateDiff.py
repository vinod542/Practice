numbers = [4,4,2,1,3]
n=sorted(numbers)
print n
l=[]
for i in range(0,len(n)-1):
     for j in range(i,len(n)):
          temp = n[j] - n[i]
          if temp > 0:
               l.append(temp)
f= sorted(l)
print f
s=0
while(s<1):
     for i in range(0,len(n)-1):
          for j in range(i):
               if n[i]-n[j] == f[s]:
                    print n[j],n[i]
     s=s+1
