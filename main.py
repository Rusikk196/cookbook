import sqlite3
import os

DB_NAME = "cookbook.db"

def ensure_db():
    is_new = not os.path.exists(DB_NAME)
    conn - sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    if is_new:
        print("База данных не найдена. Создаём cookbook.db и таблицу cookbooks...")
        cur.execute("""
                    CREATE TABLE IF NOT EXISTS cookbooks 
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT NOT NULL,
                        year INTEGER,
                        price REAL
                    )
                """)
        books = [
            ("Искусство кулинарии", 2001, 499.99),
            ("Современная кухня", 2010, 799.50),
            ("Быстрые рецепты", 2018, 350.00),
            ("Домашние блюда", 2020, 600.00),
            ("Кулинария народов мира", 2015, 999.00)
        ]
        cur.executemany("INSERT INTO cookbooks (title, year, price) VALUES (?, ?, ?)", books)
        conn.commit()
        print("Таблица создана и заполнена начальными данными.")
    else:
        print("Файл базы данных уже существует. Ничего создавать не нужно.")

    conn.close()
    
def main():
    print("Это консольное приложение хранит в себе названия поваренных книг в формате SQL.")
    ensure_db()

if __name__ == "__main__":
    main()