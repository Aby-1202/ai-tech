import sqlite3
from models import db, Country
from app import create_app

def init_db():
    app = create_app()
    app.app_context().push()

    # データベース接続
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()

    # DDLスクリプトの読み込み
    with open('createdb.ddl', 'r') as f:
        ddl_script = f.read()

    # DDLスクリプトの実行
    cursor.executescript(ddl_script)
    conn.commit()
    conn.close()

    # 初期データの追加
    countries = [
        {"name": "国A", "area": 500000, "population": 30000000, "density": 60, "gdp": 500000000000},
        {"name": "国B", "area": 1000000, "population": 50000000, "density": 50, "gdp": 1000000000000},
        {"name": "国C", "area": 750000, "population": 20000000, "density": 26.7, "gdp": 250000000000},
        # 他の国データ
    ]
    for country in countries:
        new_country = Country(**country)
        db.session.add(new_country)
    db.session.commit()

if __name__ == '__main__':
    init_db()
