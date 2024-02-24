import cv2
facecap=cv2.cascadeclassifier("cascade file ka path")
vidcap=cv2.VideoCapture(0)
while True:
    ret, viddata=vidcap.read()
    col=cv2.cvtColor(viddata, cv2.color_bgr2gray)
    faces=facecap.detectmultiscale(
        col,
        scalefactor=1.1,
        minneighbours=5,
        minsize=(30,30),
        flags=cv2.cascade_scale_image
    )
    for (x,y,w,h) in faces:
        cv2.rectangle(viddata,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow("live",viddata)
    if cv2.waitkey(5)== ord("a"):
        break
vidcap.release()