# Note: the easier way involves a mathematical formula which I don't fully understand, 
# but since the objectives were to use 

print("""+===========================+
+ Pyramid height calculator +
+===========================+""")

blocks = int(input())

height = 1
max_blocks = 1
curr_blocks = 0
pyramid = '\n'

# while there are enough blocks to fill the row
while blocks:
    # we remove a block from the pile
    blocks-=1
    # and place it on the pyramid
    curr_blocks+=1
    pyramid += '[]'
    # if we've placed the max um of blocks we can in the row
    if max_blocks == curr_blocks:
        # reset block count
        curr_blocks = 0
        # increase the max number of blocks allowed in a row
        max_blocks+=1
        if blocks >= max_blocks:
            # begin another row
            height+=1
            pyramid +='\n'
            continue
        else:
            break

print('The height of the pyramid:',height,pyramid)
print('\nBlocks left: ','[]'*blocks,sep='')
