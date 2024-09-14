# 概要

# ローカル開発環境構築

## 環境変数ファイル作成

```sh
cp env.template .env
```

## 環境変数ファイル調整

### シークレットキー

環境固有のシークレットキーを生成して、値を置き換える。

```sh
openssl rand -hex 32
```

.env の `BACKEND_SETTINGS_SECRET_KEY` の値を置き換える。

## コンテナ起動

```sh
docker compose up -d
```

# DBマイグレーション

## 追加分の作成

既存スキーマを変更するための、新しいマイグレーションファイルを作成する。

```bash
rev_id="0001_study_record"
rev_label="create_tables"
alembic revision --autogenerate --rev-id ${rev_id} -m ${rev_label}
```

`alembic/versions` 以下に、`${rev_id}_${rev_label}.py` が生成される

## リビジョンを進める

```bash
alembic upgrade head
alembic upgrade 0001
```

## リビジョンを戻す

```bash
alembic downgrade base
alembic downgrade 0001
```
