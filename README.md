> ## 简介

利用scrapy对腾讯网的各个主题的新闻进行爬取，并存于数据库，再以web的方式进行展示和检索。

> ### 目录结构

* --netshadow 爬虫程序

* --netshadow_web web操作界面


> ### 发布

> 首先安装必须的模块

* 爬虫程序发布

1. 在crontab中添加一行：

```

10 * * * * cd path/to/netshadow && path/to/scrapy crawl netshadow --nolog

```

2. 初始化数据库

修改script下的db.ini数据库连接配置，运行database_operate.sh 根据提示初始化数据库。


* web程序发布

1. 