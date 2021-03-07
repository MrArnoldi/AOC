f = open("C:\\Users\\larsd\\OneDrive - Danmarks Tekniske Universitet\\DTU\\Programming Projects\\Python\\AOC\\Puzzle3\\input.txt").read().split('\n')

#Part 1
# x = 0
# y = 0
# result = 0
# while y < len(f):
#     if f[y][x] == '#':
#         result += 1
#     y += 1
#     x += 3
#     x = x % len(f[0])
# print(result)

#Part 2
result_placeholder = 0
result = 1
trail = [[1,1], [3,1], [5,1], [7,1], [1,2]]
for z in range(5): 
    y = trail[z][1]
    x = trail[z][0]
    result_placeholder = 0
    while y < len(f):
        if f[y][x] == '#':
            result_placeholder += 1
        y += trail[z][1]        
        x += trail[z][0]
        x = x % len(f[0])
    result = result * result_placeholder
print(result)
