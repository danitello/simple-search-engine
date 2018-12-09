from searchEngine import SearchEngine
from flask import Flask, render_template, request

app = Flask(__name__)

# Maximum crawling depth as determined by user
maxDepth = 2

# Search term from user
searchTerm = "to"
#res = engine.search(searchTerm.lower())
#print(res)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method =='POST':
        startingURL = request.form['urlInput']
        engine = SearchEngine()
        numPagesIndexed, numWordsIndexed = engine.indexFrom(startingURL, maxDepth)
        return render_template("index.html", numPagesIndexed=numPagesIndexed, 
            numWordsIndexed=numWordsIndexed)
    return render_template("index.html")

@app.route("/search/")
def search():
    return render_template("search.html")


if __name__ == "__main__":
    app.run(debug=True)