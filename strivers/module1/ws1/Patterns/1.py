'''
* * *
* * *
* * *
* * *
''' 
def pattern1(n):
    for i in range(0, n):
        for j in range(0,n):
            print("*", end=" ")
        
        print()

N  = int(input())
pattern1(N) 


