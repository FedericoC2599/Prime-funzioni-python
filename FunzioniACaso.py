#Funzioni a caso
#Autore: F.Cianci

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
