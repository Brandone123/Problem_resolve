# Problem_resolve
Code python pour resourdre les problemes de transport, d'affectation et de programmation lineaire avec un simple interface 

Avant de lancer le programme, veuillez installer les dependances en tapant sur votre terminal :

pip install -r requirements.txt
si cela vous affiche une erreur, rassurer vous d'avoir installer la nouvelle version de python qui inclus pip

L'interface a été faite avec PyQt5 sur python==3.8.0

## Indication de certaines fonction
### Pour Simplex

Instructions:
Fonctions d'appel dans cet ordre :

    problème = gen_matrix(v,c)
    contraindre(problème, chaîne)
    obj(problème, chaîne de caractères)
    maxz(problème)
gen_matrix() produit une matrice à laquelle on donne des contraintes et une fonction objective pour maximiser ou minimiser.

    Elle prend var (nombre de variables) et cons (nombre de contraintes) comme paramètres.
    gen_matrix(2,3) va créer une matrice 4x7 par conception.
    
contraint() contrainte du problème. Il prend le problème comme premier argument et une chaîne comme second. La chaîne doit être saisi sous la forme 1,2,G,10 signifiant 1(x1) + 2(x2) >= 10.

    Utilisez "L" pour <= au lieu de "G".
N'utilisez obj() qu'après avoir saisi toutes les contraintes, sous la forme 1,2,0 signifiant 1(x1) +2(x2) +0

    Le dernier terme est toujours réservé à une constante et le 0 ne peut être omis.
Utilisez maxz() pour résoudre un problème de maximisation LP. Utilisez minz() pour résoudre un problème de minimisation.

Divulgation -- la fonction pivot(), sous-composante de maxz() et minz(), a quelques bogues. Jusqu'à présent, ceux-ci ne se sont produits que lorsque
    minz() a été appelé.

#### Lancer l'application en tapant la commande:

 python main_window.py
