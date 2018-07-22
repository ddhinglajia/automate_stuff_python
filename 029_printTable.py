tableData = [['apples', 'oranges', 'cherries', 'banana'
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]


dict_table = {0:[], 1:[], 2:[], 3:[]}

for i in tableData: #convert the list to dictionary
    for j in range(len(i)):
        dict_table[j].append(i[j])
        
wordWid = 0
for k, v in dict_table.items():
    length = len(''.join(v))
    if length > wordWid:
        wordWid = length

#print the tableData

for k,v in dict_table.items():
    print(' ' * (wordWid - len(''.join(v)) + ' '.join.(v)))
