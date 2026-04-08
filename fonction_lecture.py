import icalendar
import datetime
import message
def lecture_col():
    ajd = datetime.date.today()
    ajd = str(ajd)
    ajd = ajd.replace("-", "")
    ajd = int(ajd)

    message.next_col()
    fichier = "calendrier_collecte.ics"
    k=0
    contenu_ligne=[] 
    line_no=0
    with open(fichier, 'r') as file:

        line = file.readlines()

        for line_no in line:            
            contenu_ligne = line[line_no].split(":")      
            if(contenu_ligne[0] == "SUMMARY" and bac1_found == True):
                bac1_nom = contenu_ligne[1]
                bac2_trig = True
                bac1_found = False
            elif(contenu_ligne[0] == "SUMMARY" and bac2_found == True):
                bac2_nom = contenu_ligne[1]
                final = True
                bac2_found = False
                bac2_trig = False
            elif(contenu_ligne[0] == "DTSTART" and bac2_trig == False):
                bac1_time = contenu_ligne[1].split("T")
                bac1_date = int(bac1_time[0])
                if(bac1_date >= ajd):
                    bac1_found = True
            elif(contenu_ligne[0] == "DTSTART" and bac2_trig == True):
                bac2_time = contenu_ligne[1].split("T")
                bac2_date = int(bac2_time[0])
                if(bac2_date >= ajd):
                    bac2_found = True
            elif(final == True) : break
    file.close() 
    delete = message.info_col(bac1_nom, bac2_nom)
    if(delete == "O"):
        with open(fichier, 'w') as file:
            fichier.write("L'ancien fichier à été écrasé!\n")
        fichier.close()
    return
    



