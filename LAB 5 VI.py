n=int(input("Please input a natural number: "))
for i in range(0,n+1):
    for j in range(n,0,-1):
        print("", end="\t")
    for j in range(1,i+1):
        print(j, end='\t')
    n=n-1    
    print("\r")
    
    
    
