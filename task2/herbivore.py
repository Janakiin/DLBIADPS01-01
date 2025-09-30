from typing import List
from animal import Animal

class Herbivore(Animal):
    """ Repräsentiert ein pflanzenfressendes Tier (Herbivore).
        Erweitert die Basisklasse `Animal` um pflanzenfresserspezifische Attribute
        und Methoden.
        Attribute:
            favorite_plant (str): Lieblingspflanze des Tieres.
            is_ruminant (bool): Gibt an, ob das Tier ein Wiederkäuer ist.
            has_hooves (bool): Gibt an, ob das Tier Hufe hat.
            has_horns (bool): Gibt an, ob das Tier Hörner hat."""
    def __init__(self, name: str, species: str, age: int, weight: float, favorite_plant: str, is_ruminant: bool, has_hooves: bool, has_horns:bool):
        super().__init__(name, species, age, weight)
        self.favorite_plant = favorite_plant
        self.is_ruminant = is_ruminant
        self.has_hooves = has_hooves
        self.has_horns = has_horns

    def getGeneralInfos(self)->List[str]:
        """ Liefert allgemeine und pflanzenfresserspezifische Beschreibungsinformationen.
            Erweiterung von `Animal.getGeneralInfos()`:
            - Stellt das Tier als Pflanzenfresser vor.
             - Ergänzt die Lieblingspflanze (falls angegeben).
            - Ergänzt Hinweise zu Wiederkäuen, Hufen und Hörnern.
            Returns:
            List[str]: Liste von Textinformationen über das Tier. """
        description_strings = super().getGeneralInfos()

        if (self.is_valid_animal):
            description_strings.insert(0,
                f"{self.name} der Spezies {self.species} ist ein Pflanzenfresser "
            )
        if(self.favorite_plant != ""):
            description_strings.append(f"Lieblingspflanze: {self.favorite_plant}.")

        if (self.is_ruminant):
            description_strings.append(f"{self.name} ist ein Wiederkäuer.")

        if (self.has_hooves):
            description_strings.append(f"{self.name} hat Hufen.")

        if (self.has_horns):
            description_strings.append(f"{self.name} hat schöne Hörner.")

        return description_strings

    def getGrazingInfos(self, amount: float) -> List[str]:
        """ Liefert Informationen zu einem Weide- bzw. Fressvorgang.
            Ablauf:
            - Wenn Name, Lieblingspflanze oder amount ungültig sind, wird eine leere Liste zurückgegeben.
            - Andernfalls:
                * Ausgabe einer Meldung, dass das Tier seine Lieblingspflanze frisst.
                * Gewichtszunahme über `feed(amount)`.
            Args:
                amount (float): Menge an Nahrung in Kilogramm.
            Returns:
                List[str]: Eine Liste von Textinformationen über den Fressvorgang."""
        result_array: List[str] = []
        if (self.name == "" or self.favorite_plant == "" or not amount):
            return result_array

        result_array.append(f"{self.name} frisst genüsslich {self.favorite_plant}.")
        result_array.append(self.feed(amount))

        return result_array
