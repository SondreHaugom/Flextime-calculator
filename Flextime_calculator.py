# Lagte av Sondre Haugom


# importerer pandas som pd 
import pandas as pd
# deklarerer ukedager 
ukedager = [
    "Mandag",
    "Tisdag",
    "Onsdag",
    "Torsdag",
    "Fredag",
]

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


# definerer funksjon for å kalkulere fleksitid
def calculate_flex():
    # henter csv-data 
    fleksitid = read_csv()
    # definerer antall arbeidstimer per dag
    arbeidstimer_per_dag = 7.75

    # starter løkke for å hente brukerinput
    for dag in ukedager:
        # kjører input-prosessen i en løkke for å sikre gyldig input
        while True: 
            # printer nåværende fleksitid
            print(f"Nåverende samlet fleksitid er: {to_hours_and_minutes(fleksitid[-1])}")
            # ber brukeren om å skrive inn antall arbeidstimer for dagen
            timer_over = input(f"Skriv inn antall arbeidstimer for {dag}: ")
            # sjekker om brukeren ønsker å avbryte
            if timer_over.lower() in ['exit', 'quit', 'q']:
                print("Avbryter tilføringen.")
                return
            # prøver å konvertere input til float
            try:
                # konverterer input til float
                timer_over = float(timer_over)
                # sjekker om input er gyldig
            except ValueError:
                print("Ugyldig input. Skriv inn et tall for arbeidstimer prøv igjen.")
                continue
            # sjekker om timer er mellom 7.75 og 9
            if timer_over < 7.75 or timer_over > 9:
                print("Ugyldig input. Timer må være mellom 7.75 og 9.")
                continue
            # bryter løkken hvis input er gyldig
            break
        # beregner differanse mellom innrapporterte timer og standard arbeidstimer
        differanse = timer_over - arbeidstimer_per_dag
        # oppdaterer fleksitid med den nye differansen
        fleksitid.append(differanse + fleksitid[-1])
        # printer fleksitid for dagen og oppdatert samlet fleksitid
        
        # oppdaterer csv-filen med ny fleksitid
        df = pd.DataFrame(fleksitid, columns=['Fleksitid'])
        df.to_csv('fleksitid.csv', index=False)
        print(f"Fleksitid for {dag}: {to_hours_and_minutes(differanse)}")
        print(f"Oppdatert samlet fleksitid: {to_hours_and_minutes(fleksitid[-1])}")
        


                    
# definerer en funksjon for å konvertere desimaler til timer og minutter
def to_hours_and_minutes(timer_float):
    # deklarerer en variabel for timer og minutter
    hours = int(timer_float)
    # beregner antall timer og minutter
    minutes = int(round((timer_float - hours) * 60))
    # returnerer formatert streng med timer og minutter
    return f"{hours}t {minutes}m"





# definerer funksjon for å registrere brukte fleksitimer
def used_flex():
    # henter csv-data
    fleksitid = read_csv()

    # starter løkke for å hente brukerinput    
    for dag in ukedager:
        # kjører input-prosessen i en løkke for å sikre gyldig input
        while True:
            # printer nåværende fleksitid
            print(f"Nåverende samlet fleksitid er: {to_hours_and_minutes(fleksitid[-1])}")
            # ber brukeren om å skrive inn antall brukte flekstimer for dagen
            timer_brukt = input(f"Skriv inn antall brukte fleksitimer for {dag}: ")
            # sjekker om brukeren ønsker å avbryte
            if timer_brukt.lower() in ['exit', 'quit', 'q']:
                print("Avbryter tilføringen.")
                return
            # prøver å konvertere input til float
            try:
                # konverterer input til float
                timer_brukt = float(timer_brukt)
            # håndterer feil hvis input ikke kan konverteres til float
            except ValueError:
                print("Ugyldig input. Skriv inn et tall for brukte flekstimer prøv igjen.")
                continue
            if timer_brukt < 0 or timer_brukt > 9:
                print("Ugyldig input. Timer må være mellom 0 og 9.")
                continue
            # bryter løkken hvis input er gyldig
            break
        # definerer variabel for brukte timer
        brukte_timer = timer_brukt
        # oppdaterer fleksitid ved å trekke fra brukte timer
        fleksitid.append(fleksitid[-1] - brukte_timer)
        # skriver ut brukte flekstimer og oppdatert samlet fleksitid

        # oppdaterer csv-filen med ny fleksitid
        df = pd.DataFrame(fleksitid, columns=['Fleksitid'])
        df.to_csv('fleksitid.csv', index=False)

        print(f"Brukte flekstimer for {dag}: {to_hours_and_minutes(brukte_timer)}")
        print(f"Oppdatert samlet fleksitid: {to_hours_and_minutes(fleksitid[-1])}")
 


# hovedprogrammet
def main_menu():
    while True:
        print("Velkommen til Fleksitidskalkulatoren!")
        print("Legge til arbeidstimer (1) eller registrere brukte fleksitimer (2)?")
        svar = input("Skriv inn ditt svar (1/2) eller 'exit' for å avslutte: ").strip().lower()

        if svar in ("exit", "quit", "q"):
            print("Avslutter programmet.")
            return
        elif svar == "1":
            calculate_flex()
        elif svar == "2":
            used_flex()
        else:
            print("Ugyldig svar. Vennligst skriv '1' eller '2'.\n")

if __name__ == "__main__":
    main_menu()