import sqlite3

def save_to_db(data):
    # 连接到本地文件 jobs.db
    conn = sqlite3.connect("jobs.db")
    cursor = conn.cursor()

    # 1. 如果表不存在，先创建表（SQLite 需要手动确保表存在）
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS jobs (
        title TEXT,
        company TEXT,
        salary_min INTEGER,
        salary_max INTEGER,
        location TEXT,
        skills TEXT,
        keyword TEXT,
        PRIMARY KEY (title, company, keyword) 
    )
    """)

    # 2. SQLite 的“存在即更新”语法是 INSERT OR REPLACE
    sql = """
    INSERT OR REPLACE INTO jobs (title, company, salary_min, salary_max, location, skills, keyword)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """

    for d in data:
        cursor.execute(sql, (
            d["title"], d["company"], d["salary_min"],
            d["salary_max"], d["location"], d["skills"], d["keyword"]
        ))

    conn.commit()
    conn.close()
