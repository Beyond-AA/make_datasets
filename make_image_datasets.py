import os
import cv2

path = r"D:/Data_set/fake_image"

imgfile_list = os.listdir(path)
#print(imgfile_list)
k = 0
for i in imgfile_list:

    if str(i) == "CrystalImpurity":
        #os.makedirs("D:/Data_set/fake_image/img/CrystalImpurity")
        # img_list = os.listdir(path + "/" + str(i))
        for j in os.listdir(path + "/" + str(i)):
            # print("j=", j)
            try:
                img = cv2.imread(path + "/" + str(i) + "/" + str(j), 0)
                # cv2.imshow("img", img)
                # cv2.waitKey(0)
                # cv2.destroyAllWindows()
                k = str(k)
                k = k.zfill(4)
                cv2.imwrite("D:/Data_set/fake_image/img/CrystalImpurity/{}.jpg".format(k), img)
                k = int(k) + 1
            except:
                print("error")

    if str(i) == "Smudge":
        #os.makedirs("D:/Data_set/fake_image/img/Smudge")
        #img_list = os.listdir(path + "/" + str(i))
        for j in os.listdir(path + "/" + str(i)):
            try:
                img = cv2.imread(path + "/" + str(i) + "/" + str(j), 0)
                k = str(k)
                k = k.zfill(4)
                cv2.imwrite("D:/Data_set/fake_image/img/Smudge/{}.jpg".format(k), img)
                k = int(k) + 1
            except:
                print("error")

    if str(i) == "OK_Image":
        #os.makedirs("D:/Data_set/fake_image/img/OK_Image")
        # img_list = os.listdir(path + "/" + str(i))
        for j in os.listdir(path + "/" + str(i)):
            try:
                img = cv2.imread(path + "/" + str(i) + "/" + str(j), 0)
                k = str(k)
                k = k.zfill(4)
                cv2.imwrite("D:/Data_set/fake_image/img/OK_Image/{}.jpg".format(k), img)
                k = int(k) + 1
            except:
                print("error")

    if str(i) == "StarCrack":
        #os.makedirs("D:/Data_set/fake_image/img/StarCrack")
        # img_list = os.listdir(path + "/" + str(i))
        for j in os.listdir(path + "/" + str(i)):
            try:
                img = cv2.imread(path + "/" + str(i) + "/" + str(j), 0)
                k = str(k)
                k = k.zfill(4)
                cv2.imwrite("D:/Data_set/fake_image/img/StarCrack/{}.jpg".format(k), img)
                k = int(k) + 1
            except:
                print("error")




