# 🕒 Fleksitidskalkulator  

**Laget av Sondre Haugom**  

Et brukervennlig Python-program som lar deg **registrere, beregne og holde oversikt over fleksitid** i løpet av arbeidsuker.  
Du kan både legge til arbeidstimer og trekke fra brukte (uttatte) fleksitimer.  
All informasjon lagres automatisk i en CSV-fil slik at du alltid kan fortsette der du slapp.  

---

## 🚀 Hovedfunksjoner  

- 🧮 **Registrer arbeidstimer for hver ukedag** for hver dag uka vil du kunne legge til å fjerne flekstimer.  
- 📊 **Se oppdatert og historisk fleksitid** for hver dag.  
- ⏳ **Registrer brukte fleksitimer** og få full oversikt over saldoen.  
- 💾 **Automatisk lagring** og henting av data fra en CSV-fil (`fleksitid.csv`).  
- ⚠️ **Feilhåndtering** for ugyldig input, tom fil og manglende data.  

---

## 📁 Filstruktur  

| Fil | Beskrivelse |
|-----|--------------|
| `fleksitid.csv` | Lagrer all fleksitidsinformasjon automatisk. Opprettes ved første kjøring. |
| `fleksitid.py` | Hovedfilen som inneholder funksjonene for registrering og bruk av fleksitid. |

---

## 🧩 Krav  

- Python **3.8** eller nyere  
- Bibliotek: **pandas**

Installer `pandas` ved å skrive i terminalen:  
```bash
pip install pandas

```
## Bruk
``` 
python fleksitid.py
``` 

# Velg et alternativ i menyen:
- Tast 1 for å registrere arbeidstimer for en dag.

- Tast 2 for å registrere brukte fleksitimer.

- Tast exit eller quit for å avslutte programmet.

# Følg instruksjonene på skjermen
- Kun numeriske verdier mellom 7.5 og 12.5 godtas som gyldige arbeidstimer.

## Eksempel på bruk
``` 
Velkommen til Fleksitidskalkulatoren!
Legge til arbeidstimer (1) eller registrere brukte fleksitimer (2)?
Skriv inn ditt svar (1/2) eller 'exit' for å avslutte: 1
Nåverende samlet fleksitid er: 17t 47m
Skriv inn antall arbeidstimer for Mandag: 8
Fleksitid for Mandag: 0t 15m
Oppdatert samlet fleksitid: 18t 2m
Nåverende samlet fleksitid er: 18t 2m
Skriv inn antall arbeidstimer for Tisdag: 

```

Etter kjøring vil filen fleksitid.csv inneholde:

``` 
Fleksitid
0.0
0.3
2.3
```

## ⚙️ Forutsetninger
- Programmet er utviklet for Python 3.x.
- Om fleksitid.csv ikke finnes eller er tom, opprettes den automatisk.
- All fleksitid lagres som flyttall (timer), men vises i timer og minutter i konsollen.

## 🧠 Videreutvikling
Mulige forbedringer i fremtidige versjoner:
- 📅 Legge til dato og ukedag for hver registrering.
- 📆 Mulighet for å registrere flere dager samtidig (f.eks. en hel uke).
- 🧾 Generere rapporter eller grafer over fleksitidsutviklingen.
- 🧱 Forbedret feilkontroll og robusthet mot ugyldige filer.
- 🌐 Enkel GUI- eller webversjon for mer brukervennlig opplevelse.

## 🪪 Lisens
Koden er utviklet av Sondre Haugom som del av en lærlingperiode.
Den kan brukes fritt til læring, utvikling og forbedring, så lenge opphav nevnes.

