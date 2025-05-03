import feedparser
# TODO: Add a way to save individual entries from a feed to revisit later
urls = ['https://thefp.com/feed', 'https://www.wired.com/feed/rss', 'https://standardebooks.org/feeds/rss/new-releases'] 

def getfeeds(feedurl):
    
    d = feedparser.parse(feedurl)
    entrycount = 0
    
    print('--------------------')
    print(d['feed']['title'])
    print(d['feed']['date'])
    print("")
    
    for entry in d['entries']:
        print(str(entrycount) + ") " + entry['title'])
        print(entry['published'])
        print(entry['link'])
        print(entry['summary'])
        print("---")
        entrycount += 1
    
    print(d['entries'][0].keys())

def main():
    for url in urls:
        getfeeds(url)

if __name__ == '__main__':
    main()
