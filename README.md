# mediapipe_pose
Two programs (pose.py and posexy.py) are disclosed.

In order to run the programs, you should install mediapipe by:

$ pip install mediapipe


If you have a problem: 

DLL load failed while importing _framework_binding

Run the following command on Windows 10.

$ pip install msvc-runtime

Both programs can show landmarks of a human body.

pose landmarks composed of 33 points are as follows:
<img src='https://github.com/ytakefuji/mediapipe_pose/blob/main/pose_tracking_full_body_landmarks.png' width=772 heigh=438>

source:https://google.github.io/mediapipe/images/mobile/pose_tracking_full_body_landmarks.png

# pose.py
pose.py is a program to show 33 points of pose landmarks.

# posexy.py
posexy.py is a program to show 33 points of pose landmarks 
where nose coordinate(x,y) is displayed on the screen.
