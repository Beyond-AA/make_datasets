import cv2
import os

path = r"D:\Data_set\fake_image\stylegan2-ada-dataset"
# dst_file = r"D:\Data_set\fake_image\my_metfaces"

for i in os.listdir(path):
    if i == "CrystalImpurity":
        img_file = path + "/" + i
        for j in os.listdir(img_file):
            img_path = img_file + "/" + j
            img = cv2.imread(img_path)
            img = cv2.resize(img, (1024, 1024), interpolation=cv2.INTER_NEAREST)
            cv2.imwrite("D:/Data_set/fake_image/my_metfaces/{}".format(j), img)
    elif i == "OK_Image":
        img_file = path + "/" + i
        for j in os.listdir(img_file):
            img_path = img_file + "/" + j
            img = cv2.imread(img_path)
            img = cv2.resize(img, (1024, 1024), interpolation=cv2.INTER_NEAREST)
            cv2.imwrite("D:/Data_set/fake_image/my_metfaces/{}".format(j), img)
    elif i == "Smudge":
        img_file = path + "/" + i
        for j in os.listdir(img_file):
            img_path = img_file + "/" + j
            img = cv2.imread(img_path)
            img = cv2.resize(img, (1024, 1024), interpolation=cv2.INTER_NEAREST)
            cv2.imwrite("D:/Data_set/fake_image/my_metfaces/{}".format(j), img)
    else:
        img_file = path + "/" + i
        for j in os.listdir(img_file):
            img_path = img_file + "/" + j
            img = cv2.imread(img_path)
            img = cv2.resize(img, (1024, 1024), interpolation=cv2.INTER_NEAREST)
            cv2.imwrite("D:/Data_set/fake_image/my_metfaces/{}".format(j), img)