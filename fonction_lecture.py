"""
**********************************************
Auteur: Marc-André Grondin-Fournier
But de la fonction: Recherche dans un calendrier et retourne les deux prochains bacs à mettre au chemin
Nom du fichier: fonction_lecture.py
**********************************************
"""
import datetime
import message

"""
**********************************************
Fonction de traitement de date de calendrier par rapport à la date actuelle
Entré: Aucune
Sortie: Aucune
"""
def lecture_col():
    ajd = datetime.date.today() #Initialisation/préparation des variables
    ajd = str(ajd)
    ajd = ajd.replace("-", "")
    ajd = int(ajd)
    message.next_col()
    fichier = "calendrier_collecte.ics"
    contenu_ligne = [] 
    final = 0
    bac2_trig = 0
    bac1_found = 0
    bac2_found = 0

    try:
        with open(fichier, "r"):
            test = fichier.read()
            path_found = True
        fichier.close()

    except FileNotFoundError:
        message.fichier_test()
        path_found = False

    if(path_found):
        with open(fichier, 'r') as file:
            line = file.readlines()
            for line_no in line:            
                contenu_ligne = line_no.split(":")      
                if(contenu_ligne[0] == "SUMMARY" and bac1_found == True):
                    bac1_nom = contenu_ligne[1]
                    bac2_trig = True
                    bac1_found = False
                elif(contenu_ligne[0] == "SUMMARY" and bac2_found == True): #Recherche le deuxième bac seulement si le premier est trouvé
                    bac2_nom = contenu_ligne[1]
                    final = True
                    bac2_found = False
                    bac2_trig = False
                elif(contenu_ligne[0] == "DTSTART" and bac2_trig == False):#S'active seulement si ça correspond à la date lu plus tôt
                    bac1_time = contenu_ligne[1].split("T")
                    bac1_date = int(bac1_time[0])
                    if(bac1_date >= ajd):
                        bac1_found = True
                elif(contenu_ligne[0] == "DTSTART" and bac2_trig == True):
                    bac2_time = contenu_ligne[1].split("T")
                    bac2_date = int(bac2_time[0])
                    if(bac2_date >= ajd):
                        bac2_found = True #Arrête la lecture inutile du restant de fichier
                elif(final == True) : break
        file.close() 
        delete = message.info_col(bac1_nom, bac2_nom)
        if(delete == "O"):
            with open(fichier, 'w') as file:
                fichier.write("L'ancien fichier à été écrasé!\n")
            file.close()
    return
    



