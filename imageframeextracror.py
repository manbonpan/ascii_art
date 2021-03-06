import os
folder = 'cruelangel'  
os.mkdir(folder)
# use opencv to do the job
import cv2
vidcap = cv2.VideoCapture('videoplayback.webm')
count = 0
while True:
    success,image = vidcap.read()
    if not success:
        break
    cv2.imwrite(os.path.join(folder,"frame{:d}.jpg".format(count)), image)     # save frame as JPEG file
    count += 1
print("{} images are extacted in {}.".format(count,folder))
