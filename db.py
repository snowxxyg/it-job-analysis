import pymysql

def save_to_db(data):
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="0811",
        database="job_db"
    )
    cursor = conn.cursor()

    sql = """
    INSERT INTO jobs (title, company, salary_min, salary_max, location, skills, keyword)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE
    salary_min=VALUES(salary_min),
    salary_max=VALUES(salary_max)
    """

    for d in data:
        cursor.execute(sql, (
            d["title"], d["company"], d["salary_min"],
            d["salary_max"], d["location"], d["skills"], d["keyword"]
        ))

    conn.commit()
    conn.close()