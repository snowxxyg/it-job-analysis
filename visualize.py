import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import font_manager
import os

# --- 字体解决逻辑开始 ---
# 1. 获取字体文件的绝对路径
current_dir = os.path.dirname(os.path.abspath(__file__))
# 确保文件名和你文件夹里的一模一样（建议把那个长名字改成 noto.ttf 比较方便）
font_path = os.path.join(current_dir, 'fonts', 'NotoSansJP-VariableFont_wght.ttf')

# 2. 如果文件存在，注册并设置为全局默认字体
if os.path.exists(font_path):
    # 将字体加入 Matplotlib 的字体管理器
    font_manager.fontManager.addfont(font_path)
    # 获取字体的正式名称（Noto Sans JP）
    prop = font_manager.FontProperties(fname=font_path)
    # 设置全局字体
    plt.rcParams['font.family'] = prop.get_name()
    print(f"✅ 成功加载字体: {prop.get_name()}")
else:
    print(f"⚠️ 找不到字体文件: {font_path}，将使用系统默认字体（可能乱码）")

# 解决负号显示问题
plt.rcParams['axes.unicode_minus'] = False
# --- 字体解决逻辑结束 ---

def plot_jobs(df):
    plt.figure(figsize=(8, 4))
    sns.barplot(x="keyword", y="count", data=df)
    plt.title("求人数") # 现在这里会自动使用 Noto Sans JP
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
