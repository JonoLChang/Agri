length = float(input('Length: '))
width = float(input('Width: '))
length_spac = float(input('Length Spacing: '))
width_spac = float(input('Width Spacing: '))
rows_in_Block = float(input('Rows in L Blocks: '))
widthrowBlock = float(input('Spacing between blocks: '))

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