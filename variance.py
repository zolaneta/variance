import intertools
def factorial(x):
    if x==1:
        return 1
    else:
        result = factorial(x -1)* x
        return result


number = str(raw_input("What is the number? "))

n = []    # number of elements 
for i in number:
    
    if i not in n:
        n.append(i)
        print n
        print i
    else:
        print i, "i is already there"

if len(n)<len(number): # variance with reapeating
    possibilities = len(n) ** len(number)
    print "there is ", possibilities, "pssibble numbers"

else:  # factorial
    print "numbers don't repeat"
    possibilities = factorial(len(number))
    print "there is ", possibilities, "pssibble numbers"


print intertools.combinations(number, len(number))

                              

   
        
    
    

    
        
        

