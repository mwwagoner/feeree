import feedparser
# TODO: Add a way to save individual entries from a feed to revisit later
# TODO: Check for a valid url before trying to get a feed

def getfeed(feedurl):
    
    d = feedparser.parse(feedurl)
    entrycount = 0
    items = []
    
    items.append(('--------------------')
    items.append((d['feed']['title'])
    items.append((d['feed']['date'])
    items.append(("")
    
    for entry in d['entries']:
        items.append(str(entrycount) + ") " + entry['title'])
        items.append(entry['published'])
        items.append(entry['link'])
        items.append(entry['summary'])
        entrycount += 1

    return items

def main():
    urls = ['https://thefp.com/feed', 
            'https://www.wired.com/feed/rss', 
            'https://standardebooks.org/feeds/rss/new-releases'] 
    feeds = []

    for url in urls:
        feeds.append(getfeed(url))

    for feed in feeds:
        for feeditem in feed:
            print(feeditem)

if __name__ == '__main__':
    main()
