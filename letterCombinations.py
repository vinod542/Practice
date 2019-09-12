def printWordsUtil(l, curr, output, n):
  if(curr == n):
    s = ' '
    print s.join(output)
    return
  for i in range(len(hashT[l[curr]])):
    output.append(hashT[l[curr]][i]) 
    printWordsUtil(l, curr + 1, output, n)
    output.pop() 
    if(l[curr] == 0 or l[curr] == 1):
      return
          
def printW(l,n):
     printWordsUtil(l, 0, [], n)
    
def letterCombinations(digits):
  #if digits < 11:
   # return
  #else:
    hashT = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
    l=[]
    while digits > 11:
      n = digits%10
      l.append(n)
      d = d/10
    n=len(l)
    printW(l,n)
