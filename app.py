from searchEngine import SearchEngine
from flask import Flask, render_template, request

app = Flask(__name__)

# Maximum crawling depth as determined by user
MAX_DEPTH = 1

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method =='POST':
        startingURL = request.form['urlInput']
        engine = SearchEngine()
        numPagesIndexed, numWordsIndexed = engine.indexFrom(startingURL, MAX_DEPTH)
        return render_template("index.html", numPagesIndexed=numPagesIndexed, 
            numWordsIndexed=numWordsIndexed)
    return render_template("index.html")

@app.route("/search/", methods=['GET', 'POST'])
def search():
    if request.method =='POST':
        searchTerm = request.form['searchTermInput']
        engine = SearchEngine()
        resultList = engine.search(searchTerm.lower())
        return render_template("search.html", resultList=resultList, listSize=len(resultList))
    return render_template("search.html")


if __name__ == "__main__":
    app.run(debug=True)