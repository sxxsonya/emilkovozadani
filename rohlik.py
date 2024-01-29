print("Vitejte v aplikaci pro vypocet vzorecku pro obdelnik/kvadru")
print("Pro vypocet obvodu zadejte 1:")
print("Pro vypocet objemu zadejte 2:")
print("Pro vypocet obsahu zadejte 3:")
print("Pro ukonceni zadejte 4:")

#Deklarace (spise inicializace) promenych, nasledne do nich ukladame vstup
volba = input("Zadejte Vasi volbu: ")

if volba == 1:
    print("Zvolil jste si vypocet obvodu")
    a = int(input("Zadejte promenou a: "))
    b = int(input("Zadejte promenou b: "))
    c = int(input("Zadejte promenou c: "))

if a>0 and b>0 and c>0:
    vypocet = 2*a+2*b
    print("Vysledek je.. , vypocet, " cm ")
          else:
          print("Vsak nemuzes pracovat se zapornymi promenymi")


elif volba == 2:
    print("Zvolil jste si vypocet objemu")

    a = int(input("Zadejte promenou a: "))
    b = int(input("Zadejte promenou b: "))
    c = int(input("Zadejte promenou c: "))

if a>0 and b>0 and c>0:
    vypocet = a*b*c
        print("Vysledek je.. , vypocet, "cm")
     else:
     print("Vsak nemuzes pracovat se zapornymi promenymi")


elif volba == 3:
    print("Zvolil jste si vypocet obsahu")

a = int(input("Zadejte promenou a: "))
b = int(input("Zadejte promenou b: "))
c = int(input("Zadejte promenou c: "))

if a>0 and b>0 and c>0:
    vypocet = a*b
    print("Vysledek je.. , vypocet, " cm ")
          else:
          print("Vsak nemuzes pracovat se zapornymi promenymi")


elif volba == 4:
    print("Program se nyni ukonci")

else:
    #Davame uzivateli vedet, ze neco zadal asi spatne