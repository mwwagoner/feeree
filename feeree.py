import feedparser, html
# TODO: Add a way to save individual entries from a feed to revisit later
# TODO: Check for a valid url before trying to get a feed

def getfeed(feedurl):
    
    d = feedparser.parse(feedurl)
    entrycount = 0
    items = []
    
    items.append('--------------------')
    items.append(d['feed']['title'])
    items.append(d['feed']['date'])
    items.append("")
    
    for entry in d['entries']:
        # The summary field for some feeds seem to include HTML character entities so they need to be converted
        summarytext = html.unescape(entry['summary'])

        items.append(str(entrycount) + ") " + entry['title'])
        items.append(entry['published'])
        items.append(entry['link'])
        items.append(f"{summarytext}\n")
        entrycount += 1

    return items

def main():
    urls = ['https://thefp.com/feed', 
            'https://www.wired.com/feed/rss', 
            'https://standardebooks.org/feeds/rss/new-releases',
            'https://www.space.com/feeds/all'] 
    feeds = []

    for url in urls:
        feeds.append(getfeed(url))

    with open('feeds.txt', 'w', encoding="utf-8") as outputfile:
        for feed in feeds:
            for feeditem in feed:
                outputfile.write(f"{feeditem}\n")

if __name__ == '__main__':
    main()
