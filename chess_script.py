import xml.etree.ElementTree as ET
fileName = '/full/path/to/the/file/toParse.html'
tree = ET.parse(fileName)
root = tree.getroot()
children = []
pgn = []
pgn_clean =
#put your user name here
user_name = ''
search_string = str(user_name) + 'reconnected'

def CalculatePgn():
    for item in root:
        children.append(item)
    for index in range(0, len(children)):
        if index%2 == 0:
            pgn.append(children[index].text)
    print pgn

def CalculateFullPgn():
    for item in root:
        children.append(item)
    for index in range(0, len(children)):
       	pgn.append(children[index].text)
    filtered = [ x for x in pgn if not x.startswith(str(user_name)) ]
    for iterator in range(0, len(filtered)):
    	if iterator%2 == 0:
    		pgn_clean.append(filtered[iterator])

    f = open('pgn.txt', 'w')
    f.write(str(pgn))
    f_clean = open('pgn_clean.txt', 'w')
    f_clean.write(str(pgn_clean).replace(",", "").replace("'", "").replace("[", "").replace("]", ""))


CalculateFullPgn()

