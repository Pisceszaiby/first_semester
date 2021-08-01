n=int(input("Enter number of rows: "))
spaces=2*n - 2   
for row in range(0, n):     
    for column in range(0, spaces): 
        print(end=" ")       
    spaces-=1
    for column in range(0, row+1):  
        print("* ", end="") 
          
    print("\r") 
