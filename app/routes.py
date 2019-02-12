from flask import render_template
import Autocompleter
from app import app
from werkzeug.contrib.cache import SimpleCache
cache = SimpleCache()

@app.route('/')
@app.route('/index')
def index():
    rv = cache.get('my-item')
    if rv is None:
        print("RV WAS NULL")
        with open('small_words.txt') as word_file:
            keys = list(word_file.read().split())
        print("Training Model")
        t=Autocompleter.Trie()
        t.formTrie(keys)
        t.optimize()
        print("MODEL TRAINED")
        cache.set('my-item', t, timeout=5 * 60)
    return render_template('index.html')

@app.route('/result/<query>')
def getResult(query):
    t = cache.get('my-item')
    t.clearSuggestions()
    t.myPrinter(query)
    string=""
    for i in range(0,len(t.ans)):
        string=string+t.ans[i]+"\n"
    return string
    