
# def h_index(A):
#   i = 0
#   while i < len(A):
#     print(A[i], i)
#     if A[i] > i:
#       i = i + 1
#     else:
#       return i
def h_index(A):
  h = 0
  if len(A) > 1:
    q = len(A)//2
    left = A[:q]
    right = A[q:]
    
    print(left,right)
    h += h_index(left)
    h += h_index(right)

    flag = True
    i = 0

    while flag == True and i < len(left):
      if right[i] >= ((len(left) + i) + 1):
        i += 1
        h = (len(left) + i)
      else:
        flag = False
  
  return h


    
    






    
    

A = [9,8,8,3,3,1,1,1,1,1,1]
print(h_index(A))