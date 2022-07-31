

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
