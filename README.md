# 📈 Market Data Automation v2

[English] | [日本語]

---

## 🇺🇸 English Version

### 🚀 Project Evolution
This project automates financial data extraction and reporting. Originally a UI-based automation, it has been **refactored** into a professional Data Engineering tool.
- **Modular Architecture:** Separated into ETL (Extract, Transform, Load) functions.
- **Security:** Implemented environment variables (`.env`) for credential protection.
- **Robustness:** Replaced fragile UI clicks (`PyAutoGUI`) with reliable `SMTP` protocols.

### 🛠️ Tech Stack
- **Python 3.10+** (Pandas, YFinance, SMTPLib, Dotenv)

### 📋 Setup
1. `git clone https://github.com/artloock/MarketDataAutomation.git`
2. `python -m venv venv`
3. `pip install -r requirements.txt`
4. Configure `.env` file and run `python src/main.py`

---

## 🇯🇵 日本語版 (Japanese Version)

### 🚀 プロジェクトの概要
このプロジェクトは、金融データの抽出、分析、およびレポート送信を自動化するツールです。初期のGUIベースの自動化から、プロフェッショナルな**データエンジニアリング**ツールへとリファクタリングされました。

### ✨ 主な改善点
- **モジュール化:** ETL（抽出・変換・格納）設計パターンを採用し、コードの再利用性を向上。
- **セキュリティ:** `.env`ファイルを使用し、機密情報（メールパスワード等）を保護。
- **安定性:** `PyAutoGUI`による画面操作を廃止し、`SMTP`プロトコルによる直接送信を実装。
- **データ構造:** 日本のビジネス環境でも標準的な `YYYY-MM-DD` 形式を採用。

### 🛠️ 使用技術
- **Python 3.10+**
- **Pandas:** データ分析
- **YFinance:** 市場データ取得
- **SMTPLib:** メール自動送信

### 📋 セットアップ手順
1. リポジトリをクローン: `git clone ...`
2. 仮想環境の作成と有効化: `python -m venv venv`
3. 依存関係のインストール: `pip install -r requirements.txt`
4. `.env`ファイルを修正し、`python src/main.py` を実行してください。