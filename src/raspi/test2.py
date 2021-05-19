import picamera
import picamera.array
import cv2
import numpy as np
with picamera.PiCamera() as camera:
	with picamera.array.PiRGBArray(camera) as stream:
		camera.resolution=(320,240)
		camera.framerate=30
		camera.awb_mode='fluorescent'
		while True:
			camera.capture(stream,'bgr',use_video_port=True)
			img = cv2.rotate(stream.array, cv2.ROTATE_180)
			cv2.imshow('frame',img)
			hsvLower = np.array([105, 10, 10])
			hsvUpper = np.array([110, 245, 245])
			hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
			blue_mask = cv2.inRange(hsv, hsvLower, hsvUpper) 
			blue = cv2.bitwise_and(img, img, mask=blue_mask)
			cv2.imshow('blue',blue)
			if cv2.waitKey(1) & 0xFF == ord('q'):
				break
			stream.seek(0)
			stream.truncate()
		cv2.destroyAllWindows()