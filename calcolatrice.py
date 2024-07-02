def somma(a: int | float, b: int | float) -> int | float:
    return a + b

def divisione(num: int | float, den: int | float) -> float:
    if den == 0:
        raise ValueError
    return num / den

# Aggiungi le funzioni moltiplicazione e sottrazione
def somma(a: int | float, b: int | float) -> int | float:
    return a + b

def divisione(num: int | float, den: int | float) -> float:
    if den == 0:
        raise ValueError("Errore: divisione per zero")
    return num / den

def moltiplicazione(a: int | float, b: int | float) -> int | float:
    return a * b

def sottrazione(a: int | float, b: int | float) -> int | float:
    return a - b

        #Esempi di utilizzo
print(somma(10, 5))             # Output: 15
print(divisione(10, 2))         # Output: 5.0
print(moltiplicazione(10, 5))   # Output: 50
print(sottrazione(10, 5))       # Output: 5


# Aggiungi una funzione magicNumbers per restituire una lista di tutti e soli i numeri interi dispari e multipli di 5 tra start e stop





# bonus: fallo su una unica riga con la list comprehension