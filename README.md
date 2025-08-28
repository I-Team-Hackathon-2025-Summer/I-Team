**ブラウザで確認**
```
http://localhost:55000
```


### ディレクトリ構成
```
.
├── ChatApp              # サンプルアプリ用ディレクトリ
│   ├── models
│   ├── static          # 静的ファイル用ディレクトリ
│   ├── templates       # Template(HTML)用ディレクトリ
│   ├── views
│   └── app.py
├── Docker
│   ├── Flask
│   │   └── Dockerfile # Flask(Python)用Dockerファイル
│   └── MySQL
│       ├── Dockerfile  # MySQL用Dockerファイル
│       ├── init.sql    # MySQL初期設定ファイル
│       └── my.cnf
├── .env.example         # 環境変数ファイル（.env）を作成する為のサンプルファイル
├── docker-compose.yml   # Docker-composeファイル
└── requirements.txt     # 使用モジュール記述ファイル
```
