import requests
from bs4 import BeautifulSoup
from urllib.parse import quote
import re

BASE_URL = "https://xn--pckua2a7gp15o89zb.com"

headers = {
    "User-Agent": "Mozilla/5.0"
}




def parse_salary(text):
    if not text:
        return None, None

    # 去掉逗号
    text = text.replace(",", "")

    # 只处理「万」单位
    if "万" not in text:
        return None, None

    # 匹配 60万〜100万
    match = re.search(r"(\d+\.?\d*)\s*万.*?(\d+\.?\d*)\s*万", text)
    if match:
        return float(match.group(1)) * 10000, float(match.group(2)) * 10000

    # 匹配单个 80万
    match = re.search(r"(\d+\.?\d*)\s*万", text)
    if match:
        val = float(match.group(1)) * 10000
        return val, None

    return None, None

def get_jobs(keyword, page):
    keyword_encoded = quote(keyword)
    url = f"{BASE_URL}/{keyword_encoded}%E3%81%AE%E4%BB%95%E4%BA%8B-%E6%9D%B1%E4%BA%AC%E9%83%BD?pg={page}"

    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "lxml")

    jobs = []

    items = soup.select("section.p-result_card")

    for item in items:
        title = item.select_one(".p-result_name")
        company = item.select_one(".p-result_company")
        salary = item.select_one(".p-result_pay")
        location = item.select_one(".p-result_area")

        tags = item.select(".p-result_tag li")
        skills = [t.text.strip() for t in tags]

        salary_text = salary.text.strip() if salary else ""
        salary_min, salary_max = parse_salary(salary_text)

        jobs.append({
            "title": title.text.strip() if title else "",
            "company": company.text.strip() if company else "不明",
            "salary_min": salary_min,
            "salary_max": salary_max,
            "location": location.text.strip() if location else "",
            "skills": ",".join(skills)
        })

    return jobs