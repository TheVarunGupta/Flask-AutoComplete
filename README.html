<!DOCTYPE HTML>
<html>
<body>

<h1>The Python Autocomplete Application</h1>
<hr>
<p>We all see the keyboards in our mobile phones and websites complete our words for us. Well this is the same application, but more of an optimized one, the one which you won't find on internet built from scratch ;)</p>
<a href="http://johnjohnston.info/106/wp-content/uploads/2013/12/google_autocomplete.gif"> <img src="http://johnjohnston.info/106/wp-content/uploads/2013/12/google_autocomplete.gif"></a>
<h3>Prerequisites & Software Required</h3>
<p>
<ul style="list-style-type:disc">
    <li>Python</li>
    <li>Knowledge of Tries and dictionaries</li>
    <li>Visual Studio Code</li>
</ul>
</p>

<h3>Dataset</h3>

<p>The dataset is nothing but a txt file containing all the words of the dictionary. It is stored in the file name words_alpha.txt. You can mess around with it as much as you'd like. You can also change the source to small words.txt and mess around with it(It has no other purpose than that :P). </p>

<h3>Logic</h3>
<p>
The main idea behind the application is the usage of tries and their optimization. 
First of all we use a trie to create our dictionary (I've written English dictionary and python dictionaries separately so that you don't get confused while reading them). All the words in the English dictionary are created node by node. 
So let's take the word 'Teaching' for example. When we create this word, it is stored node by node as in, T is a node connected to e which is further connected to a and so on.
They are connected in the form of python dictionaries, i.e. every node has a python dictionary. So, the node T will have a python dictionary where there will be a key 'e' pointing to the address of the node of 'e'.
At the end of the word "Teaching", we will append a '/' so that we can denote that this is the end of the word. This will have a significant impact when the optimization takes place. We will discuss it later.
</p>
<h4> For example:</h4>
<a href="https://ibb.co/Jk7xTtS"><img src="https://i.ibb.co/Jk7xTtS/representation.png" alt="representation" border="0"></a>
<p>In this image the root node has a dictionary with two keys,i.e 't' and 's', what we can observe here is that the nodes themselves have no values, it is the key in the dictionary that tells us what the value of the node is.
To optimize this trie, what we can do is combine the nodes i, n and t to make it a single node 'int', similarly i, n ,g can be combined to 'ing' to conserve two nodes.
For another example, you can refer to this <a href="https://ibb.co/jrp5dxb">example.</a>
</p>
<h3> Optimization</h3>
<p>What really happens during optimization? What we are essentially trying to do is find the node which has only one child. So let's say the dictionary we have, only has two words, "teach" and "teachnig".
when we create the trie, our trie will look like this : <br>
<a href="https://ibb.co/pPD2ZmL"><img src="https://i.ibb.co/pPD2ZmL/Screenshot-from-2019-02-11-14-40-01.png" alt="Screenshot-from-2019-02-11-14-40-01" border="0"></a>
<br>
Now, we are going to look for nodes which have only one child and we are going to look recursively for the next node which has either no children or more than one children. While recursing we will store all the key values so that we can delete all the nodes occuring in between and assign a single node for the connection.
In our example, we will start from 'T' until we reach 'H' and then we will combine them all to make the node 'Teach'. Now this is where the node '/' helps us to determine that we have reached the end of the word, if '/' was not there, we would have combined all the nodes from 'T' to 'G' and our model would not have the word teach itself making it impossible to occur during the search.
Now, our model will look like this:<br>
<a href="https://imgbb.com/"><img src="https://i.ibb.co/fxfpsWV/combined.png" alt="combined" border="0"></a>
</p>
<h3> <u>How to use the code:</u></h3>
<ul>
<li>clone the git (hopefully you know how)</li>
<li>install the requirements with "pip install requirements.txt" command in the terminal</li>
<li>open terminal in the root of the cloned folder</li>
<li>type "export FLASK_APP=Dictionary.py" and press enter</li>
<li>type "flask run" and press enter</li>
<li>Your server is up now and you can open the browser with local host and port mentioned in the terminal</li>
</ul>
<h3> <u> Structure of the code:</u></h3>
<ul>
<li> /-Root Folder</li>
<li> &emsp;/-app Folder</li>
<li>&emsp;&emsp;&emsp;-Autocompleter.py</li>
<li>&emsp;&emsp;&emsp;-routes.py</li>
<li> &emsp;-Dictionary.py</li>
<li> &emsp;-Mem_analysis.py</li>
<li>&emsp;- TXT Files
</ul>
<h3><u> Understanding the code:</u></h3>
<ul>
<li>Firstly we are typing the export FLASK_APP=Dictionary.py command, what it does is  tell the flask framework to use this app when we use "flask run " command("how does routes.py execute when we export Dictionary.py"??? this is done by __init__.py  :P) </li>
<li>After that our routes.py class is run, where there is a lot of code, let's break it down.</li>
<li>First of all we import the Autocompleter class which gives us the ability to use the autocompleter Trie in our framework.</li>
<li> After that you will see functions like memory_used(), these functions are used to check how much memory is being used by our application, this actually helps us determine whether our trie is optimized or not</li>
<li>You can change "words_alpha.txt" to "small_words" if you want the application to show the name of your products/inventory or something like that.</li>
<li>the t.formTries(keys) is used to create the whole trie, where t is our trie</li>
<li>t.optimize() optimizes our trie and reduces the number of nodes</li>
<li>After the optimization, you can see the amount of memory used by your code by using the print_memory_used function in routes.py class</li>
<li> Save the ouput you are getting in a txt file and use the Mem_analysis.py to analyse which objects are consuming memory and the difference of memory used between unoptimized and optimized Trie</li>
<li> Apart from this, you can explore the autocompleter class but there are a lot of functions in it so i recommend you to access it only when routes.py make a call to the function of autocompleter class</li>
</ul>
<h3>Results:</h3>
<ul>
<li>We had 1397901 nodes before optimization, we could reduce the number to 959580 nodes. This means we save over 4 lac nodes, since these nodes will not be stored in the memory, we save a lot of load on the device.</li>
<li>This optimization is of trie only, there is no hit based system so the model we are using doesn't which show recommendation should be given next, it just shows the next few words in the dictionary. We need to use models like Hidden Markov Model to train that sort of a predictive system.</li>
</ul>
<h3> Bugs:</h3>
<ul>
<li> The searching algorithm is very poor right now, it is unable to search for the nodes which are bigger than the given input itself, so if the dictionary only had the words "Teacher" and "Teach", the algo will fail if you enter input as "Tea". This will be rectified in the future.</li>
</ul>
</body>
</html>