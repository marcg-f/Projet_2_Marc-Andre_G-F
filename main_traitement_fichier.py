import message
import fonction_lecture
import ecriture_fichier
menu = 0
while menu != "Q":
    menu=message.menu()
    match menu:
        case "A":
            fonction_lecture.lecture_col() 

        case "B":
            ecriture_fichier.write_txt()    
