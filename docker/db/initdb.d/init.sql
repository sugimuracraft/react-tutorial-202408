/* 開発用DBの作成 */

-- ユーザーの作成
CREATE USER dbuser WITH PASSWORD 'dbpassword';

-- データベースの作成
CREATE DATABASE dbname OWNER dbuser;

-- ユーザーに対するデータベースの全権限付与
GRANT ALL PRIVILEGES ON DATABASE dbname TO dbuser;


/* テスト用DBの作成 */

-- データベースの作成
CREATE DATABASE dbname_test OWNER dbuser;

-- ユーザーに対するデータベースの全権限付与
GRANT ALL PRIVILEGES ON DATABASE dbname_test TO dbuser;
