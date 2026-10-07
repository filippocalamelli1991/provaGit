# Provo branch git
import numpy as np

# importo la mia libreria
import lib

# modifica per prova commit remoto
# aggiungo modifica gestione array

def main():
    # input
    a = np.array([11, 12, 9])
    b = np.array([11, 10, 11])

    m,div = lib.multDiv(a, b)

    print(f"il prodotto e la divisione dei vettori {a} e {b} sono {np.array2string(m,precision=2)} e {np.array2string(div,precision=2)}")

if __name__ == "__main__":
    main()