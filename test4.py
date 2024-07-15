import pymysql

# Connexion à la nouvelle BaseDeDonnees1 (pour récupérer les données)
conn1 = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="NouvelleBaseDeDonnees1"
)

# Connexion à la nouvelle BaseDeDonnees2 (pour insérer les données)
conn2 = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="NouvelleBaseDeDonnees2"
)

cursor1 = conn1.cursor()
cursor2 = conn2.cursor()

try:
    # Récupérer les données de NouvelleTableA de NouvelleBaseDeDonnees1
    cursor1.execute("SELECT nom FROM NouvelleTableA")
    rows_tableA = cursor1.fetchall()

    # Récupérer les données de NouvelleTableB de NouvelleBaseDeDonnees1
    cursor1.execute("SELECT description FROM NouvelleTableB")
    rows_tableB = cursor1.fetchall()

    # Insertion des données récupérées dans NouvelleTableC de NouvelleBaseDeDonnees2
    for nom, description in zip(rows_tableA, rows_tableB):
        cursor2.execute("INSERT INTO NouvelleTableC (nom, description) VALUES (%s, %s)", (nom[0], description[0]))

    conn2.commit()
    print("Insertion de données réussie dans NouvelleTableC de NouvelleBaseDeDonnees2")

    # Afficher les données insérées dans NouvelleTableC pour vérification
    cursor2.execute("SELECT * FROM NouvelleTableC")
    rows_tableC = cursor2.fetchall()

    print("Données insérées dans NouvelleTableC de NouvelleBaseDeDonnees2:")
    for row in rows_tableC:
        print(row)

except pymysql.MySQLError as err:
    print(f"Erreur MySQL : {err}")

finally:
    # Fermeture des connexions
    cursor1.close()
    conn1.close()
    cursor2.close()
    conn2.close()
