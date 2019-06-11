file_name = "pieces.txt"

class Piece:
    def __init__(self):
        # İnitiliaze file, if not exists, create the file
        # file = open(file_name, 'w+')
        try:
            file = open(file_name, 'r')
        except IOError:
            file = open(file_name, 'w')
        file.close()

    def all(self):
        file = open(file_name,"r")
        pieces = file.readlines()
        file.close()
        return pieces

    def add(self,title,author,year):
        file = open(file_name, "a")
        file.write(title + ", " + author + ", " + year + "\n")
        file.close()

    def search(self,keyword,type):
        # Type 1 Title, 2 Author, 3 Date
        result = []
        file = open(file_name, "r")
        line = file.readline()
        while(line):
            if keyword in line.split(",")[int(type)-1]:
                result.append(line)
            line = file.readline()
        file.close()
        return result