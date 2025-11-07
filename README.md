# Fleksitidskalkulator

Laget av Sondre Haugom

Dette programmet lar deg **registrere og holde oversikt over oppspart fleksitid** i en arbeidsuke, samt registrere timer du tar ut som fleksitid. All informasjon lagres automatisk i en CSV-fil slik at du enkelt kan fortsette der du slapp.

## Hovedfunksjoner

- Legg til arbeidstimer for en dag og beregn differanse mot standard arbeidsdag (7,5 timer).
- Se oppdatert og historisk fleksitid for hver dag.
- Registrer brukte (uttatte) fleksitimer, og få full oversikt over saldo.
- All data lagres automatisk i og leses fra en CSV-fil (`fleksitid.csv`).

## Filstruktur

- **fleksitid.csv** – lagrer alle verdier for fleksitid.
- **Python-koden** – inneholder funksjoner for å registrere og bruke fleksitid.

## Bruk

1. Kjør programmet:
    ```bash
    python <navn_på_kodefil.py>
    ```

2. Velg menyvalg:
    - Tast **1** for å registrere arbeidstimer for en dag.
    - Tast **2** for å registrere brukte fleksitimer.
    - Tast **exit** eller **quit** for å avslutte programmet.

3. Følg instruksjonene på skjermen for å legge inn timer (kun verdier mellom 7,5 og 12,5 godtas).

## Eksempel på bruk
```
Velkommen til Fleksitidskalkulatoren!
Legge til arbeidstimer (1) eller registrere brukte fleksitimer (2)?
Skriv inn ditt svar: 1
Nåverende samlet fleksitid er: 2.00 timer
Skriv inn antall arbeidstimer for dagen: 8
Fleksitid for dagen: 0.50 timer
Dag 1: +0.00 timer
Dag 2: +0.50 timer
Oppdatert samlet fleksitid: 2.50 timer
```

## Forutsetninger

- Programmet er testet i Python 3 og krever at `pandas`-biblioteket er installert.
- Om **fleksitid.csv** ikke finnes eller er tom ved oppstart, opprettes den automatisk.
- Kun numeriske verdier mellom 7.5 og 12.5 godtas for arbeidstimer.

## Videreutvikling

Dette er et enkelt fleksitidsverktøy for lærlingoppgaver. Programmet kan forbedres ved å:
- Tillate registering av flere dager samtidig (for eksempel en hel uke).
- Legge til dato eller ukedag på hver føring.
- Bedre håndtering av feilsituasjoner, som f.eks. ugyldig/tom fil.
- Lage en egen rapport/utskrift over utviklingen over tid.

## Lisens

Koden er laget av Sondre Haugom som del av lærlingperiode og kan brukes fritt til læring og utvikling.
