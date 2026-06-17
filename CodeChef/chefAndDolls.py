t = int(input())

for _ in range(t):
    n = int(input())
    dolls = list(map(int, input().split()))

    ans = 0

    for doll in dolls:
        ans ^= doll

    print(ans)
