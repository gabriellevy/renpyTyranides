
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
            $ culteSournois += renpy.random.randint(1, 15)
            $ niveauReperage -= renpy.random.randint(1, 10)
            jump cycle_de_contamination
        "Éxterminer les témoins" if niveauReperage > 30 and genovores > 3:
            jump exterminer_les_temoins

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
    $ textContamination = CycleContamination()
    if textContamination != "":
        pg "[textContamination]"

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

label enquete_culte:
    pg "si suffisament repéré"

label temps_passe_culte:
    $ nbAnneesCulte = nbAnneesCulte + 1
    "fin du cycle (à virer) nbAnneesCulte : [nbAnneesCulte]"
    jump debut_cycle

# -----------------------------------------> à partir d'ici les événements exceptinnels qui ne sont pas partie du cycle :
label preparation_revolte:
    # capture de véhicules militaires et industriels

label extermination_culte:
    pg "L'arbites et/ou les space marines arrivent... ouch (pas fait)"

label celebration_culte:
    # je ne sais pas encore trop où je caserai ça... => mais ça serait cool pour l'ambiance, dans un evt aléatoire qui augmente els convertis par exemple
    aco "Les Commissaires l’appellent la malédiction. Seuls les éclairés, ceux qui ont renoncé à leurs œillères, voient la vérité."
    aco "Les choses enflées, difformes dans les conduits, ce ne sont pas des monstres. Ce sont des anges ! Ouvrez les yeux ! Ils ont été bénis et ont reçu la force des vrais vertueux."
    aco "Les inquiétudes vaines comme l’orgueil, la symétrie des traits, ne sont que pure perte de temps. Ne préférez-vous pas une apparence laide, mais assortie de la force et de la liberté, à la beauté, à la faiblesse et à l’asservissement à un régime indifférent ?"

label revolte_culte:
    # intervention Arbites ? cf intro https://omnis-bibliotheca.com/index.php/Cat%C3%A9gorie:Cultes_Genestealers
    # Intervention space marine ? (en tout cas si repérage élevé)


    pg "finalement appel de la flotte ruche"

    jump combat_spatial
