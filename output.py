import os

# function to open files; arguments: file path and output dictionary
def openFile(filepath, dict):
    if os.path.isfile(filepath):
        with open(filepath, "r", encoding="utf-8") as f1:
            for line in f1:
                t = line.split("|")
                EN = t[0]
                IT = t[1].replace("\n", "")

                dict[IT] = EN
    else:
        raise ValueError("File don't exist.")
    
    # returns a dictionary
    return dict


# function to generate dictionary; arguments: arguments: paths to dictionary files
def generateDictionary(plToEnPath, enToItPath):
    
    dictonaryENtoIT = {}
    dictonaryPLtoEN = {}
    PLtoIT = {}

    # open files
    ENtoIT = openFile(enToItPath, dictonaryENtoIT)
    PLtoEN = openFile(plToEnPath, dictonaryPLtoEN)

    # value and key inversion
    invENtoIT = {v: k for k, v in ENtoIT.items()}

    # comparison of two dictionaries
    for k in PLtoEN.items():
        for kk in invENtoIT.items():
            if k[0]==kk[0]:
                PLtoIT[k[1]] = kk[1]
                break

    # saving the output file
    output_file = open("PLtoIT.dsv", "w", encoding="utf-8")
    for PL in PLtoIT:
        IT = "".join(PLtoIT[PL])
        word = "|".join([PL, IT])
        output_file.write(word+"\n")

    output_file.close()

    # returns the path to the output file
    return os.path.abspath("PLtoIT.dsv")


# function call
filePLtoIT = generateDictionary("PLtoEN.dsv", "ENtoIT.dsv")
print(filePLtoIT + "\n")

# writing out translated words from the created file
for line in open(filePLtoIT, "r", encoding="utf-8"):
    print(line, end="")
