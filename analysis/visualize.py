import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams["font.family"] = ["Meiryo", "Yu Gothic"]


def plot_jobs(df):
    plt.figure(figsize=(8, 4))
    sns.barplot(x="keyword", y="count", data=df)
    plt.title("求人数")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig("static/job_count.png")
    plt.close()


def plot_salary(df):
    plt.figure(figsize=(8, 4))
    sns.barplot(x="keyword", y="avg_salary_man", data=df)
    plt.title("平均給与（万円）")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig("static/salary.png")
    plt.close()


def plot_skills(df):
    df = df.head(10)

    plt.figure(figsize=(8, 4))
    sns.barplot(x="skill", y="count", data=df)
    plt.title("人気スキル")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig("static/skills.png")
    plt.close()