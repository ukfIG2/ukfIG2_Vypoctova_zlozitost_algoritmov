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
    #print(vstup_, vystup)
    for i in range(len(vstup)):
        for j in range(i+1, len(vstup)):
            print(vstup[i], vstup[j], vstup[i]+vstup[j], vystup)
            if vstup[i] + vstup[j] == vystup:
                return "áno"
    return "nie"
    

print(kontrola(vstup2, vystup2))
