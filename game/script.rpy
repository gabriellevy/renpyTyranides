﻿# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Déclarez les personnages utilisés dans le jeu.
define p = Character('Prince', color="#91160f")
define hp = Character('Pilote', color="#251f99")
define narrator = Character(what_outlines=[(1, "#3a0505",0,0)], what_italic=True)

# -------> Explication du prince, galaxie
label start:

    python:
        import random

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

        # ------------- data génovore
        # suivants génovores
        cultistes = 0
        contamines = 0
        hybridesGen1 = 0
        hybridesGen2 = 0
        hybridesGen3 = 0
        hybridesGen4 = 0
        genovores = 1
        forceCulte = 0 # puissance de ce culte
        # culte religieux
        culteCree = False # création du culte (au niveau religieux)
        nomCulte = ""
        # lieux ruche
        quartier = 2 # basFonds = 1, industriel = 2, noblesse = 3
        couventSororitasEtat = 0 # 0==inconnu; 1==trouvé, 2==détruit, 3==Contrôlé
        administratumEtat = 0
        usineEtat = 0
        # donnees chasse
        nbCycleChasse = 0
        nbAnneesCulte = 0 # temps depuis quand le culte a été créé
        # donnees reperage
        inquisiteurPresent = False

        def CycleContamination():
            global hybridesGen1, hybridesGen2, hybridesGen3, hybridesGen4, genovores, cultistes, contamines, nbAnneesCulte
            text = "youpi du texte"
            # génération de la fin au début pour que les nouveaux hybrides ne soient pas pris en compte dans la génération des générations suivantes dans ce cycle
            dejaHybrides1 = hybridesGen1 != 0
            dejaHybrides2 = hybridesGen2 != 0
            dejaHybrides3 = hybridesGen3 != 0
            dejaHybrides4 = hybridesGen4 != 0

            if nbAnneesCulte > 45:
                nbNouveauxGenovores = (hybridesGen4 * random.randint(1, 50)/200)
                genovores += nbNouveauxGenovores
                nbHybridesGen4 = (hybridesGen3 * random.randint(1, 50)/200)
                hybridesGen4 += nbHybridesGen4
            if nbAnneesCulte > 30:
                nbHybridesGen3 = (hybridesGen2 * random.randint(1, 50)/200)
                hybridesGen3 += nbHybridesGen3
            if nbAnneesCulte > 15:
                nbHybridesGen2 = (hybridesGen1 * random.randint(1, 50)/200)
                hybridesGen2 += nbHybridesGen2
            nbHybridesGen1 = (contamines * random.randint(1, 50)/200)
            hybridesGen1 += nbHybridesGen1

            nbContamines = (cultistes * random.randint(1, 10)/100) + (genovores * random.randint(20, 80))
            contamines += nbContamines
            # fin : choix de la phrase à afficher
            # ajouter détection première création de génovores
            if not dejaHybrides1 and hybridesGen1 != 0:
                text = "Maintenant des hybrides génération 1"
            elif not dejaHybrides2 and hybridesGen2 != 0:
                text = "Maintenant des hybrides génération 2"
            elif not dejaHybrides3 and hybridesGen3 != 0:
                text = "Maintenant des hybrides génération 3"
            elif not dejaHybrides4 and hybridesGen4 != 0:
                text = "Maintenant des hybrides génération 4"
            return text

        def ajouteReperage(val):
            global niveauReperage, reperageMax
            niveauReperage = niveauReperage + val
            if niveauReperage > reperageMax:
                niveauReperage = reperageMax

        def calculerForce():
            global contamines, hybridesGen1, hybridesGen2, hybridesGen3, hybridesGen4, genovores
            return contamines + hybridesGen1 + hybridesGen2 + hybridesGen3 + hybridesGen4 + genovores*10

        def ajouteContamine(val):
            global contamines, genovores
            contamines = contamines + val

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

    jump test_temp # temp
    jump preparation_flotte # partie 1

# -----------------------------------------> combat spatial à l'approche du système
label combat_spatial:
    # https://omnis-bibliotheca.com/index.php/Flottes-Ruches_Tyranides
    scene bg combat_spatial
    with Dissolve(.5)
    p "pas fait"
    p "adaptation biovores selon situation"

# ---------------------------------------------> débarquement des tyranides, défenses planétaires
label invasion:
    # ici la facilité de l'invasion doit dépendre de la surprise et du niveau d'infestation de la planète => ces caracs doivent être déduites des phases précédentes et annoncées.
    # Une carac "tyranoformation" est calculée qui dépend du niveau d'infestation (ATTENTION INVESTISSEMENT)
    # possibilité de faire des larguages non offensifs juste pour tyranoformer (eau, forêts, spores...)
    # Phases d'invasion : https://omnis-bibliotheca.com/index.php/Monde_Tyrannoform%C3%A9
    # bombardement de spores https://omnis-bibliotheca.com/index.php/Spores_Tyranides
    # à partir de là ajouter une carac de "tyranoformation" pour tracer le changement de l'environnement
    # vague aérienne préventive possible : https://omnis-bibliotheca.com/index.php/Essaims_Volants_Tyranides
    # passage riglo avec es hormagaunts : https://omnis-bibliotheca.com/index.php/Gaunts :
    # En outre, à la différence des autres créatures tyranides, les Hormagaunts sont capables de se reproduire de manière autonome, et pondent des centaines d’œufs dans le sol d’une planète avant que leur brève vie ne touche à son terme. Sitôt qu’une vague de ces créatures a été éliminée, un nouvel essaim a atteint sa maturité et se tient prêt à poursuivre les ravages de la génération précédente.
    # technique par pollution de planète qui rend les renforts inutiles car planète vite perdue pour l'Imperium : https://omnis-bibliotheca.com/index.php/Disperseurs_de_Spores

    # si culte génovore finir avec la tragique extermination du culte serait beau cf fin de https://omnis-bibliotheca.com/index.php/Cat%C3%A9gorie:Cultes_Genestealers

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
    # https://omnis-bibliotheca.com/index.php/Fosses_Gastriques
    # https://omnis-bibliotheca.com/index.php/Tours_Capillaires
    # https://omnis-bibliotheca.com/index.php/Puits_%C3%A0_Magma
    # https://omnis-bibliotheca.com/index.php/B%C3%AAtes_Nourrici%C3%A8res_Tyranides
label nettoyage:
    scene bg jungle
    with Dissolve(.5)
    "traque lictor pour repérer les dernières places fortes dans une zone de jungle."
    "consommation par les voraces et extermination."
