
import cv2
import numpy as np

cap1 = cv2.VideoCapture('1.mp4')
cap2 = cv2.VideoCapture('2.mp4')
cap3 = cv2.VideoCapture('3.mp4')
cap4 = cv2.VideoCapture('4.mp4')
len = []

len.append(int(cap1.get(cv2.CAP_PROP_FRAME_COUNT)))
len.append(int(cap2.get(cv2.CAP_PROP_FRAME_COUNT)))
len.append(int(cap3.get(cv2.CAP_PROP_FRAME_COUNT)))
len.append(int(cap4.get(cv2.CAP_PROP_FRAME_COUNT)))
print (len)

lim= max(len)

print(lim)
"""
cap1 = cv2.VideoCapture('/content/drive/MyDrive/Headless_sample_video/1.mp4')
cap2 = cv2.VideoCapture('/content/drive/MyDrive/Headless_sample_video/2.mp4')
cap3 = cv2.VideoCapture('/content/drive/MyDrive/Headless_sample_video/3.mp4')
cap4 = cv2.VideoCapture('/content/drive/MyDrive/Headless_sample_video/4.mp4')

"""



count = 0
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
#out = cv2.VideoWriter('o1.mp4', fourcc, 25.0, (1920,1080))


if cap1.isOpened() == False:
    print("Error opening video stream or file")

# Concate video
def concat_vh(list_2d):
    # return final image
    return cv2.vconcat([cv2.hconcat(list_h)
                        for list_h in list_2d])

# Read until video is completed
while (True):
    # Capture frame-by-frame
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()
    ret3, frame3 = cap3.read()
    ret4, frame4 = cap4.read()


    if ret1 or ret2 or ret3 or ret4 == True:
        # final= cv2.addWeighted( frame1, 0.5, frame2, 0.5 ,0)
        if ret4 != True :
            frame4=np.zeros(frame1.shape, dtype="uint8")
        if ret2 != True :
            frame2=np.zeros(frame1.shape, dtype="uint8")
        if ret3 != True :
            frame3=np.zeros(frame1.shape, dtype="uint8")

        final = concat_vh([[frame1, frame2],
                           [frame3, frame4]])
        final = cv2.resize(final, dsize=(0, 0), fx=0.5, fy=0.5)
        cv2.imshow('Frame', final)
        #out.write(final)
        count += 1

        # Display the resulting frame
    if count >= lim:
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the video capture object
cap1.release()
cap2.release()
cap3.release()
cap4.release()
# Closes all the frames
cv2.destroyAllWindows()
