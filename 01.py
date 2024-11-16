def prRed(skk): print("\033[91m {}\033[00m" .format(skk), end ="")

def prGreen(skk): print("\033[92m {}\033[00m" .format(skk), end ="")
 
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk), end ="")

def printResults(letters, checked, left):
    for idx, char in enumerate(letters.upper()):
        if checked[idx]:
            prGreen(char)
        else:
            prRed(char)
    print("\n", *left)

def check(inscription):
    alphabet = "".join(sorted("EKANBBBDR#!IAFFGGGWYADZILN4GEERAPPPQCOOXOORUJTMVVCWVEXANNZKO#LHEJJESTESTUSAMA?"))
    inscription = inscription.upper()
    result = [True]*len(inscription)
    # print(result)

    for idx, char in enumerate(inscription):
        if char == ' ':
            # print('  ', end ="")
            continue
        if char in alphabet:
            alphabet = alphabet.replace(char, '', 1)
            # prGreen(char)
        else:
            result[idx] = False
            # prRed(char)
    # print("\n",*alphabet)
    return result, alphabet

letters = input("Podaj napis do sprawdzenia: ") #bez polskich znakow, ze spacjami
checked,left = check(letters)
printResults(letters, checked, left)