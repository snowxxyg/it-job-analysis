from flask import Flask, render_template, request
<<<<<<< HEAD
from analysis.analysis import (
    get_analysis,
    get_job_count,
    get_skill_analysis,
    get_kpi
)
from analysis.visualize import plot_jobs, plot_salary, plot_skills
=======
from analysis import get_analysis, get_job_count, get_skill_analysis, get_kpi
from visualize import plot_jobs, plot_salary, plot_skills
>>>>>>> d4ab1f1b6b7ad2bbe1ba05efc1d77e079e7130a1
from main import run_pipeline

app = Flask(__name__)


@app.route("/")
def index():
    keyword = request.args.get("keyword")

    df_jobs, df_salary = get_analysis(keyword)
    df_count = get_job_count(keyword)
    df_skills = get_skill_analysis(keyword)

    # 🔥 生成图表（每次刷新自动更新）
    plot_jobs(df_count)
    plot_salary(df_salary)
    plot_skills(df_skills)

    total_jobs, avg_salary, top_skill = get_kpi(df_jobs, df_skills)

    return render_template(
        "index.html",
        keyword=keyword,
        total_jobs=total_jobs,
        avg_salary=avg_salary,
        top_skill=top_skill,
        tables={
            "jobs": df_jobs.head(20).to_html(classes="table table-striped", index=False),
            "skills": df_skills.head(20).to_html(classes="table table-striped", index=False),
            "keyword": df_count.to_html(classes="table table-striped", index=False),
        }
    )


@app.route("/update")
def update():
    run_pipeline()
    return "データ更新完了！"


if __name__ == "__main__":
    app.run(debug=True)