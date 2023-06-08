# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import cv2
import time
import pandas as pd

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
def computer_rizzion(df):
    start_time = time.time()
    cap = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml')

    while True:
        ret, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        current_time = time.time() - start_time

        for (x, y, w, h) in faces:
            detected_entry = pd.DataFrame({
                'face_detected': 1,
                'fd_time': current_time
            }, index=[len(df)])
            df = pd.concat([df, detected_entry], ignore_index=True)

            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 5)
            # for (ex, ey, ew, eh) in eyes:
            #     cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 5)
            print(len(df))
        cv2.imshow('frame', frame)

        undetected_entry = pd.DataFrame({
            'face_detected': 0,
            'fd_time': current_time
        }, index=[len(df)])
        df = pd.concat([df,undetected_entry], ignore_index=True)

        if current_time >= 3600:
            break
        if cv2.waitKey(1) == ord('q'):
            break


    cap.release()
    cv2.destroyAllWindows()
    return df
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    friedBrain_df = pd.DataFrame(columns=['face_detected','eyes_detected', 'fd_time', 'ed_time'])
    computer_rizzion(friedBrain_df).to_csv('distractedBrain_df.csv',index=False)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
