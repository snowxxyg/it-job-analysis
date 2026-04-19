from scraper import get_jobs
import time


def crawl_data(keywords, pages=3):
    all_jobs = []

    for keyword in keywords:
        for page in range(1, pages + 1):
            print(f"[{keyword}] Page {page}")

            try:
                jobs = get_jobs(keyword, page)

                for job in jobs:
                    job["keyword"] = keyword

                all_jobs.extend(jobs)

            except Exception as e:
                print(f"Error: {e}")

            time.sleep(1)

    return all_jobs

import re

def parse_salary(text):
    if not text:
        return None, None

    # 统一处理：去空格
    text = text.replace(",", "").strip()

    # 匹配 “xx万〜yy万”
    match = re.search(r"(\d+\.?\d*)万.*?(\d+\.?\d*)万", text)
    if match:
        min_salary = float(match.group(1)) * 10000
        max_salary = float(match.group(2)) * 10000
        return min_salary, max_salary

    # 匹配单个 “xx万”
    match = re.search(r"(\d+\.?\d*)万", text)
    if match:
        val = float(match.group(1)) * 10000
        return val, None

    return None, None