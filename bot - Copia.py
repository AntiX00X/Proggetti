print("\nHey tu, come ti chiami?")
nome=input()
print("\nCiao " + nome +  " è un piacere conoscerti")

if(nome == "Admin"):
    print("salve mio signore")
else:
    print("Bel nome")

lunghezza_nome = len(nome)
lunghezza_nome_stringa = str(lunghezza_nome)
print("il tuo nome ha  " + lunghezza_nome_stringa + " lettere")


anno_di_nascita = input("\nIn che anno sei nato?")
anno_di_nascita_int = int(anno_di_nascita)
anno_corrente = input("\nIn che anno ci troviamo?")
anno_corrente_int = int(anno_corrente)
eta = anno_corrente_int - anno_di_nascita_int
print(nome + " hai esattamente " + str(eta) + "anni..." )

if(eta < 15):
  print("...beato te!")

if(eta > 18):
  print("mh non sei mica giovane")
  
risposta = ""
while(risposta != "chi è?"):
  print("\ntoc toc...")
  risposta = input()
print("un computer, PIRLA!")  





 
