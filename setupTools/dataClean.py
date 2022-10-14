olddata = open('data.json', 'r')
newFile = open("cleanData.json", "w")

while True:
    line = olddata.readline()
    
    if (line == "[\n"):
        newFile.write("{\n")
    elif (line == "]"):
        newFile.write("}")
        break
    else:
        newFile.write(line[1:].replace("}}}", "}}"))
        
newFile.close()
olddata.close()
