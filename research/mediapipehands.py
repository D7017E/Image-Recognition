import cv2
import mediapipe as mp
import numpy as np

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

gesture = {
    0:'fist', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five',
    6:'six', 7:'rock', 8:'spiderman', 9:'yeah', 10:'ok',
}
rps_gesture = {0:'rock', 5:'paper', 9:'scissors'}


# Gesture recognition model
file = np.genfromtxt('C:/Image-Recognition/research/data/gesture_train.csv', delimiter=',')
angle = file[:,:-1].astype(np.float32)
label = file[:, -1].astype(np.float32)
knn = cv2.ml.KNearest_create()
knn.train(angle, cv2.ml.ROW_SAMPLE, label)



# For webcam input:
cap = cv2.VideoCapture(0)
with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    results = hands.process(image)

    # Draw the hand annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
      rps_result = []
      for hand_landmarks in results.multi_hand_landmarks:
        mp_drawing.draw_landmarks(
            image,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing_styles.get_default_hand_landmarks_style(),
            mp_drawing_styles.get_default_hand_connections_style())
        
        joint = np.zeros((21, 3))
        for j, lm in enumerate(hand_landmarks.landmark):
            joint[j] = [lm.x, lm.y, lm.z]

        # Compute angles between joints
        v1 = joint[[0,1,2,3,0,5,6,7,0,9,10,11,0,13,14,15,0,17,18,19],:] # Parent joint
        v2 = joint[[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],:] # Child joint
        v = v2 - v1 # [20,3]
        # Normalize v
        v = v / np.linalg.norm(v, axis=1)[:, np.newaxis]

        # Get angle using arcos of dot product
        angle = np.arccos(np.einsum('nt,nt->n',
            v[[0,1,2,4,5,6,8,9,10,12,13,14,16,17,18],:], 
            v[[1,2,3,5,6,7,9,10,11,13,14,15,17,18,19],:])) # [15,]

        angle = np.degrees(angle) # Convert radian to degree

        # Inference gesture
        data = np.array([angle], dtype=np.float32)
        ret, results, neighbours, dist = knn.findNearest(data, 3)
        idx = int(results[0][0])

        # Draw gesture result
        if idx in rps_gesture.keys():
            org = (int(hand_landmarks.landmark[0].x * image.shape[1]), int(hand_landmarks.landmark[0].y * image.shape[0]))
            cv2.putText(image, text=rps_gesture[idx].upper(), org=(org[0], org[1] + 20), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(255, 255, 255), thickness=2)

            rps_result.append({
                'rps': rps_gesture[idx],
                'org': org
            })

        mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        # Who wins?
        if len(rps_result) >= 2:
            winner = None
            text = ''

            if rps_result[0]['rps']=='rock':
                if rps_result[1]['rps']=='rock'     : text = 'Tie'
                elif rps_result[1]['rps']=='paper'  : text = 'Paper wins'  ; winner = 1
                elif rps_result[1]['rps']=='scissors': text = 'Rock wins'   ; winner = 0
            elif rps_result[0]['rps']=='paper':
                if rps_result[1]['rps']=='rock'     : text = 'Paper wins'  ; winner = 0
                elif rps_result[1]['rps']=='paper'  : text = 'Tie'
                elif rps_result[1]['rps']=='scissors': text = 'Scissors wins'; winner = 1
            elif rps_result[0]['rps']=='scissors':
                if rps_result[1]['rps']=='rock'     : text = 'Rock wins'   ; winner = 1
                elif rps_result[1]['rps']=='paper'  : text = 'Scissors wins'; winner = 0
                elif rps_result[1]['rps']=='scissors': text = 'Tie'

            if winner is not None:
                cv2.putText(image, text='Winner', org=(rps_result[winner]['org'][0], rps_result[winner]['org'][1] + 70), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=2, color=(0, 255, 0), thickness=3)
            cv2.putText(image, text=text, org=(int(image.shape[1] / 2), 100), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=2, color=(0, 0, 255), thickness=3)
        
        
    # Flip the image horizontally for a selfie-view display.
    cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()