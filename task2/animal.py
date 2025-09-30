from typing import List
from stringFormatter import StringFormatter

class Animal:
    """ Repräsentiert ein allgemeines Tier mit Basisinformationen und Verhalten.
        Attribute:
            name (str): Der Name des Tieres.
            species (str): Die Tierart (z. B. "Elefant", "Löwe").
            age (int): Das Alter des Tieres in Jahren.
            weight (float): Das Gewicht des Tieres in Kilogramm.
            is_valid_animal (bool): Flag, das angibt, ob die Tierdaten gültig sind
                                    (nicht leer oder 0)."""
    def __init__(self, name: str, species: str, age: int, weight: float):
        self.name = name
        self.species = species
        self.age = age
        self.weight = weight
        self.is_valid_animal = self.is_valid_animal()

    def feed(self, amount: float) -> str:
        """ Erhöht das Gewicht des Tieres um eine bestimmte Futtermenge.
            Args:
                amount (float): Menge an Futter in Kilogramm.
            Returns:
                str: Text, der beschreibt, wie viel das Tier gefressen hat
                und wie sich sein Gewicht verändert hat."""
        self.weight += amount
        return f"{self.name} hat {amount:.1f} kg Futter gefressen und wiegt jetzt {self.weight:.1f} kg."

    def getGeneralInfos(self) -> List[str]:
        """ Liefert allgemeine Beschreibungsinformationen über das Tier.
            Enthält aktuell Angaben zum Alter (formatiert über
            StringFormatter.format_years) und zum Gewicht.
            Returns:
                List[str]: Eine Liste mit allgemeinen Informationen,
                oder eine leere Liste, falls das Tier ungültig ist."""
        description_strings: List[str] = []

        if (self.is_valid_animal):
            description_strings.append(
                f"Das Tier ist {StringFormatter.format_years(self.age)} alt und wiegt {self.weight:.1f} kg."
            )

        return description_strings;

    def is_valid_animal(self) -> bool:
        """ Prüft, ob die Tierdaten gültig sind.
            Ein Tier gilt als gültig, wenn:
            - Name und Art nicht leer sind,
            - Alter > 0 ist,
            - Gewicht > 0 ist.
            Returns:
                bool: True, wenn die Daten valide sind, sonst False."""
        return (self.name != "" and self.species != "" and self.age and self.weight)


