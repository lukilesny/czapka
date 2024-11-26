from airium import Airium

def check(inscription):
    alphabet = "".join(sorted("EKANBBBDR#!IAFFGGGWYADZILN4GEERAPPPQCOOXOORUJTMVVCWVEXANNZKO#LHEJJESTESTUSAMA?"))
    inscription = inscription.upper()
    result = [True]*len(inscription)

    for idx, char in enumerate(inscription):
        if char == ' ':
            continue
        if char in alphabet:
            alphabet = alphabet.replace(char, '', 1)
        else:
            result[idx] = False
    return result, alphabet

def generate_results_html(letters, checked, left):
    html = Airium()

    html('<!DOCTYPE html>')
    with html.html(lang="pl"):
        with html.head():
            html.meta(charset="utf-8")
            html.title(_t="Czapka symulator")

        with html.body():
            with html.h1(style="font-family:verdana;"):
                if False in checked:
                    html("NIE DA SIĘ :(")
                else:
                    html("DA SIĘ :)")

            for i in range(len(letters)):
                if checked[i]:
                    color="green"
                else:
                    color="red"
                char = letters[i]
                if char is " ":
                    char="&MediumSpace;"
                with html.span(style="font-family:verdana;color:"+color+";"):
                    html(char)
            
            with html.p(style="font-family:verdana;"):
                html(left)
            with html.form(action="/start"):
                html.input("type=\"submit\" value=\"Sprawdź kolejne literki\"")
    return str(html)

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