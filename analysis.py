import pandas as pd
import pymysql
from collections import Counter


def get_db():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="0811",
        database="job_db",
        charset="utf8mb4"
    )


def format_salary(val):
    if pd.isna(val):
        return "不明"

    # 🔥 防止异常值（比如10000这种错误数据）
    if val < 50000:
        return "不明"

    return f"{round(val / 10000, 1)}万円"

def get_analysis(keyword=None):
    db = get_db()

    query = "SELECT * FROM jobs"
    if keyword:
        query += f" WHERE keyword = '{keyword}'"

    df_jobs = pd.read_sql(query, db)

    # 🔥 转换 salary
    df_jobs["salary_min"] = df_jobs["salary_min"].apply(format_salary)
    df_jobs["salary_max"] = df_jobs["salary_max"].apply(format_salary)

    # 🔥 平均薪资（用于图表）
    df_salary = pd.read_sql("""
        SELECT keyword, AVG(salary_min) as avg_salary
        FROM jobs
        GROUP BY keyword
    """, db)

    df_salary["avg_salary_man"] = df_salary["avg_salary"] / 10000

    db.close()
    return df_jobs, df_salary


def get_job_count(keyword=None):
    db = get_db()

    query = """
        SELECT keyword, COUNT(*) as count
        FROM jobs
    """

    if keyword:
        query += f" WHERE keyword = '{keyword}'"

    query += " GROUP BY keyword ORDER BY count DESC"

    df = pd.read_sql(query, db)
    db.close()
    return df


def get_skill_analysis(keyword=None):
    db = get_db()

    query = "SELECT skills FROM jobs WHERE skills IS NOT NULL"
    if keyword:
        query += f" AND keyword = '{keyword}'"

    df = pd.read_sql(query, db)
    db.close()

    skill_list = []

    tech_white_list = {
        "Python", "SQL", "AWS", "Linux", "Oracle",
        "Excel", "機械学習", "AI", "データ分析",
        "クラウド", "Git", "Java", "C#", "PHP"
    }

    for row in df["skills"]:
        if not row:
            continue
        for s in row.split(","):
            s = s.strip()
            if s in tech_white_list:
                skill_list.append(s)

    counter = Counter(skill_list)
    return pd.DataFrame(counter.most_common(), columns=["skill", "count"])

def get_kpi(df_jobs, df_skills):
    total_jobs = len(df_jobs)

    # 🔥 平均薪资（去掉“不明”）
    salary_series = df_jobs["salary_min"].replace("不明", None).dropna()

    if len(salary_series) > 0:
        salary_series = salary_series.str.replace("万円", "").astype(float)
        avg_salary = f"{round(salary_series.mean(), 1)}万円"
    else:
        avg_salary = "不明"

    # 🔥 最热门技能
    if not df_skills.empty:
        top_skill = df_skills.iloc[0]["skill"]
    else:
        top_skill = "不明"

    # ✅ 必须返回3个
    return total_jobs, avg_salary, top_skill