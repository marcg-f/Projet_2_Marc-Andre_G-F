import message
import fonction_lecture
import ecriture_fichier

while menu != "Q":
    menu=message.menu()
    match menu:
        case "A":
            fonction_lecture.roulette_russe() 

        case "B":
            jeux_repertoire.pile_face()    

        case "C":            
            jeux_repertoire.courte_paille()