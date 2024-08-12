# Object-Tracking
This Python script performs video tracking using OpenCV's CSRT tracker. It captures video from the webcam, allows the user to select a Region of Interest (ROI) for tracking, and then tracks the object within the selected ROI in real-time. 

# Features
Real-time Object Tracking: Uses OpenCV's CSRT tracker to track objects within a selected ROI in real-time.

Error Handling: Displays error messages using Tkinter's 'messagebox' if the video cannot be accessed or if there are any issues during processing.

# Requirements
+ Python version 3.7 or higher
+ more details can be found in "REQUIREMENTS.TXT" file

# How to use
1. clone this repository and run the python script.
2. once the video feed opens, select the Region Of Interest by drawing a rectangle and press 'Enter'.
3. The script will start tracking the object within the selected ROI
4. Press 'Esc' key to exit the tracking and close the application

# Code Overview
Initializing Tkinter and opening the webcam feed

![image](https://github.com/user-attachments/assets/7516d8ff-0544-4e1d-8ed4-7d8aa5d43074)

`video = cv2.VideoCapture(0)`: the 0 argument specifies that the built-in webcam is being used


Error Hnadling:

if the video feed cannot be opened or if the script cannot read the video frames

![image](https://github.com/user-attachments/assets/ff7564d4-43d4-4987-9292-84728a1216ae)

`video.isOpened()`: returns a boolean value depending on whether the video feed is open or not 

![image](https://github.com/user-attachments/assets/675db761-67cb-4791-8621-cfaf690adc78)

`video.read()`: returns 2 values, the first one is a boolean that indicates whether the frame was successful or not. The second value is an image (frame) in the form of a NumPy array


Tracking:

The user selects the ROI, and the script tracks the object within the selected ROI

![image](https://github.com/user-attachments/assets/6740f8d5-1b65-4178-9a99-aa42d1af8f73)


Displaying the Tracking Results:

The script draws a rectangle around the tracked object or displays a failure message if tracking fails:

![image](https://github.com/user-attachments/assets/4bcaf0f4-28ad-4140-a90b-317daea01ffa)


The application closes when the 'Esc' key is pressed:

![image](https://github.com/user-attachments/assets/311c3e76-b1bb-4426-8317-8902f572c019)

`cv2.waitKey(1)`: waits for 1 millisecond for a key press and retunrs ASCII code of the key

`'& 0xFF'`: ensures that only the lower 8 bits of the key code are kept, making the key press value compatible across different platforms.
