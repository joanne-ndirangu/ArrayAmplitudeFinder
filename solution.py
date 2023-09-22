def solution(A):
    if A == None or len(A) <= 1:
        return 0

    P = max(A)
    Q = min(A)

    return P - Q