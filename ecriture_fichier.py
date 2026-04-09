"""
**********************************************
Auteur: Marc-André Grondin-Fournier
But de la fonction: Créer le titre et écrire/lire d'un fichier texte
Nom du fichier: écriture_fichier.py
Entré: Aucune
Sortie: Aucune
**********************************************
"""
import message

def write_txt():
    anwser = 0
    while(anwser == False):
        path = message.titre_fichier()
        texte = message.contenu_txt()
        fichier = (F"{path}.txt")
        with open(fichier, 'a') as file:
            file.write(texte)
        file.close()

        anwser = message.view_txt()
        if(anwser == "O"):
            with open(fichier, 'r') as file:
                ligne = file.read()
                print(ligne)
            file.close()    
    print("Retour au menu principal!")
    return