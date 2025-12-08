# 🕒 Fleksitidskalkulator  

**Laget av Sondre Haugom**  

Et brukervennlig Python-program som lar deg **registrere, beregne og holde oversikt over fleksitid** i løpet av arbeidsuker.  
Du kan både legge til arbeidstimer og trekke fra brukte (uttatte) fleksitimer.  
All informasjon lagres automatisk i en SQLlite database som aoutmatisk blir opprette ved første bruk 

---

## 🚀 Hovedfunksjoner  

- 🧮 **Registrer arbeidstimer for hver ukedag** for hver dag uka vil du kunne legge til å fjerne flekstimer.  
- 📊 **Se oppdatert og historisk fleksitid** for hver dag.  
- ⏳ **Registrer brukte fleksitimer** og få full oversikt over saldoen.  
- 💾 **Automatisk lagring** og henting av data fra en SQLlite database (`fleks.db`).  
- ⚠️ **Feilhåndtering** for ugyldig input, tom fil og manglende data.  

---

## 📁 Filstruktur  

| Fil/Mappe                | Beskrivelse                                         |
|--------------------------|----------------------------------------------------|
| `Fleksitid_kalkulator/`  | Rotmappe for prosjektet                            |
| ├── `fleksdb/`           | Mappe for databasehåndtering                       |
| │   └── `database.py`    | Funksjoner for tilkobling og spørringer mot db     |
| ├── `utils/`             | Hjelpefunksjoner (utilities)                       |
| │   └── `time_utils.py`  | Funksjoner for tidshåndtering og konvertering      |
| ├── `README.md`          | Prosjektbeskrivelse og dokumentasjon               |
| ├── `fleks.db`           | SQLite-databasefil                                 |
| └── `main.py`            | Hovedprogrammet (startpunkt for applikasjonen)     |

---

## 🧩 Krav  

- Python **3.8** eller nyere  
- Bibliotek: **pandas**
- Bibliotek: **sqlite3** - allerede inkuldert i python

Installer `pandas` ved å skrive i terminalen:  
```bash
pip install pandas

```
## Bruk
``` 
python main.py
``` 

# Velg et alternativ i menyen:
- Tast 1 for å registrere arbeidstimer for en dag.

- Tast 2 for å registrere brukte fleksitimer.

- Tast exit eller quit for å avslutte programmet.

# Følg instruksjonene på skjermen
- Kun numeriske verdier mellom 7.5 og 12.5 godtas som gyldige arbeidstimer.

## Eksempel på bruk
``` 
Velkommen til fleksitidskalkulatoren!
Legge til arbeidstimer (1) eller registrere brukte fleksitimer (2)?
Skriv inn ditt svar (1/2) eller 'exit' for å avslutte: 1
Nåverende samlet fleksitid er: 0t 0m
Skriv inn antall arbeidstimer for Mandag: 9
    → Mandag 9.0 t (differanse: +1.25 t)
Oppdatert samlet fleksitid: 1t 15m
Nåverende samlet fleksitid er: 1t 15m
Skriv inn antall arbeidstimer for Tirsdag: 

```

Etter kjøring vil databasen inneholde:

![Skjermbilde av programmet](Skjermbilde2025-12-08085837.png)
![Skjermbilde av programmet](Skjermbilde2025-12-08085901.png)

## ⚙️ Forutsetninger
- Programmet er utviklet for Python 3.x.
- Om databasen ikke ikke er oprettes, opprettes den automatisk.
- All fleksitid lagres som flyttall (timer), men vises i timer og minutter i konsollen.
