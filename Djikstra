#compute the minimum path between 2 index: start and end
def dicoDjikstra(dico,start,end):                                               #input: the dictonnary, the starting station and the ending station

    infini = sum(sum(dico[s1][s2] for s2 in dico[s1]) for s1 in dico) + 1       #we define infini as the sum of all our paths + 1 (nothing could be higher)
    s_treated = {start:[0,[start]]}                                             #s_treated = summits already treated :      [length,shortest path]
    s_not_treated = {k:[infini,''] for k in dico if k!=start}                   #s_not_treated = summits to be treated :    [length, last summit]

    for next in dico[start]:                                                    #we initialize the table by giving the right value of distance to each successor of "start"
        s_not_treated[next] = [dico[start][next],start]                             

    while s_not_treated and any(s_not_treated[k][0] < infini for k in s_not_treated):   #we continue the algorithm while we still have summits to treat and there is still infinite values for not treated summits
        u=min(s_not_treated, key=s_not_treated.get)                                     #we choose the summit u with the shortest distance to the summit we are treating
        length_u,last_u=s_not_treated[u]                                                

        for v in dico[u]:                                                               #we compute the minimum distance and modify the values of each successor of u
            if v in s_not_treated:
                d= length_u + dico[u][v]
                if d<s_not_treated[v][0]:
                    s_not_treated[v]=[d,u]


        s_treated[u]=[length_u, s_treated[last_u][1]+[u]]                               #the summit u has beet treated, we put it in the "treated table" and delete it from the other         
        del s_not_treated[u]

    for key in s_treated.keys():                                                        
        if key == end:
            return s_treated[key]                                                       #output: the path and the distance between the starting and the ending station


#Djikstra with the names of the stations instead of their index
def minimumPath(dico,dico_noms,name_start,name_end):    
    l1=[]
    l2=[]
    for i in dico_noms:                                 #create 2 lists of index of the corresponding stations
        if dico_noms[i][0]==name_start:
            l1.append(i)
        if dico_noms[i][0]==name_end:
            l2.append(i)

    minimumPath = dicoDjikstra(dico,l1[0],l2[0])   
    for i in l1:                                        #find the minimum path among these index
        for j in l2:
            m=dicoDjikstra(dico,i,j)
            if m<minimumPath:
                minimumPath = m  
    return minimumPath
