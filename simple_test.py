def solution(A):
    A = list(set(A))
    A.sort()
    print(A)
    n = 1
    for i in range(len(A)):
        if A[i] > n:
            return n
        if A[i] > 0:
            n += 1
    return n

#A = [1, 3, 6, 4, 1, 2]
#A = [1, 3, 6, 4, 1, 2, 5]
#A = [1, 2, 3]
A = [-1, -3, 0, 1, 2]
solution(A)