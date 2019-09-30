# %% für time.sleep
# import time
import os
import locale
locale.setlocale(locale.LC_ALL, '')
# %%fibo kann ich aber nicht zählen


def fibo(n):
    global counter
    counter += 1
    if n <= 1:
        # %%wenn n = 1 ist dann wird es beendet
        return n
    else:
        # %%wir einfach so weit herunter gezählt bis n = 1
        return(fibo(n - 1) + fibo(n - 2))
# %% def fibo_fast(n):


def memoize(n, _cache={}):
    global counter
    counter += 1
    if n in _cache:
        return _cache[n]
    elif n > 1:
        return _cache.setdefault(n, memoize(n-1) + memoize(n-2))
    return n


def goldenratio(n):
    global counter
    counter += 1
    golden = (1 + 5 ** 0.5) / 2
    return round(((golden**n) - ((1-golden)**n)) / 5**0.5)


# %%Input von user der auf int convertiert wird
wiederholen = ""
while wiederholen == "":
    os.system('cls')  # on windows
    counter = 0
    nterms = int(input("How many terms? "))
# %%nterms = 12
    counter = 0
    if nterms <= 0:
        print("Plese enter a positive integer")
    else:
        sequence = input("Print the Sequence(s) else the Result(r): \n")
        if sequence == "s":
            method = input("Use Recursion(r) or Use Memoize(m): \n")
            if method == "r":
                for i in range(nterms):
                    print(str(i+1) + ": " + str(fibo(i)))
            if method == "m":
                for i in range(nterms):
                    print(str(i+1) + ": " + str(memoize(i)))
        if sequence == "r":
            method = input("Use Recursion(r) or use Memoize(m) or use Golden Ration(g): \n")
            if method == "r":
                print("Ergebniss: " + "{:n}".format(fibo(nterms)))
            if method == "m":
                print("Ergebniss: " + "{:n}".format(memoize(nterms)))
            if method == "g":
                print("Ergebniss: " + "{:n}".format(goldenratio(nterms)))
        print("Counter: " + str(counter))

    wiederholen = input("Press Enter to repeat...")

    # %%for durch alle terms durch
#    start = time.time()
#    print("Summe: " + str(fibo(nterms)))
#    end = time.time();
#    print(end-start)
#    for i in range(nterms):
# %%functions aufruf
#    print("Ergebniss: " + str(memoize(nterms)))
