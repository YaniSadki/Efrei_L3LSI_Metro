# Read a line and return an array with the info given in the line
# V 0000 Abbesses ;12 ;False 0 -> ["Abbesses","12","False","0"]

from asyncio.windows_events import NULL
from multiprocessing.sharedctypes import Value
from platform import node

def read_v(line):
    number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    arr = [""] * 4
    i = 7
    j = 0
    trigger = True
    if line[0] == "V":
        while j != 3:   # j is the index of the array we are filling with our information
            if line[i] in number and trigger:   # Whenever we go from words to a number and vice-versa
                trigger = False                 # we increment the index
                j += 1
                arr += []
            if line[i] not in number and not trigger:
                trigger = True
                j += 1
                arr += []
            arr[j] += line[i]
            i += 1
        arr[0] = arr[0][:-2]    # We delete unwanted characters like ";" or spaces
        arr[2] = arr[2][2:-1]
        return arr

# Read a line and return an array with the info given in the line
# E 0 238 41 -> [0,238,41]
def read_e(line):
    j = 0
    arr = [""] * 3
    for i in range(len(line))[2:]:
        if line[i] == " " and j <= 1:
            arr[j] = int(arr[j])
            j += 1
            arr += []
        else:
            arr[j] += line[i]
    arr[j] = int(arr[j])
    return arr

# Take a file in parameter and ant return a dico
# {item = index of the station:
#  value = station infos in an array}
# V 0185 Maisons-Alfort les Juilliottes ;8 ;False 0
# {185 : {['Maisons-Alfort les Juilliottes', '8', 'False', '0']}, 186 : {['Maison Alfort, Stade', ...] ...}
def init_station(f):
    i = 0
    dico = {}
    for line in f:
        if line[0] == "E": break
        dico[i] = read_v(line)
        i += 1
    return dico

# Take a file in parameter and ant return a dico of dico
# {item = index of the station :
#  value = a dico {item  = index of the destination :
#                 value = time to go to the destination}}
# E 189 367 49
# [189, 367, 49]
# {189 : {367: 49}, 190 : {...}, ...}
#
# where we come from == 189
# where we can go    == 367
# how long it takes  == 49

def init_map(f):
    dico = {}
    for i in range(376):    # initialize the dico dico
        dico[i] = {}
    for line in f:
        if line[0] == "E":
            leg = read_e(line)
            dico[int(leg[0])][int(leg[1])] = int(leg[2])    # the graph is non oriented so we give it add the path two times
            dico[int(leg[1])][int(leg[0])] = int(leg[2])
    return dico