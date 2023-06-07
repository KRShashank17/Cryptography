def diffie_hellman(g, p, x, y):
    public_key_A = (g ** x) % p
    public_key_B = (g ** y) % p

    shared_secret_A = (public_key_B ** x) % p
    shared_secret_B = (public_key_A ** y) % p

    assert shared_secret_A == shared_secret_B

    return shared_secret_A

def primecheck(p):
    if p<1:
        return -1
    elif p>1:
        if p==2:
            return 1
        for i in range(2,p):
            if p%i == 0:
                return -1
            return 1
        
g = 5  
p = 24 
x = 6  
y = 15  

if primecheck(p)== -1:
    print("Number is not prime , Enter again")

symmetric_key = diffie_hellman(g, p, x, y)

print("Symmetric Key:", symmetric_key)
