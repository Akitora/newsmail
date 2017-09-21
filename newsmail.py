#! /usr/bin/python3
import AT_smtp,AT_feed

subject = u"まとめニュース"
text1 = AT_feed.feed('http://blog.livedoor.jp/news23vip/index.rdf')
text2 = AT_feed.feed('http://blog.livedoor.jp/dqnplus/index.rdf')
text3 = AT_feed.feed('http://alfalfalfa.com/index.rdf')
text4 = AT_feed.feed('http://www.vsnp.net/index.rdf')
text5 = AT_feed.feed('http://blog.livedoor.jp/nwknews/index.rdf')

text = text1 + text2 + text3 + text4 + text5
to_address = "casiskir@gmail.com"
AT_smtp.smtp(subject,text,to_address)

