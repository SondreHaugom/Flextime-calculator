# definerer en funksjon for å konvertere desimaler til timer og minutter
def to_hours_and_minutes(timer_float):
    # deklarerer en variabel for timer og minutter
    hours = int(timer_float)
    # beregner antall timer og minutter
    minutes = int(round((timer_float - hours) * 60))
    # returnerer formatert streng med timer og minutter
    return f"{hours}t {minutes}m"
