# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
template = {
    "name": "Galileo",
    "type": "local",
    "path": "../Galileo"
}
enable_jsdelivr = {
    "enabled": True,
    "repo": "sanmingmrx/sanmingmrx.github.io@master"
}

# 站点设置
site_name = "只听一种声音，中国好声音。"
#site_logo = "${static_prefix}/static/logo.png"
site_logo = "./static/logo.png"
site_build_date = "2019-12-18T16:51+08:00"
author = "鸡毛土人"
email = "songdiancan@gmail.com"
author_homepage = "https://www.imalan.cn"
description = "凡我所爱者，必如热血中的病毒，在人群中感染流布。--by黄章晋"
key_words = ['Maverick', '熊猫小A', 'Galileo', 'blog']
language = 'zh-CN'
external_links = [
    {
        "name": "三無計劃",
        "url": "https://www.imalan.cn",
        "brief": "熊猫小A的主页。"
    }
]
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "Twitter",
        "url": "https://twitter.com/NanjingMrLi",
        "icon": "gi gi-twitter"
    },
    {
        "name": "GitHub",
        "url": "https://github.com/SanmingMrX",
        "icon": "gi gi-github"
    },
    {
        "name": "Weibo",
        "url": "https://weibo.com/7420741870/",
        "icon": "gi gi-weibo"
    }
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''
