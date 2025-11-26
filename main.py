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
    conn = get_connection()
    cur = conn.cursor()
    fleksitid = [get_last_balance()]  # Start with initial balance of 0

    arbeidstimer_per_dag = 7.75 

    for dag in ukedager:
        while True:

            print(f"Nåverende samlet fleksitid er: {to_hours_and_minutes(fleksitid[-1])}")
            timer_over = input(f"Skriv inn antall arbeidstimer for {dag}: ")
            # sjekker om brukeren ønsker å avbryte
            if timer_over.lower() in ['exit', 'quit', 'q']:
                print("Avbryter tilføringen.")
                return
            try:
                timer_over = float(timer_over)
            except ValueError:
                print("Ugyldig input. Skriv inn et tall for arbeidstimer prøv igjen.")
                continue
            if timer_over < 6 or timer_over > 10:
                print("Ugyldig input. Timer må være mellom 6 og 10.")
                continue
            break

        difference = timer_over - arbeidstimer_per_dag
        fleksitid.append(fleksitid[-1] + difference)


        now_iso = pd.Timestamp.now().isoformat()
        row = (
            now_iso,
            'INN',
            timer_over,
            fleksitid[-1],
            f'Arbeidstimer for {dag}'
        )

        cur.execute(
            "INSERT INTO fleksitid (timestamp, type, timer, balanse, kommentar) VALUES (?, ?, ?, ?, ?);",
            row
        )
        conn.commit()
        print(f"    → {dag} {timer_over} t (differanse: {difference:+.2f} t)")
        print(f"Oppdatert samlet fleksitid: {to_hours_and_minutes(fleksitid[-1])}")
        




def used_flex():
    conn = get_connection()
    cur = conn.cursor()
    fleksitid = [get_last_balance()] 

 
    for dag in ukedager:
        while True:

            print(f"Nåverende samlet fleksitid er: {to_hours_and_minutes(fleksitid[-1])}")
            timer_brukt = input(f"Skriv inn antall bruke fleksitimer for {dag}: ")
            if timer_brukt.lower() in ['exit', 'quit', 'q']:
                print("Avbryter tilføringen. ")
                return
            
            try:
                timer_brukt = float(timer_brukt)
            except ValueError:
                print("Ugyldig input. Skriv inn et tall for brukte fleksitimer prøv igjen.")
                continue
            if timer_brukt < 0 or timer_brukt > 10:
                print("Ugyldig input. Timer må være mellom 0 og 10.")
                continue
            break

        brukte_timer = timer_brukt
        fleksitid.append(fleksitid[-1] - brukte_timer)

        now_iso = pd.Timestamp.now().isoformat()
        row = (
            now_iso,
            'UT',
            brukte_timer,
            fleksitid[-1],
            f'Brukte fleksitimer for {dag}'
        )
        cur.execute(
            "INSERT INTO fleksitid (timestamp, type, timer, balanse, kommentar) VALUES (?, ?, ?, ?, ?);",
            row
        )
        conn.commit()
        print(f"    → {dag} {timer_brukt} t (differanse: {brukte_timer:+.2f} t)")


def main_menu():
    while True:
        print("Velkommen til fleksitidskalkulatoren!")
        print("Legge til arbeidstimer (1) eller registrere brukte fleksitimer (2)?")
        svar = input("Skriv inn ditt svar (1/2) eller 'exit' for å avslutte: ").strip().lower()
        if svar in ("exit", "quit", "q"):
            print("Avslutter programmet!")
            break
        if svar == "1":
            calculate_flex()
        elif svar == "2": 
            used_flex()
        else:
            print("Ugyldig valg. Vennligst velg 1 eller 2.")

if __name__ == "__main__":
    main_menu()