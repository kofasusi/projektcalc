def log_function_call(func):
    def wrapper(*args, **kwargs):
        print(f"Wywołanie: {func.__name__} z argumentami {args[1:]} {kwargs}")
        result = func(*args, **kwargs)
        print(f"Wynik: {result}")
        return result
    return wrapper

class TimeCalculator:
    def __init__(self, hours=0, minutes=0, seconds=0):
        # Można dodać walidację lub użyć deskryptorów w module validation.py
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    @log_function_call
    def to_seconds(self):
        """Konwersja podanego czasu na sekundy."""
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    @log_function_call
    def to_minutes(self):
        """Konwersja podanego czasu na minuty."""
        return self.to_seconds() / 60

    @log_function_call
    def to_hours(self):
        """Konwersja podanego czasu na godziny."""
        return self.to_seconds() / 3600