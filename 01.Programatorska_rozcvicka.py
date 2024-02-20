vstup = "apredsajetupes"
vstup = "pppeeesss"

#Najde jeden po druhom p e s
def _01(vstup):
    pocet = 0
    for i in range(len(vstup)):
        if vstup[i] == 'p':
            for j in range(i+1, len(vstup)):
                if vstup[j] == 'e':
                    for k in range(j+1, len(vstup)):
                        if vstup[k] == 's':
                            pocet += 1
    #print(pocet)
    return pocet

#Postupne násobenie
def _02(vstup):
    pocet = 0
    pocet_p = 0
    pocet_pe = 0

    for char in vstup:
        if char == 'p':
            pocet_p += 1
            #print("P+1", pocet_p)
        elif char == 'e':
            pocet_pe += pocet_p
            #print("E+1", pocet_p, pocet_pe)
        elif char == 's':
            pocet += pocet_pe
            #print("S+1", pocet_p, pocet_pe, pocet)
        #print(char)

    return pocet

#Najde jeden po druhom p e s a ešte aj cez zoznam
def _03(vstup):
    zoznam = list(vstup)
    pocet = 0
    #print(zoznam)
    for i in range(len(zoznam)):
        if(zoznam[i] == 'p'):
            for j in range(i, len(zoznam)):
                if(zoznam[j] == 'e'):
                    for k in range(j, len(zoznam)):
                        if(zoznam[k] == 's'):
                            pocet += 1
    return pocet



#print("Riešenie _01 je:", _01(vstup))
print("Riešenie _02 je:", _02(vstup))
#print("Riešenie _03 je:", _03(vstup))