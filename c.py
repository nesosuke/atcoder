num_city, num_road = map(int, input().split())
roads = []
path = num_city  # 自都市 -> 自都市
paths_all = int((num_city * (num_city-1))/2)  # nC2
for i in range(num_road):
    roads.append(list(input().split()))

# for i in range(num_road):
#     if roads[i][0] != roads[i][1]:

# for start in range(1, num_city+1):
#     for dist in range(start, num_city+1):
#         for i in range(num_road):
#             if start == roads[i][0] and dist == roads[i][1]:
#                 path += 1

city_available = [[]*num_city]
for start in range(1, num_city+1):
    city_available[start].append(start)
    for i in range(num_road):
        if roads[i][0] == start :
            city_available.append(roads[i][1])
    print(len(city_available[start]))
