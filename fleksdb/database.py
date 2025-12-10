import sqlite3
# deklarerer databasebane
DB_PATH = "fleks.db"   

# legger til en funksjon for å koble til databasen og opprette tabellen hvis den ikke finnes
def get_connection():
    # Åpner (eller oppretter) databasen og sørger for tabellen.
    conn = sqlite3.connect(DB_PATH)
    # oppretter tabellen hvis den ikke finnes
    conn.execute("""CREATE TABLE IF NOT EXISTS fleksitid (
                       id        INTEGER PRIMARY KEY AUTOINCREMENT, 
                       type      TEXT    NOT NULL CHECK (type IN ('INN','UT')), 
                       timer     REAL    NOT NULL, 
                       balanse   REAL    NOT NULL, 
                       kommentar TEXT 
                   );""")
    
    # lager/comitter endrinegr
    conn.commit()
    # returner database-tilkoblingen 
    return conn

# funksjon for å hente siste balanse fra databasen 
def get_last_balance():
    # få forbindelse til databasen
    conn = get_connection()
    # oppretter en cursor
    cur = conn.cursor()
    # henter siste balanse
    cur.execute("SELECT balanse FROM fleksitid ORDER BY id DESC LIMIT 1;")
    # legger resultatet i en variabel
    result = cur.fetchone()
    # returnerer balansen eller 0.0 hvis ingen data finnes
    if result:
        return result[0]
    else:
        return 0.0

def db_insert(type, timer, balanse, kommentar):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO fleksitid (type, timer, balanse, kommentar) VALUES (?, ?, ?, ?);",
        (type, timer, balanse, kommentar)
    )
    conn.commit()
    conn.close()
