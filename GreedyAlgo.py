def lemonade(arr):
    
    n_5 = 0
    n_10 = 0

    
    for i in arr:
        if i ==5:
            n_5+=1
            continue
            
        elif i==10 :
            if n_5>=1:
                n_5-=1
                n_10+=1
                continue
            else:
                return False
            
        elif i==20:
            
            if n_10 >= 1 and n_5 >= 1:
                n_10 -= 1
                n_5 -= 1
                
                continue
                
            elif n_10==0 and n_5>=3:
                n_5-=3
                continue
                        
            else:
                return False
                

    
    return True


print(lemonade([5,5,10,10,5,10,5,20]))