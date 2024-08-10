# -*- coding: utf-8 -*-
import cv2
import sys

video = cv2.VideoCapture(0)

if not video.isOpened():
    print("Error: Video not found")
    sys.exit()
 
for i in range(10):
    ok, frame = video.read()
    if not ok:
        print('Cannot read video file')
        video.release()
        sys.exit()

ok, frame = video.read()
if not ok:
    print('Error: Video not found')
    video.release()
    sys.exit()

bbox = cv2.selectROI(frame, False)
tracker = cv2.TrackerCSRT_create()
ok = tracker.init(frame, bbox)

while True:
    ok, frame = video.read()
    if not ok:
        print("There was an error")
        break
        
    ok, bbox = tracker.update(frame)
        
    if ok:
        p1 = (int(bbox[0]), int(bbox[1]))
        p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
        cv2.rectangle(frame, p1, p2, (255, 255, 0), 2, 1)
    else:
        cv2.putText(frame, "Tracking failure detected", (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)
            
    cv2.imshow("tracking", frame)
    
    k = cv2.waitKey(1) & 0xff
    if k == 27:
        video.release()
        cv2.destroyAllWindows()
        break
