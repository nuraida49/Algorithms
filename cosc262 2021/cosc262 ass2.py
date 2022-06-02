def lcs(s1, s2):
    """maybe not recursive"""
    grid = [[0 for y in range(len(s1) + 1)] for x in range(len(s2) + 1)]
    x = 0
    for x in range(len(grid)):
        y = 0
        while y < len(grid[0]):
            if x == 0 or y == 0:
                grid[x][y] = 0
            elif s1[y - 1] == s2[x - 1]:
                grid[x][y] = grid[x - 1][y - 1] + 1
            else:
                grid[x][y] = max(grid[x][y - 1], grid[x - 1][y])
            y += 1
    a = len(s2)
    b = len(s1)
    longest = ''
    while a > 0 and b > 0:
        if s1[b - 1] == s2[a - 1]:
            longest += s1[b - 1]
            a -= 1
            b -= 1
        elif grid[a][b - 1] > grid[a - 1][b]:
            b -= 1
        else:
            a -= 1
    return longest[::-1]

#s1 = "Look at me, I can fly!"
#s2 = "Look at that, it's a fly"
#print(lcs(s1, s2))

#s1 = "abcdefghijklmnopqrstuvwxyz"
#s2 = "ABCDEFGHIJKLMNOPQRSTUVWXYS"
#print(lcs(s1, s2))

#s1 = "balderdash!"
#s2 = "balderdash!"
#print(lcs(s1, s2))

#s1 = 1500 * 'x'
#s2 = 1500 * 'y'
#print(lcs(s1, s2))

#s1 = "Solidandkeen\nSolidandkeen\nSolidandkeen\n"
#s2 = "Whoisn'tsick\nWhoisn'tsick\nWhoisn'tsick"
#lcs_string = lcs(s1, s2)
#print(lcs_string)
#print(repr(lcs_string))

#def tables(x, y, table, sp1, sp2):
    #"""returns table with x and y dimension"""
    #if x == 0 and y == 0:
        #table[x][y] = 0
    #elif x == 0:
        #table[x][y] = y
    #elif y == 0:
        #table[x][y] = x
    #elif sp1[y - 1] == sp2[x - 1]:
        #table[x][y] = table[x - 1][y - 1]
    #else:
        #table[x][y] = min(table[x - 1][y], table[x][y - 1], table[x - 1][y - 1]) + 1    
    #return table

#def neighbour(x, y, table, lcs):
    #"""returns neighbours"""
    #if x == 0:
        #neighbours = [table[x][y - 1]]
    #elif y == 0:
        #neighbours = [table[x - 1][y]]
    #elif lcs is True:
        #neighbours = [table[x - 1][y], table[x][y - 1]]
    #else:
        #neighbours = [table[x - 1][y], table[x][y - 1], table[x - 1][y - 1]]
    #return neighbours

#def grids(x, y, sp1, sp2):
    #"""returns a grid of the lcs"""
    #lcs1, lcs2 = sp1[y - 1], sp2[x - 1]
    #lcs_grid = [[None for ly in range(len(lcs1) + 1)] for lx in range(len(lcs2) + 1)]
    #for ly in range(len(lcs1) + 1):
        #for lx in range(len(lcs2) + 1):    
            #if lx == 0 or ly == 0:
                #lcs_grid[lx][ly] = 0
            #elif lcs1[ly - 1] == lcs2[lx - 1]:
                #lcs_grid[lx][ly] = lcs_grid[lx - 1][ly - 1] + 1
            #else:
                #lcs_grid[lx][ly] = max(lcs_grid[lx - 1][ly], lcs_grid[lx][ly - 1])   
    #return lcs_grid

#def longest(lcs1, lcs2, lcs_grid):
    #"""returns lcs of string 1 and string 2"""
    #lcs, lcs_x, lcs_y = "", len(lcs2), len(lcs1)
    #while (lcs_x >= 0 or lcs_y >= 0) and not(lcs_x == 0 and lcs_y == 0):
        #neigh = neighbour(lcs_x, lcs_y, lcs_grid, True)
        #if lcs1[lcs_y - 1] == lcs2[lcs_x - 1]:
            #lcs += lcs1[lcs_y - 1]
            #lcs_x -= 1
            #lcs_y -= 1
        #elif lcs_x > 0 and lcs_grid[lcs_x - 1][lcs_y] == max(neigh):
            #lcs_x -= 1
        #elif lcs_y > 0 and lcs_grid[lcs_x][lcs_y - 1] == max(neigh):
            #lcs_y -= 1
    #return lcs

#def edit(lcs1, lcs2, lcs, edits):
    #"""returns an array edits which consists of 3-element tuples"""
    #bra_str1 = brackets(lcs1, lcs[::-1])
    #bra_str2 = brackets(lcs2, lcs[::-1])
    #edits.append(('S', bra_str1, bra_str2)) 
    #return edits

#def brackets(st, lcs):
    #"""returns the count and bracket of strings"""
    #bra_st = ''
    #count = 0
    #for i in range(len(st)):
        #if st[i] in lcs:
            #bra_st += st[i]
            #count += 1
        #elif st[i] not in lcs:
            ##bra_st += "[["           
            #bra_st += st[i]
            ##bra_st += "]]" 
        #else:
            #bra_st += st[i]
    #return bra_st

#def line_edits(s1, s2):
    #"""checks edited lines"""
    #sp1, sp2 = (s1.splitlines(), s2.splitlines())
    #table = [[None for y in range(len(sp1) + 1)] for x in range(len(sp2) + 1)]
    #for y in range(len(sp1) + 1):
        #for x in range(len(sp2) + 1):
            #result = tables(x, y, table, sp1, sp2)
    #x, y, edits = (len(table) - 1, len(table[0]) - 1, [])
    #while x >= 0 and y >= 0 and not (x == 0 and y == 0):
        #neighbours = neighbour(x, y, table, False)
        #if not ((x > 0 and y > 0 and sp2[x - 1] == sp1[y - 1]) and (y > 0 and table[x][y - 1] == min(neighbours)) and (x > 0 and table[x - 1][y] == min(neighbours))):
            #lcs_grid = grids(x, y, sp1, sp2)
            #lcs1, lcs2 = sp1[y - 1], sp2[x - 1]
            #lcs = longest(lcs1, lcs2, lcs_grid)
            #edit(lcs1, lcs2, lcs, edits)
            #x -= 1
            #y -= 1            
        #elif x > 0 and y > 0 and sp2[x - 1] == sp1[y - 1]:
            #edits.append(('C', sp1[y - 1], sp2[x - 1]))
            #x -= 1
            #y -= 1
        #elif y > 0 and table[x][y - 1] == min(neighbours):
            #edits.append(('D', sp1[y - 1], ''))
            #y -= 1
        #elif x > 0 and table[x - 1][y] == min(neighbours):
            #edits.append(('I', '', sp2[x - 1]))
            #x -= 1
        ##else:
            ##lcs_grid = grids(x, y, sp1, sp2)
            ##lcs1, lcs2 = sp1[y - 1], sp2[x - 1]
            ##lcs = longest(lcs1, lcs2, lcs_grid)
            ##edit(lcs1, lcs2, lcs, edits)
            ##x -= 1
            ##y -= 1
    #return edits[::-1]

def get_min(grid, i, j, s1, s2):
    '''Docstrings are annoying in these lil quizzes
    
    Honestly pythons modular list access thing is the most frustarting thing
    in this entire damned cours e : ( '''
    if j >= 1:
        s1str = s1[j-1] 
    else:
        s1str = ''
    if i >= 1:
        s2str = s2[i-1]
    else:
        s2str = ''
    min_ = float('Inf')
    ni, nj = i, j
    tuple_back = ()
    if s1str == s2str:
        return [("C", s1str, s2str), i-1, j-1]
    
    if grid[i-1][j-1] < min_:
        
        min_ = grid[i-1][j-1]
        tuple_back = ("S", s1str, s2str)
        ni = i -1 
        nj = j - 1    
        
    if grid[i][j-1] < min_:
        min_ = grid[i][j-1]
        tuple_back = ("D", s1str, '')
        ni = i
        nj = j-1
  
        
    if grid[i-1][j] < min_:
        min_ = grid[i-1][j]
        tuple_back = ("I", '', s2str)
        ni = i-1
        nj = j
    
    #if grid[i-1][j-1] < min_:
        
        #min_ = grid[i-1][j-1]
        #tuple_back = ("S", s1str, s2str)
        #ni = i -1 
        #nj = j - 1
    
    return [tuple_back, ni, nj]
        
    
    

def bottom_up(lefts, rights): 
    '''yeet'''
    grid = [[-1 for i in range(len(lefts) + 1)] for j in range(len(rights) + 1)]
    for i in range(len(rights)+1):
        for j in range(len(lefts)+1):
            if i == 0 and j == 0:
                grid[i][j] = 0 
            elif j == 0:
                grid[i][j] = i
            elif i == 0:
                grid[i][j] = j 
            elif (lefts[j-1] == rights[i - 1]):
                grid[i][j] = grid[i-1][j - 1]               
            else: 
                grid[i][j] = 1 + (min(grid[i-1][j], grid[i][j-1], grid[i-1][j-1]))
    return grid

    
def checkbase(s1, s2):
    '''I dislike the pylint prick'''
    if len(s1) + len(s2) == 0:
        return ''
    if len(s1) == 0:
        return [('I', '', s2[0])]
    return [('D', s1[0], '')]
    
def line_edits(s1, s2):
    '''Comprises a docstring to appease cosc peeps'''
    lefts, rights = str.splitlines(s1), str.splitlines(s2)
    if s1 == "" or s2 == "":
        return checkbase(lefts, rights)
    
    def backtrack(grid):
        ''' :-( '''
        j, i, output = len(grid[0]) - 1, len(grid) - 1, []
        while i != 0:    
            a, i, j = get_min(grid, i, j, lefts, rights)
            output.append(a)
        return output[::-1]
    return (backtrack(bottom_up(lefts, rights)))



def main():
    s1 = "Line1\nLine2\nLine3\nLine4\n"
    s2 = "Line1\nLine3\nLine4\nLine5\n"
    expected = """('C', 'Line1', 'Line1')
    ('D', 'Line2', '')
    ('C', 'Line3', 'Line3')
    ('C', 'Line4', 'Line4')
    ('I', '', 'Line5')"""
    table = line_edits(s1, s2)
    for row in table:
        print(row)
    print('expected:')
    print(expected)
    print('\n')
    
    s1 = "Line1\nLine2\nLine3\nLine4\n"
    s2 = "Line5\nLine4\nLine3\n"
    expected = """('S', 'Line1', 'Line5')
    ('S', 'Line2', 'Line4')
    ('C', 'Line3', 'Line3')
    ('D', 'Line4', '')"""
    table = line_edits(s1, s2)
    for row in table:
        print(row)
    print('expected:')
    print(expected)
    print('\n')
    
    s1 = ""
    s2 = ""
    table = line_edits(s1, s2)
    for row in table:
        print(row)
    print('\n')
    
    s1 = "Line1\n"
    s2 = ""
    expected = """('D', 'Line1', '')"""
    table = line_edits(s1, s2)
    for row in table:
        print(row)
    print('expected:')
    print(expected)
    print('\n')

    s1 = ""
    s2 = "Line1\n"
    expected = """('I', '', 'Line1')"""
    table = line_edits(s1, s2)
    for row in table:
        print(row)
    print('expected:')
    print(expected)
    print('\n')
    
    s1 = "Line1\nLine3\nLine5\n"
    s2 = "Twaddle\nLine5\n"
    expected = """
    ('D', 'Line1', '')
    ('S', 'Line3', 'Twaddle')
    ('C', 'Line5', 'Line5')"""
    table = line_edits(s1, s2)
    for row in table:
        print(row)
    print(expected)
    print('\n')
    
    
    s1 = "Line1\nLine2\nLine3\nLine4\nLine5\n"
    s2 = "Line3\nLine2\n"
    expected = """
    ('D', 'Line1', '')
    ('D', 'Line2', '')
    ('C', 'Line3', 'Line3')
    ('D', 'Line4', '')
    ('S', 'Line5', 'Line2')"""
    table = line_edits(s1, s2)
    for row in table:
        print(row)
    print(expected)
    print('\n')
    
    s1 = "a\nb\n"
    s2 = "b\na\n"
    table = line_edits(s1, s2)
    for row in table:
        print(row)
    

main()

#s1 = "Line1\nLine2\nLine3\nLine4\n"
#s2 = "Line1\nLine3\nLine4\nLine5\n"
#table = line_edits(s1, s2)
#for row in table:
    #print(row)
    
#s1 = "Line1\nLine2\nLine3\nLine4\n"
#s2 = "Line5\nLine4\nLine3\n"
#table = line_edits(s1, s2)
#for row in table:
    #print(row)
    
#s1 = "Line1\nLine3\nLine5\n"
#s2 = "Twaddle\nLine5\n"
#table = line_edits(s1, s2)
#for row in table:
    #print(row)
    