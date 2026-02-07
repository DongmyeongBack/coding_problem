import sys
import math

input = sys.stdin.readline

def solve():
    N, M = map(int, input().split())
    
    jewels = []
    for _ in range(M):
        jewels.append(int(input()))

    left = 1
    right = max(jewels)
    ans = right

    while left <= right:
        mid = (left + right) // 2
        people_needed = 0
        for jewel in jewels:
            people_needed += math.ceil(jewel / mid)
        
        if people_needed > N:
            left = mid + 1
        else:
            ans = mid
            right = mid - 1
            
    print(ans)

if __name__ == "__main__":
    solve()