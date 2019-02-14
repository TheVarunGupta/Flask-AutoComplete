from flask import render_template
import Autocompleter
from app import app
import psutil
import os
import gc
import pdb
import sys

def list_memory_used():
    count=0
    for obj in gc.get_objects():   
        if isinstance(obj, list):
            count+=sys.getsizeof(list)
    return count
        
def print_memory_used():
    process = psutil.Process(os.getpid())
    mem0 = process.memory_info().rss
    size = {}
    for obj in gc.get_objects():
        size.setdefault(type(obj), 0)
        size[type(obj)] = size[type(obj)] + sys.getsizeof(obj)
    print("Memory of TrieNode: {}".format(size))
    print('Memory Usage',mem0)

with open('words_alpha.txt') as word_file:
    keys = list(word_file.read().split())
print("Training Model")
t=Autocompleter.Trie()
t.formTrie(keys)
t.checkSize()

print("NODESS B4 Optimization",t.count)
#print(psutil.virtual_memory())
print_memory_used()
# print("11111111111111111111111111")
# t.printTrie()
# print("-------------------------")
t.optimize()
# gc.collect()
# t.printTrie()
print list_memory_used()

print("MODEL Optimized")

print_memory_used()
t.checkSize()
print("NODESS After Optimization",t.count)
#print(psutil.virtual_memory())
print list_memory_used()
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/result/<query>')
def getResult(query):
    t.printTrie()
    t.clearSuggestions()
    t.myPrinter(query)
    string=""
    for i in range(0,len(t.ans)):
        string=string+t.ans[i]+"\n"
    return string

