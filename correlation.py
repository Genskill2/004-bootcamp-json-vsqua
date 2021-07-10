# Add the functions in this file
import json
import math

def load_journal(file_name):
    file1= open(file_name,'r')
    read_data=file1.read()
    list_of_dicts=json.loads(read_data)
    return list_of_dicts

def compute_phi(file_name,event):
    event_true=0
    event_false=0
    squirrel_true=0
    squirrel_false=0

    event_true_squirrel_true=0
    event_true_squirrel_false=0
    event_false_squirrel_true=0
    event_false_squirrel_false=0
    
    list1=load_journal(file_name)

    for i in list1:
        if i["squirrel"]:
            squirrel_true = squirrel_true+1
        else:
            squirrel_false = squirrel_false+1

        if event in i["events"]:
            event_true=event_true+1
            if i["squirrel"]:
                event_true_squirrel_true = event_true_squirrel_true+1
            else:    
                event_true_squirrel_false = event_true_squirrel_false+1

        else:
            event_false=event_false+1
            if i["squirrel"]:
                event_false_squirrel_true = event_false_squirrel_true+1
            else:    
                event_false_squirrel_false = event_false_squirrel_false+1

    correlation=((event_true_squirrel_true*event_false_squirrel_false) - (event_true_squirrel_false*event_false_squirrel_true))/math.sqrt(event_true*event_false*squirrel_true*squirrel_false)
    return correlation

def compute_correlations(file_name):
    list1=load_journal(file_name)
    events=[]
    dict={}
    for i in list1:
        list2=i["events"]
        for j in list2:
            if j not in events: 
                events.append(j)
                correlation=compute_phi(file_name,j)
                dict[j]=correlation
     
    return dict

def diagnose(file_name):
    
    dict=compute_correlations(file_name)
    pos=str(list(dict.keys())[0])
    neg=str(list(dict.keys())[0])
    for (key,val) in dict.items():
        if val>0 and val >dict[pos]:
            pos= str(key)
        if val<0 and val<dict[neg]:
            neg=str(key)

    return pos,neg
