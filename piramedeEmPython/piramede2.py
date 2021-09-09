listnumber = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
listpir = list(27 * "-")



for i in range(15):
    
    t = 26
    for p in range(15):
        
        listnumber[13] = 15
        if (listnumber[p] == 15 and listnumber[t] == 15):
            
            listpir[p] = "#"
            listpir[t] = "#"
            t -= 1
            continue
        else:
            if(t >= 15):    
                
                listnumber[p] = listnumber[p] + 1
                listnumber[t] = listnumber[t] + 1
                #listpir[p] = "O"
                #listpir[t] = "O"
                t -= 1 
    if(listnumber[12] < 15  and listnumber[14] < 15):
        listnumber[12] = listnumber[12] + 1
        listnumber[14] = listnumber[14] + 1
    final = ''                  
    print(final.join(listpir)) 
    #print(listnumber)     
