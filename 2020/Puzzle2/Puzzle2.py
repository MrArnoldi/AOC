
f = open("C:\\Users\\larsd\\OneDrive - Danmarks Tekniske Universitet\\DTU\\Programming Projects\\Python\\AOC\\Puzzle2\\puzzle2input.txt").read().split('\n')
result = 0

for i in f:
    split_data = i.split(' ')
    sploitdata = split_data[0].split('-')
    lowerlimit = int(sploitdata[0])
    upperlimit = int(sploitdata[1])
    letter = split_data[1][0]
    password = split_data[2]
    
    #Part 1
    #if lowerlimit <= password.count(letter) <= upperlimit:
        #result = result + 1

    #Part 2
    if password[int(lowerlimit)-1] == letter:
        if password[int(upperlimit)-1] != letter:
            result = result + 1
    elif password[int(lowerlimit)-1] != letter:
        if password[int(upperlimit)-1] == letter:
            result = result + 1
print(result)
