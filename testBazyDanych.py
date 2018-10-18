import sqlite3

con = sqlite3.connect('baza.db')

# dostęp do kolumn przez indeksy i przez nazwy
con.row_factory = sqlite3.Row

# utworzenie obiektu kursora
cur = con.cursor()
#usuniecie tabeli
cur.execute('''DROP TABLE IF EXISTS user''')
#tworzenie tabeli
cur.execute('''CREATE TABLE IF NOT EXISTS user(
              user_id    INTEGER PRIMARY KEY AUTOINCREMENT, 
              rejestracja  TEXT NOT NULL,
              telefon    INTEGER NOT NULL,
              zweryfikowany INTEGER DEFAULT 0
            )''')
cur.execute('''CREATE TABLE IF NOT EXISTS zgloszenia(
              zgloszenie_id     INTEGER,
              rejestracja   TEXT, 
              zgloszenie_user_id INTEGER,
              FOREIGN KEY(zgloszenie_user_id) REFERENCES user(user_id)
            )''')

#imie = str(input('Podaj rejestracje telefon'))
rekord = ['SDO1234',123456789]
#wstawianie rekordu
cur.execute('INSERT INTO user(rejestracja,telefon) VALUES(?,?);', rekord)
print("Dodano rekord")
cur.execute('SELECT * FROM user')
print(cur.fetchone()[:])
con.commit()
