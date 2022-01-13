def solution(n, s):
    if s == 1:
        return [-1]
    answer = []
    mid = s // 2
    if s % 2 == 0:
        answer = [mid, mid]
    else:
        answer = [mid, mid+1]
    return answer

n = 2
s = 165
answer = solution(n, s)
print(answer)
