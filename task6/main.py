def sum_list(numbers: list[int]) -> int:
    # Basisfall: leere Liste
    if not numbers:
        return 0
    # Rekursiver Fall: Kopf + Summe der Restliste
    return numbers[0] + sum_list(numbers[1:])

def main():
    numbers = [1, 2, 3, 4, 5]
    result = sum_list(numbers)
    print(f"The sum of the list {numbers} is {result}")

if __name__ == "__main__":
    main()
