def alignStrings(x, y, costInsert, costDelete, costSub):
  nx , ny = (len(x) + 1, len(y) + 1)
  
  S = [[0 for i in range(ny)] for j in range(nx)]
  
  for i in range(nx):
    for j in range(ny):
      if i == 0 or j == 0:
        S[i][j]= max(i,j)
  S[0][0]= 0

  for i in range(1,nx):
    for j in range(1,ny):
      if x[i-1] != y[j-1]:
        S[i][j] = min (
          S[i-1][j-1] + costSub,
          S[i][j-1] + costInsert,
          S[i-1][j] + costDelete,
        )
      else:
        S[i][j] = S[i-1][j-1]

  return S


def extractAlignment(S, x, y, costInsert, costDelete, costSub):
  nx , ny = (len(x) + 1, len(y) + 1)
  P = []
  i,j = (nx - 1,ny -1)

  while (i > 0 or j > 0):
    insert = S[i][j-1]
    delete = S[i-1][j]
    sub = S[i-1][j-1]
    
    if min(insert,delete,sub) == S[i][j]:
      move = ('no-op')
      i,j = (i-1,j-1)
    
    elif min(insert,delete,sub) == insert:
      i,j = (i,j-1)
      move = ('insert')

    elif min(insert,delete,sub) == delete:
      i,j = (i-1,j)
      move = ('delete')
    
    elif min(insert,delete,sub) == sub:
      i,j = (i-1,j-1)
      move = ('sub')
    
    P = [move] + P

  return P
    

def commonSubstrings(x, L, a):
  subStrings = []
  y = ''
  i = 0

  for inst in a:
    if inst == 'no-op':
      y = y + x[i]

    else:
      if len(y) >= L:
        subStrings.append(y)
      y = ''
      
    if inst != 'insert':
      i = i + 1

  if len(y) >= L:
        subStrings.append(y)
  
  return(subStrings) 



x = 'EXPONENTIAL'
y = 'POLYNOMIAL'

S = alignStrings(x, y, 2, 1, 2)

for i in S:
  print(i)


x = open('Song1_Folsom_Prison.txt', 'r').read()
y = open('Song2_Crescent_City_Blues.txt', 'r').read()

A = commonSubstrings(x, 10, extractAlignment(alignStrings(x, y, 1, 1, 1), x, y, 1, 1, 1))

for i in A:
  print (len(i),i)