# Vous pouvez placer le script de votre jeu dans ce fichier.


# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Déclarez les personnages utilisés dans le jeu.
define p = Character('Prince', color="#91160f")
define g = Character('Genovore', color="#3f0f5d")
define pg = Character('Patriarche génovore', color="#3f0f5d")
define hp = Character('Pilote', color="#251f99")

# -------> Explication du prince, galaxie
label start:

    python:
        niveauFaim = 8
        sante = "En pleine forme"
        niveauReperage = 0
        reperageMax = 100

        investTotal = 25
        investInfestation = 5
        investTroupes = 5
        investFlotte = 5
        investBiotitan = 0
        investTyranisation = 5
        investAdaptabilite = 5

        def ajouteReperage(val):
            global niveauReperage, reperageMax
            niveauReperage = niveauReperage + val
            if niveauReperage > reperageMax:
                niveauReperage = reperageMax

        def genovoreMange():
            niveauFaim = 0

        def rafraichirInvestissement():
            global investTotal, investInfestation, investTroupes, investFlotte, investBiotitan, investTyranisation, investAdaptabilite

            total = investInfestation + investTroupes + investFlotte + investTyranisation + investAdaptabilite + investBiotitan

            while ( total > investTotal):
                if ( investAdaptabilite > 0 ):
                    investAdaptabilite = investAdaptabilite - 1
                else:
                    investInfestation = investInfestation -1
                    investTroupes = investTroupes - 1
                    investFlotte = investFlotte - 1
                    investTyranisation = investTyranisation - 1
                    investBiotitan = investBiotitan - 1

                total = investInfestation + investTroupes + investFlotte + investTyranisation + investAdaptabilite + investBiotitan

            if ( investTotal > total ):
                investAdaptabilite = investAdaptabilite + (investTotal - total)


    scene bg galaxie
    with Dissolve(.5)
    show prince flingue at left

    jump genovore_contamine_pilote # temp

    p "L'esprit de la ruche a faim. Il veut cette galaxie toute entière."
    p "Bien que sa puissance télépathique soit incomparable il ne peut pas contrôler toutes ses créatures sur des millions d'années lumières d'étendues."
    p "Vous, comme moi, êtes une extension de son esprit. Vous êtes destiné à le servir en conquérant et dévorant la planète qu'il vous assignera dans un secteur particulier."
    p "Il vous a assigné la planète industrielle Extremis. C'est un grand honneur car c'est un monde puissant et précieux pour les misérables humains de l'Imperium. De lui dépendent plusieurs planètes secondaires que vous pourrez aussi dévorer."

    # Ajouter une boîte pour l'investissement dans les différentes compétences de la flotte ruche
    # (coûte de la biomasse et implique des effets d'invasion différents)
    # - Infestation génovore
    # - Biotitans (0 de base, investir baucoup garantit une victoire au sol)
    # - flotte de combat spatial
    # - tyranisation, traqueurs et digéreurs (inclut les modificateurs de climat) => facilite la répidité de digestion, évite els renforts et els évacuations
    # - troupes de combat classique (des termagants aux carnifex)
    # - adptabilité : permet de garder des réserves pour les cas imprévus, de réinvestir...

# label test_temp:
    show screen preparer_flotte
label texte_investissement:
    # la fonction de maj ci dessus ne marche pas.... à voir plus tard j'espère quand j'aurai des exemples de bar appelant du python
    p "Investir en infestation génovore rendra plus efficace l'envoi de génovore dans le système visé pour infiltrer la planète et en prendre le contrôle avant même que notre flotte soit arrivée."
    p "À l'heure où nous parlons un vaisseau de l'Imperium contenant des génovores est sur le point de se poser sur cette planète."
    p "Les génovores sont le meilleur moyen d'infester et affaiblir Extremis."
    p "De plus ils serviront de relais pour nous aider à trouver cette planète que nous ne connaissons que par des informations éparses récoltées dans les cerveaux de récentes victimes."
    p "Les troupes sont indispensables pour prendre la planète, surtout si les génovores n'ont pas réussi à en prendre le contrôle avant votre arrivée."
    p "Investir dans la flotte est presque indispensable. Si nous perdions la guerre spatiale il serait très difficile d'atteindre la planète."
    p "Les biotitans sont des monstres gigantesques qui, si nous les déployons, nous assurerons la victoire lors des combats au sol."
    p "Quand nous atteindrons la planète nous y larguerons des milliards de spores et de créatures qui modifieront son environnement pour la rend plus simple à attaquer et digérer tout en rendant la vie impossible aux humains."
    p "Investir en tyranisation rendra cette phase plus efficace."
    p "Elle permettra aussi d'accélérer le processus de conquête et de digestion pour le finir avant l'arrivée de renforts ennemis."
    p "Garder une réserve permettra de réagir plus efficacement aux situations de crise."
    p "Réglez les glisseurs pour déterminer votre investissement en biomasse dans chacune de ces caractéristiques puis validez."
    jump texte_investissement

# ------> arrivée sur la planète, passage en tant que simple génovore
label genovore:
    scene bg interieur vaisseau
    show genovore face at left
    # initialisation du génovore et de ses caracs et de son interface
    show screen genovore
    g "Mes respects, esprit de la ruche. Le vaisseau qui me transportait a enfin aterri sur la planète d'Extremis"
    g "J'ai su jusqu'ici rester discret, la barre de repérage ci dessus est à zéro. Mais je suis encore enfermé dans le vaisseau qui ne me semble pas avoir atteri dans la ruche même."
    g "Si je veux accomplir ce que mon instinct me crie je dois atteindre la ruche pour y contaminer des humains et la prendre comme base pour infester la planète."
    g "Par contre ce long voyage en demi hibernation a vidé mes réserves, je suis affamé. Ceci peut se voir dans la barre en haut à gauche."

    hide genovore face
    show humain pilote at right
    with Dissolve(.5)
    hp "Pas faché d'être enfin arrivé sur cette fichue planète."
    hp "J'ai été mal à l'aise pendant tout le voyage."
    hp "À croire qu'on a ramassé un démon dans le warp qui nous hante depuis."
    hp "En tout cas dès que j'ai fini la checklist je file au bar le plus proche pour oublier tout ça."

    show genovore face at left
    with Dissolve(.5)
    g "Cet humain seul est une proie facile."
    menu:
        "Que faire ?"
        "Le tuer pour le dévorer.":
            jump genovore_devore_pilote
        "Le contaminer.":
            jump genovore_contamine_pilote
        "Le suivre discrètement pour sortir d'abord du vaisseau.":
            jump genovore_sort_vaisseau_avec_pilote
        "L'ignorer et sortir par vos propres moyens.":
            jump genovore_sort_vaisseau

label genovore_devore_pilote:
    $ genovoreMange()
    $ ajouteReperage(5)
    g "pas fait"

label genovore_contamine_pilote:
    "Vous vous approchez du fragile humain puis vous mettez subitement devant lui pour croiser son regard avant qu'il ait le temps de crier de terreur."
    "Dès qu'il a fixé le fond de vos yeux il perd son expression de surprise et tombe sous votre emprise."
    "Votre ovipositeur surgit alors de votre bouche et lui implante votre ADN en perçant son épaule près du cou."
    "Bientôt il tombe définitivement sous votre influence sans même que vous ayez besoin de l'hypnotiser."
    "Vous le suivez pour quitter le vaisseau en évitant d'autres humains."
    "Il est maintenant à vous et vous pourrez le rappeler quand bon vous semblera."
    "Contaminer un pilote est déjà risqué car ça attirera l'attention sur un péril externe à la planète si il est découvert."
    "Mais si en plus il quittait son poste vous courreriez trop de risques que l'alarme soit donnée."
    "Une fois dehors vous le laissez donc aller au bar comme il l'aurait fait. En espérant que personne ne remarque trop son air absent et béat."
    # ajouter un à contaminé et 1 à repérage
    jump genovore_hors_vaisseau

label genovore_sort_vaisseau_avec_pilote:
    g "pas fait"

label genovore_sort_vaisseau:
    g "pas fait"

label genovore_hors_vaisseau:

    scene bg monde_ruche
    with Dissolve(.5)
    show genovore face at left
    with Dissolve(.5)
    g "** Il va falloir entrer dans la ruche."
    g "** Maintenant il faut contaminer des humains."
    g "** Tout en réussissant à rester caché."
    # si il y a eu investissement en infestation le génovore rencontre d'autres génovores soumis à sa direction

# ------> le genestealer  devient un patriarche et infiltre la planète
label patriarche_genovore:
    scene bg egouts
    with Dissolve(.5)
    show patriarche_genovore face at left
    pg "pas fait"
    pg "création du magus"
    # effets si la jauge "repérage" est pleine (ou si la rébellion est lancée)
    # - avertissement quand elle est à moitié pleine avec conseils
    # - grosse purge Imperium : beaucoup des infiltrés sont tués
    pg "appel de la flotte ruche"

# ------> combat spatial à l'approche du système
label combat_spatial:
    # https://omnis-bibliotheca.com/index.php/Flottes-Ruches_Tyranides
    scene bg combat_spatial
    with Dissolve(.5)
    p "pas fait"
    p "adaptation biovores selon situation"

# ------> débarquement des tyranides, défenses planétaires
label invasion:
    # ici la facilité de l'invasion doit dépendre de la surprise et du niveau d'infestation de la planète => ces caracs doivent être déduites des phases précédentes et annoncées.
    # bombardement de spores https://omnis-bibliotheca.com/index.php/Spores_Tyranides
    # à partir de là ajouter une carac de "tyranoformation" pour tracer le changement de l'environnement
    # vague aérienne préventive possible : https://omnis-bibliotheca.com/index.php/Essaims_Volants_Tyranides
    # passage riglo avec es hormagaunts : https://omnis-bibliotheca.com/index.php/Gaunts :
    # En outre, à la différence des autres créatures tyranides, les Hormagaunts sont capables de se reproduire de manière autonome, et pondent des centaines d’œufs dans le sol d’une planète avant que leur brève vie ne touche à son terme. Sitôt qu’une vague de ces créatures a été éliminée, un nouvel essaim a atteint sa maturité et se tient prêt à poursuivre les ravages de la génération précédente.
    # technique par pollution de planète qui rend les renforts inutiles car planète vite perdue pour l'Imperium : https://omnis-bibliotheca.com/index.php/Disperseurs_de_Spores


    scene bg invasion_planetaire
    with Dissolve(.5)
    show prince flingue at left
    with Dissolve(.5)
    # initialisation d la force d'invasion et de ses caracs et de son interface
    show screen invasion_planetaire

    "Extremis détecte un nuage d’un millier d’objets pénétrant le système."
    "Des cieux d'Extremis déchirés par les éclairs des lasers de défense qui tentaient de repousser les envahisseurs extraterrestres jaillissaient centaines de Bio-vaisseaux essayant d’atterrir à la surface de l’astre."
    "Des vents empoisonnés charrient des nuages de spores dans l’atmosphère."
    # tactiques diverses de débarquement
    "ils s’emparaient d’astéroïdes et autres débris spatiaux pour le projeter contre celle-ci. La planète n’était pas préparée pour un bombardement orbital de la part des Tyranides, si bien qu’il provoquait invariablement des dégâts massifs."
    "De plus, l’impact de ces météores provoquait d’importants nuages de poussière qui s’élevaient dans l’atmosphère, ce qui empêchait les armes d’interception des défenseurs de repérer leurs cibles. La Flotte-Ruche lançait alors des spores mycétiques et la grande majorité d’entre elles atterrissaient saines et sauves. Elles s’ouvraient ensuite pour libérer un essaim de Rôdeurs, parfois un Mawloc ou un Trygon."
    "Ces créatures s’enterraient immédiatement pour éviter d’être détectées et plongeaient dans un état d’hibernation. Elles restaient inertes sous terres pendant des semaines, le temps que Jormungandr rassemble ses forces. Ce n’est que lorsque l’infestation atteignait une masse critique que l’Esprit-Ruche envoyait un stimulus psychique pour réveiller ses enfants."
    "Tous les Tyranides surgissaient alors en même temps du sol tandis que les Bio-vaisseaux se plaçaient en orbite basse pour débuter l’invasion. Au moment où de nouvelles spores mycétiques libéraient des Genestealers et des Carnifex à la surface, la planète était déjà envahie par des créatures fouisseuses. "
    p "adaptation biovores selon situation"
    p "attaque par l'eau, combats marins et débarquement"

# ---------> après contamination de la planète, guerre totale

label guerre_au_sol:
    # dans les cas de retranchements difficiles à abattre (et de traque) scène sur les fouisseurs : https://omnis-bibliotheca.com/index.php/Essaims_Souterrains_Tyranides
    # éventuellement utilisation de bio titans (si investi) : https://omnis-bibliotheca.com/index.php/Biotitans_Tyranides
    # Situation de perte de créatures synapses ? https://omnis-bibliotheca.com/index.php/Cr%C3%A9atures_Synapses_Tyranides
    # tyranoformation : https://omnis-bibliotheca.com/index.php/Spores_Tyranides
    # artillerie : https://omnis-bibliotheca.com/index.php/Organismes_Artilleurs_Tyranides
    scene bg combat_au_sol
    with Dissolve(.5)
    "La végétation même avait acquis une vitalité extraordinaire depuis l’invasion, et seul un déboisement quasi-constant empêchait des lianes chargées de spores ennemies de recouvrir l’îlot de roc. "
    "adaptation biovores selon situation"
    "contre attaque space marine."

# ---------> tyranoformation, extermination des poches de résistance, digestion de la planète
    # tyranoformation : https://omnis-bibliotheca.com/index.php/Spores_Tyranides
label nettoyage:
    scene bg jungle
    with Dissolve(.5)
    "traque lictor."
    "consommation apr les voraces et extermination."
