# Call files 
import kruskal_acpm
import data_structure

f = open("data/metro.txt", "r")
dico = data_structure.init_map(f)
#dico = (data_structure.init_station(f))
#print("There is a dico :",dico) #print all the dico data structure

#call kruskal with the dico of dico
ACPM = kruskal_acpm.kruskal(dico)
print('ACPM of Paris metro map :', ACPM)  #print all the ACPM