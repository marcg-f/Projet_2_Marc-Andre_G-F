import message
def write_txt():
    path = message.titre_fichier
    texte = message.contenu_txt
    fichier = (F"{path}.txt")
    with open(fichier, 'a'):
        fichier.write(texte)
    fichier.close()
    message.view_txt
    with open(fichier, 'r'):
        ligne = fichier.read()
        print(ligne)
    fichier.close()    
    print("Retour au menu principal!")