from animalActionsPresenter import AnimalActionsPresenter
from herbivore import Herbivore
from predator import Predator

def main():
    animals = [
        Predator("Leonidas der Löwe", 5, 190.0, "Antilopen", 24),
        Herbivore("Eleas der Elefant", 12, 5400.0, "Akazienblätter", 0),
        Herbivore("Beros der Bulle", 3, 123.3, "Luzerne", 1)
    ]

    printer = AnimalActionsPresenter()

    for animal in animals:
        printer.present(animal.describe())
        if isinstance(animal, Predator):
            printer.present(animal.hunt(5.0))
        elif isinstance(animal, Herbivore):
            printer.present(animal.graze(50.0))

if __name__ == "__main__":
    main()
