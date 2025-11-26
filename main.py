# Lagte av Sondre Haugom
# importerer pandas som pd 
import pandas as pd
from fleksdb.database import get_connection, get_last_balance
from utils.time_utils import to_hours_and_minutes

    # deklarerer ukedager
ukedager = [
    "Mandag",
    "Tirsdag",
    "Onsdag",
    "Torsdag",
    "Fredag"
    ]


# definerer funksjon for å kalkulere fleksitid
def calculate_flex():
    # henter databaseforbindelse og oppretter en cursor
    conn = get_connection()
    cur = conn.cursor()
    # initialiserer liste for fleksitid med siste balanse
    fleksitid = [get_last_balance()] 


    arbeidstimer_per_dag = 7.75 

    # en for løkke som går gjennom hver dag i ukedager
    for dag in ukedager:
        # en while løkke for å få gyldig input fra brukeren
        while True:
            # viser nåværende fleksitid
            print(f"Nåverende samlet fleksitid er: {to_hours_and_minutes(fleksitid[-1])}")
            # ber brukeren om å skrive inn antall arbeidstimer for dagen
            timer_over = input(f"Skriv inn antall arbeidstimer for {dag}: ")
            # sjekker om brukeren ønsker å avbryte
            if timer_over.lower() in ['exit', 'quit', 'q']:
                print("Avbryter tilføringen.")
                return
            # prøver å konvertere input til float
            try:
                timer_over = float(timer_over)
            # håndterer ugyldig input
            except ValueError:
                print("Ugyldig input. Skriv inn et tall for arbeidstimer prøv igjen.")
                continue
            if timer_over < 6 or timer_over > 10:
                print("Ugyldig input. Timer må være mellom 6 og 10.")
                continue
            break
        # beregner forskjellen mellom innskrevne timer og standard arbeidstimer
        difference = timer_over - arbeidstimer_per_dag
        # oppdaterer fleksitid med forskjellen
        fleksitid.append(fleksitid[-1] + difference)

        # får nåværende tidspunkt i ISO-format
        now_iso = pd.Timestamp.now().isoformat()
        # forbereder rad for innsetting i databasen
        row = (
            now_iso,
            'INN',
            timer_over,
            fleksitid[-1],
            f'Arbeidstimer for {dag}'
        )
        # setter inn raden i databasen
        cur.execute(
            "INSERT INTO fleksitid (timestamp, type, timer, balanse, kommentar) VALUES (?, ?, ?, ?, ?);",
            row
        )
        # lagrer endringene i databasen
        conn.commit()
        # skriver ut resultatet for dagen
        print(f"    → {dag} {timer_over} t (differanse: {difference:+.2f} t)")
        print(f"Oppdatert samlet fleksitid: {to_hours_and_minutes(fleksitid[-1])}")
        



# definerer funksjon for å registrere brukte fleksitimer
def used_flex():
    # henter databaseforbindelse og oppretter en cursor
    conn = get_connection()
    cur = conn.cursor()
    # initialiserer liste for fleksitid med siste balanse
    fleksitid = [get_last_balance()] 

    # en for løkke som går gjennom hver dag i ukedager
    for dag in ukedager:
        # en while løkke for å få gyldig input fra brukeren
        while True:
            # viser nåværende fleksitid
            print(f"Nåverende samlet fleksitid er: {to_hours_and_minutes(fleksitid[-1])}")
            # ber brukeren om å skrive inn antall brukte fleksitimer for dagen
            timer_brukt = input(f"Skriv inn antall bruke fleksitimer for {dag}: ")
            # sjekker om brukeren ønsker å avbryte
            if timer_brukt.lower() in ['exit', 'quit', 'q']:
                print("Avbryter tilføringen. ")
                return
            # prøver å konvertere input til float
            try:
                timer_brukt = float(timer_brukt)
            # håndterer ugyldig input
            except ValueError:
                print("Ugyldig input. Skriv inn et tall for brukte fleksitimer prøv igjen.")
                continue
            if timer_brukt < 0 or timer_brukt > 10:
                print("Ugyldig input. Timer må være mellom 0 og 10.")
                continue
            break
        # oppdaterer fleksitid ved å trekke fra brukte timer
        brukte_timer = timer_brukt
        # oppdaterer  fleksitid listen
        fleksitid.append(fleksitid[-1] - brukte_timer)

        # får nåværende tidspunkt i ISO-format
        now_iso = pd.Timestamp.now().isoformat()
        # forbereder rad for innsetting i databasen
        row = (
            now_iso,
            'UT',
            brukte_timer,
            fleksitid[-1],
            f'Brukte fleksitimer for {dag}'
        )
        # setter inn raden i databasen
        cur.execute(
            "INSERT INTO fleksitid (timestamp, type, timer, balanse, kommentar) VALUES (?, ?, ?, ?, ?);",
            row
        )
        # lagrer endringene i databasen
        conn.commit()
        # skriver ut resultatet for dagen        
        print(f"    → {dag} {timer_brukt} t (differanse: {brukte_timer:+.2f} t)")

# hovedprogram
def main_menu():
    while True:
        # hovedmeny for brukeren
        print("Velkommen til fleksitidskalkulatoren!")
        print("Legge til arbeidstimer (1) eller registrere brukte fleksitimer (2)?")
        svar = input("Skriv inn ditt svar (1/2) eller 'exit' for å avslutte: ").strip().lower()
        if svar in ("exit", "quit", "q"):
            print("Avslutter programmet!")
            break
        # håndterer brukerens valg
        if svar == "1":
            calculate_flex()
        elif svar == "2": 
            used_flex()
        else:
            print("Ugyldig valg. Vennligst velg 1 eller 2.")
# kjører hovedmenyen hvis filen kjøres som et skript
if __name__ == "__main__":
    main_menu()