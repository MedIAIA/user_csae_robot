# user_csae_robot

"""
Modéliser un Robot via une classe Python.
Ce robot possède plusieurs propriétés qui sont déterminées à la conception de ce dernier:
  - numero de serie
Ainsi que des propriétés immuables, communes à chacun des robots car définies lors de la conception initiale.
  - nom du fabricant
Fonctionnalités du robot:
- Allumer
- Éteindre
- état en cours (allumé / éteint)
- récupérer le numero de serie
- récupérer le nom du fabricant
De ce robot est créée une nouvelle version: les Androides.
Les Androïdes ont au moins les mêmes propriétés qu'un Robot avec quelques spécificités:
  - un prénom
  - un nom de famille non-obligatoire
Les fonctionnalités de l'androïde sont identiques à celles du Robot, cependant il est doté de parole (sur la sortie standard):
il utilisera sa fonctionnalité pour dire "bonjour, je m'appelle [prénom de l'android] + nom si défini" systématiquement après avoir démarré.
En s'éteignant, il dira systématiquement "au revoir"
""
