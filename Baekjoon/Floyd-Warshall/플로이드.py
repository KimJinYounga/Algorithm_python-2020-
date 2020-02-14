n = int(input())
m = int(input())
bus_cost = [[100001 for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    start, end, cost = map(int, input().split())
    bus_cost[start][end] = min(cost, bus_cost[start][end])

for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            if j==k:
                bus_cost[j][k]=0
            else:
                bus_cost[j][k] = min(bus_cost[j][i]+bus_cost[i][k], bus_cost[j][k])

for i in bus_cost[1:]:
    for j in i[1:]:
        if j==100001:
            print(0, end=" ")
        else:
            print(j, end=" ")
    print()