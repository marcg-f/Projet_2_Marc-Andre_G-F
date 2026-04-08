import message
def write_txt():
    path = message.titre_fichier()
    texte = message.contenu_txt()
    fichier = (F"{path}.txt")
    with open(fichier, 'a') as file:
        file.write(texte)
    file.close()
    message.view_txt()
    with open(fichier, 'r') as file:
        ligne = file.read()
        print(ligne)
    file.close()    
    print("Retour au menu principal!")