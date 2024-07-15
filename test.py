
import pymysql

# Connexion à la base de données
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="base_combinee"
)

cursor = conn.cursor()

try:
    # Récupérer les données de la table `resultat_combinaison`
    cursor.execute("SELECT nom_employe, nom_projet FROM resultat_combinaison")
    rows_resultat_combinaison = cursor.fetchall()

    # Afficher les résultats récupérés
    print("Résultats de la table resultat_combinaison:")
    for row in rows_resultat_combinaison:
        print(row)

    # Exemple d'insertion dans une nouvelle table T3
    cursor.execute("CREATE TABLE IF NOT EXISTS T3 (id INT AUTO_INCREMENT PRIMARY KEY, nom_employe VARCHAR(50), nom_projet VARCHAR(50))")

    for row in rows_resultat_combinaison:
        nom_employe = row[0]
        nom_projet = row[1]
        cursor.execute("INSERT INTO T3 (nom_employe, nom_projet) VALUES (%s, %s)", (nom_employe, nom_projet))

    # Valider les modifications dans la base de données
    conn.commit()
    print("Insertion réussie dans la table T3")

except mysql.connector.Error as err:
    print(f"Erreur MySQL : {err}")

finally:
    # Fermer les connexions
    cursor.close()
    conn.close()
