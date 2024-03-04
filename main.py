"""

SZABO ANDREEA GEORGIANA
GRUPA 216

Aplicaţia trebuie să exemplifice cele trei metode de conversie ale numerelor naturale
(împărţiri succesive, substituţie şi utilizarea unei baze intermediare, de obicei, baza 10) între două
baze de numeraţie diferite de 10, conversiile rapide între bazele puteri ale lui 2 (2, 4, 8, 16) şi
operaţiile aritmetice într-o bază oarecare p (adunare, scădere, înmulţire cu o cifră şi împărţire la o
cifră), fără a trece numărul prin baza 10 (p{2,3,...,9,10,16}) ––– Deși această frază exprimă
cerința, nu este enunțul problemei. Enunțul problemei ar trebui să specifice mai clar ce și cum va
introduce utilizatorul și ce va obține.
De exemplu: se dau două numere în baze diferite şi o a treia bază în care ele se vor
aduna.
Sugestii:
 se va trece din baza mai mică în cea mare prin substituţie, iar din cea mare în cea
mică prin împărţiri succesive, pentru a se utiliza doar împărţiri/înmulțiri cu o
cifră.
 numerele se recomandă a se păstra în memorie prin şirul cifrelor.

Notarea se va face după următorul barem:

10% notă: punctul din oficiu

70% notă: aplicaţia (numele autorului se va găsi atât în cod, cât şi la execuţie)
1p existenţa algoritmului (în formă executabilă) de conversie prin împărţiri succesive
1p existenţa algoritmului (în formă executabilă) de conversie prin substituţie
1p existenţa algoritmului (în formă executabilă) de conversie utilizând o bază intermediară
(punctajele se înjumătăţesc dacă conversiile de mai sus au ca bază de pornire respectiv
destinaţie obligatoriu baza 10, nefuncţionând direct dintr-o bază diferită de 10 într-o altă
bază diferită de 10; şi se pierde un sfert din punctaj dacă nu se pot converti numere
în/din baza 16)
2p existenţa algoritmilor (în formă executabilă) de conversii rapide din baza 2 în baza 4, 8 sau
16 şi respectiv invers
1p adunarea a două numere într-o bază oarecare
1p scăderea a două numere într-o bază oarecare
1p înmulţirea cu o cifră într-o bază oarecare
1p împărţirea la o cifră într-o bază oarecare
1p claritatea codului (identare, comentarii, nume de variabile sugestive)


20% notă: documentaţia (numele autorului va fi scris clar, documentaţia se va scrie de mână,
excepţie făcând doar cazurile speciale)
1p enunţul problemei
1p diagrama de apel a subalgoritmilor
1p specificarea tipurilor de date folosite
3p subalgoritmii principali vor fi specificaţi şi scrişi în pseudocod (date, rezultate, precondiţii,
postcondiţii – 1p; pseudocodul – 2p)
3p cel puţin un set de date de test pentru întrega aplicaţie eventual mai multe seturi diferite
pentru părţile care necesită acest lucru
1p claritatea documentaţiei (structurată, scrisă frumos, ...)


"""


"""
transformari pe nr( nu merg pe baza 16)

def inmult_rep(nr, b_i, b_f):
    ""
    :param nr: nr dat
    :param b_i: baza in care e nr dat
    :param b_f: baza in care se transforma
    :return: numarul in baza ceruta(b_f)
    ""
    try:
        nr = int(nr)
        b_i = int(b_i)
        b_f = int(b_f)
    except: raise ValueError("numarul si bazele trebuie sa fie numere naturale")

    if b_f==10:
        p=1
        nr_f=0
        aux=nr
        while aux!=0:
            rest=aux%10
            nr_f=nr_f+rest*p
            p=p*b_i
            aux=aux//10
        return nr_f


def imp_succes(nr, b_i,b_f):
    ""
    :param nr: nr dat
    :param b_i: baza in care e nr dat
    :param b_f: baza in care se transforma
    :return: numarul in baza ceruta(b_f)
    ""
    try:
        nr = int(nr)
        b_i = int(b_i)
        b_f = int(b_f)
    except:
        raise ValueError("numarul si bazele trebuie sa fie numere naturale")

    if b_i==10:
        p=1
        nr_f=0
        while nr!=0:
            rest=nr%b_f
            nr_f=nr_f+rest*p
            p=p*10
            nr=nr//b_f
        return nr_f
"""



"""TRANSFORMARI"""

def inmult_rep1(nr, b_i, b_f):
    """
    conversie prin substituţie(inmultiri repetate) y->10"
    :param nr: nr dat
    :param b_i: baza in care e nr dat
    :param b_f: baza in care se transforma (merge doar pe baza 10)
    :return: numarul in baza ceruta(b_f)
    """
    try:
        b_i = int(b_i)
        b_f = int(b_f)
    except:
        raise ValueError("bazele trebuie sa fie numere naturale")

    nr_v=[]
    for i in range(0,len(nr)):
                if nr[i] == "A":
                    nr_v.append(10)
                elif nr[i] == "B":
                    nr_v.append(11)
                elif nr[i] == "C":
                    nr_v.append(12)
                elif nr[i] == "D":
                    nr_v.append(13)
                elif nr[i] == "E":
                    nr_v.append(14)
                elif nr[i] == "F":
                    nr_v.append(15)
                else:
                    nr_v.append(int(nr[i]))

    if b_f==10:
        p=1
        nr_f=0
        aux=len(nr_v)-1
        while aux!=-1:
            rest=nr_v[aux]
            nr_f=nr_f+rest*p
            p=p*b_i
            aux=aux-1
        return nr_f

def imp_succes1(nr, b_i, b_f):
        """
        conversie prin împărţiri succesive 10->x"
        :param nr: nr dat
        :param b_i: baza in care e nr dat (merge doar pe baza 10)
        :param b_f: baza in care se transforma
        :return: numarul in baza ceruta(b_f)
        """
        try:
            nr = int(nr)
            b_i = int(b_i)
            b_f = int(b_f)
        except:
            raise ValueError("numarul si bazele trebuie sa fie numere naturale")

        if b_i == 10:
            nr_f = ""
            if nr==0:
                nr_f="0"

            while nr != 0:
                    rest = nr % b_f
                    if rest == 10:
                        nr_f+="A"
                    elif rest == 11:
                        nr_f+="B"
                    elif rest == 12:
                        nr_f+="C"
                    elif rest == 13:
                        nr_f+="D"
                    elif rest == 14:
                        nr_f+="E"
                    elif rest == 15:
                        nr_f+="F"
                    else:
                        nr_f += str(rest)
                    nr = nr // b_f
            nr_f=nr_f[::-1]
            return nr_f


def conversii_imp_inm(ok):
    """
    permite introducerea datelor necesare de catre utilizator si apeleaza metoda ceruta
    :param ok: are o valoare utilizata doar in cod
    transmite cazul de conversie selectat de utilizator
    ok==1: conversie prin împărţiri succesive 10->x"
    ok==2: conversie prin substituţie(inmultiri repetate) y->10"
    ok==3: conversie utilizând o bază intermediară y->x"
    :return: numarul n convertit in baza ceruta (b_f)
    """
    nr=input("numarul este: ")
    b_i=input("baza numarului este: ")
    b_f=input("baza in care se doreste: ")

    if ok==2:
        k=inmult_rep1(nr, b_i,10)
    elif ok==1:
        k=imp_succes1(nr,10,b_f)
    elif ok==3:
        nr10 = inmult_rep1(nr, b_i, 10)
        k = imp_succes1(nr10, 10, b_f)
    return k


def baza2__4_8_16():
    """
    permite introducerea datelor necesare de catre utilizator si executa conversia
    conversiA e din baza 2 in baza 4/8/16 in functie de ce alege utilizatorul
    :return: numarul convertit
    """
    nr = input("numarul(in baza 2) dat este: ")

    baza = input("baza in care va fi convartit numarul dat este(4,8,16) :")
    nr_n = ""

    if baza == "4":
        nr_v = []
        if len(nr)%2!=0:
            nr1="0"+nr
            nr=nr1

        for i in range(0, len(nr),2):
            k=nr[i]+nr[i+1]
            nr_v.append(k)
        #print(nr_v)

        for i in nr_v:

            if i == "00":
                nr_n += "0"
            elif i == "01":
                nr_n += "1"
            elif i == "10":
                nr_n += "2"
            elif i == "11":
                nr_n += "3"
            else:
                print("nr scris incorect in baza 2!!!")
    elif baza == "8":
        nr_v = []

        if len(nr)%3==1:
            nr1="00"+nr
            nr=nr1

        if len(nr)%3==2:
            nr1="0"+nr
            nr=nr1

        for i in range(0, len(nr),3):
            k=nr[i]+nr[i+1]+nr[i+2]
            nr_v.append(k)

        #print(nr_v)

        for i in nr_v:
            if i == "000":
                nr_n += "0"
            elif i == "001":
                nr_n += "1"
            elif i == "010":
                nr_n += "2"
            elif i == "011":
                nr_n += "3"
            elif i == "100":
                nr_n += "4"
            elif i == "101":
                nr_n += "5"
            elif i == "110":
                nr_n += "6"
            elif i == "111":
                nr_n += "7"

            else:
                print("nr scris incorect in baza 2!!!")

    elif baza == "16":
        nr_v = []

        if len(nr)%4==1:
            nr1="000"+nr
            nr=nr1

        if len(nr)%4==2:
            nr1="00"+nr
            nr=nr1

        if len(nr)%4==3:
            nr1="0"+nr
            nr=nr1

        for i in range(0, len(nr),4):
            k=nr[i]+nr[i+1]+nr[i+2]+nr[i+3]
            nr_v.append(k)

        #print(nr_v)

        for i in nr_v:
            if i == "0000":
                nr_n += "0"
            elif i == "0001":
                nr_n += "1"
            elif i == "0010":
                nr_n += "2"
            elif i == "0011":
                nr_n += "3"
            elif i == "0100":
                nr_n += "4"
            elif i == "0101":
                nr_n += "5"
            elif i == "0110":
                nr_n += "6"
            elif i == "0111":
                nr_n += "7"
            elif i == "1000":
                    nr_n += "8"
            elif i == "1001":
                    nr_n += "9"
            elif i == "1010":
                    nr_n += "A"
            elif i == "1011":
                    nr_n += "B"
            elif i == "1100":
                    nr_n += "C"
            elif i == "1101":
                nr_n += "D"
            elif i == "1110":
                    nr_n += "E"
            elif i == "1111":
                    nr_n += "F"

            else:
                print("nr scris incorect in baza 2!!!")

    else:
        print("baza invalida!!!")
    return nr_n


def baza_4_8_16__2():
    """
        permite introducerea datelor necesare de catre utilizator si executa conversia
        conversiA e din baza 4/8/16 in functie de ce alege utilizatorul in  baza 2
        :return: numarul convertit
    """
    baza_nr_dat=input("baza numarului dat este(4,8,16) :")
    nr=input("numarul dat este: ")
    nr_v=[]
    nr_n=""
    for i in range(0,len(nr)):
        nr_v.append(nr[i])

    #print(nr_v)

    if baza_nr_dat=="4":
        for i in nr_v:

            if i=="0":
                nr_n+="00"
            elif i=="1":
                nr_n += "01"
            elif i=="2":
                nr_n += "10"
            elif i=="3":
                nr_n += "11"
            else:
                print("nr scris incorect in baza 4!!!")
    elif baza_nr_dat=="8":
        for i in nr_v:
            if i == "0":
                nr_n += "000"
            elif i == "1":
                nr_n += "001"
            elif i == "2":
                nr_n += "010"
            elif i == "3":
                nr_n += "011"
            elif i=="4":
                nr_n += "100"
            elif i=="5":
                nr_n += "101"
            elif i=="6":
                nr_n += "110"
            elif i=="7":
                nr_n += "111"

            else:
                print("nr scris incorect in baza 8!!!")

    elif baza_nr_dat=="16":
        for i in nr_v:
            if i == "0":
                nr_n += "0000"
            elif i == "1":
                nr_n += "0001"
            elif i == "2":
                nr_n += "0010"
            elif i == "3":
                nr_n += "0011"
            elif i == "4":
                nr_n += "0100"
            elif i == "5":
                nr_n += "0101"
            elif i == "6":
                nr_n += "0110"
            elif i == "7":
                nr_n += "0111"

            elif i == "8":
                nr_n += "1000"
            elif i == "9":
                nr_n += "1001"
            elif i == "A":
                nr_n += "1010"
            elif i == "B":
                nr_n += "1011"
            elif i == "C":
                nr_n += "1100"
            elif i == "D":
                nr_n += "1101"
            elif i == "E":
                nr_n += "1110"
            elif i == "F":
                nr_n += "1111"

            else:
                print("nr scris incorect in baza 16!!!(literele cu majuscule)")

    else:
        print("baza invalida!!!")
    return  nr_n


""" operatii aritmetice"""

def citire_add_sub(ok):
    """
    permite introducerea datelor necesare de catre utilizator si apeleaza metoda ceruta
    :param ok: are o valoare utilizata doar in cod
    transmite operatia selectata de utilizator
    ok==1: adunare
    ok==2: scadere (la scadere va scadea mereu nr mai mare din cel mai mic)
    :return: suma/diferenta numerelor citite convertite in baza ceruta (b3)
    """
    nr1 = input("primul numar este: ")
    b1 = input("baza lui este: ")
    nr2 = input("al doilea numar este: ")
    b2 = input("baza lui este: ")
    b3=input("baza in care se doreste operatia: ")

    try:
        b1 = int(b1)
        b2 = int(b2)
        b3 = int(b3)
    except:
        raise ValueError("bazele trebuie sa fie numere naturale(2,3..,9,16)")

    if b1!=b3:
        nr10 = inmult_rep1(nr1, b1, 10)
        nr1 = imp_succes1(nr10, 10, b3)
    if b2!=b3:
        nr10 = inmult_rep1(nr2, b2, 10)
        nr2 = imp_succes1(nr10, 10, b3)
    nrr=0
    if ok==1:
        nrr=add(nr1,nr2,b3)
    if ok==2:
        if nr1>nr2:
            nrr=sub(nr1,nr2,b3)#nr1-nr2
        if nr2>nr1:
            nrr=sub(nr2,nr1,b3)#nr2-nr1
    return nrr

def add(nr1,nr2,b):
    """
    adunam nr1 cu nr2 in baza b
    :param nr1: primul nr
    :param nr2: al doilea nr
    :param b: baza in care se efectueaza adunarea
    :return: suma lor in baza b
    """
    n1=[]
    n2=[]

    for i in range(0, len(nr1)):
        if nr1[i] == "A":
            n1.append(10)
        elif nr1[i] == "B":
            n1.append(11)
        elif nr1[i] == "C":
            n1.append(12)
        elif nr1[i] == "D":
            n1.append(13)
        elif nr1[i] == "E":
            n1.append(14)
        elif nr1[i] == "F":
            n1.append(15)
        else:
            n1.append(int(nr1[i]))

    for i in range(0, len(nr2)):
        if nr2[i] == "A":
            n2.append(10)
        elif nr2[i] == "B":
            n2.append(11)
        elif nr2[i] == "C":
            n2.append(12)
        elif nr2[i] == "D":
            n2.append(13)
        elif nr2[i] == "E":
            n2.append(14)
        elif nr2[i] == "F":
            n2.append(15)
        else:
            n2.append(int(nr2[i]))

    cf=0
    l1= len(n1)-1
    l2= len(n2)-1

    nr_f = []
    while l1!=-1 and l2!=-1:
            nr = (n1[l1] + n2[l2] + cf) % b
            cf = (n1[l1] + n2[l2] + cf) // b
            nr_f.append(nr)
            l1=l1-1
            l2=l2-1
    while l1!=-1 :
            nr = (n1[l1]  + cf) % b
            cf = (n1[l1] + cf) // b
            nr_f.append(nr)
            l1 = l1 - 1
    while l2!=-1:
        nr = (n2[l2] + cf) % b
        cf = (n2[l2] + cf) // b
        nr_f.append(nr)
        l2 = l2 - 1
    if cf!=0:
        nr_f.append(cf)

    nr_f1 = ""
    for i in range (0,len(nr_f)):
        rest = nr_f[i]
        if rest == 10:
            nr_f1 += "A"
        elif rest == 11:
            nr_f1 += "B"
        elif rest == 12:
            nr_f1 += "C"
        elif rest == 13:
            nr_f1 += "D"
        elif rest == 14:
            nr_f1 += "E"
        elif rest == 15:
            nr_f1 += "F"
        else:
            nr_f1 += str(rest)

    nr_f1 = nr_f1[::-1]
    return nr_f1

def sub(nr1,nr2,b):
    """
    scadem nr1 din nr2 in baza b
    :param nr1: primul nr (descazut)
    :param nr2: al doilea nr (scazator)
    :param b: baza in care se efectueaza scaderea
    :return: diferenta lor in baza b
    """
    n1 = []
    n2 = []

    for i in range(0, len(nr1)):
        if nr1[i] == "A":
            n1.append(10)
        elif nr1[i] == "B":
            n1.append(11)
        elif nr1[i] == "C":
            n1.append(12)
        elif nr1[i] == "D":
            n1.append(13)
        elif nr1[i] == "E":
            n1.append(14)
        elif nr1[i] == "F":
            n1.append(15)
        else:
            n1.append(int(nr1[i]))

    for i in range(0, len(nr2)):
        if nr2[i] == "A":
            n2.append(10)
        elif nr2[i] == "B":
            n2.append(11)
        elif nr2[i] == "C":
            n2.append(12)
        elif nr2[i] == "D":
            n2.append(13)
        elif nr2[i] == "E":
            n2.append(14)
        elif nr2[i] == "F":
            n2.append(15)
        else:
            n2.append(int(nr2[i]))

    cf = 0
    l1 = len(n1) - 1
    l2 = len(n2) - 1

    nr_f = []
    while l1 != -1 and l2 != -1:
        if cf==1:
            n1[l1]=n1[l1]-1

        if n1[l1]<n2[l2]:
            cf=1
            nr = ((b+n1[l1]) - n2[l2])
        else:
            nr = (n1[l1] - n2[l2])
            cf=0

        nr_f.append(nr)
        l1 = l1 - 1
        l2 = l2 - 1
    while l1 != -1:
        if cf == 1:
            n1[l1] = n1[l1] - 1

        if n1[l1] < 0:
            cf = 1
            nr = ((b + n1[l1]))
        else:
            nr = (n1[l1])
            cf = 0
        nr_f.append(nr)
        l1 = l1 - 1

    nr_f1 = ""
    for i in range(0, len(nr_f)):
        rest = nr_f[i]
        if rest == 10:
            nr_f1 += "A"
        elif rest == 11:
            nr_f1 += "B"
        elif rest == 12:
            nr_f1 += "C"
        elif rest == 13:
            nr_f1 += "D"
        elif rest == 14:
            nr_f1 += "E"
        elif rest == 15:
            nr_f1 += "F"
        else:
            nr_f1 += str(rest)

    nr_f1 = nr_f1[::-1]
    return nr_f1


def citire_mul_div(ok):
    """
    permite introducerea datelor necesare de catre utilizator si apeleaza metoda ceruta
    :param ok: are o valoare utilizata doar in cod
    transmite operatia selectata de utilizator
    ok==3: inmultire
    ok==4: impartire
    tipareste produsul/catul numerelor citite convertite in baza ceruta (b3)
    """
    nr1 = input("numarul este: ")
    b1 = input("baza lui este: ")
    nr2 = input("cifra este(se accepta si A B C D E F in baza 16): ")
    b2 = input("baza ei este: ")
    b3=input("baza in care se doreste operatia: ")

    try:
        b1 = int(b1)
        b2 = int(b2)
        b3 = int(b3)
    except ValueError("bazele trebuie sa fie numere naturale(2,3..,9,16)") as ve:
            print(ve)

    if b1<b2:
        nr10 = inmult_rep1(nr1, b1, 10)
        nr1 = imp_succes1(nr10, 10, b2)
        b=b2
    else:
        nr10 = inmult_rep1(nr2, b2, 10)
        nr2 = imp_succes1(nr10, 10, b1)
        b=b1

    nrr=0
    if ok==3:
        nrr=mul(nr1,nr2,b)
        if b!=b3:
            nr10 = inmult_rep1(nrr, b, 10)
            nrr = imp_succes1(nr10, 10, b3)
        print("produs:   ",nrr)

    if ok==4:
        nrr=div(nr1,nr2,b)#nr1-nr2
        rest=nrr[len(nrr)-1]
        cat=""

        for i in range (0,len(nrr)-1):
            cat+=nrr[i]

        if b != b3:
            nr10 = inmult_rep1(cat, b, 10)
            cat = imp_succes1(nr10, 10, b3)
            nr10 = inmult_rep1(rest, b, 10)
            rest = imp_succes1(nr10, 10, b3)
        print("cat: ", cat,'   rest: ', rest)

def mul(nr1,c,b):
    """
    inmulteste un nr cu o cifra intr-o baza oarecare
    :param nr1: termenul numar
    :param c: termenul cifra
    :param b: baza in care se efectueazaa produsul
    :return: produsul cifrei c cu nr1
    """
    n1 = []
    n2=0
    for i in range(0, len(nr1)):
        if nr1[i] == "A":
            n1.append(10)
        elif nr1[i] == "B":
            n1.append(11)
        elif nr1[i] == "C":
            n1.append(12)
        elif nr1[i] == "D":
            n1.append(13)
        elif nr1[i] == "E":
            n1.append(14)
        elif nr1[i] == "F":
            n1.append(15)
        else:
            n1.append(int(nr1[i]))

    if c == "A":
        n2=(10)
    elif c == "B":
        n2=(11)
    elif c== "C":
        n2=(12)
    elif c == "D":
        n2=(13)
    elif c == "E":
        n2=(14)
    elif c == "F":
        n2=(15)
    else:
        n2=(int(c))

    cf = 0
    l1 = len(n1) - 1

    nr_f = []

    while l1 != -1:
        nr = (n1[l1]*n2 + cf) % b
        cf = (n1[l1]*n2 + cf) // b
        nr_f.append(nr)
        l1 = l1 - 1

    if cf != 0:
        nr_f.append(cf)

    nr_f1 = ""
    for i in range(0, len(nr_f)):
        rest = nr_f[i]
        if rest == 10:
            nr_f1 += "A"
        elif rest == 11:
            nr_f1 += "B"
        elif rest == 12:
            nr_f1 += "C"
        elif rest == 13:
            nr_f1 += "D"
        elif rest == 14:
            nr_f1 += "E"
        elif rest == 15:
            nr_f1 += "F"
        else:
            nr_f1 += str(rest)

    nr_f1 = nr_f1[::-1]
    return nr_f1



def div(nr1,c,b):
    """
    imparte un nr la o cifra intr-o baza oarecare
    :param nr1: deimpartitul numar
    :param c: impartitorul cifra
    :param b: baza in care se efectueaza impartirea
    :return: un string cu n caractere
    primele n-1 caractere sunt catul si ultimul este restul( se va prelucra in functia in care sunt returnate)
    """
    n1 = []
    n2 = 0
    for i in range(0, len(nr1)):
        if nr1[i] == "A":
            n1.append(10)
        elif nr1[i] == "B":
            n1.append(11)
        elif nr1[i] == "C":
            n1.append(12)
        elif nr1[i] == "D":
            n1.append(13)
        elif nr1[i] == "E":
            n1.append(14)
        elif nr1[i] == "F":
            n1.append(15)
        else:
            n1.append(int(nr1[i]))

    if c == "A":
        n2 = (10)
    elif c == "B":
        n2 = (11)
    elif c == "C":
        n2 = (12)
    elif c == "D":
        n2 = (13)
    elif c == "E":
        n2 = (14)
    elif c == "F":
        n2 = (15)
    else:
        n2 = (int(c))

    cf = 0
    l1 = len(n1) - 1

    nr_f = []
    i=0
    while l1 >= i:
        nr = (n1[i]+ cf*b) // n2
        cf = (n1[i]+ cf*b)% n2
        nr_f.append(nr)
        i+=1

    nr_f.append(cf)

    nr_f1 = ""
    for i in range(0, len(nr_f)):
        rest = nr_f[i]
        if rest == 10:
            nr_f1 += "A"
        elif rest == 11:
            nr_f1 += "B"
        elif rest == 12:
            nr_f1 += "C"
        elif rest == 13:
            nr_f1 += "D"
        elif rest == 14:
            nr_f1 += "E"
        elif rest == 15:
            nr_f1 += "F"
        else:
            nr_f1 += str(rest)

    return nr_f1


def print_meniu():
    ok=True
    while ok:

        print("Szabo Andreea Georgiana")
        print("1. Transformari")
        print("2. Operatii aritetice")
        print("3. Exit")
        print("Se presupune ca datele ce sunt introduse de la tastatura sunt valide "
              "(ex: nr 26253425 va avea minim baza 7)")

        comanda=input("Optiunea este (scrieti doar cifra de ordine): ")

        if comanda=="1":
            print("Selecteaza tipul transformarii din cele de mai jos: ")

            print("1. conversie prin împărţiri succesive 10->x")
            print("2. conversie prin substituţie(inmultiri repetate) y->10")
            print("3. conversie utilizând o bază intermediară y->x")
            print("4. conversii rapide din baza 2 în baza 4, 8 sau 16")
            print("5. conversii rapide din baza 4, 8 sau 16 in baza 2")

            comanda1=input("Tipul(scrieti doar cifra de ordine): ")

            if comanda1=="1":
                nr=conversii_imp_inm(1)
                print(nr)
            elif comanda1=="2":
                nr=conversii_imp_inm(2)
                print(nr)
            elif comanda1 == "3":
                nr = conversii_imp_inm(3)
                print(nr)
            elif comanda1 == "4":
                nr = baza2__4_8_16()
                print(nr)
            elif comanda1 == "5":
                nr=baza_4_8_16__2()
                print(nr)
            else:
                print("optiune invalida!!!")


        elif comanda=="2":

            print("Selecteaza o operatie din cele de mai jos: ")

            print("1. adunarea a două numere într-o bază oarecare")
            print("2. scaderea a două numere într-o bază oarecare")
            print("3. înmulţirea cu o cifră într-o bază oarecare")
            print("4. împărţirea la o cifră într-o bază oarecare")

            comanda1 = input("Operatia(scrieti doar cifra de ordine): ")

            if comanda1 == "1":
                n=citire_add_sub(1)
                print(n)
            elif comanda1 == "2":
                n=citire_add_sub(2)
                print(n)
            elif comanda1 == "3":
                citire_mul_div(3)
            elif comanda1 == "4":
                citire_mul_div(4)
            else:
                print("optiune invalida!!!")

        elif comanda=="3":
            ok=False

        else:
            print("optiune invalida!!!")



print_meniu()
