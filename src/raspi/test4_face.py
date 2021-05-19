import picamera
import picamera.array
import cv2

face_cascade_path = '/home/pi/face/model/opencv-master/data/haarcascades/haarcascade_frontalface_default.xml'

face_cascade = cv2.CascadeClassifier(face_cascade_path)

with picamera.PiCamera() as camera:
    with picamera.array.PiRGBArray(camera) as stream:
        camera.resolution=(320,240)
        camera.framerate=15
        camera.awb_mode='fluorescent'
        while True:
            camera.capture(stream,'bgr',use_video_port=True)
            #cv2.imshow('frame',stream.array)
            src_gray = cv2.cvtColor(stream.array, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(src_gray)
            for x, y, w, h in faces:
                cv2.rectangle(stream.array, (x, y), (x + w, y + h), (255, 0, 0), 2)
                cv2.circle(
                    stream.array,
                    center=(x+w/2,y+h/2),
                    radius=(w+h)/2,
                    color=(0,255,0),
                    thickness=3,
                    lineType=cv2.LINE_4,
                    shift=0)
            cv2.imshow('face',stream.array)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            stream.seek(0)
            stream.truncate()
        cv2.destroyAllWindows()
