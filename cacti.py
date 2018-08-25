import tftDriver
import display
import flash
import cv2

drivers = tftDriver.getTftDrivers()
flash_driver = flash.getFlash()
cacti = []

for i in range(6):
  cacti.append( cv2.imread("./pics/" + str(i+1) + ".jpg") )


k = 0
display.showImg(cacti[k])
k = k + 1

for driver in drivers

  for j in range(driver.tft_count):
    driver.showImg(j, cacti[k])
    k = k + 1

