# Traitement de fichier icalendar et texte  
### Groupe
- 21181
### Enseignant
- Philippe Gauthier
### Étudiant
- Marc-André Grondin-Fournier
### - Table des matières 
- Résumé du projet
- Utilisation
- Fonctionnalités
- Limitations
- Téléchargement

### - Résumé du projet
Programme pour savoir les type de bacs collectés au chemin.Son but est que l'utilisateur puisse savoir rapidement les prochains bacs qui seront collectés au chemin. L'algorithme est réfléchi afin que, si les deux bacs sont trouvés, le programme ne lira pas inutilement le restant du fichier.
 De plus, il est possible de créer un fichier texte dont l'utilisateur choisi le titre et contenu. D'ailleurs, le fichier peut être consulté par la suite. 
### - Utilisation
Possède un menu principale. 
La première option recherche dans un fichier de type ics, comme un calendrier de la ville, les deux prochains bacs à remettre au chemin. De plus, chaque choix est protégé, avec possibilité de retourner/continuer entre boucles. Le deuxieme choix du menu principale permet d'écrire un nouveau fichier texte et de le lire par la suite. 

### - Fonctionnalités

**Générales:** 
 Conversion automatique des minuscules en majuscule pour éviter les erreurs d'entrées des utilisateurs. Protection s'il y a une tentative d'ouverture d'un fichier inexistant.

**Recherche de la prochaine date de collecte:** 
 Commence par vérifier la date actuelle. Ensuite, le fichier ics est découpé en lignes et est comparé à la date actuelle. Ainsi, la semaine correspondante à la semaine prochaine sera détecter et son nom est enregistré. L'itération est avorté aussitôt le deuxième bac enregistré.
 Possibilité d'écraser le fichier et d'écrire un message à l'intérieur disant qu'il a été écrasé

**Écriture/Lecture d'un fichier texte:** 
 Débute par demander un titre pour le fichier texte, ensuite l'utilisateur peut décider d'écrire à l'intérieur. Après, l'utilisateur peut lire son fichier texte.

**Entrées:** 
 Caractères ou nombres
 Fichier ics et txt (avant ouverture)
**Sorties:** 
 Fichier txt en écriture et lecture
 Fichier ics en lecture et écriture


Contient trois librairies de fonctions

### - Limitations
Limiter par le format de date du calendrier, mais conforme à celui utiliser par la ville
### - Téléchargement
Nécéssite le téléchargement de la librairie datetime