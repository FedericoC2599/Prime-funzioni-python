# Queste sono le mie prime funzioni in Python
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
    
def ciao():
    '''
    Stampa la stringa ''Ciao sono Federico''
    
    Ritorna: None
    '''
    print('Ciao sono Federico')
    
def mangia_fetta_di_pizza(un_ottavo=True):
    '''
    Valutazione della voracità di Federico
    
    Parametri:
        un_ottavo -- Se True Federico non è vorace
                    Se False Federico sta prendendo una brutta strada
        
    Ritorna: None 
    
    '''
    if un_ottavo:
        print('Sono Federico, sono un ragazzo che mangia sano e la mia fetta di pizza era proporzionata')
    else:
        print('Sono Federico e sto diventando un porco come il mio coinquilino Enrico')

def compito(a,b,c=True):
    '''
    A seconda del valore del parametro c la funzione moltiplica o dividere
    
    Parametri:
        a -- Numero intero
        b -- Numero intero
        c -- Valore booleano, 
            se True moltiplica a e b,
            se False divide a e b
            
    Ritorna: La moltiplicazone o la divisione di a e b in base al parametro c
    '''
    if c:
        print(mul(a,b))
    else:
        print(div(a,b))
