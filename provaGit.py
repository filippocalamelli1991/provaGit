# provaGit
import numpy as np

# importo la mia libreria
import lib

# modifica per prova commit remoto
# aggiungo modifica gestione array

def main():
    # input
    a = np.array([11, 12, 9])
    b = np.array([11, 10, 11])

    s,d = lib.sumDiff(a, b)

    print(f"la somma e la differenza dei vettori {a} e {b} sono {s} e {d}")

if __name__ == "__main__":
    main()

