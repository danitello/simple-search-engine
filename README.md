# Simple search engine

User constructs an index and searches using simple interface to display sites based on how many times a search query is found.

## Dependencies
Tested in python3
* flask
* beautifulSoup4
* requests

## Running
Download files
```
git clone https://github.com/danitello/simple-search-engine.git
```

From within /simple-search-engine/ run
```
python3 app.py
```

Open browser to
```
localhost:5000
```

### Indexing
On the "Index" tab, enter urls (including "http") into the search bar to index them. This saves to a local "sites.csv" file in the same folder.

**Note:** Currently the "MAX_DEPTH" of link crawling is set to 1 (just the input page). This must be changed directly in the code to a desired value. It can be found at the top of app.py.

### Searching
On the "Search" tab, enter a single word into the search bar to search for that word from your index. This displays a list of links to relevant sites ranked by the number of occurances of the search query.

## Improvements
## Possible future additions
* Implement rel="next" for paginated content
* Handle possible exceptions individually (ConnectionError, HTTPError, Timeout, TooManyRedirects, etc.)
* Optimize read/write of data and move to cloud architecture for deployment
* Dynamically display search results
* Formatting urls
* Filter out certain characters/terms from index
* Corner case checking/handling and bug fixes