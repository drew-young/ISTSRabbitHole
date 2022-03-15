from urllib.request import urlopen
import time

index = 2


website = "http://ctf.ists.io/rabbithole/"
ext = "16aa80dfee745be0d3097726ebba89f2.txt"
with open("out2.txt", 'a') as file:
    page = urlopen(website)
    contents = page.read().decode()
    file.write(contents)
    while True:
        file.write("\n----------------------------------------------------------\n")
        page = urlopen(website + ext)
        contents = page.read().decode()
        print(contents)
        splittedContents = contents.split(" ")
        print(splittedContents[2])
        fileWrite = str(index) + ": " + contents + " : " + website + ext
        file.write(fileWrite)
        ext = splittedContents[2] + ".txt"
        index+=1
        time.sleep(.01)
