from time_calculator import TimeCalculator

def main():
    try:
        hours = int(input("Podaj liczbę godzin: "))
        minutes = int(input("Podaj liczbę minut: "))
        seconds = int(input("Podaj liczbę sekund: "))
    except ValueError:
        print("Błąd: Podaj poprawne liczby całkowite!")
        return

    calc = TimeCalculator(hours, minutes, seconds)
    print("\nPrzeliczone wartości:")
    print(f"Czas w sekundach: {calc.to_seconds()}")
    print(f"Czas w minutach: {calc.to_minutes()}")
    print(f"Czas w godzinach: {calc.to_hours()}")

if __name__ == '__main__':
    main()