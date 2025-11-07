# Lagte av Sondre Haugom


# importerer pandas som pd 
import pandas as pd

# dewfinerer funksjon for å lese csv-fil
def read_csv(): 
    # leser fleksitid fra csv-fil
    try:
        fleksitid = pd.read_csv('fleksitid.csv')['Fleksitid'].tolist()
    # håndterer feil hvis filen ikke finnes
    except FileNotFoundError:
        fleksitid = [0.0]
    except pd.errors.EmptyDataError:
        print("Fleksitid CSV-fil er tom. Oppretter ny fil med standardverdi.")
        fleksitid = [0.0]
    if not fleksitid:
        fleksitid = [0.0]
    return fleksitid


def to_hours_and_minutes(timer_float):
    hours = int(timer_float)
    minutes = int(round((timer_float - hours) * 60))
    return f"{hours}t {minutes}m"


# definerer funksjon for å kalkulere fleksitid
def calculate_flex():
    # henter csv-data 
    fleksitid = read_csv()
    # definerer antall arbeidstimer per dag
    arbeidstimer_per_dag = 7.5 

    # starter løkke for å hente brukerinput
    while True:
        try:
            # viser nåværende samlet fleksitid
            print(f"Nåverende samlet fleksitid er: {to_hours_and_minutes(fleksitid[-1])}")
            # henter antall arbeidstimer fra bruker
            timer_over = input("Skriv inn antall arbeidstimer for dagen: " )
            # sjekker om brukeren ønsker å avslutte
            if timer_over.lower() in ['exit', 'quit']:
                print("Avslutter kalkulatoren.")
                break
            try:
                # konverterer input til float
                timer_over = float(timer_over)
            # håndterer ugyldig input
            except ValueError:
                print("Ugyldig input. Skriv inn et tall for arbeidstimer")
                continue
            if timer_over < 7.5 or timer_over > 12.5:
                print("Ugyldig input. Timer må være mellom 7.5 og 12.5.")
                continue
            # beregner differansen og oppdaterer fleksitid
            differanse = timer_over - arbeidstimer_per_dag
            fleksitid.append(differanse + fleksitid[-1])

            print(f"Fleksitid for dagen: {to_hours_and_minutes(differanse)}")

            # skriver ut fleksitid for hver dag
            for i, tid in enumerate(fleksitid):
                # skriver ut dag og fleksitid
              print(f"Dag {i+1}: {to_hours_and_minutes(tid)}")
            print(f"Oppdatert samlet fleksitid: {to_hours_and_minutes(fleksitid[-1])}")
            # lagrer oppdatert fleksitid til csv-fil
            df = pd.DataFrame(fleksitid, columns=["Fleksitid"])
            df.to_csv('fleksitid.csv', index=False)
        except ValueError:
            print("Ugyldig input. Skriv inn et tall for arbeidstimer")



# definerer funksjon for å registrere brukte fleksitimer
def used_flex():
    # henter csv-data
    fleksitid = read_csv()
    # viser nåværende samlet fleksitid
    if fleksitid is not None:
    
        print(f"Nåverende samlet fleksitid er: {to_hours_and_minutes(fleksitid[-1])}")

    # hondterer tilfelle uten fleksitid
    else:
        print("Ingen fleksitid tilgjengelig.")

    # starter løkke for å hente brukerinput    
    while True:
        try:
            # hente antall brukte timer fra bruker
            brukte_timer = input("Skriv inn antall brukte fleksitimer: ")
            # sjekker om brukeren ønsker å avslutte
            if brukte_timer.lower() in ['exit', 'quit']:
                print("Avslutter kalkulatoren.")
                break
            # konverterer input til float
            brukte_timer = float(brukte_timer)
            # oppdaterer fleksitidlisten
            fleksitid.append(fleksitid[-1] - brukte_timer)
            # skriver ut brukte timer
            print(f"Brukte fleksitimer: {to_hours_and_minutes(fleksitid[-1])}")

            # skriver ut fleksitid for hver dag
            for i, tid in enumerate(fleksitid):
                # skriver ut dag og fleksitid
                print(f"Dag {i+1}: {to_hours_and_minutes(tid)}")
            # skriver ut oppdatert samlet fleksitid
            print(f"Oppdatert samlet fleksitid: {to_hours_and_minutes(fleksitid[-1])}")

            # lagrer oppdatert fleksitid til csv-fil
            df = pd.DataFrame(fleksitid, columns=["Fleksitid"])
            df.to_csv('fleksitid.csv', index=False)
        except ValueError:
            print("Ugyldig input. Skriv inn et tall for brukte timer")


# hovedprogrammet
def main_menu():
    while True:
        print("Velkommen til Fleksitidskalkulatoren!")
        print("Legge til arbeidstimer (1) eller registrere brukte fleksitimer (2)?")
        svar = input("Skriv inn ditt svar (1/2) eller 'exit' for å avslutte: ").strip().lower()

        if svar in ("exit", "quit", "q"):
            print("Avslutter programmet.")
            break
        elif svar == "1":
            calculate_flex()
        elif svar == "2":
            used_flex()
        else:
            print("Ugyldig svar. Vennligst skriv '1' eller '2'.\n")

if __name__ == "__main__":
    main_menu()