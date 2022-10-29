#input dico : dico with station's name from init_station, line : line of a station,path from dicoDjikostra,station's number
#output : return the name of the terminus of line


def direction_of(dico,dico_w_name,line,path,stations_number):
    for i in range(len(dico_w_name)):
        if line==int(dico_w_name[i][1]) and  dico_w_name[i][2]=='True': #check if it's a terminus or not
            path1 = dicoDjikstra(dico,stations_number,i) #get the path from the starting point (stations_number) to the terminus
            new_path1 = path1[1][1:]
            new_path = path[1][1:]
            for line1 in new_path: #check if it's the right terminus by comparing the 2 paths
                for line2 in new_path1:
                    if line1 ==line2:
                        return dico_w_name[i][0]


#input : dico : dico with station's name from init_station, dico1 from init_map, path from dicoDjkstra, example on how to call the function :
#               read_itinary(dico2,dicoDjikstra(dico,3,5))
#output : print the whole itinary from summit A to summit B


def read_itinary1(dico_w_name,path):
    c=""
    c+="Temps estimé : "+str(path[0])+" secondes\n"
    depart_ligne = int(dico_w_name[path[1][0]][1])
    c+="Vous prenez la station "+dico_w_name[path[1][0]][0]+"ligne "+str(depart_ligne)+"direction "+direction_of(dico_w_name,depart_ligne,path,path[1][0])+'\n'
    for i in range(len(path[1])):
        depart_apres = int(dico_w_name[path[1][i]][1])
        if depart_ligne!=depart_apres:
            depart_ligne = depart_apres
            c+="Vous devez descendre à la station"+dico_w_name[path[1][i]][0]+"puis prendre la ligne "+str(depart_apres)+" direction "+direction_of(dico_w_name,depart_ligne,path,path[1][i])+'\n'
    c+="Vous êtes arrivé à la station "+dico_w_name[path[1][len(path[1])-1]][0]+"ligne "+str(depart_ligne)
    return c;
