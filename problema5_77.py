with open("caracter.txt","w")as f:
    w=input('Dati caractere:')
    f.write(w)
a=[]
n=0
for i in range(0,len(w)):
    if w[i]=='a' or w[i]=='e' or w[i]=='i' or w[i]=='o' or w[i]=='u' or w[i]=='A' or w[i]=='E' or w[i]=='I' or w[i]=='O' or w[i]=='U':
        n+=1
        a.append(w[i])
print('Numarul de vocale in sirul dat:', n)
print('Vocalele din acest sir:', a)