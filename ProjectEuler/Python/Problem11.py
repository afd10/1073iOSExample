list = """08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"""


#list = """26 38 40 67
#95 63 94 39
#97 17 78 78
#20 45 35 14
#"""
preset = list.splitlines()


## Setup the grid
pregrid = []
index =0
for lines in preset:
    pregrid.append(lines.split(' '))


## Operators

def gridtoi(gtigrid):
    final_grid = []
    for line in gtigrid:
        finline = map(lambda x: int(x), line)
        print "fl:> ", finline
        final_grid.append(finline)
    print final_grid
    return final_grid

def gmax(n,m):
    if n > m:
        return n
    return m

def ltor_max(line):
    max = 0
    for i in range (0, len(line)-3):
        subrange = line[i:i+4]
        product = reduce(lambda x,y : x*y , subrange)
        #print subrange, product
        max = gmax(max, product)
    return max

def flip_grid(init_grid):
    endgrid = init_grid[:]
    for row in range(0,len(init_grid)-1):
        for column in (0,len(init_grid[row])-1):
            endgrid[column][row]= init_grid[row][column]
            print "done %d %d" % (row, column)
        print endgrid[row] 
    print endgrid
    print init_grid
    print "ASAS"
    return endgrid

def mirror_grid(init_m):
    final_grid= []
    for row in init_m:
        print "fwd->", row
        row.reverse()
        final_grid.append(row)
        print "rev->", row
    
    return final_grid

def diags(x,y,grid):
    adiag = (grid[x][y],grid[x+1][y+1],grid[x+2][y+2],grid[x+3][y+3])
    return adiag

def max_line(mlgrid):
    max = 0
    for x in mlgrid:
        product = ltor_max(x)
        max = gmax(max, product)
    return max


def max_diag(grid):
    max = 0
    for x in range(0, len(grid)-3):
        for y in range(0, len(grid[x])-3):
            diagset = diags(x,y,grid)
            product = reduce(lambda a,b: a*b, diagset)
    	    max = gmax(max, product)
    return max

def nice_print(xgrid):
    for x in xgrid:
        print x

print "Start"
print pregrid
grid = gridtoi(pregrid)
print "Clean Grid\n\n\n"
print grid
print "\nnp grid"
nice_print(grid)
print "\n**ltor: ",max_line(grid)

print "NextOPS"
flip = flip_grid(grid)


grid = gridtoi(pregrid)
mirror = mirror_grid(grid)

print "\nnp flip"
nice_print(flip)
print "\nnp mirror"
nice_print(mirror)





print "\n**updn: ",max_line(flip)

print "diag: ",max_diag(grid)
#print "flip: ",flip
print  "mirr: ",max_diag(mirror)
