
valid = 0
not_valid = 0

def passport():
    f = open("C:\\Users\\larsd\\OneDrive - Danmarks Tekniske Universitet\\DTU\\Programming Projects\\Python\\AOC\\Puzzle4\\input.txt").read().split('\n\n')
    f_input = f
    #print(f_input)
    global valid
    global not_valid
    
    #Part 1
#     for i in range(0, len(f)):
#         count = f_input[i].count(':')
#         if count == 8:
#             valid += 1
#         elif count == 7:
#             cid_check = f_input[i].count('cid')
#             if cid_check == 1:
#                 not_valid += 1
#             elif cid_check == 0:
#                 valid += 1
#             else:
#                 print('oof')
#         else:
#             not_valid += 1
#     return valid


# print(passport())

    #Part 2
    for i in range(0, len(f_input)):  # len(f_input)

        count = f_input[i].count(':')
        print(i)
        print(f_input[i])
        print('count start:', count)
        if count == 8:
            index_byr = f_input[i].find('byr')
            index_iyr = f_input[i].find('iyr')
            index_eyr = f_input[i].find('eyr')
            index_hgt = f_input[i].find('hgt')
            index_hcl = f_input[i].find('hcl')
            index_ecl = f_input[i].find('ecl')
            index_pid = f_input[i].find('pid')
            check_byr(index_byr, index_iyr, index_eyr, index_hgt, index_hcl, index_ecl, index_pid, f_input[i])

        elif count == 7:
            if 'cid' in f_input[i]:
                print('not valid cid\n')
                not_valid += 1
            else:
                index_byr = f_input[i].find('byr')
                index_iyr = f_input[i].find('iyr')
                index_eyr = f_input[i].find('eyr')
                index_hgt = f_input[i].find('hgt')
                index_hcl = f_input[i].find('hcl')
                index_ecl = f_input[i].find('ecl')
                index_pid = f_input[i].find('pid')
                check_byr(index_byr, index_iyr, index_eyr, index_hgt, index_hcl, index_ecl, index_pid, f_input[i])
        else:
            print('not valid start count\n')
            not_valid += 1            

    return valid, not_valid, len(f_input)

def check_byr(index_byr, index_iyr, index_eyr, index_hgt, index_hcl, index_ecl, index_pid, f_input):
    global not_valid
    if 1920 <= int(f_input[index_byr + 4: index_byr + 8]) <= 2002:
        print('byr', f_input[index_byr + 4: index_byr + 8])
        check_iyr(index_iyr, index_eyr, index_hgt, index_hcl, index_ecl, index_pid, f_input)
    else:
        print('not valid byr')
        print('byr', f_input[index_byr + 4: index_byr + 8], '\n')
        not_valid += 1        


def check_iyr(index_iyr, index_eyr, index_hgt, index_hcl, index_ecl, index_pid, f_input):
    global not_valid
    if 2010 <= int(f_input[index_iyr + 4: index_iyr + 8]) <= 2020:
        print('iyr', f_input[index_iyr + 4: index_iyr + 8])
        check_eyr(index_eyr, index_hgt, index_hcl, index_ecl, index_pid, f_input)
    else: 
        print('not valid iyr')
        print('iyr', f_input[index_iyr + 4: index_iyr + 8], '\n')
        not_valid += 1        
         


def check_eyr(index_eyr, index_hgt, index_hcl, index_ecl, index_pid, f_input):
    global not_valid
    if 2020 <= int(f_input[index_eyr + 4: index_eyr + 8]) <= 2030:
        print('eyr', f_input[index_eyr + 4: index_eyr + 8])
        check_hgt(index_hgt, index_hcl, index_ecl, index_pid, f_input)
    else: 
        print('not_valid eyr')
        print('eyr', f_input[index_eyr + 4: index_eyr + 8], '\n')
        not_valid += 1        


def check_hgt(index_hgt, index_hcl, index_ecl, index_pid, f_input):
    global not_valid
    if f_input[index_hgt+7] == 'c' or f_input[index_hgt+7] == 'm':
        if f_input[index_hgt + 4: index_hgt + 7].isnumeric():
            if 150 <= int(f_input[index_hgt + 4: index_hgt + 7]) <= 193:
                print('hgt', f_input[index_hgt + 4: index_hgt + 7])
                check_hcl(index_hcl, index_ecl, index_pid, f_input)
            else:
                print('1. not_valid hgt')
                print('hgt', f_input[index_hgt: index_hgt + 7], '\n')
                not_valid += 1                
        else:
            print('2. not_valid hgt')
            print('hgt', f_input[index_hgt: index_hgt + 7], '\n')
            not_valid += 1           
              

    elif f_input[index_hgt + 7] == 'i' or f_input[index_hgt + 7] == 'n':
        print(f_input[index_hgt + 4: index_hgt + 6])
        print(f_input[index_hgt + 4: index_hgt + 6].isnumeric())
        if f_input[index_hgt + 4: index_hgt + 6].isnumeric():
            if 59 <= int(f_input[index_hgt + 4: index_hgt + 6]) <= 76:
                print('hgt', f_input[index_hgt + 4: index_hgt + 6])
                check_hcl(index_hcl, index_ecl, index_pid, f_input)
            else: 
                print('3. not_valid hgt')
                print('hgt', f_input[index_hgt: index_hgt + 6], '\n')
                not_valid += 1                                  
                  
        else: 
            print('4. not_valid hgt')
            print('hgt', f_input[index_hgt: index_hgt + 6], '\n')
            not_valid += 1           
              
    else: 
        print('error!!')
          


def check_hcl(index_hcl, index_ecl, index_pid, f_input):
    f_hcl = f_input
    global not_valid
    f_hcl = f_input[index_hcl:index_hcl + 13]
    f_hcl = f_hcl.split(' ')[0]
    f_hcl = f_hcl.split('\n')[0]
    print(f_hcl)
    print(len(f_hcl))
    count = f_hcl.count('#')
    print('count hcl', count)
    if count != 1:
        print('not valid hcl no #\n')
    else:
        if len(f_hcl) != 11:        
            print('not valid hcl\n')
            not_valid += 1
        else:
            print('hcl OK')
            check_ecl(index_ecl, index_pid, f_input)


def check_ecl(index_ecl, index_pid, f_input):
    global not_valid
    eye_color_code = 'amb blu brn gry grn hzl oth'
    count = eye_color_code.count(f_input[index_ecl + 4: index_ecl + 7])
    print('ecl count', count)
    if count == 1:
        print('ecl OK')
        check_pid(index_pid, f_input)
    else: 
        print('not valid ecl\n')
        not_valid += 1
          


def check_pid(index_pid, f_input):
    global valid
    global not_valid
    f_pid = f_input[index_pid + 4: index_pid + 14]
    f_pid = f_pid.split(' ')[0]
    f_pid = f_pid.split('\n')[0]
    print(f_pid)
    print(len(f_pid))
    print(f_pid.isnumeric())
    if f_input[index_pid + 4: index_pid + 13].isnumeric():
        print('valid\n')
        valid += 1
    else:        
        print('not valid pid\n')
        not_valid += 1        
          

print(passport())
