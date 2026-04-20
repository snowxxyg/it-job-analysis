from analysis import get_analysis, get_skill_analysis, get_job_count
from crawler import crawl_data
from db import save_to_db
from report import generate_report
from visualize import plot_jobs, plot_salary, plot_skills
import os

def run_pipeline():
    os.makedirs("output", exist_ok=True)

    keywords = [
        "SQL",
        "Python",
        "データ分析",
        "データサイエンティスト",
        "機械学習",
        "AIエンジニア"
    ]

    # 1️⃣ 爬虫
    print("1. 爬虫中...")
    data = crawl_data(keywords)

    # 2️⃣ 入库
    print("2. 存数据库...")
    save_to_db(data)

    # 3️⃣ 数据分析
    print("3. 分析数据...")
    df_jobs, df_keyword = get_analysis()
    df_skills = get_skill_analysis()
    df_count = get_job_count()

    # 4️⃣ 图表
    print("4. 生成图表...")
    plot_jobs(df_count)
    plot_salary(df_keyword)   # ✅ 改这里
    plot_skills(df_skills)

    # 5️⃣ 报告
    print("5. 生成报告...")
    generate_report(df_jobs, df_keyword, df_skills, df_count)

    print("✅ 全流程完成！")

if __name__ == "__main__":
    run_pipeline()
