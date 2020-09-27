﻿# Vous pouvez placer le script de votre jeu dans ce fichier.


# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Déclarez les personnages utilisés dans le jeu.
define p = Character('Prince', color="#91160f")
define g = Character('Genovore', color="#3f0f5d")


# Explication du prince
label start:

    scene bg galaxie
    with Dissolve(.5)
    show prince flingue at left
    p "L'esprit de la ruche a faim. Il veut cette galaxie toute entière."
    p "Bien que sa puissance télépathique soit incomparable il ne peut pas contrôler toutes ses créatures sur des millions d'années lumières d'étendues."
    p "Vous, comme moi, êtes une extension de son esprit. Vous êtes destiné à le servir en conquérant et dévorant la planète qu'il vous assignera dans un secteur particulier."
    p "Il vous a assigné la planète industrielle Extremis. C'est un grand honneur car c'est un monde puissant et précieux pour les misérables humains de l'Imperium. De lui dépendent plusieurs planètes secondaires que vous pourrez aussi dévorer."
    p "À l'heure où nous parlons un vaisseau de l'Imperium contenant des génovores est sur le point de s'écraser sur cette planète."
    p "Les génovores sont le meilleur moyen d'infester et affaiblir Extremis."
    p "De plus ils serviront de relais pour nous aider à trouver cette planète que nous ne connaissons que par des informations éparses récoltées dans les cerveaux de récentes victimes."


    menu:
        "Quelle partie vous intéresse ?"
        "Débarquement génovore":
            jump genovore
        "Invasion planétaire":
            jump invasion
        "Guerre au sol":
            jump guerre_au_sol

# arrivée sur la planète, passage en tant que simple genestelaer
label genovore:
    scene bg interieur vaisseau
    show genovore face at left
    # initialisation du génovore et de ses caracs et de son interface
    $ sante = "En pleine forme"
    $ niveauFaim = 8
    $ niveauReperage = 0
    show screen genovore
    g "Mes respects, esprit de la ruche. Le vaisseau qui me transportait a enfin atteri sur la planète d'Extremis"
    g "J'ai su jusqu'ici rester discret, la barre de discrétion ci dessus est à zéro. Mais je suis encore enfermé dans le vaisseau qui ne me semble pas avoir atteri dans la ruche même."
    g "Si je veux accomplir ce que mon instinct me crie je dois atteindre la ruche pour y contaminer des humains et la prendre comme base pour infester la planète."
    g "Par contre ce long voyage en demi hibernation a vidé mes réserves, je suis affamé. Ceci peut se voir dans la barre en haut à gauche."
    menu:
        "Que faire"
        "Chercher un membre isolé de l'équipage pour le dévorer.":
            jump genovore_devore_1
        "Sortir d'abord du vaisseau le plus discrètement possible.":
            jump genovore_sort_vaisseau

    label genovore_devore_1:
    g "pas fait"
    label genovore_sort_vaisseau:
    g "pas fait"

    scene bg monde_ruche
    show genovore face at left
    g "** Il va falloir entrer dans la ruche."
    g "** Maintenant il faut contaminer des humains."
    g "** Tout en réussissant à rester caché."

label invasion:
    scene bg invasion_planetaire
    with Dissolve(.5)
    # initialisation d la force d'invasion et de ses caracs et de son interface
    show screen invasion_planetaire

    "Extremis détecte un nuage d’un millier d’objets pénétrant le système."
    "Des cieux d'Extremis déchirés par les éclairs des lasers de défense qui tentaient de repousser les envahisseurs extraterrestres jaillissaient centaines de Bio-vaisseaux essayant d’atterrir à la surface de l’astre."
    "Des vents empoisonnés charrient des nuages de spores dans l’atmosphère."
    # tactiques diverses de débarquement
    "ils s’emparaient d’astéroïdes et autres débris spatiaux pour le projeter contre celle-ci. La planète n’était pas préparée pour un bombardement orbital de la part des Tyranides, si bien qu’il provoquait invariablement des dégâts massifs. De plus, l’impact de ces météores provoquait d’importants nuages de poussière qui s’élevaient dans l’atmosphère, ce qui empêchait les armes d’interception des défenseurs de repérer leurs cibles. La Flotte-Ruche lançait alors des spores mycétiques et la grande majorité d’entre elles atterrissaient saines et sauves. Elles s’ouvraient ensuite pour libérer un essaim de Rôdeurs, parfois un Mawloc ou un Trygon. Ces créatures s’enterraient immédiatement pour éviter d’être détectées et plongeaient dans un état d’hibernation. Elles restaient inertes sous terres pendant des semaines, le temps que Jormungandr rassemble ses forces. Ce n’est que lorsque l’infestation atteignait une masse critique que l’Esprit-Ruche envoyait un stimulus psychique pour réveiller ses enfants. Tous les Tyranides surgissaient alors en même temps du sol tandis que les Bio-vaisseaux se plaçaient en orbite basse pour débuter l’invasion. Au moment où de nouvelles spores mycétiques libéraient des Genestealers et des Carnifex à la surface, la planète était déjà envahie par des créatures fouisseuses. "


label guerre_au_sol:
# après contamination de la planète
    "La végétation même avait acquis une vitalité extraordinaire depuis l’invasion, et seul un déboisement quasi-constant empêchait des lianes chargées de spores ennemies de recouvrir l’îlot de roc. "