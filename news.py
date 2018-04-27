import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import feedparser


def fetch_news(newsurls):

	for key,url in newsurls.items():
		try:
			news_url=url
			Client=urlopen(news_url)
			xml_page=Client.read()
			Client.close()

			soup_page=soup(xml_page,"xml")
			news_list=soup_page.findAll("item")
			# Print news title, url and publish date
			for news in news_list:
			  print(news.title.text)
			  print(news.link.text)
			  print(news.pubDate.text)
			  print("-"*60)

		except:
			print('could not fetch url:', url)



worldnewsurls = {
    'bbcnews'       : 'http://feeds.bbci.co.uk/news/world/rss.xml',
    'cnn'           : 'http://rss.cnn.com/rss/edition_world.rss',
    'guardian'      : 'https://www.theguardian.com/world/rss',
    'Reuters'       : 'http://feeds.reuters.com/Reuters/worldNews',
    'washingtonpost': 'http://feeds.washingtonpost.com/rss/world',
    'aljajeera'     : 'https://www.aljazeera.com/xml/rss/all.xml',
    'googlenews'    : 'https://news.google.com/news/rss/',
    'yahoonews'     : 'http://news.yahoo.com/rss/',
    'yahooworld'    : 'https://www.yahoo.com/news/rss/world',    
    'buzzfeed'      : 'https://www.buzzfeed.com/world.xml'
}

technewsurls = {
	'techmeme':'https://www.techmeme.com/feed.xml',
	'TechCrunch':'http://feeds.feedburner.com/TechCrunch',
	'arstechnica':'http://feeds.arstechnica.com/arstechnica/technology-lab',
	'reddittech':'https://www.reddit.com/r/technology/.rss',
	'computerworld':'https://www.computerworld.com/index.rss',
	'nytimestech':'http://rss.nytimes.com/services/xml/rss/nyt/Technology.xml',
	'cnettech':'https://www.cnet.com/rss/news/',
	'washingtonposttech':'http://feeds.washingtonpost.com/rss/business/technology',
	'huffingtonposttech':'https://www.huffingtonpost.com/section/technology/feed',
	'alleyinsider':'http://feeds.feedburner.com/typepad/alleyinsider/silicon_alley_insider',
	'reuterstech':'http://feeds.reuters.com/reuters/technologyNews',
	'mirrortech':'https://www.mirror.co.uk/tech/?service=rss',
	'howtogeektech':'https://feeds.howtogeek.com/HowToGeek'

}

fashionnewsurls = {
	'elle'            : 'https://www.elle.com/rss/all.xml/',
	'vogue'           : 'https://www.vogue.com/feed',
	'nytimesfasion'   : 'https://www.nytimes.com/svc/collections/v1/publish/http://www.nytimes.com/section/fashion/rss.xml',
	'whowhatwear'     : 'http://www.whowhatwear.com/rss',
	'popsugar'        : 'https://www.popsugar.com/fashion/feed',
	'fashionmagazine' : 'https://fashionmagazine.com/feed/',
	'lookbook'        : 'http://lookbook.nu/rss',
	'refinery29'      : 'https://www.refinery29.com/fashion/rss.xml'


}

buisnessnewsurls = {
	'cnnmoney' : 'http://rss.cnn.com/rss/money_topstories.rss', 
	'cnbc' : 'http://www.cnbc.com/id/19746125/device/rss/rss.xml', 
	'yahoofinance' : 'https://finance.yahoo.com/news/rssindex', 
	'investing' : 'https://www.investing.com/rss/news.rss', 
	'investing' : 'https://prod-qt-images.s3.amazonaws.com/production/c/feed.xml', 
	'chicagobusiness' : 'http://www.chicagobusiness.com/section/news?template=rss&mime=xml', 
	'businessinsider' : 'http://markets.businessinsider.com/rss/news'
}
fetch_news(buisnessnewsurls)