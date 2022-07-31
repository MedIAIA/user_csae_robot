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
"""


class Robot:
    def __init__(self, serial_number, fabricant):
        self.serial_number = serial_number
        self.fabricant = fabricant
        self.stat = "off"

    def power_on(self):
        self.stat = "On"

    def power_off(self):
        self.stat = "Off"

    def check_stat(self):
        return self.stat


class Androides(Robot):
    def __init__(self, serial_number, fabricant, firstname, family_name=None):
        super().__init__(serial_number, fabricant)
        self.firstname = firstname
        self.family_name = family_name
        self.talk()

    def power_on(self):
        self.stat = "On"
        print(f"Bonjour, je m'appelle {self.firstname} + {self.family_name}")

    def talk(self):
        print(self.firstname)

    def power_off(self):

        print(" Aurevoir")


def main():

    robot_object = Androides(
        serial_number=1111, fabricant="honda", firstname="alix", family_name="Tesla"
    )
    robot_object.power_on()
    print("l'etat du robot ", robot_object.check_stat())
    robot_object.power_off()


if __name__ == "__main__":
    main()
