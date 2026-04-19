import pandas as pd


def generate_report(df_jobs, df_salary, df_skills, df_count):
    with pd.ExcelWriter("output/report.xlsx") as writer:

        df_jobs.to_excel(writer, sheet_name="raw_data", index=False)
        df_salary.to_excel(writer, sheet_name="salary", index=False)
        df_skills.to_excel(writer, sheet_name="skills", index=False)
        df_count.to_excel(writer, sheet_name="job_count", index=False)

    print("📊 Excel报告生成完成")