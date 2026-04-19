
# 🚀 求人市場分析プラットフォーム  
### Job Market Intelligence Platform（Python × Flask × ETL × Data Engineering）

---

## 📌 概要（Overview）

本プロジェクトは、求人データを対象にした  
**データ収集・処理（ETL）・分析・可視化・Webアプリケーション化**を  
一貫して実装したデータ分析プラットフォームです。

スクレイピングにより取得した求人情報を、  
SQLデータベースに保存し、Pandasで分析、Matplotlibで可視化し、  
Flaskダッシュボードとして提供します。

---

## 🎯 目的（Purpose）

- IT求人市場のトレンド分析
- スキル需要の可視化
- 給与分布の把握
- データドリブンな意思決定支援

---

## 🧠 システムアーキテクチャ

```

[ Scraping Layer ]
↓
[ Data Storage (SQL) ]
↓
[ Data Processing (ETL / Pandas) ]
↓
[ Visualization (Matplotlib / Seaborn) ]
↓
[ Web Dashboard (Flask) ]

````

---

## 🤖 自動化（ETL Pipeline）

本システムは以下の処理を自動化：

1. Extract：求人データ取得（スクレイピング）
2. Transform：データ整形・クレンジング
3. Load：SQLデータベース保存
4. Analysis：KPI自動算出
5. Visualization：グラフ生成
6. Delivery：Webダッシュボード反映

---

## ⚙️ 自動更新機能

- `/update` にアクセスすることで  
  **データ取得 → 分析 → 可視化 → 表示更新** を一括実行

---

## ⏱️ バッチ処理

```bash
# cron例
0 9 * * * python main.py
````

---

## 🚀 主な機能

### 🕷️ データ収集

* 求人情報スクレイピング
* 複数ページ対応

### 🗄️ データ管理

* SQL保存
* 再利用可能なデータ設計

### 📊 データ分析

* 求人数
* 平均給与
* スキル分析

### 📈 KPI分析

* 総求人数
* 平均給与
* 人気スキル

### 📉 可視化

* 求人数グラフ
* 給与分布
* スキルランキング

### 🌐 Webダッシュボード

* Flask UI
* キーワード検索
* リアルタイム表示

---

## 📂 ディレクトリ構成

```
job-market-analysis/
│
├── app.py                      # Flask Webアプリのエントリーポイント
├── main.py                     # データパイプライン一括実行スクリプト
├── config.py                  # 設定管理（DB・パスなど）
├── requirements.txt           # 依存ライブラリ一覧
├── README.md                  # プロジェクト説明書（重要）
├── .gitignore                 # Git除外設定
│
├── crawler/                   # データ収集モジュール
│   ├── scraper.py             # 単一ページのスクレイピング処理
│   ├── crawler.py             # 複数ページのクロール制御
│   └── __init__.py
│
├── data/                      # データベース・データ管理
│   ├── db.py                  # MySQL接続・保存処理
│   └── __init__.py
│
├── analysis/                  # データ分析・可視化
│   ├── analysis.py           # データ集計・統計処理
│   ├── visualize.py          # グラフ生成（Matplotlib）
│   ├── report.py             # Excelレポート生成
│   └── __init__.py
│
├── templates/                # フロントエンド（Flask）
│   └── index.html
│
├── static/                   # 画像・グラフ出力
│   ├── job_count.png
│   ├── salary.png
│   └── skills.png
│
├── output/                   # 出力データ（Excelレポート）
│   └── report.xlsx
│
└── logs/                     # ログ管理（追加）
    └── app.log
```

---

## ⚙️ 技術スタック（Tech Stack）

### 🧩 言語

* Python
* SQL

### 🌐 Web / Backend

* Flask
* Jinja2

### 📊 データ分析

* Pandas
* NumPy

### 📈 可視化

* Matplotlib
* Seaborn

### 🕷️ スクレイピング

* Requests
* BeautifulSoup
* 正規表現

### 🗄️ データベース

* MySQL
* SQLクエリ設計

### 🔄 自動化 / ETL

* ETLパイプライン設計
* バッチ処理（main.py）
* スケジューリング対応

### 🖥️ システム

* OSファイル操作
* Logging

### 📦 出力

* Excelレポート

### 🧪 開発

* Git / GitHub
* モジュール設計

### ☁️ 拡張（予定）

* REST API
* Docker
* クラウドデプロイ

---

## 🧠 アーキテクチャ設計（Architecture Highlights）

### 🧩 レイヤー分離

* Crawler / Data / Analysis / Web を分離

### 🔄 ETL設計

* データ処理をパイプライン化

### ⚙️ 自動化

* ワンクリック更新 + バッチ処理

### 📊 KPI設計

* ビジネス指標に基づく分析

### 🔗 分離設計

* 分析ロジックとUIの独立

### 🧱 モジュール化

* 保守性・再利用性向上

### 📈 拡張性

* API / クラウド / 分散処理対応

---

## 📽️ デモ（Demo）

### 🎬 システム動作イメージ

以下は実際のダッシュボード操作のデモです：

![demo](static/demo.gif)

---

### 🖼️ 補足スクリーンショット

![salary](static/salary.png)
![skills](static/skills.png)
---

### 💻 ローカル実行

```bash
git clone https://github.com/yourname/job-market-analysis.git
cd job-market-analysis

pip install -r requirements.txt
python app.py
```

アクセス：
[http://127.0.0.1:5000](http://127.0.0.1:5000)

---


## 💡 技術的なポイント

* ETLパイプライン設計
* データ分析 × Web統合
* KPIベース設計
* 自動化処理
* モジュール化設計

---

## 🔄 今後の改善

* REST API化
* 認証機能
* Docker対応
* AWS / GCPデプロイ
* リアルタイム更新

---

## 🎯 想定用途

* HR分析
* 転職市場分析
* データ分析ポートフォリオ

---


## 🧾 面接用一言

求人データをスクレイピングし、SQLで管理、
Pandasで分析、Matplotlibで可視化し、
Flaskでダッシュボード化した
ETL型データ分析システムを開発しました。

---
## 作者

snowxxyg

---
