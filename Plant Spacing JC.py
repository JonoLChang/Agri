#set up virtual environment and mathplotlib to graph planting area
"""
parameters = {
    "length" : float(input('Length of Planing Area: ')),
    "width" : float(input('Width of Planting Area: ')),
    "spacingWithinRows" : float(input('Spacing within rows: ')),
    "spacingBetweenRows" : float(input('Spacing between rows: ')),
    #"rowsPerBlock" : float(input('Number of Rows per Planting Block: ')),
    "numberOfBlocks" : float(input('Number of blocks:  (Type 0 if not using planting blocks within the planting area)')),
    "spacingBetweenBlocks" : float(input('Spacing between blocks: ')),
    #"offsetFromAreaBoundary" : float(input('Offset from Area Boundary: '))
}
"""

print('Use consistent units i.e. ft, in, metres, etc.')
length = float(input('Length of Planing Area: '))
width = float(input('Width of Planting Area: '))
spacingWithinRows = float(input('Spacing within rows: '))
spacingBetweenRows = float(input('Spacing between rows: '))
#rowsPerBlock = float(input('Number of Rows per Planting Block: '))
numberOfBlocks = float(input('Number of blocks:  (Type 0 if not using planting blocks within the planting area or using blocks throughout)'))
spacingBetweenBlocks = float(input('Spacing between blocks: '))
#orientationOfBlocks = float(input('Orientation of Blocks: (Type L - lengthways; W - Widthways) ')) #Code should produce results for both orientations
#offsetFromAreaBoundary = float(input('Offset from Area Boundary: '))

# Calculate number of blocks
if numberOfBlocks == 0:
    if orientationOfBlocks == 'L':
        numberOfBlocks = length/spacingBetweenBlocks


"""
numberRows= float((length/length_spac)) #Find the number of Rows
width_in_block= (rows_in_Block*length_spac)  #Find the width of soil Block
sum = 0
blocks = 0
sum1=0
w=0
while sum1<=length:
    sum = sum + length_spac
    w=w+1
    if((sum%width_in_block)==0):
        blocks=blocks+1
        sum1=sum+widthrowBlock

z=(length)-(widthrowBlock*(blocks-length_spac)) #Find the remaining space

numberLRows = z/length_spac

print(f'Number of blocks: {blocks-length_spac}')
print(f'W: {w}')
print(f'Sum: {sum1}')
print(f'Number of rows: {numberLRows}')
"""