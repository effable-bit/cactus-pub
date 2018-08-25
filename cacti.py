import tftDriver
import display
import flash
import cv2
import time

drivers = tftDriver.getTftDrivers()
flash_driver = flash.getFlash()
cacti = []

for i in range(6):
  cacti.append( cv2.imread("/home/pi/Development/Cactus/pics/" + str(i+1) + ".jpg") )


k = 0
display.showImg(cacti[k])
k = k + 1

for driver in drivers:

  for j in range(driver.tft_count):
    driver.showImg(j, cacti[k])
    k = k + 1

k = 1
for driver in drivers:

  for j in range(driver.tft_count):
    driver.showImg(j, cacti[k])
    k = k + 1

while True:
  time.sleep(1000000);