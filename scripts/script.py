import cv2
import glob
import os


local = 1
LRW_raw = "LRWmini"
LRW_raw_frames = "LRWmini_raw_frames"
LRW_output_frames = "LRWmini_output_frames"

if local:
    root_virtual = "G:/dataset/lipreading/lrw/graph/virtual_root"
else:
    root_virtual = ""

files = glob.glob(root_virtual + "/home/bmax/data_users/zxy/" + LRW_raw + "/*/*/*.mp4")



for i in files:
    # print(i)
    frame_save_dir = i.split('.')[0].replace("\\", "/").replace("/" + LRW_raw + "/", "/" + LRW_raw_frames + "/")
    print(frame_save_dir)
    dir1 = "/".join(frame_save_dir.split("/")[:-2])
    # print(dir1)
    if not os.path.exists(dir1):
        os.mkdir(dir1)
    if not os.path.exists(dir1.replace("/" + LRW_raw_frames + "/", "/" + LRW_output_frames + "/")):
        os.mkdir(dir1.replace("/" + LRW_raw_frames + "/", "/" + LRW_output_frames + "/"))
    dir2 = "/".join(frame_save_dir.split("/")[:-1])
    if not os.path.exists(dir2):
        os.mkdir(dir2)
    if not os.path.exists(dir2.replace("/" + LRW_raw_frames + "/", "/" + LRW_output_frames + "/")):
        os.mkdir(dir2.replace("/" + LRW_raw_frames + "/", "/" + LRW_output_frames + "/"))
    dir3 = "/".join(frame_save_dir.split("/")[:])
    if not os.path.exists(dir3):
        os.mkdir(dir3)
    if not os.path.exists(dir3.replace("/" + LRW_raw_frames + "/", "/" + LRW_output_frames + "/")):
        os.mkdir(dir3.replace("/" + LRW_raw_frames + "/", "/" + LRW_output_frames + "/"))

    cap = cv2.VideoCapture(i)
    suc = cap.isOpened()
    frame_count = 0
    suc, frame = cap.read()
    while suc:
        frame_count += 1

        cv2.imwrite(dir3 + "/" + str(frame_count) + ".png", frame)
        suc, frame = cap.read()

    cap.release()
    # print('unlock movie: ', frame_count)