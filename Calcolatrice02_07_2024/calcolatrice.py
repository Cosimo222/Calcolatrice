print("hello")
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

def magic_Numbers(start, stop):
 
 numeri_multiplo_di_3 = [numero for numero in range(start,stop+1) if numero % 5 == 0 and numero % 2 != 0]
 return numeri_multiplo_di_3

print (magic_Numbers(5, 15))



# bonus: fallo su una unica riga con la list comprehension