import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="Ahmed",
    password="Ruxxaa@000",
    database="Football"
)

cursor = db.cursor()

# cursor.execute("CREATE TABLE TeamB (id int PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50), age smallint UNSIGNED)")
# cursor.execute("INSERT INTO TeamA (name, age) VALUES ('wael', 12)")
# db.commit()

# cursor.execute("SELECT * FROM TeamB")
# for x in cursor:
#     print(x)


# TeamB = [("medhat", "28"),
#          ("hassan", "82"),
#          ("taha", "11"),
#          ]

# cursor.executemany("INSERT INTO TeamB (name, age) VALUES (%s, %s)", TeamB)
# db.commit()


cursor.execute(" SELECT * FROM TeamA JOIN TeamB USING (id) WHERE id = 1 ")
db.commit()

