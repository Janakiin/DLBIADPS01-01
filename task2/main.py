import random
from animalPresenter import AnimalPresenter
from herbivore import Herbivore
from infoFetcher import InfoFetcher
from carnivore import Carnivore

def main():
    animals = [
        Carnivore("Leonidas", "Löwe", 5, 190.0, "Antilopen", 24, False),
        Carnivore("", "", False, False, "", False, False),
        Herbivore("Eleas","Elefant", 1, 5400.0, "Akazienblätter", False, True, False),
        Herbivore("Beros", "Bulle", 3, 123.3, "Luzerne", True, True, True)
    ]

    fetcher = InfoFetcher()
    presenter = AnimalPresenter()

    for animal in animals:
        if animal.is_valid_animal:
            foodAmount = random.uniform(0.5, 10.3)
            animalInfos = fetcher.fetch(animal, foodAmount)
            presenter.present(animalInfos)

if __name__ == "__main__":
    main()
