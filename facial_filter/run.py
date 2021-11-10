from os import makedirs
from types import DynamicClassAttribute
import cv2
import mediapipe as mp
import pyvirtualcam
import numpy as np



lips = [(61, 146),
    (146, 91),
    (91, 181),
    (181, 84),
    (84, 17),
    (17, 314),
    (314, 405),
    (405, 321),
    (321, 375),
    (375, 291),
    (61, 185),
    (185, 40),
    (40, 39),
    (39, 37),
    (37, 0),
    (0, 267),
    (267, 269),
    (269, 270),
    (270, 409),
    (409, 291),
    (78, 95),
    (95, 88),
    (88, 178),
    (178, 87),
    (87, 14),
    (14, 317),
    (317, 402),
    (402, 318),
    (318, 324),
    (324, 308),
    (78, 191),
    (191, 80),
    (80, 81),
    (81, 82),
    (82, 13),
    (13, 312),
    (312, 311),
    (311, 310),
    (310, 415),
    (415, 308),
    ]


left_eyebrow = [
    (276, 283),
    (283, 282),
    (282, 295),
    (295, 285),
    (300, 293),
    (293, 334),
    (334, 296),
    (296, 336),
]

right_eye = [
        (33, 7),
    (7, 163),
    (163, 144),
    (144, 145),
    (145, 153),
    (153, 154),
    (154, 155),
    (155, 133),
    (33, 246),
    (246, 161),
    (161, 160),
    (160, 159),
    (159, 158),
    (158, 157),
    (157, 173),
    (173, 133),
]

"""
# Left eyebrow.
    (276, 283),
    (283, 282),
    (282, 295),
    (295, 285),
    (300, 293),
    (293, 334),
    (334, 296),
    (296, 336),
    # Right eye.
    (33, 7),
    (7, 163),
    (163, 144),
    (144, 145),
    (145, 153),
    (153, 154),
    (154, 155),
    (155, 133),
    (33, 246),
    (246, 161),
    (161, 160),
    (160, 159),
    (159, 158),
    (158, 157),
    (157, 173),
    (173, 133),
    # Right eyebrow.
    (46, 53),
    (53, 52),
    (52, 65),
    (65, 55),
    (70, 63),
    (63, 105),
    (105, 66),
    (66, 107),
    # Face oval.
    (10, 338),
    (338, 297),
    (297, 332),
    (332, 284),
    (284, 251),
    (251, 389),
    (389, 356),
    (356, 454),
    (454, 323),
    (323, 361),
    (361, 288),
    (288, 397),
    (397, 365),
    (365, 379),
    (379, 378),
    (378, 400),
    (400, 377),
    (377, 152),
    (152, 148),
    (148, 176),
    (176, 149),
    (149, 150),
    (150, 136),
    (136, 172),
    (172, 58),
    (58, 132),
    (132, 93),
    (93, 234),
    (234, 127),
    (127, 162),
    (162, 21),
    (21, 54),
    (54, 103),
    (103, 67),
    (67, 109),
    (109, 10)
"""

# INITIALIZING OBJECTS
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_face_mesh = mp.solutions.face_mesh
mp_hands = mp.solutions.hands

drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280) # カメラ画像の横幅を1280に設定
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720) 
success, image = cap.read()



cam = pyvirtualcam.Camera(width=image.shape[1], height=image.shape[0], fps=30)

# DETECT THE FACE LANDMARKS
with mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5) as face_mesh:
  while True:
    success, image = cap.read()
    # cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280) # カメラ画像の横幅を1280に設定
    # cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720) # カメラ画像の縦幅を720に設定
    # Flip the image horizontally and convert the color space from BGR to RGB
    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)

    # To improve performance
    image.flags.writeable = False
    gray = np.zeros((image.shape[0], image.shape[1], 3), dtype=np.uint8)
    
    # Detect the face landmarks
    results = face_mesh.process(image)

    
    # To improve performance
    image.flags.writeable = True

    # Convert back to the BGR color space
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    
    # Draw the face mesh annotations on the image.
    if results.multi_face_landmarks:
      for face_landmarks in results.multi_face_landmarks:
        # mp_drawing.draw_landmarks(
        #     image=image,
        #     landmark_list=face_landmarks,
        #     connections=mp_face_mesh.FACEMESH_TESSELATION,
        #     landmark_drawing_spec=None,
        #     connection_drawing_spec=mp_drawing_styles
        #     .get_default_face_mesh_tesselation_style())
        
        # mp_drawing.draw_landmarks(
        #     image=gray,
        #     landmark_list=face_landmarks,
        #     connections=mp_face_mesh.FACEMESH_TESSELATION,
        #     landmark_drawing_spec=None,
        #     connection_drawing_spec=mp_drawing_styles
        #     .get_default_face_mesh_tesselation_style())
        
        # mp_drawing.draw_landmarks(
        #     image=gray,
        #     landmark_list=face_landmarks,
        #     connections=mp_face_mesh.FACEMESH_CONTOURS,
        #     landmark_drawing_spec=None,
        #     connection_drawing_spec=mp_drawing_styles
        #     .get_default_face_mesh_contours_style())
        

        
        # mp_drawing.draw_landmarks(
        #     image=image,
        #     landmark_list=face_landmarks,
        #     connections=lips,
        #     landmark_drawing_spec=None,
        #     connection_drawing_spec=mp_drawing_styles
        #     .get_default_face_mesh_contours_style())
        
            ref = np.array([u for u in range(468)])
                    
            
            tmp = []
            # for i in np.ravel(right_eye):
            # for i in np.ravel(lips):
            for i in range(468):
                # print(face_landmarks.landmark[i])
                    pt1 = face_landmarks.landmark[i]
                    x = int(pt1.x * 1280)
                    y = int(pt1.y * 720)                    
                    tmp.append((x,y))
            convexhull  = cv2.convexHull(np.array(tmp))
            mask = cv2.fillConvexPoly(gray, convexhull, ((124, 150, 206)))
            # mask = cv2.fillConvexPoly(gray, convexhull, ((29, 30, 100)))
            mask = cv2.GaussianBlur(mask, (7, 7), 20)
            

            # exit()    
   
    # if h_results.multi_hand_landmarks:
    #     for hand_landmarks in h_results.multi_hand_landmarks:
    #         mp_drawing.draw_landmarks(
    #       gray,
    #       hand_landmarks,
    #       mp_hands.HAND_CONNECTIONS,
    #       mp_drawing_styles.get_default_hand_landmarks_style(),
    #       mp_drawing_styles.get_default_hand_connections_style())
            
        # mp_drawing.draw_landmarks(
        #     image=image,
        #     landmark_list=face_landmarks,
        #     connections=mp_face_mesh.FACEMESH_IRISES,
        #     landmark_drawing_spec=None,
        #     connection_drawing_spec=mp_drawing_styles
        #     .get_default_face_mesh_iris_connections_style())


    
    # Display the image
    # cam.send(gray)
    # cam.sleep_until_next_frame()
    # cam.sleep_until_next_frame()
    
    # test = cv2.bitwise_and(gray, image)
    
    resulting_image = cv2.addWeighted(mask, 0.05, image, 1, 0.)
    
    cv2.imshow('MediaPipe FaceMesh', resulting_image)
    cv2.imshow('Mask', mask)
    
    # Terminate the process
    if cv2.waitKey(5) & 0xFF == 27:
      break

cap.release()

import numpy as np

# with pyvirtualcam.Camera(width=1280, height=720, fps=30) as cam:
# while True:
#     frame = np.zeros((cam.height, cam.width, 4), np.uint8) # RGBA
#     frame[:,:,:3] = cam.frames_sent % 255 # grayscale animation
#     frame[:,:,3] = 255
#     cam.send(frame[:,:,:3])
#     cam.sleep_until_next_frame()
#     cam.sleep_until_next_frame()