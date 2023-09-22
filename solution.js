function solution(A) {
    let P = Math.max(...A)
    let Q = Math.min(...A)
    return P-Q
}