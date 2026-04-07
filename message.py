def next_col():
    choix = input("Voulez-vous voir si la prochaine collecte est celle des déchets, du composte ou recyclage? O/N\n")
    choix = choix.upper()
    while(choix != "O"):
        choix = input("Entrée inconnue!\nVoulez-vous voir si la prochaine collecte est celle des déchets, du composte ou recyclage? O/N\n")
        choix = choix.upper()
        if(choix == "N"): break    
    return

def info_col(bac1_nom, bac2_nom):
    anwser=input(F"La prochaine collecte du mercredi sera le bac de {bac1_nom} et de {bac2_nom} \nVoulez-vous envoyer le calendrier au recyclage? O/N")
    anwser = anwser.upper()
    while(anwser != "O"):
        anwser = input("Entrée inconnue!\nVoulez-vous envoyer le calendrier au recyclage? O/N\n")
        anwser = anwser.upper()
        if(anwser == "N"): break    