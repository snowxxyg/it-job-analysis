
# 🚀 求人市場分析プラットフォーム (IT Job Market Analysis)
### Python × Flask × ETL × Cloud Deployment (Render)

[![Live Demo](https://img.shields.io/badge/demo-online-green.svg)](https://it-job-analysis-5.onrender.com/)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/flask-v3.x-lightgrey.svg)](https://flask.palletsprojects.com/)

求人データを活用したエンドツーエンドの**データ分析基盤（ETLパイプライン）**を構築。スクレイピングによるデータ取得から、SQLiteによる永続化、可視化ダッシュボードまでを一貫して実装したプロジェクトです。

---

## 📽️ Dashboard Overview (デモ)

🔗 **Live Demo: [https://it-job-analysis-5.onrender.com/](https://it-job-analysis-5.onrender.com/)**

> ⚠️ **Note:** 無料プランを使用しているため、最初のアクセス時にスリープ解除で30秒〜1分ほどかかる場合があります。

以下は実際のダッシュボード操作のデモです：

![demo](static/demo.gif)

---

## 🔥 プロジェクトのハイライト (Highlights)

- **一気通貫のETL実装**: データ取得（Extract）→ 整形（Transform）→ 保存（Load）→ 可視化。
- **ポータブルな設計**: MySQLからSQLiteへの移行により、サーバーレス環境（Render）へのデプロイを実現。
- **データドリブンな考察**: スキル需要と給与の関係を定量的に分析。
- **即時更新機能**: `/update` エンドポイントにより、Web上から最新のデータ取得をトリガー可能。

---

## 📈 分析レポートと可視化 (Analysis & Insights)

求人サイトから取得した最新データを基に、IT市場のトレンドを以下の3つの視点で分析しました。

### 1. 職種別の需要（求人数）分析
**Python** 関連の求人が最多であり、次いで **データサイエンティスト**、**機械学習** と続きます。これは、現在の市場において AI・データ活用スキルがエンジニアの共通言語（必須スキル）となっていることを裏付けています。

> **💡 Insight:** Pythonをベースとした職種が全体の過半数を占めており、安定した需要が見込めます。

<img width="600" alt="Job Count Analysis" src="https://github.com/user-attachments/assets/4dbea818-7205-445c-9aaa-cf86ce25476f" />

---

### 2. 給与水準と専門性の相関
職種別の平均給与を比較したところ、**AIエンジニア** と **データサイエンティスト** が 500〜600 万円以上の高水準に位置しています。求人数は Python 単体より少ないものの、専門性が高いほど給与水準も顕著に上昇する傾向があります。

> **💡 Insight:** 高年収を目指す場合、単なる開発スキルだけでなく、AIやデータ分析の専門特化が有効な戦略となります。

<img width="600" alt="Salary Analysis" src="https://github.com/user-attachments/assets/84535dd8-7fc1-43a6-88b5-4bcd6193e1ce" />

---

### 3. テクニカルスキル・ランキング
求人票から抽出した具体的なスキル需要では、**Python** が圧倒的1位であり、**データ分析**、**AWS**、**AI** がトップグループを形成しています。

> **💡 Insight:** 市場価値を最大化するには、`Python` を核として `SQL` や `AWS（クラウド）` を組み合わせる「スキルの掛け合わせ」が実務において非常に重要です。

<img width="600" alt="Skill Ranking" src="https://github.com/user-attachments/assets/5feed010-5243-4b08-b7f1-da30bcd264b0" />

---

## 🏗️ システムアーキテクチャ (Architecture)



```text
[ Web Scraping ]  --> [ Data Cleaning ] --> [ SQLite Database ]
      (BeautifulSoup)       (Pandas)              (jobs.db)
                                                     |
[ Flask Dashboard ] <-- [ Visualization ] <----------+
  (Render Hosting)       (Matplotlib/Seaborn)
````

-----

## ⚙️ 技術スタック (Tech Stack)

| カテゴリ | 技術 |
| :--- | :--- |
| **Backend** | Python 3.10+, Flask |
| **Data Analysis** | Pandas, NumPy |
| **Visualization** | Matplotlib, Seaborn |
| **Scraping** | Requests, BeautifulSoup4 |
| **Database** | SQLite (Self-contained) |
| **Deployment** | Render, Gunicorn |

-----

## 💻 ローカル実行方法 (Local Setup)

```bash
# クローン
git clone [https://github.com/snowxxyg/it-job-analysis.git](https://github.com/snowxxyg/it-job-analysis.git)
cd it-job-analysis

# 依存ライブラリのインストール
pip install -r requirements.txt

# データベースの初期化
python main.py

# アプリ起動
python app.py
```

-----

## 🚀 今後の展望 (Future Roadmap)

  - [ ] **Docker化**: 開発・本番環境の完全同期。
  - [ ] **REST APIの実装**: 分析結果をJSON形式で外部提供。
  - [ ] **クラウドDB (PostgreSQL) への移行**: データの永続性向上。

-----

### 作者

**snowxxyg**

  - GitHub: [@snowxxyg](https://www.google.com/search?q=https://github.com/snowxxyg)

<!-- end list -->
