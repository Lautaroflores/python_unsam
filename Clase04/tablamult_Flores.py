def tablamult():
    
    for num in range(1,10):
        for num2 in range(1,10):
            
            print(f'{num*num2:>3}', end= '')
        print()
    
tablamult()