#! /usr/bin/python3
import newsmail_smtp,newsmail_feed

subject = u"まとめニュース"
text1 = newsmail_feed.feed('http://www.dlsite.com/home/rss/=/channel/news_maniax')
text2 = newsmail_feed.feed('http://blog.livedoor.jp/dqnplus/index.rdf')
text3 = newsmail_feed.feed('http://alfalfalfa.com/index.rdf')
text4 = newsmail_feed.feed('http://www.vsnp.net/index.rdf')
text5 = newsmail_feed.feed('http://blog.livedoor.jp/nwknews/index.rdf')

text = text1 + text2 + text3 + text4 + text5
to_address = "xxx@xxx.com"
AT_smtp.smtp(subject,text,to_address)

