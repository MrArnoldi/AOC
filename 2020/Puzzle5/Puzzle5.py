import numpy as np
f = open("C:\\Users\\larsd\\OneDrive - Danmarks Tekniske Universitet\\DTU\\Programming Projects\\Python\\AOC\\Puzzle5\\input.txt").read().split('\n')
boarding_passes = np.array(f)
Row = np.arange(0, 127)
Seats = np.arange(0, 1023)
Column = np.arange(0, 7)

#seat_ID = np.delete(seat_ID, 2)
print(0,len(boarding_passes))
for i in range(len(boarding_passes)):
    #print(len(seat_ID))
    #print(Row)
    otherrow = np.arange(0, 127)
    othercolumn = np.arange(0, 7)
    
    row_length = len(otherrow)
    row_half_length = int(row_length/2)
    column_length = len(othercolumn)
    column_half_length = int(column_length/2)

    for j in range(0,9):
        #print(length)
        #print(half_length)

        if boarding_passes[i][j] == 'F':
            otherrow = otherrow[0: row_half_length]
            Row = np.delete(Row, otherrow)
            #print(seat_ID)
        elif boarding_passes[i][j] == 'B':
            otherrow = otherrow[row_half_length: row_length]
            Row = np.delete(Row, otherrow)
            #print(seat_ID)
        elif boarding_passes[i][j] == 'R':
            othercolumn = othercolumn[0: column_half_length]
            Column = np.delete(Column, othercolumn)
        elif boarding_passes[i][j] == 'L':
            othercolumn = othercolumn[column_half_length: column_length]
            Column = np.delete(Column, othercolumn)
        else:
            print('error')     

print(Row, Column)
