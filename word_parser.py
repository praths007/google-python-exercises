# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 13:27:02 2016

@author: prathmesh.savale
"""

list2 = ["groupname","fromdate","todate","scrumtime","notifytime"]


string = "groupname prathmesh savale vijay fromdate 12th todate a scrumtime 13:00, 15:00 notifytime 14:30"

#string = ''.join(e for e in string if e.isalnum())
list1 = string.split(sep=" ")
#print(list1)

newlist = []
lasti = 0

for i in range(0, len(list1)):
    #print(i)
    for j in range(0,len(list2)):
       
        try:
            
            str1 = ''.join(e for e in list1[i] if e.isalnum())
            str2 = ''.join(e for e in list2[j] if e.isalnum())
            '''
            print(str1) 
            print(str2)
            '''
            if str1 == str2:
                '''
                a = list1[lasti:i]
                
                #print a
                b = a.append
                a.append()
                
                print(list1[lasti:i])

                
                '''
                
                newlist.append(list1[lasti:i])
                
                #newlist = newlist + (list1[lasti:i])
                #print(len(list1[lasti:i])-1)
                
                #newlist = newlist.append(list1[lasti:i])
        
                lasti = i
                
        except:
            pass
#print(list1[lasti:])  

newlist.append(list1[lasti:])

newlist.pop(0)

#print(newlist)

for i in range(0,len(newlist)):
    
    if newlist[i][0] == 'groupname':
        groupname = newlist[i].pop(0)
        groupname = newlist[i]
        
    if newlist[i][0] == 'fromdate':
        fromdate = newlist[i].pop(0)
        fromdate = newlist[i]
        
    if newlist[i][0] == 'todate':
        todate = newlist[i].pop(0)
        todate = newlist[i]
        
    if newlist[i][0] == 'scrumtime':
        scrumtime = newlist[i].pop(0)
        scrumtime = newlist[i]
        
    if newlist[i][0] == 'notifytime':
        notifytime = newlist[i].pop(0)
        notifytime = newlist[i]
        
        


 
print(groupname)
print(fromdate)
print(todate)
print(scrumtime)
print(notifytime)              
         
            
    