from itertools import count
from cvzone.HandTrackingModule import HandDetector
import cv2
import numpy as np
import math
import string
import os

# Create the Data set directory structure
if not os.path.exists("Handtracking/ASL_Data_set"):
    os.makedirs("Handtracking/ASL_Data_set")
    # print ("Folder Created")

#Making Integer folders 1 - 9
for i in range(1, 10):
    if not os.path.exists("Handtracking/ASL_Data_set/" + str(i) ):
        os.makedirs("Handtracking/ASL_Data_set/" + str(i))
        # print ("Folder Made " + str(i))


#Making Alphabet folder A - Z
for i in string.ascii_uppercase:
    if not os.path.exists("Handtracking/ASL_Data_set/" +i ):
        os.makedirs("Handtracking/ASL_Data_set/"+i)
        # print ("Folder Made " + str(i))


cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=2)
offset = 30
imgSize = 300
folder = 'Handtracking/ASL_Data_set/'

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)
    # Only If Hands Visible
    if hands:
        hand = hands[0]
        x, y, w, h = hand['bbox']        
        imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255
        imgCrop = img[y - offset:y + h + offset, x - offset:x + w + offset]
        imgCropShape = imgCrop.shape

        aspectRatio = h / w


        if aspectRatio > 1:
            k = imgSize / h
            wCal = math.ceil(k * w)
            imgResize = cv2.resize(imgCrop, (wCal, imgSize))
            imgResizeShape = imgResize.shape
            wGap = math.ceil((imgSize - wCal) / 2)
            imgWhite[:, wGap:wCal + wGap] = imgResize
        else:
            k = imgSize / w
            hCal = math.ceil(k * h)
            imgResize = cv2.resize(imgCrop, (imgSize, hCal))
            imgResizeShape = imgResize.shape
            hGap = math.ceil((imgSize - hCal) / 2)
            imgWhite[hGap:hCal + hGap, :] = imgResize

        # cv2.imshow("ImageCrop", imgCrop)
        cv2.imshow("ImageWhite", imgWhite)

    cv2.imshow("Image", img)

    count = {
        'one': len(os.listdir(folder + "1")),
        'two': len(os.listdir(folder + "2")),
        'three': len(os.listdir(folder + "3")),
        'four': len(os.listdir(folder + "4")),
        'five': len(os.listdir(folder + "5")),
        'six': len(os.listdir(folder + "6")),
        'seven': len(os.listdir(folder + "7")),
        'eight': len(os.listdir(folder + "8")),
        'nine': len(os.listdir(folder + "9")),

        # ----------Making Alphabet Directory---------
        'a': len(os.listdir(folder + "A")),
        'b': len(os.listdir(folder + "B")),
        'c': len(os.listdir(folder + "C")),
        'd': len(os.listdir(folder + "D")),
        'e': len(os.listdir(folder + "E")),
        'f': len(os.listdir(folder + "F")),
        'g': len(os.listdir(folder + "G")),
        'h': len(os.listdir(folder + "H")),
        'i': len(os.listdir(folder + "I")),
        'j': len(os.listdir(folder + "J")),
        'k': len(os.listdir(folder + "K")),
        'l': len(os.listdir(folder + "L")),
        'm': len(os.listdir(folder + "M")),
        'n': len(os.listdir(folder + "N")),
        'o': len(os.listdir(folder + "O")),
        'p': len(os.listdir(folder + "P")),
        'q': len(os.listdir(folder + "Q")),
        'r': len(os.listdir(folder + "R")),
        's': len(os.listdir(folder + "S")),
        't': len(os.listdir(folder + "T")),
        'u': len(os.listdir(folder + "U")),
        'v': len(os.listdir(folder + "V")),
        'w': len(os.listdir(folder + "W")),
        'x': len(os.listdir(folder + "X")),
        'y': len(os.listdir(folder + "Y")),
        'z': len(os.listdir(folder + "Z"))
    }


    # Save Image data set A - Z through keybpard keys 
    key = cv2.waitKey(1)
    if key == ord('a'):
        cv2.imwrite(folder+'A/'+str(count['a'])+'.jpg', imgWhite)
        print(count['a'])
    elif key == ord("b"):
        cv2.imwrite(folder + 'B/ '+str(count['b'])+'.jpg', imgWhite)
        print(count['b'])
    elif key == ord("c"):
        cv2.imwrite(folder + 'C/'+str(count['c'])+'.jpg', imgWhite)
        print(count['c'])
    elif key == ord("d"):
        cv2.imwrite(folder + 'D/'+str(count['d'])+'.jpg', imgWhite)
        print(count['d'])
    elif key == ord("e"):
        cv2.imwrite(folder + 'E/'+str(count['e'])+'.jpg', imgWhite)
        print(count['e'])
    elif key == ord("f"):
        cv2.imwrite(folder + 'F/'+str(count['f'])+'.jpg', imgWhite)
        print(count['f'])
    elif key == ord("g"):
        cv2.imwrite(folder + 'G/'+str(count['g'])+'.jpg', imgWhite)
        print(count['g'])
    elif key == ord("h"):
        cv2.imwrite(folder + 'H/'+str(count['h'])+'.jpg', imgWhite)
        print(count['h'])
    elif key == ord("i"):
        cv2.imwrite(folder + 'I/'+str(count['i'])+'.jpg', imgWhite)
        print(count['i'])
    elif key == ord("j"):
        cv2.imwrite(folder + 'J/'+str(count['j'])+'.jpg', imgWhite)
        print(count['j'])
    elif key == ord("k"):
        cv2.imwrite(folder + 'K/'+str(count['k'])+'.jpg', imgWhite)
        print(count['k'])
    elif key == ord("l"):
        cv2.imwrite(folder + 'L/'+str(count['l'])+'.jpg', imgWhite)
        print(count['l'])
    elif key == ord("m"):
        cv2.imwrite(folder + 'M/'+str(count['m'])+'.jpg', imgWhite)
        print(count['m'])
    elif key == ord("n"):
        cv2.imwrite(folder + 'N/'+str(count['n'])+'.jpg', imgWhite)
        print(count['n'])
    elif key == ord("o"):
        cv2.imwrite(folder + 'O/'+str(count['o'])+'.jpg', imgWhite)
        print(count['o'])
    elif key == ord("p"):
        cv2.imwrite(folder + 'P/'+str(count['p'])+'.jpg', imgWhite)
        print(count['p'])
    elif key == ord("q"):
        cv2.imwrite(folder + 'Q/'+str(count['q'])+'.jpg', imgWhite)
        print(count['q'])
    elif key == ord("r"):
        cv2.imwrite(folder + 'R/'+str(count['r'])+'.jpg', imgWhite)
        print(count['r'])
    elif key == ord("s"):
        cv2.imwrite(folder + 'S/'+str(count['s'])+'.jpg', imgWhite)
        print(count['s'])
    elif key == ord("t"):
        cv2.imwrite(folder + 'T/'+str(count['t'])+'.jpg', imgWhite)
        print(count['t'])
    elif key == ord("u"):
        cv2.imwrite(folder + 'U/'+str(count['u'])+'.jpg', imgWhite)
        print(count['u'])
    elif key == ord("v"):
        cv2.imwrite(folder + 'V/'+str(count['v'])+'.jpg', imgWhite)
        print(count['v'])
    elif key == ord("w"):
        cv2.imwrite(folder + 'W/'+str(count['w'])+'.jpg', imgWhite)
        print(count['w'])
    elif key == ord("x"):
        cv2.imwrite(folder + 'X/'+str(count['x'])+'.jpg', imgWhite)
        print(count['x'])
    elif key == ord("y"):
        cv2.imwrite(folder + 'Y/'+str(count['y'])+'.jpg', imgWhite)
        print(count['y'])
    elif key == ord("z"):
        cv2.imwrite(folder + 'Z/'+str(count['z'])+'.jpg', imgWhite)
        print(count['z'])

# -------------Numbers from 1 - 9-------------------
    elif key == ord('1'):
        cv2.imwrite(folder + '1/'+str(count['one'])+'.jpg', imgWhite)
        print(count['one'])
    elif key == ord("2"):
        cv2.imwrite(folder + '2/'+str(count['two'])+'.jpg', imgWhite)
        print(count['two'])
    elif key == ord("3"):
        cv2.imwrite(folder + '3/'+str(count['three'])+'.jpg', imgWhite)
        print(count['three'])
    elif key == ord("4"):
        cv2.imwrite(folder + '4/'+str(count['four'])+'.jpg', imgWhite)
        print(count['four'])
    elif key == ord("5"):
        cv2.imwrite(folder + '5/'+str(count['five'])+'.jpg', imgWhite)
        print(count['five'])
    elif key == ord("6"):
        cv2.imwrite(folder + '6/'+str(count['six'])+'.jpg', imgWhite)
        print(count['six'])
    elif key == ord("7"):
        cv2.imwrite(folder + '7/'+str(count['seven'])+'.jpg', imgWhite)
        print(count['seven'])
    elif key == ord("8"):
        cv2.imwrite(folder + '8/'+str(count['eight'])+'.jpg', imgWhite)
        print(count['eight'])
    elif key == ord("9"):
        cv2.imwrite(folder + '9/'+str(count['nine'])+'.jpg', imgWhite)
        print(count['nine'])

    elif key == 27:  # 27 is the ASCII value for 'Esc' key
        cap.release()
        cv2.destroyAllWindows()
