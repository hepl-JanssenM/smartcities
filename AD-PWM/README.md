
# PWM
Un signal PWM est un signal carré sur lequel 2 charactéristque son important : sa fréquence est son duty-cycle. Sa fréquence détermine combien de fois il pas de haut bas haut en un cycle et son duty-cycle est le pourcentage de temps il est en haut par rapport a un cycle complet.

# ADC READ
Ce code lit la valeur d'un "rotary angle sensor". Le microcontrôleur reçois une valeur analogique et l'interprète sur 16 bits (65536 valeurs). Pour y arriver il divise 5V en 65536 pas et compare ces pas a la tension qu'il reçois. Par exemple s’il reçois 0.7514V il sait qu'on lui a envoyé la valeur 10000.
La fonction ADC() est la même idée que Pin("numéro de pin", pin.IN) mais pour un ADC.
La fonction read_u16() dit qu'il faut interprète la valeur analogique sur 16 bit non signé.
# ADC LED CONTROL
Ce code lit la valeur analogique du "rotary angle sensor" et décide de prendre une décision. Dans ce cas s'est d'allumé la led quand la valeur est plus grande que 30000.
# LED INTENSITY
Ce code fait varié l'intensité de la led dépendant de la valeur du "rotary angle sensor". Pour se faire la led est piloté par un signal PWM qui a un duty cycle de la valeur du "rotary angle sensor" sur 16 bits divisé par 65536.
On utilise la fonction PWM() qui définit qu'on va transmettre de la PWM et pas du continue sur la PIN. La fonction freq() qui définit la nombre de cycle de PWM par seconde et la fonction duty_u16() qui détermine le pourcentage de temps que la PWM est ON sur un cycle (exemple si on lui donne la valeur 32768 sa vaudrait dire qu'elle s'allume 50% de temps car la valeur est codé sur 16 bits)
# LED BREATHING
Ce code fait changer la valeur de l'intensité de la led progressivement entre allumé et éteint puis à nouveau allumé. 
# Music
Ce code joue une partie de l'hymne a la joie de Beethoven. Pour faciliter la tâche on utilise "def" pour définir des fonctions qui dans notre cas sont les notes qu'on voudrait bien jouer. Ceci nous permet d'une fois définir nos notes et il suffit par la suite d'appeler leur fonction pour les jouer.
