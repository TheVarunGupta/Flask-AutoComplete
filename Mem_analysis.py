mydict1={}
mydict2={}
with open('UnoptimizedMem.txt') as word_file:
    keys = list(word_file.read().split(','))
    for key in keys:
        x,y=key.split(":")
        if x not in mydict1.keys():
            mydict1[x]=int(y)
        else:
            mydict1[x]+= int(y)
with open('OptimizedMem.txt') as word_file:
    keys = list(word_file.read().split(','))
    for key in keys:
        x,y=key.split(":")
        if x not in mydict2.keys():
            mydict2[x]= int(y)
        else:
            mydict2[x]+= int (y)
for key in mydict2.keys():
    if key not in mydict1.keys():
        print ("EXTRA MEM AT {} {}".format(mydict2[key],key))
    elif int(mydict2[key])-int(mydict1[key]) !=0:
        print("DIFFERENCE IN MEMORY AT: {} {}".format(int(mydict2[key])-int(mydict1[key]),key))