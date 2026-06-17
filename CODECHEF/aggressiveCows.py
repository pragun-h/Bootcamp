def canPlace(stalls, cows, distance):
    count = 1
    last = stalls[0]

    for i in range(1, len(stalls)):
        if stalls[i] - last >= distance:
            count += 1
            last = stalls[i]

            if count == cows:
                return True

    return False


t = int(input())

for _ in range(t):
    n, c = map(int, input().split())

    stalls = []
    for _ in range(n):
        stalls.append(int(input()))

    stalls.sort()

    low = 1
    high = stalls[-1] - stalls[0]
    answer = 0

    while low <= high:
        mid = (low + high) // 2

        if canPlace(stalls, c, mid):
            answer = mid
            low = mid + 1
        else:
            high = mid - 1

    print(answer)