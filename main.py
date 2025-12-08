# Lagte av Sondre Haugom
# importerer pandas som pd 
from fleksdb.database import get_connection, get_last_balance, db_insert


# deklarerer ukedager
ukedager = [
    "Mandag",
    "Tirsdag",
    "Onsdag",
    "Torsdag",
    "Fredag"
    ]
# Definerer en funksjon for å håndtere brukerinput
def user_input(dag):
    # løkke for å få gyldig input fra brukeren
    while True:
        # ber brukeren om å skrive inn antall arbeidstimer for en gitt dag
        timer_str = input(f"Skriv inn antall arbeidstimer for {dag}: ")
        # sjekker om brukeren ønsker å avslutte programmet
        if timer_str.lower() in ['exit', 'quit', 'q']:
            print("Avslutter programmet!")
            return None
        # prøver å konvertere input til float og sjekker gyldighet
        try:
            timer_over = float(timer_str)
        except ValueError:
            print("Ugyldig input. Skriv inn et tall for arbeidstimer prøv igjen.")
            continue
        if timer_over < 0 or timer_over > 10:
            print("Ugyldig input. Timer må være mellom 0 og 10.")
            continue
        return timer_over


# definerer funksjon for å kalkulere fleksitid
def calculate_flex():
    # henter databaseforbindelse og oppretter en cursor
    conn = get_connection()
    # initialiserer liste for fleksitid med siste balanse
    fleksitid = [get_last_balance()] 

    # definerer standard  arbeidstimer per dag
    arbeidstimer_per_dag = 7.75 

    # hovedløkke for programmet
    while True:
        print("Velkommen til fleksitidskalkulatoren!")
        print("Legge til arbeidstimer (1) eller registrere brukte fleksitimer (2)?")
        svar = input("Skriv inn ditt svar (1/2) eller 'exit' for å avslutte: ").strip().lower()
        if svar in ("exit", "quit", "q"):
            print("Avslutter programmet!")
            break
        # håndterer brukerens valg
        for dag in ukedager:
            if svar == "1":
                timer_over = user_input(dag)
                difference = timer_over - arbeidstimer_per_dag
                fleksitid.append(fleksitid[-1] + difference)
                print(f"    → {dag} {timer_over} t (differanse: {difference:+.2f} t)")
                print(f"Oppdatert samlet fleksitid: {fleksitid[-1]}")
                print()  # Legger til en tom linje for bedre lesbarhet
                db_insert('INN', timer_over, fleksitid[-1], f'Arbeidstimer for {dag}')
            elif svar == "2":
                timer_brukt = user_input(dag)
                brukte_timer = timer_brukt
                # oppdaterer  fleksitid listen
                fleksitid.append(fleksitid[-1] - brukte_timer)
                print(f"    → {dag} {brukte_timer} t)")
                print(f"Oppdatert samlet fleksitid: {fleksitid[-1]}")
                print()  # Legger til en tom linje for bedre lesbarhet
                db_insert('UT', timer_brukt, fleksitid[-1], f'Brukte fleksitimer for {dag}')

    
    # Lukker database-forbindelsen
    conn.close()
    print("Ferdig med registrering for alle dager!")

# kjører hovedmenyen hvis filen kjøres som et skript
if __name__ == "__main__":
    calculate_flex()