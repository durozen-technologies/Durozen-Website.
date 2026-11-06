import psycopg

try:
    print("Testing connection to PostgreSQL with password 'root'...")
    conn = psycopg.connect("postgresql://postgres:root@localhost:5432/postgres")
    print("SUCCESS: Connected to PostgreSQL server!")
    conn.autocommit = True
    with conn.cursor() as cur:
        cur.execute("SELECT 1 FROM pg_database WHERE datname = 'durozen_db'")
        exists = cur.fetchone()
        if not exists:
            cur.execute("CREATE DATABASE durozen_db")
            print("SUCCESS: Created database 'durozen_db'!")
        else:
            print("Database 'durozen_db' already exists.")
    conn.close()

    # Now verify connection directly to durozen_db
    conn2 = psycopg.connect("postgresql://postgres:root@localhost:5432/durozen_db")
    print("SUCCESS: Connected to 'durozen_db' database!")
    conn2.close()

except Exception as e:
    print("ERROR:", e)

