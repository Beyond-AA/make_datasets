import os
# import json

file_name = r"D:/Data_set/fake_image/dataset.txt"
imgfile = r"D:\Data_set\fake_image\img"

imgfile_list = os.listdir(imgfile)
f = open(file_name, mode="w")

for i in imgfile_list:
    if str(i) == "CrystalImpurity":
        for j in os.listdir(imgfile + "/" + str(i)):
            k = str(j)
            #f = open(file_name, mode="w")
            f.write("[\"" + k + "\"" + "," + "1" + "]" + "\n")
            #f.close()
            # print("j=", j)

    if str(i) == "Smudge":
        for j in os.listdir(imgfile + "/" + str(i)):
            #f = open(file_name, mode="w")
            k = str(j)
            f.write("[\"" + k + "\"" + "," + "2" + "]" + "\n")
            #f.close()

    if str(i) == "OK_Image":
        for j in os.listdir(imgfile + "/" + str(i)):
            #f = open(file_name, mode="w")
            k = str(j)
            f.write("[\"" + k + "\"" + "," + "3" + "]" + "\n")
            #f.close()

    if str(i) == "StarCrack":
        for j in os.listdir(imgfile + "/" + str(i)):
            f# = open(file_name, mode="w")
            k = str(j)
            f.write("[\"" + k + "\"" + "," + "4" + "]" + "\n")
            #f.close()
f.close()


