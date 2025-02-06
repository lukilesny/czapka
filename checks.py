from airium import Airium

standard_set = "EKANBBBDR#!IAFFGGGWYADZILN4GEERAPPPQCOOXOORUJTMVVCWVEXANNZKO#LHEJJESTESTUSAMA?"

strings_dict = {
    "standard": standard_set,
    "luca_di_bosqo": standard_set.replace("L", "",1).replace("U", "",1).replace("C", "",1).replace("A", "",1).replace("D", "",1).replace("I", "",1).replace("B", "",1).replace("O", "",2).replace("S", "",1).replace("Q", "",1),
}

def generate_alfabet(selected, added, rmed):
    output_str = added
    for key in selected:
        if key in strings_dict:
            output_str += strings_dict[key]
        else:
            print("ERROR: No key {} in hardcoded sets of letters", key)
    for rm in rmed:
        if rm in output_str:
            output_str = output_str.replace(rm, "", 1)
        else:
            print("ERROR: Tried to remove {} from {}", rm, output_str)
    # errors should be showed to user
    return "".join(sorted(output_str))

def check(inscription, alphabet):
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
                if char == " ":
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