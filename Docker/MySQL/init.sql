
DROP DATABASE tabitalk;
DROP USER 'Iteam';

CREATE USER 'Iteam' IDENTIFIED BY 'Iteam';
CREATE DATABASE tabitalk;
USE tabitalk
GRANT ALL PRIVILEGES ON tabitalk.* TO 'Iteam';

CREATE TABLE users (
    user_id VARCHAR(255) PRIMARY KEY,
    user_name VARCHAR(255) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE areas(
    --AUTO_INCREMENT：自動的に一意の値を割り当ててくれる
    area_id INT AUTO_INCREMENT PRIMARY KEY,
    channel_id INT NOT NULL,
    area_name VARCHAR(255) UNIQUE NOT NULL,
    --channel_idがopen_channelsテーブルの主キーであるchannel_idカラムを参照するように指定
    FOREIGN KEY (channel_id) REFERENCES open_channels(channel_id)
)

CREATE TABLE open_channels (
    channel_id INT AUTO_INCREMENT PRIMARY KEY,
    area_id INT AUTO_INCREMENT PRIMARY KEY,
    prefecture VARCHAR(255) NOT NULL,
    --親テーブル(area)でレコードが削除されたら、子テーブル(open_channels)のレコードも削除されるように設定
    FOREIGN KEY (area_id) REFERENCES areas(area_id) ON DELETE CASCADE
);

CREATE TABLE open_messages (
    message_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id VARCHAR(255) NOT NULL,
    message TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    --親テーブル(users)でレコードが削除されたら、子テーブル(open_message)のレコードも削除されるように設定
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

INSERT INTO users(user_id, user_name, email, password) VALUES('970af84c-dd40-47ff-af23-282b72b7cca8','テスト','test@gmail.com','testtest123');

INSERT INTO areas(area_id,channel_id, area_name) 
VALUES
(1, 1, '北海道/東北'),
(2, 2, '関東'),
(3, 3, '中部'),
(4, 4, '近畿'),
(5, 5, '中国'),
(6, 6, '四国'),
(7, 7, '九州/沖縄');

INSERT INTO open_channels(channel_id, area_id, prefecture) 
VALUES
(1, 1, '北海道',)
(1, 2, '青森'),
(1, 3, '岩手'),
(1, 4, '宮城'),
(1, 5, '秋田'),
(1, 6, '山形'),
(1, 7, '福島'),
(2, 1, '茨城'),
(2, 2, '栃木'),
(2, 3, '群馬'),
(2, 4, '埼玉'),
(2, 5, '千葉'),
(2, 6, '東京'),
(2, 7, '神奈川'),
(3, 1, '新潟'),
(3, 2, '富山'),
(3, 3, '石川'),
(3, 4, '福井'),
(3, 5, '山梨'),
(3, 6, '長野'),
(3, 7, '岐阜'),
(3, 8, '静岡'),
(3, 9, '愛知'),
(4, 1, '京都'),
(4, 2, '大阪'),
(4, 3, '滋賀'),
(4, 4, '兵庫'),
(4, 5, '奈良'),
(4, 6, '和歌山'),
(4, 7, '三重'),
(5, 1, '鳥取'),
(5, 2, '島根'),
(5, 3, '岡山'),
(5, 4, '広島'),
(5, 5, '山口'),
(6, 1, '愛媛'),
(6, 2, '高知'),
(6, 3, '徳島'),
(6, 4, '香川'),
(7, 1, '福岡'),
(7, 2, '佐賀'),
(7, 3, '長崎'),
(7, 4, '熊本'),
(7, 5, '大分'),
(7, 6, '宮崎'),
(7, 7, '鹿児島'),
(7, 8, '沖縄');
