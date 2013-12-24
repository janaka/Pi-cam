import time
import picamera

with picamera.Picamera() as camera:
    camera.resolution = (1280, 720)
    camera.start_preview()
    camera.exposure_compensation = 2
    camera.exposure_mode = 'spotlight'
    camera.meter_mode = 'matrix'
    camera.image_effect = 'gpen'
    time.sleep(2)
    camera.capture('foo.jpeg')
    camera.stop_preview()
    
    
