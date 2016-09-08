CREATE DATABASE qq_scrapy DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE qq_scrapy;
CREATE TABLE `qq_article` (
  `linkmd5id`  varchar(100) COMMENT '链接MD5',
  `title` text COMMENT '标题',
  `link` text  COMMENT 'url链接',
  `content` text COMMENT '文章正文',
  `field` text COMMENT '文章类别',
  `date_str` text COMMENT '文章日期'
  PRIMARY KEY (`linkmd5id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;