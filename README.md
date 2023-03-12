# smartcities
Pour notre projet smartcities nous utilisons un microcontrôleur appelé "Raspberry Pi Pico W". Celui-ci est un des plus petits Raspberry pi qu’il existe mais comporte tout de même de nombreuse fonctionnalité. Il comporte une carte wifi, un processeur Arm Cortex-M0+ qui a une clock speed de 133Mhz,26 port GPIO, 2 port UART , 2 contrôleur I2C et 16 chanel PWN.
![215263828-670ae9c1-3d4e-4bfa-a0dd-d2cfe9a20086](https://user-images.githubusercontent.com/124840260/224541794-625b3c65-3961-4446-a9a5-8e0c820023cb.png)

Pour contrôler le "Raspberry Pi Pico W" nous utilisons un langage de programmation appelé le mircopython qui est une variante de python. Se langage est spécialement fais pour fonctionner sur des microcontrôleurs. Pour que notre "Raspberry Pi Pico W" puisse être programmé avec micropython il faut lui installer un interpreteur de mircopython. Pour se faire on connecte « Raspberry Pi Pico W » à notre ordinateur. On peu ensuite ouvrir un disk externe appelé « RPI-RP2 » qui contient un lien vers le site ou on peut télécharger l’interpréteur. Une fois téléchargé on copie le ficher dans « RPI-RP2 » et celui-ci peut maintenant interpréter le mircopython.

Pour écrire le code nous utilisons l'IDE Thonny Python. Il suffit de changer son interpréteur à celui de mircopython pour nous permettre d'écrire du code et le transmettre au « Raspberry Pi Pico W ».

![thonny1](https://user-images.githubusercontent.com/124840260/224549134-1b8349d3-06da-44c6-9cc4-6f642b10f716.png)
![Thonny2](https://user-images.githubusercontent.com/124840260/224549165-496c1ba1-218d-4187-9077-ceb7a4982a49.png)

Pour faciliter les connexions entre des composant externe et le « Raspberry Pi Pico W » nous utilisons un shield qui s'appelle "Grove shield for pi pico"
![Pico_hardware](https://user-images.githubusercontent.com/124840260/224549416-10e89502-71d5-4f1c-af97-0cf43d55ec3d.png)
