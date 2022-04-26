import cv2
import mediapipe as mp


v_path = "./demo.mkv"

video = cv2.VideoCapture(v_path)

while True:
    key = cv2.waitKey(1)
    if key == 27:
        break
    
    ret, frame = video.read()
    
    if not ret:
        break




    cv2.imwrite("./demo.png", frame)
    break
    cv2.imshow("test", frame)




cv2.destroyAllWindows()
video.release()