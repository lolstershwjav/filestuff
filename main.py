import os
import shutil
#print(dir(os))
os.getcwd()
#os.mkdir("HEHEHA")
asdf = os.listdir("/Users/abhijoy/Desktop")

#print(asdf)

path = os.path.exists("/Users/abhijoy/Desktop")
print(path)

root, ext = os.path.splitext("/Users/abhijoy/Downloads/IMG_5914.HEIC")
print("root of the file is", root)
print("Extention of the file is", ext)

result = os.path.basename("/Users/abhijoy/Downloads/IMG_5914.HEIC")
print("result of the file is", result)

#print("Extention of the file is", ext)

source = "/Users/abhijoy/Downloads"

destination = "/Users/abhijoy/Desktop/qwe"

#result = shutil.move(source, destination)

list_of_files = os.listdir(source)
print(list_of_files)
for i in list_of_files:
    root, ext = os.path.splitext(i)
    print("root is ", root)
    print("extention is ", ext)


