import time
import os
import resource
import sys
import gc
import psutil
from memory_profiler import profile

def print_memory_used():
    process = psutil.Process(os.getpid())
    mem0 = process.memory_info().rss
    size = 0
    for obj in gc.get_objects():
        if isinstance(obj, list):
            for x in obj:
                print (x)
    # print (len(gc.get_objects()))
    print("Memory of TrieNode: {}",(size))
    print('Memory Usage',mem0)

class TrieNode():
    def __init__(self):
        self.children={}
        
class Trie():
    def __init__(self):
        self.root=TrieNode()
        self.word_list=[]
        self.count=0
        self.ans=[]
        

    def formTrie(self,keys):
        for key in keys:
            self.insert(key)

    def insert(self, key):
        node=self.root

        for a in list(key):
            if not node.children.get(a):
                node.children[a]=TrieNode()
            node=node.children[a]
        node.children["/"]=TrieNode()
        node=node.children['/']



    
    def printTrie(self):
        print("inside print trie ")
        self.printTrieUtil(self.root)
        
    def printTrieUtil(self,node):
        # print("inside printTrieUtil")
        for key in node.children.keys():
            # print("->")
            print("key: {}, children: {} size: {}", (key, node.children[key], sys.getsizeof(node)))
            temp=node.children.get(key)
            self.printTrieUtil(temp)
    def checkSize(self):
        self.count=0
        self.checkSizeUtil(self.root)

    def checkSizeUtil(self,node):
        for key in node.children.keys():
            self.count+=1
            temp=node.children.get(key)
            self.checkSizeUtil(temp)

   # @profile
    def optimize(self):
        # node=self.root
        #print (self.root.children.keys())
        for key in self.root.children.keys():
            temp=self.root.children.get(key)
            self.optimizeUtil(temp,key,self.root,False)
                
    # @profile
    def optimizeUtil(self,node,string,start,flag):
        #print(len(node.children))
        # print_memory_used()
        if node==None:
            return
        if len(node.children)!=1 and flag!=False:
            start.children.pop(string[0], None)
            start.children[string]=node
            if len(node.children)==0:
                # start.last=True
                start.children['/']=TrieNode()
                return
            else:
                for key in node.children.keys():
                    temp=node.children.get(key)
                    self.optimizeUtil(temp,key,node,False)
                
        elif len(node.children)==1:
            if next(iter(node.children))=='/':
                if flag==True:
                    start.children.pop(string[0], None)
                    start.children[string]=node
                    
            else:
                string+=(next(iter(node.children)))
                node2=node.children[next(iter(node.children))]
                del(node)
                node=node2
                self.optimizeUtil(node,string,start,True)
        else:
            for key in node.children.keys():
                temp=node.children.get(key)
                self.optimizeUtil(temp,key,node,False)

    def display(self,root,string,level):
        if next(iter(root.children))=='/':  
            string[level] = '\0'
            print (string)
  
        for i in range(0,26):  
            if (root.children.get(chr(ord('a')+i)))!=None: 
                string[level] = chr(ord('a')+i)
                self.display(root.children.get(chr(ord('a')+i)), string, level + 1); 
            
    def clearSuggestions(self):
        self.word_list=[]
        self.ans=[]

    def mySuggestionsRec(self, node, word): 
        if '/' in node.children:
            self.word_list.append(word)

        for key in node.children:
            self.mySuggestionsRec(node.children.get(key),word+key)

    def myPrinter(self,key):
        node = self.root 
        not_found = False
        temp_word = ''
        for i in range(0,len(key)):
            a=key[0:i+1]
           # print("CHECKING {0}".format(a))
            if not node.children.get(a): 
                not_found = True
                continue
            else:
                temp_word+=a
                node=node.children[a]
                self.mySuggestionsRec(node,temp_word)
        count=0
        for s in self.word_list:
            if key in s and count<5:
                if s.index(key)==0:
                    self.ans.append(s)
                    count+=1
        
                    
       
    '''def printAutoSuggestions(self, key): 
          

        node = self.root 
        not_found = False
        temp_word = '' 
        
        for a in list(key): 
            if not node.children.get(a): 
                not_found = True
                break
  
            temp_word += a 
            node = node.children[a] 
  
        if not_found: 
            return 0
        elif node.last and not node.children: 
            return -1
  
        self.suggestionsRec(node, temp_word) 
  
        for s in self.word_list: 
            print(s) 
        return 1'''
'''
start = time.time()
with open('words_alpha.txt') as word_file:
    keys = list(word_file.read().split())
status = ["Not found", "Found"] 
end = time.time()
print("File read time- %f"%(end - start))
start = time.time()
t = Trie()  
t.formTrie(keys) 
end = time.time()
print("Trie generation time- %f"%(end - start))
t.checkSize()
print("NUMBER OF NODES BEFORE OPTIMIZATION:{0}".format(t.count))
print("STARTING OPTIMIZATION!!!",end='\n')
t.optimize()
t.checkSize()
print("NUMBER OF NODES AFTER OPTIMIZATION:{0}".format(t.count))

key = input("Enter the key\n")
while(key!="quit"):
    while len(key)<2:
        print ("ENTER AT LEAST 2 CHARACTERS")
        key=input()
    
    start = time.time()
    comp = t.myPrinter(key)
    if comp == 0: 
        print("No string found with this prefix\n") 
    end = time.time() 
    print("Print time- %f"%(end - start))
    key=input("\n\nENTER 'quit' to stop \n")
    t.clearSuggestions()
    #process = psutil.Process(os.getpid())
    #print(process.memory_info().rss)
    print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)'''

