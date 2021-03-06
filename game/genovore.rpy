define g = Character('Genovore', color="#3f0f5d")

# ---------------------------------> arrivée sur la planète, passage en tant que simple génovore
label genovore:

    scene bg interieur vaisseau
    show genovore face at left
    # initialisation du génovore et de ses caracs et de son interface
    show screen genovore
    g "Mes respects, esprit de la ruche. Le vaisseau qui me transportait a enfin atterri sur la planète d'Extremis"
    g "J'ai su jusqu'ici rester discret, la barre de repérage ci dessus est à zéro. Mais je suis encore enfermé dans le vaisseau qui ne me semble pas avoir atterri dans la ruche même."
    g "Si je veux accomplir ce que mon instinct me crie je dois atteindre la ruche pour y contaminer des humains et la prendre comme base pour infester la planète."
    g "Par contre ce long voyage en hibernation a vidé mes réserves, je suis affamé. Ceci peut se voir dans la barre en haut à gauche."
    "Votre esprit supérieur submerge le génovore. Vous êtes maintenant lui, il est maintenant vous. Cette planète sera bientôt vôtre."

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
    "Vous vous approchez du fragile humain puis vous mettez subitement devant lui pour croiser son regard avant qu'il ait le temps de crier de terreur."
    "Dès qu'il a fixé le fond de vos yeux il perd son expression de surprise et tombe sous votre emprise hypnotique."
    "Vous m'emmenez alors dans un coin sombre et tranquille du vaisseau pour le dévorer sauvagement."
    "Sa disparition et les restes attireront inévitablement l'attention mais au moins vous êtes bien rasassié."
    $ niveauFaim = 0
    $ ajouteReperage(5)
    jump genovore_sort_vaisseau

label genovore_contamine_pilote:
    "Vous vous approchez du fragile humain puis vous mettez subitement devant lui pour croiser son regard avant qu'il ait le temps de crier de terreur."
    "Dès qu'il a fixé le fond de vos yeux il perd son expression de surprise et tombe sous votre emprise hypnotique."
    "Votre ovipositeur surgit alors de votre bouche et lui implante votre ADN en perçant son épaule près du cou."
    "Bientôt il tombe définitivement sous votre influence sans même que vous ayez besoin de l'hypnotiser."
    "Vous le suivez pour quitter le vaisseau en évitant d'autres humains."
    "Il est maintenant à vous et vous pourrez le rappeler quand bon vous semblera."
    "Contaminer un pilote est déjà risqué car ça attirera l'attention sur un péril externe à la planète si il est découvert."
    "Mais si en plus il quittait son poste vous courreriez trop de risques que l'alarme soit donnée."
    "Une fois dehors vous le laissez donc aller au bar comme il l'aurait fait. En espérant que personne ne remarque trop son air absent et béat."
    "Cette nuit la graîne que lui avez implanté fera son chemin et votre marque sera implantée dans son ADN, corrompant ses enfants avec les gènes génovores."
    $ ajouteReperage(1)
    $ ajouteContamine(1)
    jump genovore_hors_vaisseau

label genovore_sort_vaisseau_avec_pilote:
    hp "Ces frissons me reprennent, il faut vraiment que je sorte d'ici ou je vais devenir fou."
    "Vous suivez l'humain facilement."

label genovore_sort_vaisseau:
    hide humain pilote
    with moveoutright
    "Le vaisseau est plain de cachettes et l'équipage est très réduit."
    "Dehors le spatioport est presque désert et vous finissez par avoir une occasion de le quitter discrètement pour prendre le chemin de la ruche."
    jump genovore_hors_vaisseau

label genovore_hors_vaisseau:
    scene bg monde_ruche
    with Dissolve(.5)
    show genovore face at left
    with Dissolve(.5)

    "La cité est nettement visible à l'horizon malgré les brouillards radioactifs qui l'entourent."
    "Son extrémité se perd dans les nuages."
    "Les environs ne sont qu'un misérable désert de cendre où se trouvent quelques bidonvilles sans intérêt. La pollution intense qui vient de la cité usine a anéanti l'environnement."
    "Peu importe : les humains eux-mêmes y sont inombrables et sont une délicieuse nourriture pour la flotte ruche."
    g "La cité est à moins d'une journée de marche. Mais il serait dangereux de voyager à découverte en plein jour."
    menu:
        "Attendre la nuit.":
            jump genovore_voyage_nuit
        "Voyager prudemment à l'écart des routes.":
            jump genovore_voyage

label genovore_voyage_nuit:
    "La fin de la journée passe vite et votre trajet nocturne se déroule sans encombre."
    "Il fait encore nuit noire quand vous arrivez aux pieds de la ruche."
    $ niveauFaim = niveauFaim + 1
    jump genovore_entree_ruche

label genovore_voyage:
    "Vous avez vaguement le sentiment d'avoir été observé sur le chemin mais il ne s'agit que de pilotes distraits."
    "En tout cas personne ne vous approche et il fait nuit noire quand vous arrivez aux pieds de la ruche."
    $ ajouteReperage(1)
    jump genovore_entree_ruche

label genovore_entree_ruche:
    $ niveauFaim = niveauFaim + 1
    "Pendant le trajet vous avez pu contempler l'aspect complètement démesuré de cette ville à partir de laquelle vous vous lancerez à la conquête de ce monde."
    "C'est une mégalopole verticale, parsemée de spires d’adamantium et de lithobéton si vastes qu’elles peuvent recouvrir un continent tout entier. "
    "Elle s’élève vers le ciel à des kilomètres de hauteur, tandis que ses racines plongent profondément dans les entrailles de la planète. Elle abrite des milliards d'humains et constitue une nation en elle-même."

    if investInfestation > 0:
        g "Je sens la présence d'autres génovores dans cette ruche. Les efforts de l'esprit ruche ont payé ! À plusieurs nous infesterons ce monde bien plus vite."
        "Ils ont commencé la contamination avant votre arrivée. Ils sont cachés dans divers endroits des méandres de cette gigantesque structure mais déjà vous les pliez à votre volonté par la force supérieure de l'esprit de la ruche."
        $ contamines = contamines + investInfestation * 3
        $ genovores = genovores + investInfestation

    "S'introduire dans cette ville ne devrait pas être difficile mais il faudrait décider d'où vous préféreriez vous installer."
    "Les niveaux les plus bas et les plus décrépits de la sous-ruche, frappés par le crime et la pauvreté, sont le repaire des gangs armés, des criminels et autres crapules, tout autant que des mutants et des cultes hérétiques venus se cacher là des autorités."
    "C'est l'endroit idéal pour rester discret mais vous ne pourrez y contaminer que la lie de cette planète."
    "Les secteurs d'habitations sont plus exposés mais ils ne manquent pas de cachettes. Il s'agit essentiellement d'habitations et de titanesques usines."
    "Il faudra néanmoins escalader la spire pendant des heures pour l'atteindre."
    "Enfin, il reste la tête de la spire où se trouve la noblesse. Là vous gagnerez bien plus vite de l'influence en contaminant des personnes haut placées mais il sera bien plus dangereux d'y demeurer."

    menu:
        "S'introduire dans les bas-fonds.":
            jump genovore_entree_bas_fonds
        "S'installer dans les quartiers industriels.":
            jump genovore_entree_habitations
        "Escalader la spire pour atteindre la cité noble.":
            jump genovore_entree_noblesse

label genovore_entree_bas_fonds:
    $ quartier = 1
    "Vous vous introduisez facilement dans les bas-fonds mais en évitant tout de même les endroits les plus toxiques où vous ne croiseriez de toute façon que des mutants."
    "Les glissements de terrain, une pollution toxique et parfois mortelle, les pannes énergétiques et les effondrements de tunnel sont le lot quotidien des habitants des niveaux les plus profonds des cités-ruches."
    "Ce sont des endroits où la légalité impériale n’a plus vraiment cours, des lieux où règnent le délabrement, la pauvreté, l’anarchie et la superstition, mais qui valent pourtant mieux que le monde cauchemardesque qui s’étend encore plus loin au-dessous, dans les profondeurs de la sous-Ruche."
    jump cycle_de_chasse

label genovore_entree_habitations:
    $ quartier = 2
    $ ajouteReperage(1)
    $ niveauFaim = niveauFaim + 1
    "Vous parvenez en quelques heures à escalader la cité jusqu'à un niveau suffisant pour atteindre les niveaux d'habitations de la classe laborieuse."
    "C’est là que vit la quasi-totalité de la population d’une Ruche, dans une concentration d’humanité si écrasante qu’elle doit être surveillée en permanence et que des régulations draconiennes doivent être mises en place pour restreindre l’autonomie et la liberté de mouvement des individus, afin d’éviter tout risque d’effondrement du système qui se solderait par une catastrophe."
    "La majorité des habitants de la moyenne Ruche ne verront jamais rien d’autre que leur propre cité au cours de leur existence. Jamais ils ne la quitteront, jamais ils ne verront le ciel et jamais ils ne poseront le pied sur la surface de leur propre planète."
    show bg manufactures
    with Dissolve(.5)
    jump cycle_de_chasse

label genovore_entree_noblesse:
    "Il vous faut presque la journée complète et énormément d'astuce pour atteindre les plus hauts quartiers de la cité, au sommet des tours étincelantes qui transpercent la couche nuageuse qui recouvre la basse-ruche."
    "C’est là que résident les aristocrates des grandes familles impériales, les plus riches des grands princes marchands et les maîtres des guildes, dans un luxe et un confort absolument inimaginable pour ceux qui maintiennent les systèmes qui nourrissent ces riches seigneurs et leurs cours de parasites."
    $ quartier = 3
    $ ajouteReperage(3)
    $ niveauFaim = niveauFaim + 3
    jump cycle_de_chasse

label cycle_de_chasse:
    show genovore face at left
    with moveinbottom

    if niveauFaim >= 10:
        g "La faim me tiraille je ne peux plus y résister !"
        "Retournant subitement à la sauvagerie le génovore agresse le premier humain solitaire qu'il croise et l'emporte dans les égoûts pour le dévorer."
        "Ce meurtre au hasard est dangereux mais au moins la faim est passée."
        $ ajouteReperage(quartier*3)
        $ niveauFaim = 0
        $ nbCycleChasse = nbCycleChasse + 1

    g "Je suis à nouveau à l'abri dans mon repaire maître. Les proies humaines ne manquent pas par ici, ni les cachettes."
    g "Ordonnez, je suis prêt à obéir."

    menu:
        "Rassasiez vous de proies." if niveauFaim >= 2:
            jump cycle_de_chasse_mange
        "Contaminez le maximum d'humains.":
            jump cycle_de_chasse_contamine
        "Explorez les environs." if couventSororitasEtat != 1 or administratumEtat != 1 or usineEtat != 1:
            jump cycle_de_chasse_explore

label cycle_de_chasse_mange:
    "pas fait miam"
    $ niveauFaim = 0
    $ contamines = contamines + genovores + 3
    jump fin_cycle_de_chasse

label cycle_de_chasse_contamine:
    "pas fait contamine"
    $ niveauFaim = niveauFaim + 2
    $ contamines = contamines + 3 * genovores + 5
    jump fin_cycle_de_chasse

label cycle_de_chasse_explore:
    "pas fait explore"
    # tirez au hasard des découvertes parmi les accessibles dans la quartier du génovore :
    #  - base militaire (si niveau 2 ou 3)
    #  - église (tous quartiers) -> si attaquée gros bonus pour le culte plus tard
    #  - armurerie
    #  - fabricants d'outils industriels massifs
    $ niveauFaim = niveauFaim + 2
    $ contamines = contamines + genovores + 3
label cycle_de_chasse_explore_random:
    $ indexExploration = renpy.random.randint(1, 3)
    if indexExploration == 1:
        if couventSororitasEtat == 1:
            jump cycle_de_chasse_explore_random
        "pas fait découvert couvent Sororitas"
        $ couventSororitasEtat = 1 # 0==inconnu; 1==trouvé, 2==détruit, 3==Contrôlé
    elif indexExploration == 2:
        if administratumEtat == 1:
            jump cycle_de_chasse_explore_random
        "pas fait découvert administratum"
        $ administratumEtat = 1
    elif indexExploration == 3:
        if usineEtat == 1:
            jump cycle_de_chasse_explore_random
        "pas fait découvert usine"
        $ usineEtat = 1

    jump fin_cycle_de_chasse

label fin_cycle_de_chasse:
    $ ajouteReperage(quartier)
    # événement aléatoire :
    # - un génovore trouvé (1 mort + repérage += 10)
    # - + investInfestation génovores arrivent à votre service
    # - grosse faim + 3
    $ nbCycleChasse = nbCycleChasse + 1

    if nbCycleChasse > 8 and contamines > 100:
            jump fin_chasse
    if niveauReperage > 50:
        if enqueteArbites:
            "pas fait : trouvé et exécuté" # seulement 30% de chance
        else:
            $ enqueteArbites = True # seulement 30% de chance

    jump cycle_de_chasse

label fin_chasse:
    # possibilité d'attaquer un bâtiment exploré avant de devenir patriarche (par exemple église pour affaiblir culte)
    if couventSororitasEtat == 1 or administratumEtat == 1 or usineEtat == 1:
        $ forceCulte = calculerForce()
        if forceCulte > 120:
            g "Le culte est suffisamment puissant pour attaquer nos ennemis."
            g "Nous risquons de nous faire repérer et d'avoir des pertes mais ce serait le moment idéal pour frapper un grand coup par surprise et prendre l'avantage."
            if couventSororitasEtat:
                g "Attaquer le couvent des soeurs de bataille écarte un ennemi très dangereux et nous donnera un gros avantage pour notre propagande religieuse."
            if administratumEtat:
                g "Exterminer le poste de l'administratum nous permettra d'éliminer des traces de nos actions et de remettre le repérage à 0."
            if usineEtat:
                g "pas fait usine."
            menu:
                "Détruire le couvent" if couventSororitasEtat == 1:
                    "pas fait"
                    $ couventSororitasEtat = 2
                    jump fin_bataille_chasse
                "Détruire le centre administratif" if administratumEtat == 1:
                    $ niveauReperage = 0
                    $ administratumEtat = 2
                    jump fin_bataille_chasse
                "Détruire l'usine" if usineEtat == 1:
                    "pas fait"
                    $ usineEtat = 2
                    jump fin_bataille_chasse
                "Mieux vaut être prudent et remettre l'attaque à plus tard":
                    jump patriarche_genovore

    jump patriarche_genovore

label fin_bataille_chasse:
    $ pertes_genovores = renpy.random.randint(0, genovores-1)
    $ genovores -= pertes_genovores
    $ pertes_contamines = renpy.random.randint(20, 90)
    $ contamines -= pertes_contamines
    "pas fait récit de bataille + pertes [pertes_genovores] génovores et [pertes_contamines] contaminés"

    jump patriarche_genovore
