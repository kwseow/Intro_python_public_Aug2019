import os
where = "C:\\Program Files"

def searchByName(name):
    totalSize = 0
    for root, dirs, files in os.walk(where):
        for file in files:
            if file == name:
                fullName = os.path.join(root,file)
                fileSize = os.path.getsize(fullName)
                print("%6d %s"%(fileSize, fullName))
                totalSize += fileSize
    return totalSize

total = searchByName("readme.txt")
print("Total file size : %d"%total)