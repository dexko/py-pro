#1
def minpositive(a):
    A = set(a)
    ans = 1
    while ans in A:
        ans += 1
        return ans
#2
def max_gap(x):
    max_gap_length = 0
    current_gap_length = 0
    for i in range(x.bit_length()):
        if x & (1 << i):
            if current_gap_length > max_gap_length:
                max_gap_length = current_gap_length
            current_gap_length = 0
         else:
            current_gap_length += 1
    if current_gap_length > max_gap_length:
        max_gap_length = current_gap_length
    return max_gap_length

#3
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
K = 4
def solution(A, K):
   if K == 0 or len(A)/K ==0:
      return A
   if K > len(A):
      K = K/len(A)
   A = A[len(A)-K:len(A)] + (A[0:len(A)-K])
   return A
