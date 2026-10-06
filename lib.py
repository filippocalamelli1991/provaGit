# prima funzione

def sumDiff(a, b):
    "somma e sottrare a+b, a-b"
    sum = a + b
    diff = a - b

    if a<b:
        print("Attenzione a è minore di b. Non posso fare la sottrazione!")
        diff =  float("nan")
    
    return sum,diff
