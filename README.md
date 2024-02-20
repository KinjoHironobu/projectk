## 各種コマンド

### コンテナ起動
``` bash
docker compose up
```

### マイグレーションの作成
``` bash
docker compose exec web python manage.py makemigrations
```

### マイグレーション実行
``` bash
docker compose exec web python manage.py migrate
```

### 管理者ユーザの作成
``` bash
docker compose exec web python manage.py createsuperuser
```

### Docker掃除用
``` bash
docker system prune
docker volume prune
docker image prune -a
docker builder prune
```