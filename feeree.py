import feedparser
# TODO: Add a way to save individual entries from a feed to revisit later
# TODO: Check for a valid url before trying to get a feed

def getfeed(feedurl):
    
    d = feedparser.parse(feedurl)
    entrycount = 0
    items = []
    
    print('--------------------')
    print(d['feed']['title'])
    print(d['feed']['date'])
    print("")
    
    for entry in d['entries']:
        #print(str(entrycount) + ") " + entry['title'])
        items.append(str(entrycount) + ") " + entry['title'])
        #print(entry['published'])
        items.append(entry['published'])
        #print(entry['link'])
        items.append(entry['link'])
        #print(entry['summary'])
        items.append(entry['summary'])
        #print("---")
        entrycount += 1

    #print(items)
    return items
    
    #print(d['entries'][0].keys())

def main():
    urls = ['https://thefp.com/feed', 
            'https://www.wired.com/feed/rss', 
            'https://standardebooks.org/feeds/rss/new-releases'] 
    feeds = []

    for url in urls:
        #feeds += getfeed(url)
        feeds.append(getfeed(url))

    for feed in feeds:
        print(feed)

if __name__ == '__main__':
    main()
