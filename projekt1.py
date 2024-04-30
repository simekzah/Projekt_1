"""
projekt1.py: první projekt do Engeto Online Python Akademie 
author: Michal Šimek
email: simek.vys@seznam.cz
discord: smk6666
"""
from task_template import TEXTS
uzivatele = {
"bob":"123",
"ann":"pass123",
"mike":"password123",
"liz":"pass123",
}
cara = "-" * (len("Enter a number btw. 1 and 3 to select: ")+1)
user = input("username: ")
pas =  input("password: ")

if not ((user in uzivatele.keys())and (pas == uzivatele[user])):

    print(f"""unregistered user, terminating the program..
""", end = "")

elif (user in uzivatele.keys())and (pas == uzivatele[user]):
    print(f"""{cara}
Welcome to the app, {user}
We have 3 texts to be analyzed.
{cara}
""", end = "")
    vyber = input("Enter a number btw. 1 and 3 to select: ")
    if not vyber.isdigit():
        print("Nezadal jsi číslo.")
    elif not (vyber in ["1", "2", "3"]):
        print("Nevybral jsi číslo z nabídky.")
    else:
        # izolování řetězců
        a = TEXTS[int(vyber)-1].replace("\n", " ")

        retezce = []
        stringy = []
        b = 0
        for _ in range(a.count(" ")):
            retezce.append(list(a.partition(" ")))
            a = retezce[b][2]
            b = b + 1

        for c in range(len(retezce)):
            if retezce[c][0].strip() != "":
                stringy.append(retezce[c][0].strip())

        # nepatřičné znaky zleva
        pryc = 0
        for c, r in enumerate(stringy):
            pryc = 0
            for d, s in enumerate(stringy[c]):
                if stringy[c][d].isalnum():
                    break
                else:
                    pryc = pryc + 1
            stringy[c] = stringy[c][pryc:len(stringy[c])]

        # nepatřičné znaky zprava

        for c, r in enumerate(stringy):
            pryc = 0
            for d, s in enumerate(stringy[c]):
                if stringy[c][-1-d].isalnum():
                    break
                else:
                    pryc = pryc + 1
            stringy[c] = stringy[c][0:len(stringy[c])-pryc]

        # procházení  v stringy
        pocet_retez = len(stringy)
        soucet_cisel = 0
        pocet_cisel = 0
        velka_pism = 0
        mala_pism = 0
        prvni_vel = 0
        for c in range(len(stringy)):
            if stringy[c].isnumeric() or stringy[c].isdecimal():
                soucet_cisel = soucet_cisel + int(stringy[c])
                pocet_cisel = pocet_cisel + 1

            if  stringy[c].isalpha() and stringy[c].isupper():
                velka_pism += 1
            elif stringy[c].isalpha() and stringy[c].islower():
                mala_pism += 1
            if stringy[c][0].istitle():
                prvni_vel += 1
        #print(soucet_cisel, pocet_cisel)
        #print(velka_pism)
        #print(mala_pism)
        #print(prvni_vel)

        # cetnost delek
        cetnost = {}
        for c, r in enumerate(stringy):
            if len(stringy[c]) in cetnost:
                cetnost[len(stringy[c])] = cetnost[len(stringy[c])] + 1
            else:
                cetnost[len(stringy[c])] = 1
        else:
            poradi = sorted(cetnost)
            maxcet = cetnost[sorted(cetnost, key =cetnost.get, reverse = True)[0]]
            sirka = int(14 + ((maxcet-14)+abs((maxcet-14)))/2)
        #print(cetnost, "\n", poradi, "\n", maxcet, "\n", sirka)

#tisk grafu
        print(f"""{cara}
There are {pocet_retez} words in the selected text.
There are {prvni_vel} titlecase words.
There are {velka_pism} uppercase words.
There are {mala_pism} lowercase words.
There are {pocet_cisel} numeric strings.
The sum of all the numbers {soucet_cisel}
{cara}
LEN|{' ' * int(((sirka - 10)+(sirka - 10)%2)/2) + 'occurences' + ' ' * int(((sirka - 10)+(sirka - 10)%2)/2)}|NR.
{cara}
""", end = "")

        for c, r in enumerate(poradi):
            print(" " * (3-len(str(r))) + str(r) + "|" + "*" * cetnost[r]+ " " * ((sirka + sirka%2) - cetnost[r]) + "|" + str(cetnost[r]))