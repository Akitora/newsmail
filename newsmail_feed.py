# -*- coding: utf-8 -*-

import feedparser
feedparser.PREFERRED_XML_PARSERS.remove('drv_libxml2')

import os.path
def feed(rssurl): 
    d = feedparser.parse(rssurl)

    strings = [d.feed.title + "\n"]
    for entry in d['entries']:
        title = entry.title
        link = entry.link
        strings.append(title)
        strings.append(link)
   
    if os.path.exists(rssurl.replace("/","_") + ".dat"):
        f2 = open(rssurl.replace("/","_") + ".dat","r+",encoding = "UTF-8")
    else:
        f2 = open(rssurl.replace("/","_") + ".dat","w",encoding = "UTF-8")
        f2.close()
        f2 = open(rssurl.replace("/","_") + ".dat","r+",encoding = "UTF-8")
 
    strings2 = [d.feed.title + "\n"]
    main_subject = ""
    for row in f2:
        main_subject = row
    for entry in d['entries']:
        title = entry.title
        link = entry.link
        if (title == main_subject):
            break
        strings2.append(title)
        strings2.append(link)

    ret = "\n".join(strings2)
    f = open(rssurl.replace("/","_") + ".dat","w",encoding = "UTF-8")

    f.write(strings[1])

    f.close()
    f2.close()
    #print(ret)
    return ret + "\n\n"
if __name__ == '__main__':
    rssurl = 'http://www.dlsite.com/home/rss/=/channel/news_maniax'
    feed(rssurl)
