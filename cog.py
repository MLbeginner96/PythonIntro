def fibonnaci(n):
        
    start = 1
    next = 1
    final  = next + start
    print(start, next, "final=", final)
    
    for i in range(final, n):
        start = next
        next = final
        final  = next + start
        print(start, next, "final=", final)
        
       
n  = int(input("Enter end: "))
fibonnaci(n)

