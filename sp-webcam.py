import cv2
import streamlit as st
from datetime import datetime


def fps_count(frame_counter_, start_time_):
    current_time = datetime.now()
    elapsed_time = current_time - start_time_
    fps_ = 0
    if elapsed_time.seconds > 0:
        fps_ = float(frame_counter_) / float(elapsed_time.seconds)
    return round(fps_)


st.title("Motion Detector")
start = st.button("Start Camera")

if start:
    streamlit_image = st.image([])
    camera = cv2.VideoCapture(0)

    start_time = datetime.now()
    frame_counter = 0

    while True:
        check, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        fps = fps_count(frame_counter, start_time)
        now = datetime.now()
        day = now.strftime('%A')
        time_str = now.strftime('%H:%M:%S')

        cv2.putText(img=frame, text=f"FPS {fps}", org=(50, 50), fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2,
                    color=(100, 20, 200), thickness=2, lineType=cv2.LINE_AA)
        cv2.putText(img=frame, text=f"{day}", org=(50, 80), fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2,
                    color=(255, 255, 200), thickness=2, lineType=cv2.LINE_AA)
        cv2.putText(img=frame, text=f"{time_str}", org=(50, 110), fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2,
                    color=(255, 20, 20), thickness=2, lineType=cv2.LINE_AA)

        streamlit_image.image(frame)
        frame_counter += 1
