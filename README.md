以下のコマンドで開始
``` bash
# データディレクトリの作成
mkdir my_dbdata

# プロジェクトの作成
# docker compose run web django-admin startproject projectk .

# コンテナ起動
docker compose up

# マイグレーションの作成
docker compose exec web python manage.py makemigrations

# マイグレーション実行
docker compose exec web python manage.py migrate

# 管理者ユーザの作成
docker compose exec web python manage.py createsuperuser

```