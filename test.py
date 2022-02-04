import urllib.request as urllib2
from urllib.parse  import urljoin
from bs4 import *
import codecs


def crawl(pages, depth=None):
    indexed_url = [] # a list for the main and sub-HTML websites in the main website
    for i in range(depth):
        for page in pages:
            if page not in indexed_url:
                indexed_url.append(page)
                try:
                    c = urllib2.urlopen(page)
                except:
                    print( "Could not open %s" % page)
                    continue
                soup = BeautifulSoup(c.read())
                links = soup('a') #finding all the sub_links
                for link in links:
                    if 'href' in dict(link.attrs):
                        url = urljoin(page, link['href'])
                        if url.find("'") != -1:
                                continue
                        url = url.split('#')[0] 
                        if url[0:4] == 'http':
                                indexed_url.append(url)
        pages = indexed_url
    return indexed_url


#pagelist=['https://licejus.edupage.org/timetable/']
#urls = crawl(pagelist, depth=1)
#print( urls )


page = 'https://licejus.edupage.org/timetable/'
with urllib2.urlopen(page) as f:
    html = f.read().decode('utf-8')

# print(html)
# soup = BeautifulSoup(html,features="html.parser")
# svgs = soup('svg')

# for svg in svgs:
#     print(svg)
#     break;

file = codecs.open("html.html", "w", "utf-8")
file.write(html)
file.close()
