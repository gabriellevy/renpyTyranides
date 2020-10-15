label preparation_flotte:
    scene bg galaxie
    with Dissolve(.5)
    show prince flingue at left

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

    show screen preparer_flotte
label texte_investissement:
    # la fonction de maj ci dessus ne marche pas.... à voir plus tard j'espère quand j'aurai des exemples de bar appelant du python
    scene bg monde_ruche
    with Dissolve(.5)
    show prince flingue at left
    with moveinleft
    p "Investir en infestation génovore rendra plus efficace l'envoi de génovore dans le système visé pour infiltrer la planète et en prendre le contrôle avant même que notre flotte soit arrivée."
    show genovore face at right
    with moveinright
    p "À l'heure où nous parlons un vaisseau de l'Imperium contenant des génovores est sur le point de se poser sur cette planète."
    p "Les génovores sont le meilleur moyen d'infester et affaiblir Extremis."
    g "Vous n'avez qu'un ordre à donner pour que l'infestation commmence, maître."
    p "De plus ils serviront de relais pour nous aider à trouver cette planète que nous ne connaissons que par des informations éparses récoltées dans les cerveaux de récentes victimes."

    scene bg combat_au_sol
    with Dissolve(.5)
    show prince flingue at left
    with moveinleft
    p "Les troupes sont indispensables pour prendre la planète, surtout si les génovores n'ont pas réussi à en prendre le contrôle avant votre arrivée."
    scene bg combat_spatial
    with Dissolve(.5)
    show prince flingue at left
    with moveinleft
    p "Investir dans la flotte est presque indispensable. Si nous perdions la guerre spatiale il serait très difficile d'atteindre la planète."
    scene bg titan
    with Dissolve(.5)
    show prince flingue at left
    with moveinleft
    p "Les biotitans sont des monstres gigantesques qui, si nous les déployons, nous assurerons la victoire lors des combats au sol."
    scene bg tyranisation
    with Dissolve(.5)
    show prince flingue at left
    with moveinleft
    p "Quand nous atteindrons la planète nous y larguerons des milliards de spores et de créatures qui modifieront son environnement pour la rend plus simple à attaquer et digérer tout en rendant la vie impossible aux humains."
    p "Investir en tyranisation rendra cette phase plus efficace."
    p "Elle permettra aussi d'accélérer le processus de conquête et de digestion pour le finir avant l'arrivée de renforts ennemis."
    p "Garder une réserve permettra de réagir plus efficacement aux situations de crise."
    p "Réglez les glisseurs pour déterminer votre investissement en biomasse dans chacune de ces caractéristiques puis validez."
    jump texte_investissement

    jump genovore # partie 2
