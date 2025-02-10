import psycopg2

try:
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="Admin1234",
        host="localhost",
        port="5432",
        options="-c client_encoding=UTF8"
    )
    print("Connexion PostgreSQL réussie !")
    conn.close()
except Exception as e:
    print("Erreur de connexion :", e)
