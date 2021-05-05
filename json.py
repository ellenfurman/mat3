#read the file
def readfile ():
    file=input(" please enter your file ")
    file=open(file, encoding ='UTF-8')
    file=file.read()
    return file

#use the file from the function and split the lines
myfile = readfile()
Lines=myfile.splitlines()
numbers=dict()
mylist=list()
i=0
j=0
#keys for the names/numbers
for line in Lines:
    strat=line.find("-")
    end=line.find(":",strat+2)
    if(end>0 and line[strat+2:end] not in numbers):
        numbers[line[strat+2:end]] = i
        i=i+1
    #make a dictionary for each post
    #put all the dictionary in one list
    if(end>0):   
        mylist.append(dict()) 
        mylist[j]['datatime']= line[0:strat]
        mylist[j]['id']= numbers[line[strat+2:end]]
        mylist[j]['text']= line[end:]
        j=j+1
        
#creating a new dictionary with more details    
metadata=dict()
index1=myfile.find('"')
index2= myfile.find('"',index1+1)                                
metadata['chat_name']=myfile[index1 +1:index2] 
    
index3=Lines[1].find("-")                         
metadata['creation_date']=Lines[1][0:index3]

metadata['num_of_participants']=len(numbers)
index4=Lines[1].rfind(" ")

metadata['creator']=Lines[1][index4-4:]

#comprehensive dictionary
dictionary=dict()
dictionary['messages']=mylist
dictionary['metadata']=metadata

import json
name=metadata['chat_name'] +".txt"
with open(name, 'w', encoding='utf8') as name:
    json.dump(dictionary, name, ensure_ascii=False)
