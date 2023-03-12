# LED ON
Ce programme allume la led du Raspberry pico.
Il utilise la fonction Pin() pour définir une nouvelle Pin.
Dans ce cas on donne a la fonction la pin "LED" et on dit qu'elle est en OUT.
L'autre fonction qu'on utilise est la fonction value() qui defini la valeur qu'on donne à la led.
Dans notre cas on lui donne la valeur 1 ce qui l'allume
# Blink
Ce programme fait clignoté la led du Raspberry pico.
Il utilise une nouvelle fonction qui est la fonction toggle().
Cette fonction inverse la valeur de la Pin qui lui est attribué.
Si la Pin était allumé elle passe éteint et si elle était éteinte elle passe allumé.
# Blink externe
Ce programme est le même que Blink mais à la lace de faire clignoter la Led du Raspberry pico elle fait clignoter une led externe sur la pin 16
# Button Led
Ce programme utilise un button pour contrôler la led. Si le button est poussé la led s'allume et quand on relâche le button la led s'éteint
Pour ce programme on défini 2 Pin une pour la led en OUT et une pour le button en IN.
# Button Led ON OFF
Ce programme permet de contrôler la led quand on pousse le button pour qu'elle change de valeur. Donc si la led était allumé elle s'éteint et si elle est éteinte elle s'allume. Le code comprend en commentaire l’exemple que le cour donne mais utilise une autre façon de faire le code.
