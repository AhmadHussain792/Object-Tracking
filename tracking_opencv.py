# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import cv2
import sys
import tkinter as tk
from tkinter import messagebox

root=tk.Tk()
root.withdraw()
video = cv2.VideoCapture(0)

if not video.isOpened():
    messagebox.showerror("ERROR", "Video not found")
    root.destroy()
    sys.exit()

#skip the first 10 frames of the video, if the webcam takes longer to adjust completely to the lighting and brighten up
for i in range(10):
    ok, frame = video.read()
    if not ok:
        messagebox.showerror("ERROR", "Could not read the file")
        root.destroy()
        video.release()
        sys.exit()

ok, frame = video.read()
if not ok:
    messagebox.showerror("ERROR", "Video not found")
    video.release()
    root.destroy()
    sys.exit()

bbox = cv2.selectROI(frame, False)
tracker = cv2.TrackerCSRT_create()
ok = tracker.init(frame, bbox)

while True:
    ok, frame = video.read()
    if not ok:
        messagebox.showerror("ERROR", "There was an unexpected error")
        root.destroy()
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
        root.destroy()
        break

video.release()
cv2.destroyAllWindows()
