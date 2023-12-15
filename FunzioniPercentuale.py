# Funzioni relative al calcolo della percentuale
# Autore: F.Cianci
# Data: 15/12/2023 00:40

def percentuale(num,tot):
    '''
    Calcola la percentuale di un numero sul totale
    
    Parametri:
        num -- Numero intero di cui calcolare la percentuale
        tot -- Numero intero rappresentante il totale
        
    Ritorna: La percentuale sul totale ottenuta moltiplicando il totale per il numero espresso in centesimi
    
    '''
    
    return(tot*(num/100))

def formatta(num):
    '''
    Formatta il valore del numero in percentuale con la precisione di una cifra decimale
    
    Parametri:
        num -- Numero intero da formattare
        
    Ritorna: Il valore del numero dato in input in forma percentuale a una cifra decimale
    '''
    return '{:.2f}%'.format(num)
