
name = "mbox-short.txt"
handle = open(name)
dic=dict()                                     # defines an empty dictionary
for line in handle:
    if not line.startswith("From ") : continue #select only lines with "From "
    words=line.split()                         #turns string into list of words
    word2=words[5]                             #select hour 
    word2=word2[:2]                            #slice 2 first characters 
    dic[word2]=dic.get(word2,0)+1              #accumulate in dictionary

flipped = list()
for clave, valor in dic.items():
    nvatupla = clave, valor                    #changes the order of key-value pair
    flipped.append(nvatupla)                   #add to list flipped  

flipped.sort()                                 #sort list flipped
for clave,valor in flipped:
    print clave,valor                          #print ordered list


name = "mbox-short.txt"
handle = open(name)
dic=dict()                                     # defines an empty dictionary
for line in handle:
    if not line.startswith("From ") : continue #select only lines with "From "
    words=line.split()                         #turns string into list of words
    word2=words[5]                             #select hour 
    word2=word2[:2]                            #slice 2 first characters 
    dic[word2]=dic.get(word2,0)+1              #accumulate in dictionary

flipped = list()
for clave, valor in dic.items():
    nvatupla = clave, valor                    #changes the order of key-value pair
    flipped.append(nvatupla)                   #add to list flipped  

flipped.sort()                                 #sort list flipped
for clave,valor in flipped:
    print clave,valor                          #print ordered list
