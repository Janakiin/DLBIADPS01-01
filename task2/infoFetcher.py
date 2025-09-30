from typing import List
from animal import Animal
from herbivore import Herbivore
from carnivore import Carnivore

class InfoFetcher:
    """
        Stellt Methoden zum Abrufen von Informationen über ein Tier bereit.

        Hinweise:
        - `animal.getGeneralInfos()` liefert allgemeine, artunabhängige Informationen
          und wird für jede Animal-Instanz verwendet.
        - Wenn `amount` > 0 ist, werden zusätzlich art-spezifische Informationen
          ergänzt:
            * Bei Carnivoren: `animal.getHuntingInfos(amount)`
            * Bei Herbivoren: `animal.getGrazingInfos(amount)`

        Die Klasse kapselt die Entscheidung, welche art-spezifischen Info-Methoden
        aufgerufen werden müssen, so dass aufrufender Code nur `fetch()` verwenden muss.
        """
    def fetch(self, animal: Animal, amount: float) -> List[str]:
        """
                Sammelt allgemeine und optional art-spezifische Informationen zu einem Tier.

                Ablauf:
                1. Allgemeine Informationen über `animal.getGeneralInfos()` abrufen.
                2. Wenn `amount` > 0:
                   - Bei Carnivoren werden Jagd-bezogene Infos über `getHuntingInfos(amount)` ergänzt.
                   - Bei Herbivoren werden Weide-bezogene Infos über `getGrazingInfos(amount)` ergänzt.

                Args:
                    animal (Animal): Das Tierobjekt, zu dem Informationen gesammelt werden.
                    amount (float): Die berücksichtigte Futtermenge (nur relevant, wenn > 0).

                Returns:
                    List[str]: Eine Liste von Textinformationen über das Tier.
                """
        infos = animal.getGeneralInfos()
        if amount > 0:
            if isinstance(animal, Carnivore):
                infos.extend(animal.getHuntingInfos(amount))
            elif isinstance(animal, Herbivore):
                infos.extend(animal.getGrazingInfos(amount))
        return infos;