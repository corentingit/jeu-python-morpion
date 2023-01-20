from typing import List
import random

plateauJeu : List[List[str]] = []

joueur : str
gagnant : str = ""
ligne : int
colonne : int
plateauPlein : bool = True
    
    
#plateauJeu = [
#    ["X","O","O"],
#    ["X","D","O"],
#    ["O","X","O"],
#         ]

plateauJeu = [
         ["-","-","-"],
         ["-","-","-"],
         ["-","-","-"],
         ]

def initPlateau() -> None:
    plateauJeu = [
         ["","",""],
         ["","",""],
         ["","",""],
         ]
    
    return plateauJeu
    

def afficherPlatau(plateauJeu):
    
    for i in range(3): 
        if i == 0:
            print("| ", end="")
            
        print(plateauJeu[0][i], end=' | ')
        
        if i == 2:
            print("")
    
        
    for i in range(3): 
        if i == 0:
            print("| ", end="")
            
        print(plateauJeu[1][i], end=' | ')
        
        if i == 2:
            print("")
    
    
    for i in range(3): 
        if i == 0:
            print("| ", end="")
            
        print(plateauJeu[2][i], end=' | ')
        
        if i == 2:
            print("")


def tirageAleatoireJoueur():
    nb = random.randint(1, 2)
    
    if nb == 1:
        joueur = "X"
    
    else:
        joueur = "O"
    
    return joueur



def saisiChoixJoueur(plateauJeu, joueur):
    
    ligne = input("Quel est le numéro de la ligne à jouer ? : ")
    
    while int(ligne) < 0 or int(ligne) > 2:
        print("Erreur : Le numéro de la ligne doit être entre 0 et 2")
        ligne = input("Quel est le numéro de la ligne à jouer ? : ")
        
    
    colonne = input("Quel est le numéro de la colonne à jouer ? : ")
    
    while int(colonne) < 0 or int(colonne) > 2:
        print("Erreur : Le numéro de la colonne doit être entre 0 et 2")
        colonne = input("Quel est le numéro de la colonne à jouer ? : ")
    
    placement = (ligne, colonne)
    return placement





def majPlateau(plateauJeu, joueur, ligne, colonne):
    
    if plateauJeu[int(ligne)][int(colonne)] != "-":
        print("Cette case a déjà été jouée. Veuillez recommencer.")
        saisiChoixJoueur(plateauJeu, joueur)
        
    else:
        plateauJeu[int(ligne)][int(colonne)] = joueur
        
    
    
def plateauPlein(plateauJeu):
    
    
    for j in range(3):
        if plateauJeu[0][j] == "-":
            plateauPlein = False
    
    
    for j in range(3):
        if plateauJeu[1][j] == "-":
            plateauPlein = False            
    
    
    for j in range(3):
        if plateauJeu[2][j] == "-":
            plateauPlein = False  
    
    return plateauPlein
    


def changerJouer(joueur):
    
    if joueur == "X":
        joueur = "O"
    
    else: 
        joueur = "X"

    
    return joueur




def gagantPartie(plateauJeu):
    
    gagnant = ""
    
    if (plateauJeu[0][0] == plateauJeu[0][1]) and (plateauJeu[0][1] == plateauJeu[0][2]) and (plateauJeu[0][0] != "-"):
        gagnant = plateauJeu[0][0]
        
        
        
    if (plateauJeu[1][0] == plateauJeu[1][1]) and (plateauJeu[1][1] == plateauJeu[1][2]) and (plateauJeu[1][0] != "-"):
        gagnant = plateauJeu[1][0]


    if (plateauJeu[2][0] == plateauJeu[2][1]) and (plateauJeu[2][1] == plateauJeu[2][2]) and (plateauJeu[2][0] != "-"):
        gagnant = plateauJeu[2][0]
       
        
        
    if (plateauJeu[0][0] == plateauJeu[1][0]) and (plateauJeu[1][0] == plateauJeu[2][0]) and (plateauJeu[0][0] != "-"):
        gagnant = plateauJeu[0][0]

        
  
    if (plateauJeu[0][1] == plateauJeu[1][1]) and (plateauJeu[1][1] == plateauJeu[2][1]) and (plateauJeu[0][1] != "-"):
        gagnant = plateauJeu[0][1]
       
        
        
    if (plateauJeu[0][2] == plateauJeu[1][2]) and (plateauJeu[1][2] == plateauJeu[2][2]) and (plateauJeu[0][2] != "-"):
        gagnant = plateauJeu[0][2]



    if (plateauJeu[0][0] == plateauJeu[1][1]) and (plateauJeu[1][1] == plateauJeu[2][2]) and (plateauJeu[0][0] != "-"):
        gagnant = plateauJeu[0][0]
         
        
        
    if (plateauJeu[2][0] == plateauJeu[1][1]) and (plateauJeu[1][1] == plateauJeu[0][2]) and (plateauJeu[2][0] != "-"):
        gagnant = plateauJeu[2][0]
        
    
    return gagnant



joueur = tirageAleatoireJoueur()
print(f"C'est au tour du joueur {joueur}")
print("")
print("Les lignes et les colonnes vont de 0 à 2")
(ligne, colonne) = saisiChoixJoueur(plateauJeu, joueur)
majPlateau(plateauJeu, joueur, ligne, colonne)

print("\n")
afficherPlatau(plateauJeu)
print("\n")

plateauPlein = plateauPlein(plateauJeu)


for k in range(9):


    if (plateauPlein == False) and (gagnant == ""):
        
        joueur = changerJouer(joueur)
        print(f"C'est au tour du joueur {joueur}")
        
        (ligne, colonne) = saisiChoixJoueur(plateauJeu, joueur)
        majPlateau(plateauJeu, joueur, ligne, colonne)
        
        print("\n")
        afficherPlatau(plateauJeu)
        print("\n")
        
        gagnant = gagantPartie(plateauJeu)
    
    
    else:
        
        if gagnant != "":
            print(f"le joueur {gagnant} à gagné !")
        
        else:
            print("Match nul !")
        





