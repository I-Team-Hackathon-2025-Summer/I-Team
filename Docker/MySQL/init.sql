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
    /*AUTO_INCREMENT：自動的に一意の値を割り当ててくれる*/
    area_id INT AUTO_INCREMENT PRIMARY KEY,
    /*channel_id INT NOT NULL,*/
    area_name VARCHAR(255) UNIQUE NOT NULL
    /*channel_idがopen_channelsテーブルの主キーであるchannel_idカラムを参照するように指定
    FOREIGN KEY (channel_id) REFERENCES open_channels(channel_id)*/
);

CREATE TABLE open_channels (
    channel_id INT AUTO_INCREMENT PRIMARY KEY,
    area_id INT NOT NULL,
    prefecture VARCHAR(255) NOT NULL,
    /*親テーブル(area)でレコードが削除されたら、子テーブル(open_channels)のレコードも削除されるように設定*/
    FOREIGN KEY (area_id) REFERENCES areas(area_id) ON DELETE CASCADE
);

CREATE TABLE open_messages (
    message_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id VARCHAR(255) NOT NULL,
    channel_id INT NOT NULL,
    message TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    /*親テーブル(users)でレコードが削除されたら、子テーブル(open_message)のレコードも削除されるように設定*/
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    /*親テーブル(open_channels)でレコードが削除されたら、子テーブル(open_message)のレコードも削除されるように設定*/
    FOREIGN KEY (channel_id) REFERENCES open_channels(channel_id) ON DELETE CASCADE
);

INSERT INTO users(user_id, user_name, email, password) VALUES('970af84c-dd40-47ff-af23-282b72b7cca8','テスト','test@gmail.com','testtest123');

INSERT INTO areas(area_id,area_name) 
VALUES
(1, '北海道/東北'),
(2, '関東'),
(3, '中部'),
(4, '近畿'),
(5, '中国'),
(6, '四国'),
(7, '九州/沖縄');

INSERT INTO open_channels(channel_id, area_id, prefecture) 
VALUES
(1, 1, '北海道'),
(2, 1, '青森'),
(3, 1, '岩手'),
(4, 1, '宮城'),
(5, 1, '秋田'),
(6, 1, '山形'),
(7, 1, '福島'),
(8, 2, '茨城'),
(9, 2, '栃木'),
(10, 2, '群馬'),
(11, 2, '埼玉'),
(12, 2, '千葉'),
(13, 2, '東京'),
(14, 2, '神奈川'),
(15, 3, '新潟'),
(16, 3, '富山'),
(17, 3, '石川'),
(18, 3, '福井'),
(19, 3, '山梨'),
(20, 3, '長野'),
(21, 3, '岐阜'),
(22, 3, '静岡'),
(23, 3, '愛知'),
(24, 4, '京都'),
(25, 4, '大阪'),
(26, 4, '滋賀'),
(27, 4, '兵庫'),
(28, 4, '奈良'),
(29, 4, '和歌山'),
(30, 4, '三重'),
(31, 5, '鳥取'),
(32, 5, '島根'),
(33, 5, '岡山'),
(34, 5, '広島'),
(35, 5, '山口'),
(36, 6, '愛媛'),
(37, 6, '高知'),
(38, 6, '徳島'),
(39, 6, '香川'),
(40, 7, '福岡'),
(41, 7, '佐賀'),
(42, 7, '長崎'),
(43, 7, '熊本'),
(44, 7, '大分'),
(45, 7, '宮崎'),
(46, 7, '鹿児島'),
(47, 7, '沖縄');
