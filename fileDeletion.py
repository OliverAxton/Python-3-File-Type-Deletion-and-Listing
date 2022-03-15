
import os
import fnmatch


def main():
    option=int(getMenu())
    
    if option == 1:
       listFileTypes()
    elif option == 2:
        fileDeletion()
    else: exit() 
    
    
    
def fileDeletion():
    count=int(0)
    print("")
    fileType=input("What file extension would you like to delete? (Please insert with a .")
    for root, dir, files in os.walk("."):
        #print(root)
        #print("")
        for items in fnmatch.filter(files, "*"):
            if items.endswith(fileType):
                    #os.remove(items)
                print(os.path.join(root, items))
                os.remove(os.path.join(root, items))
                count+=1
    print("")
    print(count , " files deleted")
    main()
    
    
    
def listFileTypes():
    return
     
def getMenu():
    print("")
    
    print("1. List all file types and count on system")
    print("2. Delete all files with chosen file extension")
    print("3. Exit")
    option=input("Select option: ")
    return option
    
    
main()