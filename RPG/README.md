# Projet RPG

## Consignes

Quand je lance le programme, je "spawn" (tout en console, on imagine hein) lvl 1 avec 10 pv et 1 pour toutes les stats  
Les stats sont les suivantes : pv, atq, magie, esquive

Je peux gagner de l'expérience en tapant des monstres -> en écrivant "pex" dans la console  
Chaque monstre me rapporte 10 exp. Pour atteindre le lvl 2, il faut 10 exp (un monstre)  
Chaque niveau suivant s'obtient comme cela -> exp requise = exp actuelle requise + 10  
Pour atteindre le lvl 3, il faut donc 20 exp (deux monstres)
Pour atteindre le lvl 4, il faut donc 30 exp (trois monstres). Etc...  
Tous les lvl, jusqu'au lvl 5, je gagne 1 point partout sauf en esquive

Quand j'atteinds le lvl 5, je dois avoir une classe attribuée au hasard entre guerrier, mage et archer  
Le guerrier gagne 3 pv et 2 atq par lvl. Il fait les dégats de son atq en combat  
Le mage gagne 1 pv et 3 magie par lvl. Il fait les dégats de sa magie ET se soigne lui même de moitié en combat  
L'archer gagne 2 pv, 1 atq et 2 esquive par lvl. Il fait les dégats de son atq ET possède une chance d'esquiver -> esquive/100

Je peux combattre une classe de mon niveau en tapant "tabasser {classe}" dans la console  
Le combat se simulera alors en me décrivant chaque tour ce qu'il se passe et me déterminant donc le gagnant quand un combattant meurt
