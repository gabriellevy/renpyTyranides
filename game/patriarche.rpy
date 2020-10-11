
define pg = Character('Patriarche', color="#3f0f5d")
define aco = Character('Acolyte Amalcus Nuthe', who_outlines=[(1, "#28231b",0,0)])
define mg = Character('Dherregau Threndact, Magus', color = "#5b1b11", who_outlines=[(1, "#1b1213",0,0)])

# ------> le genestealer  devient un patriarche et infiltre la planète
label patriarche_genovore:
    scene bg egouts
    with Dissolve(.5)
    show patriarche_genovore face at left
    with moveinbottom
    "Vous avez maintenant suffisamment d'adeptes sur cette planète pour les laisser continuer la contamination sans votre action directe."
    "Alors que le nombre de vos suivants augmentait vous avez senti votre taille s'accroître, vos griffes s'allonger."
    "Mais surtout vous avez senti votre crâne et vos pouvoirs psychiques devenir démesurés."
    "À présent vous ne devez plus prendre le risque de sortir de votre repaire au fonds des égoûts. Votre vie est trop précieuse pour l'esprit de la ruche."
    "Vous êtes maintenant un patriarche Génovore et votre destin est de régner sur ce monde."
    pg "pas fait"

label cycle_de_contamination:
    # effets si la jauge "repérage" est pleine (ou si la rébellion est lancée)
    # - avertissement quand elle est à moitié pleine avec conseils + inquisiteur arrivé => rend tout plus dangereux, possibilités de l'éliminer/contaminer...
    # - grosse purge Imperium : beaucoup des infiltrés sont tués (cf https://omnis-bibliotheca.com/index.php/Cat%C3%A9gorie:Cultes_Genestealers)
    # annonces des premières naissances de chaque génération (environ tous les 15 ans sauf peut-être la première génération 2 ans)
    # ajouter carac "respectabilité du culte" qui apporte des cultes mêmes sur les planètes étrangères et permet de créer des monuments légaux, baisse le repérage

label hybrides_gen1:
    # https://omnis-bibliotheca.com/index.php/Cat%C3%A9gorie:Cultes_Genestealers section "La Création d'un Culte" pour image et description hybrides

label hybrides_gen2:

label hybrides_gen3:
    # prise de contrôle des usines et autres endroits qui peuvent être communautarisés avec l'aide des contaminés

label hybrides_gen4:
    # infiltration sérieuse peut commencer

label creation_magus:
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

label preparation_revolte:
    # capture de véhicules militaires et industriels

label celebration_culte:
    # je ne sais pas encore trop où je caserai ça... => mais ça serait cool pour l'ambiance, dans un evt aléatoire qui augmente els convertis par exemple
    aco "Les Commissaires l’appellent la malédiction. Seuls les éclairés, ceux qui ont renoncé à leurs œillères, voient la vérité."
    aco "Les choses enflées, difformes dans les conduits, ce ne sont pas des monstres. Ce sont des anges ! Ouvrez les yeux ! Ils ont été bénis et ont reçu la force des vrais vertueux."
    aco "Les inquiétudes vaines comme l’orgueil, la symétrie des traits, ne sont que pure perte de temps. Ne préférez-vous pas une apparence laide, mais assortie de la force et de la liberté, à la beauté, à la faiblesse et à l’asservissement à un régime indifférent ?"

label revolte_culte:
    # intervention Arbites ? cf intro https://omnis-bibliotheca.com/index.php/Cat%C3%A9gorie:Cultes_Genestealers
    # Intervention space marine ? (en tout cas si repérage élevé)


    pg "appel de la flotte ruche"

    jump combat_spatial
