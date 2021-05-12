n = int(input())

ways = [0]*(n+1)

ways[0] = 1
ways[1] = 1
ways[2] = 2

for i in range(3,n+1):
    ways[i] = ways[i-3] + ways[i-2] + ways[i-1]

print(ways[n])

