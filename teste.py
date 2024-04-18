preferencia = input("O que você prefere fazer à noite?\n A - Ler Um livro \n B - Ir à uma festa\n")
if preferencia == "A":
    print("Lendo um livro, boa escola!")
elif preferencia == "B":
    print("Indo a uma festa, parece divertido!")
else:
    print("Você deve digitar A ou B, digamos que você gosta de ler")
    preferencia = "A"
emprego = input("Qual o seu emeprego dos sonhos? \n A - Ser um curador no Instituto Smithsonian \n B - Administrar uma empresa\n")
if emprego == "A":
    print("Curador, boa escolha!")
elif emprego == "B":
    print("Administrar um negócio? parece divertido!")
else:
    print("Você deve digitar A ou B, digamos que você quer ser curador")
    emprego = "A"
importancia = input("O que é mais importante? \n A - Dinheiro \n B - Amor\n")
if importancia == "A":
    print("Dinheiro, boa escolha!")
elif importancia == "B":
    print("Amor? boa escolha!")
else:
    print("Você deve digitar A ou B, mas digamos que dinheiro seja mais importante")
    importancia = "A"
decada = input("Qual a sua década favorita? \n A - Década de 1910 \n B - Década de 2010\n")
if decada == "A":
    print("1910, boa escolha!")
elif decada == "B":
    print("2010, parece divertido!")
else:
    print("Você deve digitar A ou B, mas digamos que 1910 seja sua década favorita!")
    decada = "A"
transporte = input("Qual é o seu modo favorito de viajar? \n A - Automóvel \n B - Avião\n")
if transporte == "A":
    print("Diriginto? boa escolha!")
elif transporte == "B":
    print("Voar? parece divertido!")
else:
    print("Você deve digitar A ou B, mas digamos que você prefere ir dirigindo!")
    transporte = "A"
#Criando variáveis para pontuação
#Sam perspicaz
#Kai animado
#Cam curioso
#Indy observador
sam = 0
cam = 0
kai = 0
indy = 0

#atualiza variáveis de pontuações com base na escolha de "preferencia".
if preferencia == "A":
    sam = sam + 2 
    indy = indy + 2
    kai = kai + 2
else:
    cam = cam + 1
    indy = indy + 1

if emprego == "A":
    sam = sam + 2
    indy = indy + 2
    cam = cam - 1
else:
    sam = sam - 1
    kai = kai + 2
    indy = indy + 1
if importancia == "A":
    sam = sam - 1
    kai = kai + 1
else:
    sam = sam + 2
    cam = cam + 2
    indy = indy + 1
if decada == "A":
    cam = cam + 2
    sam = sam + 2
else:
    kai = kai + 1
    indy = indy + 2
if transporte == "A":
    sam = sam - 2
    kai = kai + 1
    indy = indy - 1
else:
    kai = kai - 1
    cam = cam + 1
    sam = sam + 1

#Resultado:
if sam >= 3:
    print("Você é mais parecido com Sam de olhos aguçados")
elif cam >= 3:
    print("Você é mais parecido com Cam, o curioso")
elif kai >= 3:
    print("Você é mais parecido com Keen Kai, o animado")
else:
    print("Você é mais parecido com Indy, o observador ")