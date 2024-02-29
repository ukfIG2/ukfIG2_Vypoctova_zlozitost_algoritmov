vstup = [1,2,3,5,9] 
vstup2 = [13,27,28,30,31,51,62,77,101,632]
vystup2 = 105
vstup_1 = 12
vystup1 = "ano"
vstup_2 = 77
vystup_2 = "nie"

vstup3 = [10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,200]
vystup3 = 210

def kontrola(vstup, vystup):
    pocet1 = 0
    #print(vstup_, vystup)
    for i in range(len(vstup)):
        for j in range(i+1, len(vstup)):
            #print(vstup[i], vstup[j], vstup[i]+vstup[j], vystup)
            pocet1+=1
            if vstup[i] + vstup[j] == vystup:
                print(pocet1)
                return "áno"
    print(pocet1)
    return "nie"

def kontrolaGPT(vstup, vystup):
    pocet2 = 0
    seen = set()
    for num in vstup:
        complement = vystup - num
        pocet2+=1
        if complement in seen or num == vystup:
            print(pocet2)
            return "áno"
        seen.add(num)
    print(pocet2)
    return "nie"


print(kontrola(vstup3, vystup3))
print(kontrolaGPT(vstup3, vystup3))
