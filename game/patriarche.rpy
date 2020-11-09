
define pg = Character('Patriarche', color="#3f0f5d")
define aco = Character('Acolyte Amalcus Nuthe', who_outlines=[(1, "#28231b",0,0)])
define mg = Character('Dherregau Threndact, Magus', color = "#5b1b11", who_outlines=[(1, "#1b1213",0,0)])

# ------> le genestealer  devient un patriarche et infiltre la planète
label patriarche_genovore:
    # intro
    scene bg egouts
    with Dissolve(.5)
    show patriarche_genovore face at left
    with moveinbottom
    show screen patriarche_genovore
    "Vous avez maintenant suffisamment d'adeptes sur cette planète pour les laisser continuer la contamination sans votre action directe."
    "Alors que le nombre de vos suivants augmentait vous avez senti votre taille s'accroître, vos griffes s'allonger."
    "Mais surtout vous avez senti votre crâne et vos pouvoirs psychiques devenir démesurés."
    "À présent vous ne devez plus prendre le risque de sortir de votre repaire au fonds des égoûts. Votre vie est trop précieuse pour l'esprit de la ruche."
    "Vous êtes maintenant un patriarche Génovore et votre destin est de régner sur ce monde."

label test_temp:
label debut_cycle:
    scene bg egouts
    with Dissolve(.5)
    show patriarche_genovore face at left
    with moveinbottom
    show screen patriarche_genovore

label choix_priorites_cycle:
    menu:
        "Quel sera votre priorité cette année patriarche ?"
        "Créer un culte religieux me vénérant comme un dieu" if not culteCree:
            jump creation_culte
        "Étendre le culte par la propagande" if culteCree:
            $ prioritePatrarche = prioritePatrarcheExtensionCulte
            jump cycle_de_contamination
        "Favoriser la discrétion, cacher vos cultistes, corrompre les témoins, infiltrer la société" if niveauReperage > 10:
            $ prioritePatrarche = prioritePatrarcheDiscretion
            $ culteSournois += renpy.random.randint(1, 15)
            $ niveauReperage -= renpy.random.randint(1, 10)
            jump cycle_de_contamination
        "Essayer de contaminer le maximum d'humains":
            $ prioritePatrarche = prioritePatrarcheContamination
            jump cycle_de_contamination
        "Envoyer des éclaireurs dans les autres régions de la planète" if hybridesGen4 > 0:
            jump repandre_eclaireurs
        # actions violentes :
        "Lancer la révolte planétaire" if nbPrimus > 0:
            jump revolte_genovore
        "Exterminer les témoins" if niveauReperage > 30 and genovores > 3:
            jump exterminer_les_temoins
        # actions politiques :
        "Infiltrer les hautes sphères de la société" if puissancePolitiqueCulte >= puissancePolitiqueCulteMax:
            jump revolte_politique
        "Prendre le contrôle de la planète politiquement" if nbMagus > 0 or quartier == 2:
            jump infiltration_politique

label infiltration_politique:
    "infiltration politique : pas écrite"
    $ puissancePolitiqueCulte += renpy.random.randint(1, 10)
    $ puissancePolitiqueCulte += nbMagus
    $ niveauReperage += renpy.random.randint(0, 5)
    jump cycle_de_contamination

label repandre_eclaireurs:
    # TODO : ajouter une image de cultistes à moto ou autre véhicule ?
    "Vos cultistes les plus motivés partent sur divers véhicules légers répandre le culte au travers du monde."
    "Cela va grandement accélérer la contamination mais rendra aussi bien plus dur de rester discret."
    $ cultistes += renpy.random.randint(100, 500)
    $ contamines += renpy.random.randint(10, 200)
    $ niveauReperage += renpy.random.randint(5, 20)
    jump cycle_de_contamination

label exterminer_les_temoins:
    # TODO MATHIEU : ajouter un peu de random, des risques d'échec et de pertes ?
    show genovore face at right
    with moveinright
    g "Extermination menée à bien, patriarche. Le sang des humains tapîsse les murs. Ils ne parleront plus contre le culte."
    $ culteSournois += renpy.random.randint(1, 5)
    $ culteViolent += renpy.random.randint(1, 5)
    $ niveauReperage -= renpy.random.randint(5, 15)
    jump cycle_de_contamination

label creation_culte:
    $ culteCree = True
    python:
        nomCulte = renpy.input("Comment voulez vous nommer votre culte ?")
        nomCulte = nomCulte.strip() or "La spirale mystique"
    pg "Le culte [nomCulte] est créé et déjà vos contaminés se chargent de recruter des adeptes et de répandre la bonne parole des étoiles."
    jump cycle_de_contamination

label cycle_de_contamination:
    # == reproduction
    # https://omnis-bibliotheca.com/index.php/Cat%C3%A9gorie:Cultes_Genestealers section "La Création d'un Culte" pour image et description hybrides
    # Hybrides gen 3 : prise de contrôle des usines et autres endroits qui peuvent être communautarisés avec l'aide des contaminés
    # Hybrides gen 4 : infiltration sérieuse peut commencer
    $ resContamination = CycleContamination()
    if resContamination == "gen1":
        "Une fois qu’un humain a été infecté, le matériel génétique du Genestealer se met à l’œuvre dans son système biologique."
        "L’instinct dominant du Genestealer, qui est de propager son espèce influe subtilement les pensées de l’hôte génétique, et celui-ci fera tout son possible pour fonder une famille."
        "Son premier né est un Hybride de première génération, mi-homme, mi-Genestealer, et en vérité à peine reconnaissable comme un enfant humain."
        "Les parents semblent tout à fait indifférent à la vraie nature de leur progéniture."
        "Ils dissimulent l’Hybride pour sa sécurité et le traitent comme s’il était un enfant normal."
        "L’affection naturelle des parents se combine avec l’instinct primordial de défendre leur enfant qui est protégé de tout danger même s’il n’est visiblement pas humain."
        "La famille peut concevoir d’autres enfants, mais ce seront des humains normaux : chaque humain infecté ne peut produire qu’un unique rejeton porteur de gènes Genestealers et c’est invariablement le premier-né."
    elif resContamination == "gen2":
        show hybride_gen1 attaque at right
        with moveinright
        "Les Hybrides de première génération ont grandi jusqu’à maturité, toujours cachés dans la communauté, et ont infecté à leur tour des humains, de la même manière que le Génovore qui infecta leurs parents."
        "Le processus est répété et la seconde génération d’Hybrides naît."
        "Toujours profondément alien, et presque toujours pourvue de trois bras."
        "Des traits humains commencent tout de même à prendre le dessus pour le visage ou la posture."
    elif resContamination == "gen3":
        show hybride_gen1 attaque at right
        "Les Hybrides de deuxième génération ont grandi jusqu’à maturité, toujours cachés dans la communauté pour ne pas révéler leur évidente nature alien."
        "Le processus se poursuit pour la nouvelle génération d’Hybrides, séparés par une génération de parents humains."
        "De cette manière, chaque Hybride a une fratrie, qui ressent à la fois la loyauté humaine normale envers leur étrange frère et le lien primal d’une race Xenos dont les gênes sont intimement liés aux siens."
        "Pouvant difficilement passer pour des humains, les Hybrides de seconde génération utilisent les mêmes techniques que ceux de la première pour transmettre leur gène et donner naissance à la troisième génération."

    elif resContamination == "gen4":
        "La troisième génération infecte d'une façon ou d’une autres des prisonniers endoctrinés, produisant ainsi la quatrième génération qu’il est difficile de différencier des humains normaux au premier abord."
        "Cependant, un Hybride garde toujours les instincts primaires des Genestealers ;"
        "cela est toujours implanté dans leur structure génétique, et peu importe leur apparence humaine, les Hybrides appartiennent à la lignée des Genestealers."
        "C’est ce qui rend de nombreuses façons la dernière génération d’Hybrides la plus dangereuse : "
        "ils peuvent se déplacer librement parmi les humains, transmettant discrètement leur terrible infection et prenant le contrôle des plus importantes organisations en accédant aux postes clés."

    elif resContamination == "genovore":
        "La quatrième génération se reproduit avec la population locale et engendre des Genestealers."
        "La boucle est bouclée."

label phase_extension_culte:
    $ texteExtensionCulte = CycleExtensionCulte()
    if texteExtensionCulte != "":
        pg "[texteExtensionCulte]"

label generation_creatures_culte:
    if culteViolent > 50 and hybridesGen4 > 0:
        $ culteViolent = 0
        jump creation_primus
    elif culteSournois > 50 and hybridesGen4 > 0:
        $ culteSournois = 0
        jump creation_magus
    jump phase_reperage

label creation_primus:
    $ nbPrimus += 1
    pg "Création primus : pas fait"
    jump phase_reperage

label creation_magus:
    $ nbMagus += 1
    "Votre emprise sur la planète et le nombre de vos hybrides de quatrième génération a enfin permis le passage de votre culte à un stade essentiel : "
    with Dissolve(.5)
    show magus face at right
    with moveinright
    "La création d'un Magus. Le Magus est un maître de la politique, de l'infiltration, doté de redoutables pouvoirs psychiques."
    "Avec lui à votre service vous pourrez étendre votre culte aux plus hautes sphères."
    mg "L’humble héritera des étoiles."
    mg "Lui seul est capable de discerner la gloire dans le rejet du pouvoir individuel au profit de la communauté."
    mg "Que l’idiot et le païen brûlent dans les braises de guerres égoïstes. Nous nous dresserons au-dessus des flammes tel un Phœnix ressuscité !"
    mg "Un ost d’anges à l’image des véritables maîtres de cette galaxie ! Une panoplie de dieux pour qui rien n’est hors de portée !"
    mg "Je suis à votre service, DIeu vivant venu des étoiles."
    mg "Ordonnez j'obéirai."
    jump phase_reperage

label phase_reperage:
    # effets si la jauge "repérage" est pleine (ou si la rébellion est lancée)
    # - avertissement quand elle est à moitié pleine avec conseils + inquisiteur arrivé => rend tout plus dangereux, possibilités de l'éliminer/contaminer...
    # - grosse purge Imperium : beaucoup des infiltrés sont tués (cf https://omnis-bibliotheca.com/index.php/Cat%C3%A9gorie:Cultes_Genestealers)
    # annonces des premières naissances de chaque génération (environ tous les 15 ans sauf peut-être la première génération 2 ans)
    # ajouter carac "respectabilité du culte" qui apporte des cultes mêmes sur les planètes étrangères et permet de créer des monuments légaux, baisse le repérage
    $ texteReperage = CycleReperageCulte()
    if texteReperage != "":
        pg "[texteReperage]"
    jump enquete_culte

label enquete_culte:
    if enqueteArbites:
        pg "!! L'Adeptus Arbites enquête : pas fait."
    if enqueteInquisition:
        pg "!! L'inquisiteur enquête : pas fait."
        if niveauReperage > 100:
            jump extermination_culte
    jump temps_passe_culte

label temps_passe_culte:
    $ nbAnneesCulte = nbAnneesCulte + 1
    jump debut_cycle

# -----------------------------------------> à partir d'ici les événements exceptionnels qui ne sont pas partie du cycle :
label preparation_revolte:
    # capture de véhicules militaires et industriels

label extermination_culte:
    pg "L'arbites et/ou les space marines arrivent... ouch (pas fait)"

label celebration_culte:
    # je ne sais pas encore trop où je caserai ça... => mais ça serait cool pour l'ambiance, dans un evt aléatoire qui augmente els convertis par exemple
    aco "Les Commissaires l’appellent la malédiction. Seuls les éclairés, ceux qui ont renoncé à leurs œillères, voient la vérité."
    aco "Les choses enflées, difformes dans les conduits, ce ne sont pas des monstres. Ce sont des anges ! Ouvrez les yeux ! Ils ont été bénis et ont reçu la force des vrais vertueux."
    aco "Les inquiétudes vaines comme l’orgueil, la symétrie des traits, ne sont que pure perte de temps. Ne préférez-vous pas une apparence laide, mais assortie de la force et de la liberté, à la beauté, à la faiblesse et à l’asservissement à un régime indifférent ?"

label revolte_genovore:
    "révolte pas faite"
    # ajouter des conditions en plus de la nécessité du primus ?
    # intervention Arbites ? cf intro https://omnis-bibliotheca.com/index.php/Cat%C3%A9gorie:Cultes_Genestealers
    # Intervention space marine ? (en tout cas si repérage élevé)

label revolte_politique:
    "révolte par la politique pas faite"


    pg "finalement appel de la flotte ruche"

    jump combat_spatial
