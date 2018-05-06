#!/usr/bin/env python
# -*- coding: utf-8 -*-
import feedparser
import codecs
import os

rss_url = "http://www.tagesschau.de/xml/rss2"

feed = feedparser.parse(rss_url)

with codecs.open("RAM/RSS.txt", "w", "utf-8") as out:
    out.write(feed['entries'][0]['title'].replace("  ", "") + "\n")
    out.write(feed['entries'][1]['title'].replace("  ", "") + "\n")
    out.write(feed['entries'][2]['title'].replace("  ", "") + "\n")
    os.system("touch RAM/refresh")
    out.close()
