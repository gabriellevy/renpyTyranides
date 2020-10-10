# ---------------------------------> arrivée sur la planète, passage en tant que simple génovore
label genovore:
    scene bg interieur vaisseau
    show genovore face at left
    # initialisation du génovore et de ses caracs et de son interface
    show screen genovore
    g "Mes respects, esprit de la ruche. Le vaisseau qui me transportait a enfin aterri sur la planète d'Extremis"
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
    $ genovoreMange()
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
label test_temp:

    show screen genovore
    scene bg monde_ruche
    with Dissolve(.5)
    show genovore face at left
    with Dissolve(.5)
    g "** Il va falloir entrer dans la ruche."
    g "** Maintenant il faut contaminer des humains."
    g "** Tout en réussissant à rester caché."
    # si il y a eu investissement en infestation le génovore rencontre d'autres génovores soumis à sa direction

    jump patriarche_genovore
