import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('lolo.csv')
#########################################
Adresses= df['Source']
Add0=list(Adresses)
Add=[]
for i in Add0:
    if i not in Add:
        Add.append(i)
#########################################
#Dans cet exemple on a collecte 40 adresses,
#Alors ce n<est pas pratique d'afficher la classification par protocole pour chaque adresse,
#Donc on va afficher a l<utilisateur la liste des adresses, puis il choisit l<adreese qu<il veut ,
#pour que le prgramme lui affiche la classification des protocoles pour cette adresse
#print(df.head(5))
print("La liste des adresses detectees dans ce traffic est: ")
print(Add)
#On donne la main a l'utilisateur pour saisir l<adresse
Adress= input("veuillez choisir une adresse!")
print('L\'adresse que vous avez choisi est ' ,Adress)
df_r=df[df.Source==Adress]
#Preparer les datasets des protocoles pour l'adresse choisie par l'utilisateur
A=df[df.Source==Adress]
Listes_des_protocoles0= []
Listes_des_protocoles0=list(A['Protocol'])
Listes_des_protocoles=[]
#Preparer la liste qui va contenir les protocoles qu'on a collcte du dataset
for i in Listes_des_protocoles0:
    if i not in Listes_des_protocoles:
        Listes_des_protocoles.append(i)
l=len(Listes_des_protocoles)
x2=[0]*l
#Calculer le nombre de paquets dans le traffic pour chaque protocole
for i in range (0,l):
    x2[i]=Listes_des_protocoles0.count(Listes_des_protocoles[i])
############################################################
some = sum(x2)
#Liste qui va contenir le pourcentage de chaque protocole
x3 = [0]*l
for i in range (0,l):
    j=(x2[i]/some)*100
    x3[i]=j
######################################################
# On va afficher chaque protocole avec son pourcentage dans le traffic
print('Voici le pourcentage de chaque protocole pour l\'adresse ',Adress)
for i in range(0, l):
    print(Listes_des_protocoles[i], ' : ' ,x3[i] ,'%')
print(Listes_des_protocoles)

#Présentation graphique

plt.bar(Listes_des_protocoles, x3)
plt.title('Pourcentage de chaque protocole pour l\'adresse '+Adress)
plt.xlabel('Les protocoles')
plt.ylabel('(%)')
plt.show()

