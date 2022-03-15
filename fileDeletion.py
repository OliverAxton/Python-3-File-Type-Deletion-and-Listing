
import os
import fnmatch
from collections import Counter

def main():
    option=int(getMenu())
    
    if option == 1:
       listFileTypes()
    elif option == 3:
        fileDeletion()
    elif option == 2:
        searchByExtension()
    else: exit() 
    
    
    
def fileDeletion():
    count=int(0)
    print("")
    fileType=input("What file extension would you like to delete? (Please insert with a .) ")
    print("WARNING: Are you sure that you want to delete ALL files with the file extension " , fileType, " this can result in loss of data")
    checkuser=input("WARNING: Are you sure you want to delete files (Y/N)")
    if checkuser == "Y":
        for root, dir, files in os.walk("."):

            for items in fnmatch.filter(files, "*"):
                if items.endswith(fileType):
                    #os.remove(items)
                    print(os.path.join(root, items))
                    os.remove(os.path.join(root, items))
                    count+=1
        print("")
        print(count , " files deleted")
        main()  
    else: main()
    
    
    
    
    
    
    
def listFileTypes():
    SplitTypes=[]
    for root, dir, files in os.walk("."):
        for items in fnmatch.filter(files, "*"):
            SplitTypes.append(items.split('.')[-1])
    print()
    print(Counter(SplitTypes))
    main()
 
def searchByExtension():
    print("")
    fileType=input("What file extension would you like to search for? (Please insert with a .) ")
    for root, dir, files in os.walk("."):
        for items in fnmatch.filter(files, "*"):
            if items.endswith(fileType):
                print(os.path.join(root, items))
    print("")
    
    
    main()
     
def getMenu():
    print("")
    
    print("1. List all file types and count on system")
    print("2. Search files by extension")
    print("3. Delete all files with chosen file extension")

    print("4. Exit")
    option=input("Select option: ")
    return option
    
    
main()