#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 并发下载器
import urllib.request
import gevent
from gevent import monkey

monkey.patch_all()

def downloader(img_name,img_url):
    req = urllib.request.urlopen(img_url)

    img_content = req.read()

    with open(img_name,'wb') as f:
        f.write(img_content)

def main():
    gevent.joinall([
        gevent.spawn(downloader,'1.jpg','https://rpic.douyucdn.cn/asrpic/190718/5822819_5289461_35169_2_2005.jpg?x-oss-process=image/format,webp')
        gevent.spawn(downloader,'2.jpg','https://rpic.douyucdn.cn/live-cover/appCovers/2019/06/24/5515841_20190624174031_small.jpg?x-oss-process=image/format,webp')
    ])

if __name__ == '__main__':
    main()