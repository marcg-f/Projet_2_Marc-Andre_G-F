def next_col():
    choix = input("Voulez-vous voir si la prochaine collecte est celle des déchets, du composte ou recyclage? O/N\n")
    choix = choix.upper()
    while(choix != "O"):
        choix=input("Entrée inconnue!\nVoulez-vous voir si la prochaine collecte est celle des déchets, du composte ou recyclage? O/N\n")
        choix = choix.upper()
        if(choix == "N"): break    
    return
