def menu():
    tracer = 0
    message = input("Voulez-vous acceder à votre calendrier de collecte de bacs, ou écrire/lire un nouveau fichier texte? \nA: Collecte de bacs \nB: Écrire un nouveau calendrier \nQ: Quitter \n" )
    message = message.upper()
    while tracer == 0:
        if message == ("A")or("B")or("Q"):
            tracer = 1
        else:
            message = input("Entré inconnue! \nVoulez-vous acceder à votre calendrier de collecte de bacs, ou écrire un nouveau calendrier? \nA: Collecte de bacs \nB: Écrire un nouveau calendrier \nQ: Quitter \n" )
            message = message.upper()    
    return message
def next_col():
    choix = input("Voulez-vous voir si la prochaine collecte est celle des déchets, du composte ou recyclage? O/N\n")
    choix = choix.upper()
    while(choix != "O"):
        choix = input("Entrée inconnue! \nVVoulez-vous voir si la prochaine collecte est celle des déchets, du composte ou recyclage? O/N\n")
        choix = choix.upper()
        if(choix == "N"): break    
    return choix

def info_col(bac1_nom, bac2_nom):
    anwser=input(F"La prochaine collecte du mercredi sera le bac de {bac1_nom} et de {bac2_nom} \nVoulez-vous envoyer le calendrier au bac à recyclage? O/N")
    anwser = anwser.upper()
    while(anwser != "O"):
        anwser = input("Entrée inconnue!\nVoulez-vous envoyer le calendrier au bac à recyclage? O/N\n")
        anwser = anwser.upper()
        if(anwser == "N"): break    
    return anwser

def titre_fichier():
    titre=input("Quelle titre voulez-vous pour votre fichier txt?")
    
    while(titre == False):
        titre = input("Le fichier doit posséder un titre!\n")
    return titre

def contenu_txt():
    texte = input("Entrer le texte à inserer dans le fichier:\n")
    return texte

def view_txt():
    anwser = input("Voulez-vous consulter votre fichier nouvellement créé? (O/N)")
    anwser = anwser.upper()
    while(anwser != "O"):
        anwser = input("Entrée inconnue!\nVoulez-vous consulter votre fichier nouvellement créé? (O/N)\n")
        anwser = anwser.upper()
        if(anwser == "N"): break    
    return anwser
