#!/usr/bin/python3

# Normally the QtGlPreview implementation is recommended as it benefits
# from GPU hardware acceleration.

import time
import numpy as np
from picamera2 import Picamera2
import matplotlib.pyplot as plt
import libcamera
import numba

picam2 = Picamera2()

preview_config = picam2.create_preview_configuration(main={"format": 'BGR888','size':(1920,1080)})
preview_config["transform"] = libcamera.Transform(hflip=1, vflip=1)
picam2.configure(preview_config)

picam2.start()

img = picam2.capture_array()
print(img.shape)
plt.imshow(img)
plt.show()