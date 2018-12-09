from searchEngine import SearchEngine

# Maximum crawling depth as determined by user
maxDepth = 2

# URL to index from user
startingURL = "http://www.iohk.io"

# Search term from user
searchTerm = "to"

# TODO: make sure to put the creation of the engine inside the button click
engine = SearchEngine()
#engine.indexFrom(startingURL, maxDepth)

res = engine.search(searchTerm.lower())
print(res)