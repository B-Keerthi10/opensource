N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
for row in matrix:
    print(" ".join(map(str,row[::-1])))
