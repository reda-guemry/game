



#grille 6*6 of 0 
grill = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0],
] 

conditions = [
    [3 , 2],
    [1 , 4]
]
    


for y in range(grill.__len__()) :
    for x in range(grill[y].__len__()) :
        if (y , x) in conditions :
            continue 
        if y == 0 or x == 0 : 
            grill[y][x] = 1
        

# print (grill)       

for y in range(grill.__len__()) :
    
    if y == 0 : continue
    
    for x in range(grill[y].__len__()) :
                
        if x == 0 : continue
        
        
        if [y , x] in conditions : continue 
        
        grill[y][x] =  grill[y-1][x] + grill[y][x-1] 


print (grill) 

print (grill[5][5] )







