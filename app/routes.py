from flask import render_template
import Autocompleter
from app import app
import psutil
import os
import gc
import pdb
import sys

list2=[12,312,3,123,123,123,123,1]
print(psutil.virtual_memory())
del(list2)
print(psutil.virtual_memory())

#process = psutil.Process(os.getpid())
#mem0 = process.memory_info().rss
#print('Memory Usage After Action',mem0/(1024**2),'MB')
with open('small_words.txt') as word_file:
    keys = list(word_file.read().split())
print("Training Model")
t=Autocompleter.Trie()
t.formTrie(keys)
t.checkSize()
print("NODESS B4 Optimization",t.count)
t.optimize()
print("MODEL Optimized")
t.checkSize()
print("NODESS After Optimization",t.count)
print(psutil.virtual_memory())
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/result/<query>')
def getResult(query):
    t.clearSuggestions()
    t.myPrinter(query)
    string=""
    for i in range(0,len(t.ans)):
        string=string+t.ans[i]+"\n"
    #gc.collect()
    #process = psutil.Process(os.getpid())
    #mem0 = process.memory_info().rss
    #print('Memory Usage After Action',mem0/(1024**2),'MB')
    return string

