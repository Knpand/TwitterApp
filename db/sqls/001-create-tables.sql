create table dictionary
(id int not null auto_increment primary key, sentence varchar(140) not null unique)DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

INSERT INTO dictionary (sentence) VALUES ("大好きだよ！！きゅうーん！！");