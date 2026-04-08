"""
**********************************************
Projet: 2
Auteur: Marc-André Grondin-Fournier
But du projet: Programme qui cherche dans un calendrier les deux prochains bacs à mettre au chemin et qui permet aussi la création/lecture d'un fichier txt
Date: 2026/04/08
Nom du fichier: main_traitement_fichier.py
**********************************************
"""
import message
import fonction_lecture
import ecriture_fichier
menu = 0
while menu != "Q":
    menu = message.menu()
    match menu:
        case "A":
            fonction_lecture.lecture_col() 

        case "B":
            ecriture_fichier.write_txt()    
