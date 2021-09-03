listnumber = [0, 1, 2, 3, 4, 3, 2, 1, 0]
listpir = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

for i in range(6):
    
    t = 8
    for p in range(9):
        listnumber[4] = 5
        
        if (listnumber[p] == 5 and listnumber[t] == 5):
            
            listpir[p] = "#"
            listpir[t] = "#"
            t -= 1
            continue
        else:
            if(t >= 5):    
                listnumber[p] = listnumber[p] + 1
                listnumber[t] = listnumber[t] + 1
                #listpir[p] = "O"
                #listpir[t] = "O"
                t -= 1       
    print(listpir)    