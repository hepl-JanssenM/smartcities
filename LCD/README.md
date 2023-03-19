# Afficheur LCD
Un Afficheur LCD est composé d'une mulitude de section avec un "liquid crystal". Quand un tension est appliqué a un "liquid crystal" celui-ci ne laisse plus passé la lumière. Pour afficher un charactère il suffit de lui dire qu'elle zone du LCD on veut rendre opaque ou passant.
# Les functions de la library LCD1602 utilisé dans les codes
clear: efface le display et rend le curseur

setCursor(col,row):defini la position du display avec col qui est la colonne et row la rangé

no_display: déactive le display

display: active le display

print(text): affiche le text dans print sur le display (string et charactere ASCII uniquement)

write(text) : affiche les charctere dont la valeur binnaire ou hex sont données dans ce tableau:

![1TKZH](https://user-images.githubusercontent.com/124840260/226204461-12059a18-cf78-4fda-8daa-f1aa4940b7ba.gif)
 
# lcd_HelloWorld
 Ce code affiche le texte hello world sur deux ligne:
 ![MicrosoftTeams-image](https://user-images.githubusercontent.com/124840260/226204931-891c101c-6c9e-4e5b-b032-673ff4c3b9b3.png)
 
 # lcd_Angle
Ce code affiche l'angle de rotation d'un potentiomètre. Pour afficher le charactère ° on utilise la fonction write défini plus haut. En utilsant le tableau donné on voit que le charactère ° a la valeur hex "df".

![MicrosoftTeams-image (1)](https://user-images.githubusercontent.com/124840260/226205159-ee61e1ca-32a5-415e-906d-f77ae71ee37a.png)
