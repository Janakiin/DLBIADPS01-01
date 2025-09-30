class StringFormatter:
    """
        Hilfsklasse zur Formatierung von Zeichenketten für bestimmte Ausgaben.
        Enthält statische Methoden, die ohne Instanziierung genutzt werden können.
        """
    @staticmethod
    def format_years(age: int) -> str:
        """
               Formatiert eine Altersangabe in Jahren als String.

               Gibt bei genau einem Jahr die Einzahl ("1 Jahr") zurück,
               ansonsten die Mehrzahl ("n Jahre").

               Args:
                   age (int): Das Alter in Jahren.

               Returns:
                   str: Formatierte Altersangabe, z. B. "1 Jahr" oder "5 Jahre".
               """
        return f"{age} Jahr" if age == 1 else f"{age} Jahre"

