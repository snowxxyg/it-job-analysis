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


# 🔥 显示用（不影响计算）
def format_salary(val):
    if pd.isna(val):
        return "不明"

    # 防止异常值（比如 1万円）
    if val < 50000:
        return "不明"

    return f"{round(val / 10000, 1)}万円"


def get_analysis(keyword=None):
    db = get_db()

    query = "SELECT * FROM jobs"
    if keyword:
        query += f" WHERE keyword = '{keyword}'"

    df_jobs = pd.read_sql(query, db)

    # ✅ 新增展示字段
    df_jobs["salary_min_display"] = df_jobs["salary_min"].apply(format_salary)
    df_jobs["salary_max_display"] = df_jobs["salary_max"].apply(format_salary)

    # ======================
    # 🔥 这里直接删除原始列！！！
    # ======================
    df_jobs = df_jobs.drop(columns=["salary_min", "salary_max"])

    # 图表用（数值）
    df_salary = pd.read_sql("""
        SELECT keyword, AVG(salary_min) as avg_salary
        FROM jobs
        WHERE salary_min IS NOT NULL
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

    # 🔥 KPIはDBから再取得するので問題なし
    salary_series = df_jobs["salary_min_display"].replace("不明", None).dropna()

    # 从字符串变回数字（万円 → 数值）
    def to_num(s):
        try:
            return float(s.replace("万円", ""))
        except:
            return None

    salary_num = salary_series.apply(to_num).dropna()

    if len(salary_num) > 0:
        avg_salary = f"{round(salary_num.mean(), 1)}万円"
    else:
        avg_salary = "不明"

    # 最热门技能
    if not df_skills.empty:
        top_skill = df_skills.iloc[0]["skill"]
    else:
        top_skill = "不明"

    return total_jobs, avg_salary, top_skill