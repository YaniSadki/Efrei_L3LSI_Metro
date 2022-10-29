from PIL import Image, ImageDraw

#input file postpoint.txt
#output matrix with coordinates of all stations
def matrixééééé(f):
    d=[]
    for line in f:
        line = line.rstrip('\n') #delete the \n at the end of each line
        x = line.split(";")#create a tuple without ;
        d.append(x)
    return d


#input path from point a to point b
#output drawing of the path

def drawing_path(path):
    im = Image.open("data/metrof_r.png")
    img1 = ImageDraw.Draw(im)
    for i in range(len(path[1])-1):
        a = get_coordinate(path[1][i])
        b= get_coordinate(path[1][i+1])
        shape = [(int(a[0]),int(a[1])),(int(b[0]),int(b[1]))]
        img1.line(shape,fill = "black",width=3)
    im.show()


#input number of the station
#output coordinates of the station

def get_coordinate(a,matrix_point,dico2):
    for i in range(len(matrix_point)): #
        if matrix_point[i][2]==dico2[a][0]:
            return matrix_point[i][:2]


def drawing_ACPM(ACPM):
    im = Image.open("data/metrof_r.png")
    img1 = ImageDraw.Draw(im)

    for i in range(len(ACPM)):
        a = get_coordinate(ACPM[i][0])
        b= get_coordinate(ACPM[i][1])
        shape = [(int(a[0]), int(a[1])), (int(b[0]), int(b[1]))]
        img1.line(shape, fill="black", width=3)

    im.show()
