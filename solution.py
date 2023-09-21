def solution(A):
    if not A:
        return 0
    
    P = max(A)
    Q = min(A)

    return P - Q