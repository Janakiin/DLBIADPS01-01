from typing import List

class AnimalPresenter:
    """
        Verantwortlich für die Ausgabe von Tierinformationen.

        Diese Klasse übernimmt eine Liste von Tierinformationen (Strings)
        und präsentiert sie der Benutzerin bzw. dem Benutzer.
        Momentan geschieht das ausschließlich durch Konsolenausgabe.
    """
    def present(self, animalInfos: List[str]):
        """
            Gibt die übergebenen Tierinformationen in der Konsole aus.

            Jede Information wird in einer eigenen Zeile dargestellt,
            danach folgt eine Trennlinie, um die Ausgabe übersichtlicher
            zu gestalten.

            Args:
                animalInfos (List[str]): Eine Liste von Strings mit
                                             Informationen über ein Tier.
        """
        for s in animalInfos:
            print(s)
        print("----------")



