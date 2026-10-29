import sqlite3

def get_user(username):
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()

    cursor.execute(
        "CREATE TABLE users (username TEXT, role TEXT)"
    )
    cursor.execute(
        "INSERT INTO users VALUES ('demo', 'user')"
    )

    # INTENTIONAL VULNERABILITY: SQL query built using string formatting.
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)

    result = cursor.fetchall()
    conn.close()
    return result


if __name__ == "__main__":
    print(get_user("demo"))
