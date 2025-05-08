#creation d'une bitmap
#modules
from tkinter import *
from time import *
import winsound
#creation de la fenetre
Mafenetre=Tk()
Mafenetre.geometry('750x650')
#variable pour le bug du deplacement instantané
touches=[]
#variable de vie
vie=3
#variables pour le changement de matrice 
niveaux=0
ancien_niveaux=0
#variable dialogue
t=0
#variables objets
e=0
m=0
#voriables objectifs
c1=0
c2=0
c3=0
r=0
# =============================================================================
# Créations des Images et Matrices
# =============================================================================
#creation des cases images
carrénoir=PhotoImage(file="carré_noir.gif")
caseplancher=PhotoImage(file="plancher.gif")
casebibliothèque=PhotoImage(file="bibliothèque.gif")
caselit=PhotoImage(file="lit.gif")
caseplante_plancher=PhotoImage(file="plante_plancher.gif")
caseplante_mur=PhotoImage(file="plante_mur.gif")
casemur_bois=PhotoImage(file="mur_bois.gif")
casemarteau=PhotoImage(file="marteau.gif")
monte1=PhotoImage(file="link_face_gauche.gif")
monte2=PhotoImage(file="link_face_droite.gif")
carrénoirsortie=PhotoImage(file="carré_noir.gif")
button=PhotoImage(file="epeetf.gif")
fond=PhotoImage(file="fondfinal.gif")
fond_fin=PhotoImage(file="fin.gif")
fond_mort=PhotoImage(file="game_over.gif")
yes=PhotoImage(file="yes.gif")
no=PhotoImage(file="no.gif")
coeur_plein=PhotoImage(file="coeur_plein.gif")
coeur_plein2=PhotoImage(file="coeur_plein.gif")
nb_vie=PhotoImage(file="nb_vie.gif")
herbe=PhotoImage(file="herbe.gif")
herbe2=PhotoImage(file="herbe2.gif")
herbe3=PhotoImage(file="herbe3.gif")
arbre=PhotoImage(file="pin.gif")
chemin1=PhotoImage(file="chemin1.gif")
chemin2=PhotoImage(file="chemin2.gif")
viragegh=PhotoImage(file="virage1.gif")
viragedh=PhotoImage(file="virage2.gif")
viragebd=PhotoImage(file="virage3.gif")
viragebg=PhotoImage(file="virage4.gif")
mur_pierre=PhotoImage(file="mur_pierre.gif")
sol=PhotoImage(file="sol.gif")
gros_rocher=PhotoImage(file="gros_rocher.gif")
mur_pierre_mousse=PhotoImage(file="mur_pierre_mousse.gif")
coffre_fermé=PhotoImage(file="coffre_fermé.gif")
coffre_ouvert=PhotoImage(file="coffre_ouvert.gif")
enigme=PhotoImage(file="énigme.gif")
plaque_pression=PhotoImage(file="plaque_pression.gif")
droite1=PhotoImage(file="link_droite_gauche.gif")
droite2=PhotoImage(file="link_droite_droite.gif")
gauche1=PhotoImage(file="link_gauche_gauche.gif")
gauche2=PhotoImage(file="link_gauche_droite.gif")
monte1=PhotoImage(file="link_dos_gauche.gif")
monte2=PhotoImage(file="link_dos_droite.gif")
bas1=PhotoImage(file="link_face_gauche.gif")
bas2=PhotoImage(file="link_face_droite.gif")
marteaunoir=PhotoImage(file="marteau_noir.gif")
epeenoir=PhotoImage(file="épée_noir.gif")
sortie=PhotoImage(file="sortie.gif")
coeur_vide=PhotoImage(file="coeur_vide.gif")
entree=PhotoImage(file="entrée.gif")
croisementbas=PhotoImage(file="croisement_bas.gif")
croisementgauche=PhotoImage(file="croisement_gauche.gif")
lave=PhotoImage(file="lave.gif")
panneau=PhotoImage(file="panneau.gif")
entreeherbe=PhotoImage(file="entrée_herbe.gif")
entreecote=PhotoImage(file="entrée_côté.gif")
arbuste=PhotoImage(file="arbuste2.gif")
teleporteur=PhotoImage(file="téléporteur.gif")
epeeplante=PhotoImage(file="épée_plantée.gif")
colonne=PhotoImage(file="colonne.gif")
tapis=PhotoImage(file="tapis.gif")
tri=PhotoImage(file="tri.gif")
indice=PhotoImage(file="indice.gif")
croix=PhotoImage(file="croix.gif")
pierretombale=PhotoImage(file="pierre_tombale.gif")
regle=PhotoImage(file="règles.gif")
start=PhotoImage(file="start.gif")
tab_droite = [droite1,droite2]
tab_haut = [monte2,monte1]
tab_bas = [bas1,bas2]
tab_gauche = [gauche1,gauche2]
#liste pour les textes
tableau=["Déplacement : z,q,s,d / interaction : espace"," ","Vous n'êtes pas assez fort, progressez dans l'aventure pour être digne de le brandir","En brandissant l'épée de légende, un souffle de vigueur et de force vous emporte","Prononcez mon nom, et je disparais. Qui suis-je?","Le secret","Le caméléon","L'argent","Le silence","La vérité","Le son","Pour accéder au temple du vide, ramener la lumière dans le temple de l'ombre, il vous faudra;\nPuis triompher de l'épreuve de force tu devras"," → : Maison, ↑ : Epreuve de l'épée, ← : Temple de l'ombre, ↓ : Temple du vide","L'épée est à la feuille...","...ce que le marteau est à la roche","Le temple du vide vous est à présent accessible","Hommage à M.Alliot, qui dans sa difficile quête, sombra dans les bras de Morphée,\nlui révélant ainsi la clé","La destination du téléporteur a été modifiée","Des sens s'émoussent, des diformités se séparent soudainement de son squelette,\nquoi que Zelda quadrille quelques salle.","Pour vaincre ce piège machiavélique, qui dans une boucle vous a piégé, à l'épreuve de l'épée,\nla mort vous devez confronter","Cette aventure n'était qu'une illusion. Pour révéler la fin tant convoitée,\nles récits de votre vie passée, vous devez vous inspirer","vous n'avez pas sommeil"]
#creation de la matrice
L0=["E","E","E","E","E","E","E1","E2","E","E","E","nb_vie","Coeur0","Coeur1","Coeur2"]
L1=["E","E","E","E","E","E","E","E","E","E","E","E","E","E","E"]
L2=["E","E","B","B","B","B","V","V","V","B","B","B","B","E","E"]
L3=["E","E","B1","B","B","B","PM","M","PM","B","B","B","B","E","E"]
L4=["E","E","P","P","P","P","P","P","P","P","P","P","P","E","E"]
L5=["E","E","P","P","P","P","P","P","P","P","P","P","P","E","E"]
L6=["S1","P","P","P","P","P","P","P","P","P","P","P","L","E","E"]
L7=["E","E","P","P","P","P","P","P","P","P","P","P","P","E","E"]
L8=["E","E","P","P","P","P","P","P","P","P","P","P","P","E","E"]
L9=["E","E","P","P","P","P","P","P","P","P","P","P","P","E","E"]
L10=["E","E","P","P","P","P","P","P","P","P","P","P","P","E","E"]
L11=["E","E","E","E","E","E","E","E","E","E","E","E","E","E","E"]
L12=["E","E","E","E","E","E","E","E","E","E","E","E","E","E","E"]

ma_matrice0=[L0,L1,L2,L3,L4,L5,L6,L7,L8,L9,L10,L11,L12]

L0=["E","E","E","E","E","E","E1","E2","E","E","E","nb_vie","Coeur0","Coeur1","Coeur2"]
L1=["E","E","E","E","E","E","E","S2","E","E","E","E","E","E","E"]
L2=["E","E","H2","H2","H2","H3","MP","ENT","MP","H2","A","A","A","E","E"]
L3=["E","E","H2","H2","H3","H","H","ch2","H3","A","A","A","A","E","E"]
L4=["E","E","H2","A","Vbd","ch","ch","Vgh","A","A","A","A","A","E","E"]
L5=["E","E","A","H","ch2","A","A","A","I1","A","A","H2","H2","E","E"]
L6=["E","S10","ch","ch","Cgau","A","H3","H3","H3","A","Vbd","ch","ch","S0","E"]
L7=["E","E","H","H2","ch2","A","H2","A","A","H2","ch2","H","H","E","E"]
L8=["E","E","H2","H2","ch2","H2","H","PAN","H2","H3","ch2","H2","H2","E","E"]
L9=["E","E","H","H2","Vdh","ch","ch","Cbas","ch","ch","Vgh","H3","H2","E","E"]
L10=["E","E","H","A","H3","A","H2","ch2","H3","H2","H2","H3","H3","E","E"]
L11=["E","E","E","E","E","E","E","S11","E","E","E","E","E","E","E"]
L12=["E","E","E","E","E","E","E","E","E","E","E","E","E","E","E"]

ma_matrice1=[L0,L1,L2,L3,L4,L5,L6,L7,L8,L9,L10,L11,L12]

L0=["E","E","E","E","E","E","E1","E2","E","E","E","nb_vie","Coeur0","Coeur1","Coeur2"]
L1=["E","E","S4","E","S9","E","E","E","E","E","E","S4","E","E","E"]
L2=["E","E","sol","MP","sol","MP","sol","sol","sol","MP","MPM","sol","MPM","E","E"]
L3=["E","E","sol","MP","sol","sol","sol","MP","sol","sol","MP","sol","MPM","E","E"]
L4=["E","E","sol","MP","MPM","MP","MP","MP","MP","MP","MP","sol","sol","S3","E"]
L5=["E","E","sol","sol","sol","sol","sol","sol","sol","sol","MPM","MP","MPM","E","E"]
L6=["E","E","MP","MPM","sol","MPM","MP","MP","MPM","sol","sol","sol","sol","S3","E"]
L7=["E","S9","sol","sol","sol","sol","sol","sol","MP","sol","MP","MP","MPM","E","E"]
L8=["E","E","MP","MP","MP","MP","MPM","sol","MP","sol","sol","sol","sol","S3","E"]
L9=["E","S9","sol","sol","sol","sol","sol","sol","MP","MP","MP","MP","MPM","E","E"]
L10=["E","E","MP","MP","MP","MP","MPM","sor","MPM","sol","MP","sol","sol","S9","E"]
L11=["E","E","E","E","E","E","E","S1","E","E","E","E","E","E","E"]
L12=["E","E","E","E","E","E","E","E","E","E","E","E","E","E","E"]

ma_matrice2=[L0,L1,L2,L3,L4,L5,L6,L7,L8,L9,L10,L11,L12]

L0=["E","E","E","E","E","E","E1","E2","E","E","E","nb_vie","Coeur0","Coeur1","Coeur2"]
L1=["E","E","E","S5","E","S5","E","E","E","E","S5","E","S5","E","E"]
L2=["E","E","MP","sol","MPM","sol","MPM","sol","sol","MPM","sol","MPM","sol","E","E"]
L3=["E","E","MPM","sol","MP","sol","MPM","MP","MP","MP","sol","MP","sol","E","E"]
L4=["E","S2","sol","sol","sol","sol","MP","sol","sol","sol","sol","sol","sol","E","E"]
L5=["E","E","MPM","MP","MP","MP","MPM","sol","MPM","MP","MP","MP","MP","E","E"]
L6=["E","S9","sol","sol","sol","sol","MP","sol","sol","sol","sol","sol","sol","E","E"]
L7=["E","E","MPM","MP","MP","MP","MPM","sol","MP","MP","MP","MP","sol","E","E"]
L8=["E","S2","sol","sol","sol","MP","MPM","sol","sol","sol","sol","MP","sol","E","E"]
L9=["E","E","MPM","MP","sol","sol","sol","sol","MP","MP","sol","MP","sol","E","E"]
L10=["E","S2","sol","sol","sol","MP","MP","MP","MPM","MP","sol","MP","sol","E","E"]
L11=["E","E","E","E","E","E","E","E","E","E","S9","E","S9","E","E"]
L12=["E","E","E","E","E","E","E","E","E","E","E","E","E","E","E"]

ma_matrice3=[L0,L1,L2,L3,L4,L5,L6,L7,L8,L9,L10,L11,L12]

L0=["E","E","E","E","E","E","E1","E2","E","E","E","nb_vie","Coeur0","Coeur1","Coeur2"]
L1=["E","E","E","E","E","E","E","E","E","E","E","E","E","E","E"]
L2=["E","E","EN15","sol","sol","sol","MP","sol","sol","sol","sol","sol","sol","S5","E"]
L3=["E","E","sol","MPM","MP","MP","MP","MPM","sol","MPM","MP","MP","MPM","E","E"]
L4=["E","E","sol","MP","sol","sol","sol","sol","sol","sol","sol","sol","sol","E","E"]
L5=["E","E","sol","MP","sol","MPM","MP","MP","MPM","MP","MP","MP","sol","S9","E"]
L6=["E","E","sol","MPM","sol","MPM","sol","sol","sol","MP","sol","sol","sol","E","E"]
L7=["E","E","sol","sol","sol","MP","sol","MP","sol","sol","sol","MP","sol","E","E"]
L8=["E","E","MP","MPM","sol","MPM","MP","MP","MP","MP","MP","MP","MPM","E","E"]
L9=["E","E","sol","MP","sol","sol","sol","sol","sol","sol","sol","sol","MP","E","E"]
L10=["E","E","sol","MPM","sol","MPM","MP","MP","MP","MP","MPM","sol","MPM","E","E"]
L11=["E","E","S9","E","S2","E","E","E","E","E","E","S2","E","E","E"]
L12=["E","E","E","E","E","E","E","E","E","E","E","E","E","E","E"]

ma_matrice4=[L0,L1,L2,L3,L4,L5,L6,L7,L8,L9,L10,L11,L12]

L0=["E","E","E","E","E","E","E1","E2","E","E","E","nb_vie","Coeur0","Coeur1","Coeur2"]
L1=["E","E","E","E","E","E","E","E","E","E","E","S9","E","E","E"]
L2=["E","S4","sol","sol","MP","TEL1","sol","sol","sol","sol","MPM","TEL9","MPM","E","E"]
L3=["E","E","MPM","sol","MPM","sol","sol","EPP","sol","sol","MP","sol","MP","E","E"]
L4=["E","E","MP","sol","MP","sol","sol","sol","sol","sol","MP","sol","MP","E","E"]
L5=["E","E","MP","sol","MP","MP","MP","MP","MP","MP","MP","sol","MP","E","E"]
L6=["E","E","MPM","sol","MPM","sol","sol","sol","sol","MPM","MPM","sol","MPM","E","E"]
L7=["E","E","MP","sol","sol","sol","MPM","MPM","sol","sol","sol","sol","sol","S9","E"]
L8=["E","E","MPM","MP","MPM","MP","MPM","MP","MP","MPM","MP","MPM","MP","E","E"]
L9=["E","E","sol","sol","MP","sol","sol","sol","sol","sol","sol","MP","sol","E","E"]
L10=["E","E","sol","sol","MPM","sol","MPM","MP","MP","MPM","sol","MPM","sol","E","E"]
L11=["E","E","E","S9","E","S3","E","E","E","E","S3","E","S9","E","E"]
L12=["E","E","E","E","E","E","E","E","E","E","E","E","E","E","E"]

ma_matrice5=[L0,L1,L2,L3,L4,L5,L6,L7,L8,L9,L10,L11,L12]

L0=["E","E","E","E","E","E","E1","E2","E","E","E","nb_vie","Coeur0","Coeur1","Coeur2"]
L1=["E","E","E","E","E","E","E","E","E","E","E","E","E","E","E"]
L2=["E","E","CRF1","sol","MP","sol","MP","sol","sol","sol","MP","sol","sol","E","E"]
L3=["E","E","MPM","sol","MPM","sol","MPM","sol","MPM","MP","MP","MPM","sol","E","E"]
L4=["E","E","MPM","sol","MP","sol","sol","sol","MP","sol","sol","sol","sol","E","E"]
L5=["E","E","sol","sol","MP","MP","MPM","sol","sol","sol","MP","MPM","MP","E","E"]
L6=["E","E","sol","MP","sol","sol","MPM","sol","MPM","sol","sol","sol","sol","S12","E"]
L7=["E","E","sol","MPM","sol","MP","sol","sol","MP","MPM","sol","MP","MP","E","E"]
L8=["E","E","sol","sol","sol","sol","sol","MP","MPM","MP","sol","sol","sol","E","E"]
L9=["E","E","sol","MPM","MP","sol","MP","sol","sol","sol","sol","MP","sol","E","E"]
L10=["E","E","sol","MPM","sol","sol","MP","sor1","sol","MP","MPM","sol","sol","E","E"]
L11=["E","E","E","E","E","E","E","S7","E","E","E","E","E","E","E"]
L12=["E","E","E","E","E","E","E","E","E","E","E","E","E","E","E"]

ma_matrice6=[L0,L1,L2,L3,L4,L5,L6,L7,L8,L9,L10,L11,L12]

L0=["E","E","E","E","E","E","E1","E2","E","E","E","nb_vie","Coeur0","Coeur1","Coeur2"]
L1=["E","E","E","E","E","E","E","S6","E","E","E","E","E","E","E"]
L2=["E","E","MPM","MP","MP","MPM","MPM","sol","MPM","MPM","MP","MP","MPM","E","E"]
L3=["E","E","sol","sol","sol","sol","sol","sol","sol","sol","sol","sol","sol","E","E"]
L4=["E","E","sol","sol","sol","sol","sol","sol","sol","sol","sol","sol","sol","E","E"]
L5=["E","E","sol","sol","sol","sol","GR","GR","GR","sol","sol","sol","sol","E","E"]
L6=["E","E","sol","sol","sol","sol","GR","CRF2","GR","sol","sol","sol","sol","E","E"]
L7=["E","E","sol","sol","sol","sol","GR","GR","GR","sol","sol","sol","sol","E","E"]
L8=["E","E","sol","sol","sol","sol","sol","sol","sol","sol","sol","sol","sol","E","E"]
L9=["E","E","sol","sol","sol","sol","sol","sol","sol","sol","sol","sol","sol","E","E"]
L10=["E","E","MPM","MPM","MP","MP","MPM","MPM","MPM","MP","MP","MPM","MPM","E","E"]
L11=["E","E","E","E","E","E","E","E","E","E","E","E","E","E","E"]
L12=["E","E","E","E","E","E","E","E","E","E","E","E","E","E","E"]

ma_matrice7=[L0,L1,L2,L3,L4,L5,L6,L7,L8,L9,L10,L11,L12]

L0=["E","E","E","E","E","E","E1","E2","E","E","E","nb_vie","Coeur0","Coeur1","Coeur2"]
L1=["E","E","E","E","E","E","E","E","E","E","E","E","E","E","E"]
L2=["E","E","MPM","MP","MPM","MPM","MP","MP","MP","MPM","MPM","MP","MPM","E","E"]
L3=["E","E","TEL11","sol","sol","sol","sol","sol","sol","sol","sol","sol","sol","E","E"]
L4=["E","E","sol","sol","sol","sol","sol","EN1","sol","sol","sol","sol","sol","E","E"]
L5=["E","E","Pl2","sol","sol","Pl3","sol","sol","sol","Pl4","sol","sol","Pl5","E","E"]
L6=["E","E","EN3","sol","sol","EN4","sol","sol","sol","EN5","sol","sol","EN6","E","E"]
L7=["E","E","sol","sol","sol","sol","sol","sol","sol","sol","sol","sol","sol","E","E"]
L8=["E","E","Pl1","sol","sol","MP","MP","MP","MP","MP","sol","sol","Pl6","E","E"]
L9=["E","E","EN2","sol","sol","MP","TEL1","sol","sol","MP","sol","sol","EN7","E","E"]
L10=["E","E","sol","sol","sol","MP","sol","sor","sol","MP","sol","sol","sol","E","E"]
L11=["E","E","E","E","E","E","E","S15","E","E","E","E","E","E","E"]
L12=["E","E","E","E","E","E","E","E","E","E","E","E","E","E","E"]

ma_matrice8=[L0,L1,L2,L3,L4,L5,L6,L7,L8,L9,L10,L11,L12]

L0=["E","E","E","E","E","E","E1","E2","E","E","E","nb_vie","Coeur0","Coeur1","Coeur2"]
L1=["E","E","E","E","E","E","E","E","E","E","E","E","E","E","E"]
L2=["E","E","sol","sol","sol","TEL1","sol","sol","sol","TEL51","sol","sol","sol","E","E"]
L3=["E","E","sol","sol","sol","sol","sol","sol","sol","sol","sol","sol","sol","E","E"]
L4=["E","E","TEL1","sol","MPM","MPM","MP","MP","MP","MPM","MPM","sol","TEL1","E","E"]
L5=["E","E","sol","sol","MPM","LA","LA","LA","LA","LA","MPM","sol","sol","E","E"]
L6=["E","E","sol","sol","MP","LA","LA","sol","LA","LA","MP","sol","sol","E","E"]
L7=["E","E","sol","sol","MPM","LA","LA","LA","LA","LA","MPM","sol","sol","E","E"]
L8=["E","E","TEL1","sol","MPM","MPM","MP","MP","MP","MPM","MPM","sol","TEL52","E","E"]
L9=["E","E","sol","sol","sol","sol","sol","sol","sol","sol","sol","sol","sol","E","E"]
L10=["E","E","sol","sol","sol","TEL1","sol","sol","sol","TEL1","sol","sol","sol","E","E"]
L11=["E","E","E","E","E","E","E","E","E","E","E","E","E","E","E"]
L12=["E","E","E","E","E","E","E","E","E","E","E","E","E","E","E"]

ma_matrice9=[L0,L1,L2,L3,L4,L5,L6,L7,L8,L9,L10,L11,L12]

L0=["E","E","E","E","E","E","E1","E2","E","E","E","nb_vie","Coeur0","Coeur1","Coeur2"]
L1=["E","E","E","E","E","E","E","E","E","E","E","E","E","E","E"]
L2=["E","E","A","H2","H","H2","A","H3","H2","H2","H2","H","H3","E","E"]
L3=["E","E","H3","Vbd","ch","ch","ch","ch","Vdg","A","H2","H2","H3","E","E"]
L4=["E","E","H2","ch2","H2","A","A","H2","ch2","H2","A","H2","A","E","E"]
L5=["E","E","H3","ch2","A","H3","H3","A","ch2","A","H2","A","A","E","E"]
L6=["E","E","A","ch2","H2","A","H3","H3","Vdh","ch","ch","ch","ch","S1","E"]
L7=["E","E","A","ch2","H2","H2","A","A","A","H2","H3","A","H3","E","E"]
L8=["E","E","H3","Vdh","ch","ch","ch","Vdg","H2","A","A","I2","A","E","E"]
L9=["E","E","H2","H2","A","H","H3","ch2","A","H2","A","H3","H2","E","E"]
L10=["E","E","A","H2","H2","H2","H2","ch2","A","H2","H3","H2","H2","E","E"]
L11=["E","E","E","E","E","E","E","S12","E","E","E","S12","E","E","E"]
L12=["E","E","E","E","E","E","E","E","E","E","E","E","E","E","E"]

ma_matrice10=[L0,L1,L2,L3,L4,L5,L6,L7,L8,L9,L10,L11,L12]

L0=["E","E","E","E","E","E","E1","E2","E","E","E","nb_vie","Coeur0","Coeur1","Coeur2"]
L1=["E","E","E","E","E","E","E","S1","E","E","E","E","E","E","E"]
L2=["E","E","A","A","H","H2","H2","ch2","H2","A","H2","A","H","E","E"]
L3=["E","E","A","H","A","H2","H2","ch2","H2","H2","A","A","H3","E","E"]
L4=["E","E","H2","A","H","A","H2","H2","A","H2","H2","A","H3","E","E"]
L5=["E","E","H2","H","H2","H3","H2","H2","H3","A","A","H","H3","E","E"]
L6=["E","S12","H","H3","A","H3","H2","A","H2","H","H2","A","H","E","E"]
L7=["E","E","A","A","H2","H2","A","A","I3","H2","H2","H","H3","E","E"]
L8=["E","E","H2","H2","H2","H3","H3","H","H2","A","H2","A","H2","E","E"]
L9=["E","E","H3","A","H3","H2","H2","H2","H3","H3","H","A","H2","E","E"]
L10=["E","E","H","A","H3","A","MPM","EH","MPM","A","A","H2","A","E","E"]
L11=["E","E","E","E","E","E","E","S13","E","E","E","E","E","E","E"]
L12=["E","E","E","E","E","E","E","E","E","E","E","E","E","E","E"]

ma_matrice11=[L0,L1,L2,L3,L4,L5,L6,L7,L8,L9,L10,L11,L12]

L0=["E","E","E","E","E","E","E1","E2","E","E","E","nb_vie","Coeur0","Coeur1","Coeur2"]
L1=["E","E","E","E","E","E","E","S10","E","E","E","S10","E","E","E"]
L2=["E","E","H3","A","H2","H2","H2","ch2","H2","H3","H2","H2","A","E","E"]
L3=["E","E","H3","A","A","H3","H2","ch2","H2","H3","H3","H2","H2","E","E"]
L4=["E","E","H","H","H2","H2","A","H2","H2","A","H2","H2","A","E","E"]
L5=["E","E","MPM","A","A","H3","H2","H2","H","A","A","H","H2","E","E"]
L6=["E","S6","EC","ARB","H","H2","A","H3","H3","H3","H2","H3","H2","S11","E"]
L7=["E","E","MPM","A","H2","A","H2","A","H2","A","H2","H3","H2","E","E"]
L8=["E","E","H2","H2","H2","H2","H","A","H2","H","H2","H2","A","E","E"]
L9=["E","E","A","H3","H3","H","A","H2","A","H2","A","A","H3","E","E"]
L10=["E","E","H2","A","H2","H2","H2","H3","H","H2","A","H2","H2","E","E"]
L11=["E","E","E","E","E","E","E","E","E","E","E","E","E","E","E"]
L12=["E","E","E","E","E","E","E","E","E","E","E","E","E","E","E"]

ma_matrice12=[L0,L1,L2,L3,L4,L5,L6,L7,L8,L9,L10,L11,L12]

L0=["E","E","E","E","E","E","E1","E2","E","E","E","nb_vie","Coeur0","Coeur1","Coeur2"]
L1=["E","E","E","E","E","E","E","S11","E","E","E","E","E","E","E"]
L2=["E","E","MP","MPM","MPM","MP","MPM","sol","MPM","MP","MPM","MPM","MP","E","E"]
L3=["E","S9","sol","sol","sol","sol2","sol2","sol","sol","sol2","sol","sol2","sol","S9","E"]
L4=["E","E","sol2","sol2","sol","sol2","sol2","sol2","sol","sol2","sol","sol2","sol","E","E"]
L5=["E","E","sol","sol","sol","sol","sol","sol","sol","sol","sol","sol","sol","E","E"]
L6=["E","E","sol","sol2","sol2","sol2","sol","sol2","sol","sol2","sol","sol2","sol2","E","E"]
L7=["E","E","sol","sol","sol","sol2","sol2","sol2","sol","sol2","sol","sol","sol","S9","E"]
L8=["E","E","sol","sol2","sol","sol","sol","sol2","sol2","sol2","sol","sol","sol2","E","E"]
L9=["E","E","sol","sol","sol2","sol","sol2","sol","sol","sol","sol2","sol","sol","S9","E"]
L10=["E","E","MP","sol","MPM","sol","MP","sol","MP","sol","MPM","sol","MP","E","E"]
L11=["E","E","E","S9","E","S9","E","S14","E","S14","E","S14","E","E","E"]
L12=["E","E","E","E","E","E","E","E","E","E","E","E","E","E","E"]

ma_matrice13=[L0,L1,L2,L3,L4,L5,L6,L7,L8,L9,L10,L11,L12]

L0=["E","E","E","E","E","E","E1","E2","E","E","E","nb_vie","Coeur0","Coeur1","Coeur2"]
L1=["E","E","E","E","E","E","E","S13","E","S13","E","S13","E","E","E"]
L2=["E","E","MPM","MPM","MP","MP","MP","sol","MP","sol","MPM","sol","MP","E","E"]
L3=["E","E","sol","sol","sol","sol","sol","sol","MPM","sol","sol","sol","sol","E","E"]
L4=["E","E","sol","MPM","MPM","MP","MP","MP","MP","MPM","MP","MP","MP","E","E"]
L5=["E","E","sol","TEL1","MP","sol","TEL81","MPM","sol","TEL12","MP","sol","TEL82","E","E"]
L6=["E","E","sol","sol","MPM","sol","sol","MP","sol","sol","MPM","sol","sol","E","E"]
L7=["E","E","sol","TEL141","MP","sol","TEL4","MPM","sol","TEL2","MP","sol","TEL10","E","E"]
L8=["E","E","sol","sol","MP","sol","sol","MPM","sol","sol","MPM","sol","sol","E","E"]
L9=["E","E","sol","TEL6","MP","sol","TEL0","MP","sol","TEL143","MP","sol","TEL7","E","E"]
L10=["E","E","MP","MP","MPM","MP","MP","MP","MP","MP","MP","MPM","MP","E","E"]
L11=["E","E","E","E","E","E","E","E","E","E","E","E","E","E","E"]
L12=["E","E","E","E","E","E","E","E","E","E","E","E","E","E","E"]

ma_matrice14=[L0,L1,L2,L3,L4,L5,L6,L7,L8,L9,L10,L11,L12]

L0=["E","E","E","E","E","E","E1","E2","E","E","E","nb_vie","Coeur0","Coeur1","Coeur2"]
L1=["E","E","E","E","E","E","E","S8","E","E","E","E","E","E","E"]
L2=["E","E","MP","MP","MP","MP","MP","TAP","MP","MP","MP","MP","MP","E","E"]
L3=["E","E","MP","sol","sol","CO","sol","TAP","sol","CO","sol","sol","MP","E","E"]
L4=["E","E","MP","sol","sol","CO","sol","TAP","sol","CO","sol","sol","MP","E","E"]
L5=["E","E","MP","sol","sol","CO","sol","TAP","sol","CO","sol","sol","MP","E","E"]
L6=["E","E","MP","sol","sol","CO","sol","TAP","sol","CO","sol","sol","MP","E","E"]
L7=["E","E","MP","sol","sol","sol","sol","TAP","sol","sol","sol","sol","MP","E","E"]
L8=["E","E","MP","sol","sol","sol","sol","TRI","sol","sol","sol","sol","MP","E","E"]
L9=["E","E","MP","sol","sol","sol","sol","sol","sol","sol","sol","sol","MP","E","E"]
L10=["E","E","MP","MP","MP","MP","MP","MP","MP","MP","MP","MP","MP","E","E"]
L11=["E","E","E","E","E","E","E","E","E","E","E","E","E","E","E"]
L12=["E","E","E","E","E","E","E","E","E","E","E","E","E","E","E"]

ma_matrice15=[L0,L1,L2,L3,L4,L5,L6,L7,L8,L9,L10,L11,L12]

L0=["E","E","E","E","E","E","E1","E2","E","E","E","nb_vie","Coeur0","Coeur1","Coeur2"]
L1=["E","E","E","E","E","E","E","E","E","E","E","E","E","E","E"]
L2=["E","E","MP","MP","MP","MP","MP","MP","MP","MP","MP","MP","MP","E","E"]
L3=["E","E","MP","A","A","H","H3","CR","H3","H","A","A","MP","E","E"]
L4=["E","E","MP","A","H3","H","H3","PI","H3","H","H3","A","MP","E","E"]
L5=["E","E","MP","H","H3","H","H2","H2","H2","H","H3","H","MP","E","E"]
L6=["E","E","MP","H2","H3","H3","H3","H3","H3","H3","H3","H2","MP","E","E"]
L7=["E","E","MP","H","H","H","H2","H2","H2","H","H","H","MP","E","E"]
L8=["E","E","MP","A","H3","H3","H3","H3","H3","H3","H3","A","MP","E","E"]
L9=["E","E","MP","A","A","H","H2","H2","H2","H","A","A","MP","E","E"]
L10=["E","E","MP","MP","MP","MP","MP","TEL1","MP","MP","MP","MP","MP","E","E"]
L11=["E","E","E","E","E","E","E","E","E","E","E","E","E","E","E"]
L12=["E","E","E","E","E","E","E","E","E","E","E","E","E","E","E"]

ma_matrice16=[L0,L1,L2,L3,L4,L5,L6,L7,L8,L9,L10,L11,L12]

#creation de la map
dico={"E":carrénoir,"E1":carrénoir,"E2":carrénoir,"P":caseplancher,"V":casemur_bois,"PP":caseplante_plancher,"PM":caseplante_mur,"M":casemarteau,"B":casebibliothèque,"B1":casebibliothèque,"ENT":entree,"PAN":panneau,"EH":entreeherbe,"EC":entreecote,"ARB":arbuste,"TEL":teleporteur,"EPP":epeeplante,"CO":colonne,"I1":indice,"I2":indice,"CR":croix,
"L":caselit,"S0":carrénoirsortie,"S1":carrénoirsortie,"S2":carrénoirsortie,"S3":carrénoirsortie,"S4":carrénoirsortie,"S5":carrénoirsortie,"S6":carrénoirsortie,"S7":carrénoirsortie,"S8":carrénoirsortie,"S9":carrénoirsortie,"S10":carrénoirsortie,"S11":carrénoirsortie,"S12":carrénoirsortie,"S13":carrénoirsortie,"S14":carrénoirsortie,"S15":carrénoirsortie,"S16":carrénoirsortie
,"Coeur0":coeur_plein,"Coeur2":coeur_plein,"Coeur1":coeur_plein2,"nb_vie":nb_vie,"H":herbe,"H2":herbe2,"H3":herbe3,"A":arbre,"ch":chemin1,"ch2":chemin2,"Vgh":viragegh,"Vdh":viragedh,"Cbas":croisementbas,"Cgau":croisementgauche,"LA":lave,"TAP":tapis,"TRI":tri,"PI":pierretombale,"I3":indice
,"Vbd":viragebd,"Vdg":viragebg,"MP":mur_pierre,"sol":sol,"sol2":sol,"MPM":mur_pierre_mousse,"GR":gros_rocher,"CRF1":coffre_fermé,"CRF2":coffre_fermé,"TEL9":teleporteur,"TEL51":teleporteur,"TEL52":teleporteur,"TEL1":teleporteur,"TEL0":teleporteur,"TEL2":teleporteur,"TEL4":teleporteur,"TEL6":teleporteur,"TEL7":teleporteur,"TEL12":teleporteur,"TEL10":teleporteur,"TEL141":teleporteur,"TEL142":teleporteur,"TEL143":teleporteur,"TEL82":teleporteur,"TEL81":teleporteur,"TEL11":teleporteur
,"EN1":enigme,"EN2":enigme,"EN3":enigme,"EN4":enigme,"EN5":enigme,"EN15":enigme,"EN6":enigme,"EN7":enigme,"EN8":enigme,"EN9":enigme,"Pl1":plaque_pression,"Pl2":plaque_pression,"Pl3":plaque_pression,"Pl4":plaque_pression,"Pl5":plaque_pression,"Pl6":plaque_pression,"sor":sortie,"sor1":sortie,"sor2":sortie}
#les interdits
interdites = ["B1","I1","I2","I3","MPM","CRF1","CRF2","EN15","EN1","EN2","EN3","EN4","EN5","EN6","EN7","EN8","EN9","E","V","PP","PM","M","B","S0","S1","S2","S3","S4","S5","S6","S7","S8","S9","S10","S11","S12","S13","S14","S15","S16","L","A","MP","PAN","ARB","EPP","CO","TRI","I","CR","PI","EPP","GR"]
#liste des matrices pour les variables de changement
matrice = [ma_matrice0,ma_matrice1,ma_matrice2,ma_matrice3,ma_matrice4,ma_matrice5,ma_matrice6,ma_matrice7,ma_matrice8,ma_matrice9,ma_matrice10,ma_matrice11,ma_matrice12,ma_matrice13,ma_matrice14,ma_matrice15,ma_matrice16]
# =============================================================================
# MENU
# =============================================================================
def menu():
    """creation du menu"""
    global can,fond,button
    can=Canvas(Mafenetre,width=750,height=650)
    can.place(x=0,y=0)
    image_fond=can.create_image(0,0,image=fond,anchor="nw")
    bouton1 = Button(Mafenetre,command=intro)
    bouton1.place(x=345,y=255)
    bouton1.config(image = button,width=54,height=141,bd=0)
    winsound.PlaySound("sound.wav", winsound.SND_ASYNC)

def intro():
    global can,fond,button
    can.destroy()
    can=Canvas(Mafenetre,width=750,height=650)
    can.place(x=0,y=0)
    image_fond=can.create_image(0,0,image=regle,anchor="nw")
    bouton4 = Button(Mafenetre,command=jeu)
    bouton4.place(x=175,y=500)
    bouton4.config(image = start,width=400,height=84,bd=0)
    winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
# =============================================================================
# FONCTIONS PRINCIPALES
# =============================================================================
def jeu() :
    """initialisation du jeu"""
    global posY,posX,perso,can1,compteur_de_pas,dialogue,r
    #musique
    winsound.PlaySound("house_music.wav", winsound.SND_ASYNC)
    #zone de dessin
    can1=Canvas(Mafenetre,bg="white",width=750,height=650)
    can1.place(x=0,y=0)
    compteur_de_pas = 0
    #dessin du niveau
    for i in range(13):
        for j in range(15):
            can1.create_image(50*j,50*i,image=dico[matrice[niveaux][i][j]],anchor="nw")
    #creation texte
    dialogue = can1.create_text(25,560,text="",fill="white",font=("Arial",12),anchor="nw")
            
    #position du personnage
    posX=550  #abscisse de départ
    posY=300 #ordonnée de départ
    perso=can1.create_image(posX,posY,image=monte2,anchor="nw")
    #teste pour un texte
    if r == 1:
        t=-2
        can1.itemconfig(dialogue,text=tableau[t])
    
    #attente d'événement sur le can1
    can1.focus_set()
    can1.bind("<KeyPress>",Clavier)
    can1.bind("<KeyRelease>",released)


#evenement sur le clavier
def Clavier(event):
    """fonction qui se met en route
       à l'appuie d'une touche"""    
    global t,dialogue,can1,dico,tableau,e,c1,c2,m,r,matrice,niveaux,touche
    touche = event.keysym
    print(touche)
    #teste pour le bug de déplacement
    if not touche in touches:
        touches.append(touche)
        #position du personnage en ligne et colonne
        ligne = posY // 50
        colonne = posX // 50
        #texte des controles disparait après qu'une touche de déplacement est appuyé
        can1.itemconfig(dialogue,text=tableau[t])
        #condition pour le déplacement
        if touche == "z" and matrice[niveaux][ligne-1][colonne] not in interdites and ligne-1>=0:
            t=1
            mvt_haut()        
        elif touche == "d" and matrice[niveaux][ligne][colonne+1] not in interdites and colonne-1<=len(matrice[niveaux][0]):
            t=1
            mvt_droite()       
        elif touche == "q" and matrice[niveaux][ligne][colonne-1] not in interdites and colonne>=0:
            t=1
            mvt_gauche() 
        elif touche == "s" and matrice[niveaux][ligne+1][colonne] not in interdites :
            t=1
            mvt_bas()
        #condition de tout les interaction disponible
        elif touche == "space":
            #interaction avec le marteau
            if matrice[niveaux][ligne-1][colonne] == "M":
                if e != 1:
                    t=2
                    can1.itemconfig(dialogue,text=tableau[t])
                else:
                    can1.create_image(colonne*50,(ligne-1)*50,image=casemur_bois,anchor="nw")
                    dico["M"]=casemur_bois
                    can1.create_image(colonne*50,(ligne-4)*50,image=marteaunoir,anchor="nw")
                    dico["E2"]=marteaunoir
                    m=1
            #interaction avec l'epee
            elif matrice[niveaux][ligne-1][colonne] == "EPP":
                can1.create_image(colonne*50,(ligne-1)*50,image=sol,anchor="nw")
                dico["EPP"]=sol
                can1.create_image(300,0,image=epeenoir,anchor="nw")
                dico["E1"]=epeenoir
                t=3
                e=1
                matrice[niveaux][ligne-1][colonne] = "sol"
                can1.after(500,niveau)
            elif matrice[niveaux][ligne+1][colonne] == "EPP":
                can1.create_image(colonne*50,(ligne+1)*50,image=sol,anchor="nw")
                dico["EPP"]=sol
                can1.create_image(300,0,image=epeenoir,anchor="nw")
                dico["E1"]=epeenoir
                t=3
                e=1
                matrice[niveaux][ligne+1][colonne] = "sol"
                can1.after(500,niveau)               
            elif matrice[niveaux][ligne][colonne+1] == "EPP":
                can1.create_image((colonne+1)*50,ligne*50,image=sol,anchor="nw")
                dico["EPP"]=sol
                can1.create_image(300,0,image=epeenoir,anchor="nw")
                dico["E1"]=epeenoir
                t=3
                e=1
                matrice[niveaux][ligne][colonne+1] = "sol"
                can1.after(500,niveau)
            elif matrice[niveaux][ligne][colonne-1] == "EPP":
                can1.create_image((colonne-1)*50,ligne*50,image=sol,anchor="nw")
                dico["EPP"]=sol
                can1.create_image(300,0,image=epeenoir,anchor="nw")
                dico["E1"]=epeenoir
                t=3
                e=1
                matrice[niveaux][ligne][colonne-1] = "sol"
                can1.after(500,niveau)
            #interaction avec les steles
            elif matrice[niveaux][ligne-1][colonne][:2] == "EN":
                t=3+int(matrice[niveaux][ligne-1][colonne][2:])
                can1.itemconfig(dialogue,text=tableau[t])
            #interaction avec les differents panneaux
            elif matrice[niveaux][ligne-1][colonne] == "PAN":
                t=12
                can1.itemconfig(dialogue,text=tableau[t])
            elif matrice[niveaux][ligne-1][colonne] == "I1":
                t=13
                can1.itemconfig(dialogue,text=tableau[t])
            elif matrice[niveaux][ligne-1][colonne] == "I2":
                t=14
                can1.itemconfig(dialogue,text=tableau[t])
            elif matrice[niveaux][ligne-1][colonne] == "I3":
                t=11
                can1.itemconfig(dialogue,text=tableau[t])
            #interaction avec la pierre tombale
            elif matrice[niveaux][ligne-1][colonne] == "PI":
                t=16
                can1.itemconfig(dialogue,text=tableau[t])
            #interaction avec les coffres
            elif matrice[niveaux][ligne-1][colonne]=="CRF1":
                c1=1
                can1.create_image(colonne*50,(ligne-1)*50,image=coffre_ouvert,anchor="nw")
                dico["CRF1"]=coffre_ouvert
            elif matrice[niveaux][ligne][colonne-1]=="CRF1":
                c1=1
                can1.create_image((colonne-1)*50,ligne*50,image=coffre_ouvert,anchor="nw")
                dico["CRF1"]=coffre_ouvert
            elif matrice[niveaux][ligne+1][colonne]=="CRF2":
                c2=1
                can1.create_image(colonne*50,(ligne+1)*50,image=coffre_ouvert,anchor="nw")
                dico["CRF2"]=coffre_ouvert
                t=15
                can1.itemconfig(dialogue,text=tableau[t])
            elif matrice[niveaux][ligne][colonne+1]=="CRF2":
                c2=1
                can1.create_image((colonne+1)*50,ligne*50,image=coffre_ouvert,anchor="nw")
                dico["CRF2"]=coffre_ouvert
                t=15
                can1.itemconfig(dialogue,text=tableau[t])
            elif matrice[niveaux][ligne-1][colonne]=="CRF2":
                c2=15
                can1.create_image(colonne*50,(ligne-1)*50,image=coffre_ouvert,anchor="nw")
                dico["CRF2"]=coffre_ouvert
                t=15
                can1.itemconfig(dialogue,text=tableau[t])
            elif matrice[niveaux][ligne][colonne-1]=="CRF2":
                c2=15
                can1.create_image((colonne-1)*50,ligne*50,image=coffre_ouvert,anchor="nw")
                dico["CRF2"]=coffre_ouvert
                t=15
                can1.itemconfig(dialogue,text=tableau[t])
            #interaction avec les gros rochers
            elif matrice[niveaux][ligne][colonne-1]=="GR" and m==1:
                dico["GR"]=sol
                can1.after(500,niveau)
                interdites[-1] = ""
            elif matrice[niveaux][ligne][colonne+1]=="GR" and m==1:
                dico["GR"]=sol
                can1.after(500,niveau)
                interdites[-1] = ""
            elif matrice[niveaux][ligne-1][colonne]=="GR" and m==1:
                dico["GR"]=sol
                can1.after(500,niveau)
                interdites[-1] = ""
            elif matrice[niveaux][ligne+1][colonne]=="GR" and m==1:
                dico["GR"]=sol
                can1.after(500,niveau)
                interdites[-1] = ""
            #interaction avec les arbustes
            elif matrice[niveaux][ligne][colonne-1]=="ARB" and e==1:
                matrice[niveaux][ligne][colonne-1]="H"
                can1.after(500,niveau)
            #interaction avec le triple triangle
            elif matrice[niveaux][ligne][colonne-1]=="TRI" or matrice[niveaux][ligne][colonne+1]=="TRI" or matrice[niveaux][ligne-1][colonne]=="TRI" or matrice[niveaux][ligne+1][colonne]=="TRI" :
                reset()
                jeu()
            #interaction avec la bibliothèque
            elif matrice[niveaux][ligne-1][colonne]=="B1" and r>=1:
                t=19
                can1.itemconfig(dialogue,text=tableau[t])
            #interaction avec le lit
            elif matrice[niveaux][ligne][colonne+1]=="L" or matrice[niveaux][ligne-1][colonne]=="L" or matrice[niveaux][ligne+1][colonne]=="L" :
                if r<1:
                    t=-1
                    can1.itemconfig(dialogue,text=tableau[t])
                elif  r>=1:
                    can1.destroy()
                    can1=Canvas(Mafenetre,bg="white",width=750,height=650)
                    can1.place(x=0,y=0)
                    image_fond_fin=can1.create_image(0,0,image=fond_fin,anchor="nw")
                    winsound.PlaySound("victoire.wav", winsound.SND_ASYNC)
    cases_speciales()

def released(event):
    """on enlève la touche relachée de la liste touches"""
    global touches
    fr = event.keysym
    if fr in touches:
        touches.remove(fr)

def mvt_haut():
        """déplace vers le haut"""
        global posY,posX,perso,can1,compteur_de_pas,t,dialogue
        posY -=50
        if posY<0 :
            posY = 0
        compteur_de_pas +=1
        can1.itemconfig(perso,image=tab_haut[compteur_de_pas%len(tab_haut)])
        can1.coords(perso,posX,posY)
        can1.itemconfig(dialogue,text=tableau[t])

def mvt_droite():
        """déplace vers la droite"""
        global posY,posX,perso,can1,compteur_de_pas,t,dialogue
        posX +=50
        if posX>750 :
            posX = 750
        compteur_de_pas +=1
        can1.itemconfig(perso,image=tab_droite[compteur_de_pas%len(tab_droite)])
        can1.coords(perso,posX,posY)
        can1.itemconfig(dialogue,text=tableau[t])

def mvt_gauche():
        """déplace vers la gauche"""
        global posY,posX,perso,can1,compteur_de_pas,t,dialogue
        posX -=50
        if posX<0 :
            posX = 0
        compteur_de_pas +=1
        can1.itemconfig(perso,image=tab_gauche[compteur_de_pas%len(tab_gauche)])
        can1.coords(perso,posX,posY)
        can1.itemconfig(dialogue,text=tableau[t])
        
def mvt_bas():
        """déplace vers le bas"""
        global posY,posX,perso,can1,compteur_de_pas,t,dialogue
        posY +=50
        if posY>650 :
            posY = 650
        compteur_de_pas +=1
        can1.itemconfig(perso,image=tab_bas[compteur_de_pas%len(tab_bas)])
        can1.coords(perso,posX,posY)
        can1.itemconfig(dialogue,text=tableau[t])

def cases_speciales():
    """teste les cases spéciales"""
    global posY,posX,interdites,perso,posX,posY,can1,compteur_de_pas,niveaux,ancien_niveaux,c1,c2,c3,vie,m,t,e,r,touches
    ligne = posY // 50
    colonne = posX // 50
    #conditions pour changer de matrice
    if matrice[niveaux][ligne][colonne-1][0]=="S":
        ancien_niveaux = niveaux
        niveaux = int(matrice[niveaux][ligne][colonne-1][1:])
        touches=[]
        can1.after(500,niveau)
    elif matrice[niveaux][ligne][colonne+1][0]=="S":
        ancien_niveaux = niveaux
        niveaux = int(matrice[niveaux][ligne][colonne+1][1:])
        touches=[]
        can1.after(500,niveau)
    elif matrice[niveaux][ligne-1][colonne][0]=="S":
        ancien_niveaux = niveaux
        niveaux = int(matrice[niveaux][ligne-1][colonne][1:])
        touches=[]
        can1.after(500,niveau)
    elif matrice[niveaux][ligne+1][colonne][0]=="S":
        #conditions specials pour changer de matrice
        if int(matrice[niveaux][ligne+1][colonne][1]) == 7:
            if c1 == 1:
                ancien_niveaux = niveaux
                niveaux = int(matrice[niveaux][ligne+1][colonne][1])
                touches=[]
                can1.after(500,niveau)
        elif int(matrice[niveaux][ligne+1][colonne][1:]) == 13:
            if c2 == 1:
                ancien_niveaux = niveaux
                niveaux = int(matrice[niveaux][ligne+1][colonne][1:])
                touches=[]
                can1.after(500,niveau)
        else:
            ancien_niveaux = niveaux
            niveaux = int(matrice[niveaux][ligne+1][colonne][1:])
            touches=[]
            can1.after(500,niveau)
    #condition pour la teleportation
    elif matrice[niveaux][ligne][colonne][:3]=="TEL":
        ancien_niveaux = niveaux
        if int(matrice[niveaux][ligne][colonne][3:5]) == 14 :
            niveaux = int(matrice[niveaux][ligne][colonne][3:5])
        else:
            niveaux = int(matrice[niveaux][ligne][colonne][3])
        #condition pour les coordonnées d'arrivés
        if matrice[ancien_niveaux][ligne][colonne]=="TEL1":
            posX=350
            posY=200
        elif matrice[ancien_niveaux][ligne][colonne]=="TEL52":
            posX=550
            posY=200
        elif matrice[ancien_niveaux][ligne][colonne]=="TEL51":
            posX=450
            posY=150
        elif matrice[ancien_niveaux][ligne][colonne]=="TEL141":
            posX=250
            posY=350
        elif matrice[ancien_niveaux][ligne][colonne]=="TEL142":
            posX=400
            posY=350
        elif matrice[ancien_niveaux][ligne][colonne]=="TEL143":
            posX=550
            posY=350
        elif matrice[ancien_niveaux][ligne][colonne]=="TEL82":
            posX=400
            posY=450
        elif matrice[ancien_niveaux][ligne][colonne]=="TEL0":
            posX=450
            posY=300
        elif matrice[ancien_niveaux][ligne][colonne]=="TEL2":
            posX=200
            posY=250
        elif matrice[ancien_niveaux][ligne][colonne]=="TEL4":
            posX=550
            posY=200
        elif matrice[ancien_niveaux][ligne][colonne]=="TEL6":
            posX=550
            posY=200
        elif matrice[ancien_niveaux][ligne][colonne]=="TEL7":
            posX=550
            posY=200
        elif matrice[ancien_niveaux][ligne][colonne]=="TEL11":
            posX=350
            posY=400
            niveaux=11
        elif matrice[ancien_niveaux][ligne][colonne]=="TEL12":
            posX=550
            posY=250
        elif matrice[ancien_niveaux][ligne][colonne]=="TEL10":
            posX=550
            posY=250
        elif matrice[ancien_niveaux][ligne][colonne]=="TEL10":
            posX=550
            posY=200
        touches=[]
        can1.after(500,niveau) 
    #condition pour une erreur dans un labyrinte
    elif matrice[niveaux][ligne][colonne]=="sol2":
        posX=350
        posY=150
        touches=[]
        can1.after(500,niveau)
    #condition pour perdre une vie
    elif matrice[niveaux][ligne][colonne][:2]=="Pl" and int(matrice[niveaux][ligne][colonne][2])!=4 or matrice[niveaux][ligne][colonne]=="LA":
        vie-=1
        if vie >= 1:
            can1.create_image((15-2+vie)*50,0,image=coeur_vide,anchor="nw")
            dico["Coeur"+str(vie)]=coeur_vide
            niveaux = 0
            touches=[]
            winsound.PlaySound("house_music.wav", winsound.SND_ASYNC)
            can1.after(500,niveau)
        else:
            reset()
            r-=1
            mort()
    #condition pour la réponse a l'énigme
    elif matrice[niveaux][ligne][colonne]=="Pl4":
        matrice[14][5][6]="TEL142"
        t=17
        can1.itemconfig(dialogue,text=tableau[t])

def mort():
    """Affichage de l'ecran de mort à la mort"""
    global can1,fond_mort,button,r
    can1.destroy()
    can1=Canvas(Mafenetre,bg="white",width=750,height=650)
    can1.place(x=0,y=0)
    winsound.PlaySound("mort.wav", winsound.SND_ASYNC)
    image_fond_mort=can1.create_image(0,0,image=fond_mort,anchor="nw")
    bouton2 = Button(Mafenetre,command=jeu)
    bouton2.place(x=200,y=550)
    bouton2.config(image = yes,width=65,height=26,bd=0)
    bouton3 = Button(Mafenetre,command=menu)
    bouton3.place(x=500,y=550)
    bouton3.config(image = no,width=45,height=26,bd=0)
    r=-1

def reset():
    """Réinitialisation des variables avec le reset"""
    global vie,niveaux,ancien_niveaux,t,e,m,c1,c2,c3,r,dico
    vie=3
    niveaux=0
    ancien_niveaux=0
    t=0
    e=0
    m=0
    c1=0
    c2=0
    c3=0
    r+=1
    for i in range(3):
        dico["Coeur"+str(i)]=coeur_plein
    interdites[-1]="GR"
    dico["CRF2"]=coffre_fermé
    dico["CRF1"]=coffre_fermé
    dico["GR"]=gros_rocher
    dico["M"]=casemarteau
    dico["E2"]=carrénoir 
    dico["E1"]=carrénoir
    dico["EPP"]=epeeplante
    matrice[12][6][3]="ARB"
    matrice[5][3][7]="EPP"
    matrice[2][7][1]="S16"    
    matrice[14][5][6]="TEL81"
    
def niveau():
    """Fonction servant a changer de matrice"""
    global posY,posX,perso,can1,compteur_de_pas,ma_matrice,ancien_niveaux,dialogue,dico
    dico["sol"]=sol
    dico["MPM"]=mur_pierre_mousse
    dico["MP"]=mur_pierre
    #effet sonor
    if niveaux == 1 or niveaux == 10 or niveaux == 11 or niveaux == 12 :
        winsound.PlaySound("forest_sound.wav", winsound.SND_ASYNC)
    elif niveaux==0:
        winsound.PlaySound("house_music.wav", winsound.SND_ASYNC)
    elif niveaux == 15 or niveaux == 16:
        winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
    else:
        winsound.PlaySound("labyrinte_music.wav", winsound.SND_ASYNC)
    ligne = posY // 50
    colonne = posX // 50
    #position du personnage
    if niveaux != 9 or matrice[ancien_niveaux][ligne][colonne]=="TEL9":
        if matrice[ancien_niveaux][ligne][colonne-1][0]=="S":
            posX=550  #abscisse de départ
        elif matrice[ancien_niveaux][ligne][colonne+1][0]=="S":
            posX=150  #abscisse de départ
        elif matrice[ancien_niveaux][ligne-1][colonne][0]=="S":
            posY=450  #abscisse de départ
        elif matrice[ancien_niveaux][ligne+1][colonne][0]=="S":
            posY=150  #abscisse de départ
    #position exeptionnel 
    else:
        posX=350
        posY=300
    #pour un labyrinte    
    if niveaux == 6:
        dico["sol"]=carrénoir
        dico["MPM"]=carrénoir
        dico["MP"]=carrénoir
        
    can1.destroy()
    can1=Canvas(Mafenetre,bg="white",width=750,height=650)
    can1.place(x=0,y=0)
    #dessin du niveau
    for i in range(13):
        for j in range(15):
            can1.create_image(50*j,50*i,image=dico[matrice[niveaux][i][j]],anchor="nw")
    dialogue = can1.create_text(25,560,text="",fill="white",font=("Arial",12),anchor="nw")
    perso=can1.create_image(posX,posY,image=monte2,anchor="nw")
    can1.itemconfig(dialogue,text=tableau[t])
    #attente d'événement sur le can1
    can1.focus_set()
    can1.bind("<KeyPress>",Clavier)
    can1.bind("<KeyRelease>",released)
    

# =============================================================================
# MAIN : PROGRAMME PRINCIPAL
# =============================================================================
menu()
Mafenetre.mainloop()
