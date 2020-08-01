import os
from os.path import isdir
import shutil

desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')


def getItems():
    return os.listdir(desktop)

def moveToHolder(holder, file):
    shutil.move(os.path.join(desktop, file), os.path.join(os.path.join(desktop, holder), file))

def checkList(keepList, item):
    for i in keepList:
        if i in item:
            return False

    return True

def moveItemsToHolder(holder, items, keepList):
    for i in items:
        if  holder not in i and checkList(keepList, i):
            print("Moving: " + i)
            moveToHolder(holder, i)

def getKeepList(file="keeplist.txt"):
    with open(file, "r", encoding="utf-8") as f:
        return f.read().split('\n')

def isEmptyFolder(folder):
    if not os.path.isdir(os.path.join(desktop, folder)):
        return False
    if len(os.listdir(os.path.join(desktop, folder).replace("\\\\","\\"))) == 0:
        return True
    else:    
        return False

def deleteEmpytFolders(items):
    for i in items:
        if isEmptyFolder(i):
            print("Deleting:", i, "empty folder")
            os.rmdir(os.path.join(desktop, i))

def main():
    holderDirName = "desktop"
    keepList = getKeepList()
    print("\n I will keep these: " + str(keepList))
    
    items = getItems()
    deleteEmpytFolders(items)
    
    items = getItems()
    print("\n" + str(items))
    
    moveItemsToHolder(holderDirName, items, keepList)
    input("...")
    

if __name__ == "__main__":
    main()