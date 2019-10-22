import random

def flips_1(A):
  flips = 0
  for i in range(len(A)):
    for j in range(len(A)):
      if((A[i] > A[j]) and i < j):
        flips = flips + 1
  return flips


def flips_2(A):
  flips = 0
  if len(A) > 1:
    q = len(A)//2
    Low = A[:q]
    High = A[q:]

    flips = flips + flips_2(Low)
    flips = flips + flips_2(High)

    i = 0
    j = 0
    k = 0
    while i < len(Low) and j < len(High):
      if Low[i] < High[j]:
        A[k] = Low[i]
        i = i + 1
      else:
        A[k] = High[j]
        f = i
        while f < len(Low):
          f = f + 1
        flips = flips + (len(Low) - i)
        j = j + 1
      k = k + 1
    
    while i < len(Low):
      A[k] = Low[i]
      i = i + 1
      k = k + 1
    
    while j < len(High):
      A[k] = High[j]
      j = j + 1
      k = k + 1

  return flips


def flips(n):
  A = []
  for i in range(n):
    A.append(i + 1)
  random.shuffle(A)
  return flips_1(A), flips_2(A)

size = 2
print('%-21s%-10s' % ('Size', 'Flips(flips_1, flips_2)'))
while size <= 2**12:
  number_of_flips = flips(size)
  print('%-20d: %s' % (size,number_of_flips))
  size *=2
