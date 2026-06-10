import random
import copy

rozmery_plochy = int(input("Zadaj rozmery hracej plochy: "))
pocet_hracov = int(input("Zadaj pocet hracov: "))
plocha = []

def generuj_plochu():    
    pocet_teleportov = rozmery_plochy//2
    riadok = []

    for i in range(rozmery_plochy):
        for j in range(rozmery_plochy):
            riadok.append(".")
        plocha.append(riadok)
        riadok = []

    plocha[0][0] = "+"
    if rozmery_plochy%2 == 0:
        plocha[rozmery_plochy-1][0] = "*"
    else:
        plocha[rozmery_plochy-1][rozmery_plochy-1] = "*"

    ascii_velke = 65
    ascii_male = 97

    for i in range(pocet_teleportov):
        teleport = chr(ascii_velke)
        pozicia_riadku_konciaceho = random.randint(1,rozmery_plochy-1)
        pozicia_stlpca_konciaceho = random.randint(0,rozmery_plochy-1)

        while plocha[pozicia_riadku_konciaceho][pozicia_stlpca_konciaceho] != ".":
            pozicia_riadku_konciaceho = random.randint(1,rozmery_plochy-1)
            pozicia_stlpca_konciaceho = random.randint(0,rozmery_plochy-1)
        plocha[pozicia_riadku_konciaceho][pozicia_stlpca_konciaceho] = teleport

        pozicia_riadku_zaciatocneho = random.randint(0,rozmery_plochy-2)
        pozicia_stlpca_zaciatocneho = random.randint(0,rozmery_plochy-1)

        while plocha[pozicia_riadku_zaciatocneho][pozicia_stlpca_zaciatocneho] != "." or pozicia_riadku_zaciatocneho >= pozicia_riadku_konciaceho:
            pozicia_riadku_zaciatocneho = random.randint(0,rozmery_plochy-2)
            pozicia_stlpca_zaciatocneho = random.randint(0,rozmery_plochy-1)
        plocha[pozicia_riadku_zaciatocneho][pozicia_stlpca_zaciatocneho] = teleport

        teleport = chr(ascii_male)

        pozicia_riadku_zaciatocneho = random.randint(1,rozmery_plochy-1)
        pozicia_stlpca_zaciatocneho = random.randint(0,rozmery_plochy-1)

        while plocha[pozicia_riadku_zaciatocneho][pozicia_stlpca_zaciatocneho] != ".":
            pozicia_riadku_zaciatocneho = random.randint(1,rozmery_plochy-1)
            pozicia_stlpca_zaciatocneho = random.randint(0,rozmery_plochy-1)
        plocha[pozicia_riadku_zaciatocneho][pozicia_stlpca_zaciatocneho] = teleport

        pozicia_riadku_konciaceho = random.randint(0,rozmery_plochy-2)
        pozicia_stlpca_konciaceho = random.randint(0,rozmery_plochy-1)

        while plocha[pozicia_riadku_konciaceho][pozicia_stlpca_konciaceho] != "." or pozicia_riadku_konciaceho >= pozicia_riadku_zaciatocneho:
            pozicia_riadku_konciaceho = random.randint(0,rozmery_plochy-2)
            pozicia_stlpca_konciaceho = random.randint(0,rozmery_plochy-1)
        plocha[pozicia_riadku_konciaceho][pozicia_stlpca_konciaceho] = teleport

        ascii_velke += 1
        ascii_male += 1

def vykresli_plochu():
    print("Hracie pole:")
    print("  ", end="")
    for i in range(rozmery_plochy):
        print(i, end=" ")
    print()
    for i in range(rozmery_plochy):
        print(i, end=" ")
        for j in range(rozmery_plochy):
            print(plocha[i][j],end=" ")
        print()
    print("=======================")

def simulacia_jeden_hrac():
    if rozmery_plochy < 5 or rozmery_plochy > 10:
        print("Nie je mozne vytvorit plochu s vami zadanymi rozmermy")
        return None
    generuj_plochu()
    vykresli_plochu()

    povodna_plocha = copy.deepcopy(plocha)
    pozicia_hraca = [0,0]
    
    while True:
        if rozmery_plochy%2 == 0:
            if pozicia_hraca == [rozmery_plochy-1,0]:
                print("Hrac c. 1 VYHRAL!")
                break
        else:
            if pozicia_hraca == [rozmery_plochy-1,rozmery_plochy-1]:
                print("Hrac c. 1 VYHRAL!")
                break

        print("Pozicia hraca:")
        print("Hrac c. 1",pozicia_hraca)
        print("---")

        cislo_na_kocke = random.randint(1,6)
        posun = cislo_na_kocke
        while cislo_na_kocke == 6:
            cislo_na_kocke = random.randint(1,6)
            posun += cislo_na_kocke
        print("Hrac c. 1 hodil spolu na kocke:",posun,"bodov")

        if pozicia_hraca[0]%2 == 0:
            if pozicia_hraca[1] + posun <= rozmery_plochy-1:
                pozicia_hraca = [pozicia_hraca[0],pozicia_hraca[1]+posun]
                print("Hrac c. 1 sa posuna na policko:",pozicia_hraca)
            else:
                novy_riadok = (pozicia_hraca[1] + posun)//rozmery_plochy + pozicia_hraca[0]
                if novy_riadok >= rozmery_plochy:
                    print("Hrac c. 1 hodil viac bodov nez je vzdialenost do ciela!")
                else:
                    if novy_riadok%2 == 0:
                        novy_stlpec = (pozicia_hraca[1] + posun)%rozmery_plochy
                    else:
                        novy_stlpec = (rozmery_plochy-1) - ((pozicia_hraca[1] + posun)%rozmery_plochy)
                    pozicia_hraca = [novy_riadok,novy_stlpec]
                    print("Hrac c. 1 sa posuna na policko:",pozicia_hraca)
                    
        else:
            if pozicia_hraca[1] - posun >= 0:
                pozicia_hraca = [pozicia_hraca[0],pozicia_hraca[1]-posun]
                print("Hrac c. 1 sa posuna na policko:",pozicia_hraca)
            else:
                novy_riadok = ((rozmery_plochy-1) - pozicia_hraca[1] + posun)//rozmery_plochy + pozicia_hraca[0]
                    
                if novy_riadok >= rozmery_plochy:
                    print("Hrac c. 1 hodil viac bodov nez je vzdialenost do ciela!")
                else:
                    if novy_riadok%2 == 0:
                        novy_stlpec = ((rozmery_plochy-1) - pozicia_hraca[1] + posun)%rozmery_plochy
                    else:
                        novy_stlpec = (rozmery_plochy-1) - ((rozmery_plochy-1) - pozicia_hraca[1] + posun)%rozmery_plochy
                    pozicia_hraca = [novy_riadok,novy_stlpec]
                    print("Hrac c. 1 sa posuna na policko:",pozicia_hraca)

        if plocha[pozicia_hraca[0]][pozicia_hraca[1]] >= "A" and plocha[pozicia_hraca[0]][pozicia_hraca[1]] <= "E":
                pismeno = plocha[pozicia_hraca[0]][pozicia_hraca[1]]
                for i in range(pozicia_hraca[0]+1,rozmery_plochy):
                    for j in range(rozmery_plochy):
                        if plocha[i][j] == pismeno:
                            pozicia_hraca = [i,j]
                            print("Hrac c. 1 sa cez pozitivny telepor posuva na policko:",pozicia_hraca)
                            
        if plocha[pozicia_hraca[0]][pozicia_hraca[1]] >= "a" and plocha[pozicia_hraca[0]][pozicia_hraca[1]] <= "e":
                pismeno = plocha[pozicia_hraca[0]][pozicia_hraca[1]]
                for i in range(0,pozicia_hraca[0]):
                    for j in range(rozmery_plochy):
                        if plocha[i][j] == pismeno:
                            pozicia_hraca = [i,j]
                            print("Hrac c. 1 sa cez negativny telepor posuva na policko:",pozicia_hraca)
                          
        plocha[pozicia_hraca[0]][pozicia_hraca[1]] = 1
        vykresli_plochu()
        plocha[pozicia_hraca[0]][pozicia_hraca[1]] = povodna_plocha[pozicia_hraca[0]][pozicia_hraca[1]]

def simulacia_k_hracov():
    if rozmery_plochy < 5 or rozmery_plochy > 10:
        print("Nie je mozne vytvorit plochu s vami zadanymi rozmermy")
        return None
    if pocet_hracov < 1 or pocet_hracov > 4:
        print("Vas zadany pocet hracov nekoresponduje s pravidlami hry!")
        return None
    generuj_plochu()
    vykresli_plochu()

    povodna_plocha = copy.deepcopy(plocha)

    pozicie_hracov = []
    for i in range(pocet_hracov):
        pozicie_hracov.append([0,0])
    

    while True:
        for i in range(len(pozicie_hracov)):
            print("Pozicie hracov:")
            for m in range(len(pozicie_hracov)):
                print("Hrac c.",m+1,pozicie_hracov[m])
            print("---")

            cislo_na_kocke = random.randint(1,6)
            posun = cislo_na_kocke
            while cislo_na_kocke == 6:
                cislo_na_kocke = random.randint(1,6)
                posun += cislo_na_kocke
            print("Hrac c.",i+1,"hodil spolu na kocke:",posun,"bodov")
        
            if pozicie_hracov[i][0]%2 == 0:
                if pozicie_hracov[i][1] + posun <= rozmery_plochy-1:
                    pozicie_hracov[i] = [pozicie_hracov[i][0],pozicie_hracov[i][1]+posun]
                    print("Hrac c.",i+1,"sa posuna na policko:",pozicie_hracov[i])
                else:
                    novy_riadok = (pozicie_hracov[i][1] + posun)//rozmery_plochy + pozicie_hracov[i][0]
                    if novy_riadok >= rozmery_plochy:
                        print("Hrac c.",i+1,"hodil viac bodov nez je vzdialenost do ciela!")
                    else:
                        if novy_riadok%2 == 0:
                            novy_stlpec = (pozicie_hracov[i][1] + posun)%rozmery_plochy
                        else:
                            novy_stlpec = (rozmery_plochy-1) - ((pozicie_hracov[i][1] + posun)%rozmery_plochy)
                        pozicie_hracov[i] = [novy_riadok,novy_stlpec]
                        print("Hrac c.",i+1,"sa posuna na policko:",pozicie_hracov[i])
            else:
                if pozicie_hracov[i][1] - posun >= 0:
                    pozicie_hracov[i] = [pozicie_hracov[i][0],pozicie_hracov[i][1]-posun]
                    print("Hrac c.",i+1,"sa posuna na policko:",pozicie_hracov[i])
                else:
                    novy_riadok = ((rozmery_plochy-1) - pozicie_hracov[i][1] + posun)//rozmery_plochy + pozicie_hracov[i][0]
                        
                    if novy_riadok >= rozmery_plochy:
                        print("Hrac c.",i+1,"hodil viac bodov nez je vzdialenost do ciela!")
                    else:
                        if novy_riadok%2 == 0:
                            novy_stlpec = ((rozmery_plochy-1) - pozicie_hracov[i][1] + posun)%rozmery_plochy
                        else:
                            novy_stlpec = (rozmery_plochy-1) - ((rozmery_plochy-1) - pozicie_hracov[i][1] + posun)%rozmery_plochy
                        pozicie_hracov[i] = [novy_riadok,novy_stlpec]
                        print("Hrac c.",i+1,"sa posuna na policko:",pozicie_hracov[i])

            if povodna_plocha[pozicie_hracov[i][0]][pozicie_hracov[i][1]] >= "A" and povodna_plocha[pozicie_hracov[i][0]][pozicie_hracov[i][1]] <= "E":
                pismeno = povodna_plocha[pozicie_hracov[i][0]][pozicie_hracov[i][1]]
                for m in range(pozicie_hracov[i][0]+1,rozmery_plochy):
                    for j in range(rozmery_plochy):
                        if povodna_plocha[m][j] == pismeno:
                            pozicie_hracov[i] = [m,j]
                            print("Hrac c.",i+1,"sa cez pozitivny telepor posuva na policko:",pozicie_hracov[i])

            if povodna_plocha[pozicie_hracov[i][0]][pozicie_hracov[i][1]] >= "a" and povodna_plocha[pozicie_hracov[i][0]][pozicie_hracov[i][1]] <= "e":
                pismeno = povodna_plocha[pozicie_hracov[i][0]][pozicie_hracov[i][1]]
                for m in range(0,pozicie_hracov[i][0]):
                    for j in range(rozmery_plochy):
                        if povodna_plocha[m][j] == pismeno:
                            pozicie_hracov[i] = [m,j]
                            print("Hrac c.",i+1,"sa cez negativny telepor posuva na policko:",pozicie_hracov[i])

            for j in range(len(pozicie_hracov)):
                plocha[pozicie_hracov[j][0]][pozicie_hracov[j][1]] = j+1

            vykresli_plochu()

            for j in range(len(pozicie_hracov)):
                plocha[pozicie_hracov[j][0]][pozicie_hracov[j][1]] = povodna_plocha[pozicie_hracov[j][0]][pozicie_hracov[j][1]]
            
            for m in range(len(pozicie_hracov)):
                if rozmery_plochy%2 == 0:
                    if pozicie_hracov[m] == [rozmery_plochy-1,0]:
                        print("Hrac c.",m+1,"VYHRAL!")
                        exit()
                else:
                    if pozicie_hracov[m] == [rozmery_plochy-1,rozmery_plochy-1]:
                        print("Hrac c.",m+1,"VYHRAL!")
                        exit()

simulacia_k_hracov()