import picamera
import picamera.array
import cv2
with picamera.PiCamera() as camera:
    with picamera.array.PiRGBArray(camera) as stream:
        camera.resolution=(640,480)
        camera.framerate=15
        camera.awb_mode='fluorescent'
        while True:
            camera.capture(stream,'bgr',use_video_port=True)
#             cv2.rectangle(stream.array,
#               pt1=(250, 200),
#               pt2=(300, 250),
#               color=(200, 150, 40),
#               thickness=7,
#               lineType=cv2.LINE_4,
#               shift=0)
#             cv2.imshow('frame',stream.array)
#             if cv2.waitKey(1) & 0xFF == ord('q'):
#                 break
#             stream.seek(0)
#             stream.truncate()
#         cv2.destroyAllWindows()
            cv2.circle(stream.array,
                center=(320,240),
                radius=100,
                color=(0,255,0),
                thickness=3,
                lineType=cv2.LINE_4,
                shift=0)
            cv2.imshow('frame',stream.array)
            cv2.circle(stream.array,
                center=(250,250),
                radius=30,
                color=(200,150,75),
                thickness=3,
                lineType=cv2.LINE_4,
                shift=0)
            cv2.imshow('frame',stream.array)
            cv2.circle(stream.array,
                center=(320,250),
                radius=40,
                color=(200,150,75),
                thickness=3,
                lineType=cv2.LINE_4,
                shift=0)
            cv2.imshow('frame',stream.array)
            cv2.circle(stream.array,
                center=(390,250),
                radius=30,
                color=(200,150,75),
                thickness=3,
                lineType=cv2.LINE_4,
                shift=0)
            cv2.imshow('frame',stream.array)
  
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            stream.seek(0)
            stream.truncate()
        cv2.destroyAllWindows()