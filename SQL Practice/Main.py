import mysql.connector 
#importing MySQL and connecting it with my localhost.
db = mysql.connector.connect(
    host="localhost",
    user="Ahmed",
    password="XXXXXXXXXX",
    database="testdatabase"
)

cursor = db.cursor()

#Creating, inserting and assigning its attributes
cursor.execute("CREATE TABLE person (name VARCHAR(50), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)")

cursor.execute("INSERT INTO person(name, age) VALUES('hazem', 30)")
db.commit()

cursor.execute("SELECT * FROM person")

for x in cursor:
    print(x)

cursor.execute("SELECT * FROM person WHERE personId = 2 ")

for x in cursor:
    print(x)

#Making changes in my tables.
cursor.execute("ALTER TABLE person ADD COLUMN email VARCHAR(250) ")

cursor.execute("ALTER TABLE person CHANGE name first_name VARCHAR(50)")
cursor.execute("DESCRIBE person")

for i in cursor:
    print(i)

#Creating two tables and joining them together with one to one connection. 

users = [("ahmed", "123"),
         ("hazem", "000"),
         ("hussein", "888")
         ]

user_scores = [(45, 100),
               (88, 212),
               (91, 180)
               ]



Q1 = "CREATE TABLE Users (id int PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50), password VARCHAR(100))"
Q2 = "CREATE TABLE Scores (userId int PRIMARY KEY, FOREIGN KEY(userId) REFERENCES Users(id), game1 int DEFAULT 0, game2 int DEFAULT 0)"
#for "for loop"
Q3 = "INSERT INTO Users (name, password) VALUES (%s, %s)"
Q4 = "INSERT INTO Scores (userId, game1, game2) VALUES (%s, %s, %s)"

cursor.execute(Q1)
cursor.execute(Q2)

cursor.execute("SHOW TABLES")
for x in cursor:
    print(x)


#Here is way to insert all the data from a giving list with the "executemany"
cursor.executemany("INSERT INTO Scores (game1, game2) VALUES (%i , %i)", user_scores)
db.commit()

cursor.execute("SELECT * FROM Scores")
for x in cursor:
    print(x)


#Here is another way of inserting the data using "For Loop"

for x, user in enumerate(users):
    cursor.execute(Q3, user)
    last_id = cursor.lastrowid
    cursor.execute(Q4, (last_id,) + user_scores[x])

cursor.execute("SELECT * FROM Users ")

for x in cursor:
    print(x)







