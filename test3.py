import pymysql

# Connexion à la base de données BaseDeDonnees1
conn1 = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="BaseDeDonnees1"
)

# Connexion à la base de données BaseDeDonnees2
conn2 = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="BaseDeDonnees2"
)

cursor1 = conn1.cursor()
cursor2 = conn2.cursor()

try:
    # Récupérer les données de TableA de BaseDeDonnees1
    cursor1.execute("SELECT nom FROM TableA")
    rows_tableA = cursor1.fetchall()

    # Récupérer les données de TableB de BaseDeDonnees1
    cursor1.execute("SELECT description FROM TableB")
    rows_tableB = cursor1.fetchall()

    # Associer les données de TableA et TableB et insérer dans TableC de BaseDeDonnees2
    for nom, description in zip(rows_tableA, rows_tableB):
        cursor2.execute("INSERT INTO TableC (nom, description) VALUES (%s, %s)", (nom[0], description[0]))

    # Valider les modifications dans la base de données BaseDeDonnees2
    conn2.commit()
    print("Insertion réussie dans la table TableC de BaseDeDonnees2")

    # Récupérer et afficher les données insérées dans TableC de BaseDeDonnees2
    cursor2.execute("SELECT * FROM TableC")
    rows_tableC = cursor2.fetchall()

    print("Données insérées dans TableC de BaseDeDonnees2:")
    for row in rows_tableC:
        print(row)

except pymysql.MySQLError as err:
    print(f"Erreur MySQL : {err}")

finally:
    # Fermer les connexions
    cursor1.close()
    conn1.close()
    cursor2.close()
    conn2.close()
