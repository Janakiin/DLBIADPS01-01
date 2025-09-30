from typing import List
from animal import Animal

class Carnivore(Animal):
    """ Repräsentiert ein fleischfressendes Tier (Raubtier).
        Erweitert die Basisklasse `Animal` um raubtierspezifische Attribute
        und Methoden.
        Attribute:
            prey (str): Bevorzugte Beuteart (z. B. "Antilopen").
            eaten_prey_count (int): Anzahl bereits gefressener Beutetiere.
            is_scavenger (bool): Gibt an, ob das Tier Aasfresser ist. """
    def __init__(self, name: str, species: str, age: int, weight: float, prey: str, eaten_prey_count: int, is_scavenger: bool):
        super().__init__(name, species, age, weight)
        self.prey = prey
        self.eaten_prey_count = eaten_prey_count
        self.is_scavenger = is_scavenger

    def getGeneralInfos(self) -> List[str]:
        """ Liefert allgemeine und raubtierspezifische Beschreibungsinformationen.
            Erweiterung von `Animal.getGeneralInfos()`:
            - Stellt das Tier als Raubtier vor.
            - Ergänzt bevorzugte Beute (falls angegeben).
            - Ergänzt Anzahl bereits gefressener Beutetiere (falls > 0).
            - Ergänzt Hinweis, ob das Tier Aasfresser ist.
            Returns:
            List[str]: Liste von Textinformationen über das Tier. """
        description_strings = super().getGeneralInfos()

        if (self.is_valid_animal):
            description_strings.insert(0,
                f"{self.name} der Spezies {self.species} ist ein Raubtier."
            )
        if(self.prey != ""):
            description_strings.append(f"Bevorzugte Beute: {self.prey}.")
        if(self.eaten_prey_count != 0):
            description_strings.append(f"{self.name} hat {self.eaten_prey_count} {self.prey} gefressen.")
        if(self.is_scavenger):
            description_strings.append(f"{self.name} ist ein Aasfresser.")

        return  description_strings

    def getHuntingInfos(self, amount: float) -> str:
        """ Liefert Informationen zu einem Jagdvorgang, falls möglich.
            Ablauf:
            - Wenn Name, Beute oder amount ungültig sind, wird eine leere Liste zurückgegeben.
            - Andernfalls:
            * Ausgabe einer Meldung, dass das Tier auf die Jagd geht.
            * Gewichtszunahme über `feed(amount)`.
            Args:
                amount (float): Menge an Nahrung in Kilogramm.
            Returns:
                List[str]: Eine Liste von Textinformationen über den Jagdvorgang. """
        result_array: List[str] = []
        if (self.name == "" or self.prey == "" or not amount):
            return result_array

        result_array.append(f"{self.name} geht auf die Jagd nach {self.prey}!")
        result_array.append(self.feed(amount))

        return result_array