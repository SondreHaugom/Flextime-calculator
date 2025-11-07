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
        return [0.0]
    return fleksitid

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
            print(f"Nåverende samlet fleksitid er: {fleksitid[-1]:.2f} timer")
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
            # oppdaterer fleksitidlisten
            fleksitid.append(differanse + fleksitid[-1])
            # skriver ut fleksitid for dagen
            print(f"Fleksitid for dagen: {differanse:.2f} timer")

            # skriver ut fleksitid for hver dag
            for i, tid in enumerate(fleksitid):
                # skriver ut dag og fleksitid
                print(f"Dag {i+1}: {tid:+.2f} timer")
            print(f"Oppdatert samlet fleksitid: {fleksitid[-1]:.2f} timer")
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
    
        print(f"Nåverende samlet fleksitid er: {fleksitid[-1]:.2f} timer")
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
            print(f"Brukte fleksitimer: {brukte_timer:.2f} timer")

            # skriver ut fleksitid for hver dag
            for i, tid in enumerate(fleksitid):
                # skriver ut dag og fleksitid
                print(f"Dag {i+1}: {tid:+.2f} timer")
            # skriver ut oppdatert samlet fleksitid
            print(f"Oppdatert samlet fleksitid: {fleksitid[-1]:.2f} timer")

            # lagrer oppdatert fleksitid til csv-fil
            df = pd.DataFrame(fleksitid, columns=["Fleksitid"])
            df.to_csv('fleksitid.csv', index=False)
        except ValueError:
            print("Ugyldig input. Skriv inn et tall for brukte timer")


# hovedprogrammet
while True:
    # starter hovedmeny
    if __name__ == "__main__":
        # hovedmeny tekst
        print("Velkommen til Fleksitidskalkulatoren!")
        # menyvalg
        print("Legge til arbeidstimer (1) eller registrere brukte fleksitimer (2)? ")
        # meny input
        svar = input("Skriv inn ditt svar: ")
        # sjekker menyvalg
        if svar == "exit" or svar == "quit":
            print("Avslutter programmet.")
            break
        elif svar == "1":
            calculate_flex()
        elif svar == "2":
            used_flex()
        else:
            print("Ugyldig svar. Vennligst skriv '1' eller '2'.")