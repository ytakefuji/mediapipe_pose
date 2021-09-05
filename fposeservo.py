import cv2
import mediapipe as mp
import pyfirmata
b=pyfirmata.Arduino('COM3')
it = pyfirmata.util.Iterator(b)
it.start()
pin = b.get_pin('d:2:s')
#b.digital[2].write(0)
pin.write(90)

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

cap = cv2.VideoCapture(0)
pose= mp_pose.Pose(
    min_detection_confidence=0.8,
    min_tracking_confidence=0.8)

while True:
    success, image = cap.read()
    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
    image.flags.writeable = False
    results = pose.process(image)
    if results.pose_landmarks:
     landmarks = []
     for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = image.shape 
            cx, cy = int(lm.x * w), int(lm.y * h) 
            landmarks.append((cx,cy))    
    else: continue
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    mp_drawing.draw_landmarks(
        image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
    nose=landmarks[0][0]
    nose=nose-150
    if nose<1:nose=1
    if nose>180:nose=180
    cv2.putText(image, "nose="+str(nose), (85, 125), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 5)
    pin.write(nose)
    cv2.imshow('MediaPipe Pose', image)
    if cv2.waitKey(1) == ord('q'):
      break
cap.release()
cv2.destroyAllWindows()
