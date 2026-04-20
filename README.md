
# 🚀 求人市場分析プラットフォーム (IT Job Market Analysis)

### Python × Flask × ETL × Cloud Deployment (Render)

[](https://www.google.com/search?q=https://it-job-analysis-5.onrender.com/)
[](https://www.python.org/)
[](https://flask.palletsprojects.com/)

求人データを活用したエンドツーエンドの\*\*データ分析基盤（ETLパイプライン）\*\*を構築。スクレイピングによるデータ取得から、SQLiteによる永続化、可视化ダッシュボードまでを一貫して実装したプロジェクトです。

-----

## 📽️ Dashboard Overview (デモ)

アクセス：**[https://it-job-analysis-5.onrender.com/](https://www.google.com/search?q=https://it-job-analysis-5.onrender.com/)**

> ※無料プランを使用しているため、最初のアクセス時にスリープ解除で30秒〜1分ほどかかる場合があります。

以下は実際のダッシュボード操作のデモです：

![demo](static/demo.gif)

-----

## 🔥 プロジェクトのハイライト (Highlights)

  - **一気通貫のETL実装**: データ取得（Extract）→ 整形（Transform）→ 保存（Load）→ 可視化。
  - **ポータブルな設計**: MySQLからSQLiteへの移行により、サーバーレス環境（Render）へのデプロイを実現。
  - **データドリブンな考察**: スキル需要と給与の関係を定量的に分析。
  - **即時更新機能**: `/update` エンドポイントにより、Web上から最新のデータ取得をトリガー可能。

-----

## 📈 分析レポート (Insights)

求人サイトから取得したデータを基に、以下の傾向を確認しました：

### 1\. Pythonの圧倒的需要と給与水準

Python関連求人は、データ分析・ML（機械学習）領域において中心的な役割を果たしており、非常に需要が高いことが確認されました。
![salary](static/salary.png)


### 2\. スキルの組み合わせの強さ

`Python + SQL` の組み合わせが、求人数・平均给与ともに高い傾向にあります。Python単体よりも、実務価値が高いと判断されています。
![skills](static/skills.png)


### 3\. 高年収領域の特定

`Machine Learning` や `AI` 関連求人は求人数は少ないものの、平均給与は他スキルと比較して約15%〜20%高い傾向にあります。

-----

## 🏗️ システムアーキテクチャ (Architecture)

```text
[ Web Scraping ]  --> [ Data Cleaning ] --> [ SQLite Database ]
      (BeautifulSoup)       (Pandas)              (jobs.db)
                                                     |
[ Flask Dashboard ] <-- [ Visualization ] <----------+
  (Render Hosting)       (Matplotlib/Seaborn)
```

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
git clone https://github.com/snowxxyg/it-job-analysis.git
cd it-job-analysis

# 依存ライブラリのインストール
pip install -r requirements.txt

# データベースの初期化（オプション：既存のjobs.dbがない場合）
python main.py

# アプリ起動
python app.py
```

アクセス： `http://127.0.0.1:5000`

-----

## 📂 ディレクトリ構成 (File Structure)

```text
.
├── app.py              # Flask Webアプリ（エントリーポイント）
├── main.py             # ETLパイプライン実行スクリプト
├── analysis.py         # 数据集计・统计处理ロジック
├── visualize.py        # グラフ生成（Matplotlib）
├── crawler.py          # クロール制御
├── scraper.py          # スクレイピング処理
├── db.py               # データベース操作 (SQLite)
├── jobs.db             # データベースファイル
├── requirements.txt    # 依存パッケージ
└── static/             # 生成されたグラフ・CSS・デモ画像
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

-----
