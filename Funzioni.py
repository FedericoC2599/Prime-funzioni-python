# Queste sono funzioni di aritmetica di base
# Autore: F.Cianci

def sum(a, b):
    '''
    Somma due numeri interi
    
    Parametri:
        a -- Numero intero 
        b -- Numero intero
        
    Ritorna: Somma di a e b
    '''
    return a+b


def sub(a,b):
    '''
    Sottrazione due numeri interi
    
    Parametri:
        a -- Numero intero
        b -- Numero intero
        
    Ritorna: Sottrazione a e b
    '''
    
    return a-b


    
def mul(a,b):
    '''
    Moltiplicazione due numeri interi
    
    Parametri:
        a -- Numero intero
        b -- Numero intero
        
    Ritorna: Moltiplicazione a e b
    '''
    return a*b

def div(a,b):
    '''
    Divisione due numeri interi
    
    Parametri:
        a -- Numero intero
        b -- Numero intero >0
        
    Ritorna: Divisione a e b
    '''
    if b>0:
        return a/b
    else:
        raise ValueError("Non puoi dividere per zero")
    
