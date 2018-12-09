import requests
import csv
from bs4 import BeautifulSoup

class SearchEngine:

    def __init__(self):
        self.loadFile()

    def loadFile(self):
        ''' Loads current site information into class instance '''
        
        # Dict of sites read from file
        self.sitesDict = {}
        try:
            with open('sites.csv', newline='') as f:
                reader = csv.reader(f)
                # File is stored as url | title | all words..
                for line in reader:
                    self.sitesDict[line[0]] = line[1:]
        except:
            pass
    
    def search(self, term):
        ''' Searches index for matching term '''
        
        term = term.lower()
        result = {}
        for url, values in self.sitesDict.items():
           
            termCount = 0
            for word in values:
                if term == word.lower():
                    termCount += 1
            if termCount > 0:
                result[url] = termCount
        return result


    def indexFrom(self, url, maxDepth):
        ''' Wrapper function to initiate crawl and write final data '''

        # List of sites indexed this time 
        # to prevent infinitely going back over the same ones
        self.indexedSites = set()

        self.getLinksFromURL(url, url, 1, maxDepth)

        with open('sites.csv', 'w', newline='') as f:
                writer = csv.writer(f)

                # File is stored as url | title | all words..
                for key, value in self.sitesDict.items():
                    writeList = [key]
                    writeList += value
                    writer.writerow(writeList)


    def getLinksFromURL(self, url, fromURL, currentDepth, maxDepth):
        ''' Recursively retrieves links from given url '''

        # Download from URL
        try:
            r = requests.get(url)
        except requests.exceptions.RequestException as e:
            print(e)
            return
        
        # Parse
        soup = BeautifulSoup(r.text, "html.parser")
        for elem in soup(["script", "style"]):
            elem.extract()
        words = soup.get_text().split()

        # Write new site information into dict
        if not soup.title == None and not soup.title.string.startswith("404"):
            self.sitesDict[url] = [soup.title.string.strip()] + words
            self.indexedSites.add(url)
    
        # TODO: Add words to file as wellwell

        # Extract child links
        if currentDepth < maxDepth:
            for link in soup.findAll("a"):
                newURL = link.get("href")
                if newURL is not None:
                    newURL = newURL.strip("/")
                    print(url, newURL)
                    if not newURL.startswith("http"):
                        newURL = fromURL + "/" + newURL
                    if newURL not in self.indexedSites:
                        self.getLinksFromURL(newURL, url, currentDepth+1, maxDepth)
    