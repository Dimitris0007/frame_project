#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd5in65f
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG)

try:
    logging.info("epd5in65f Demo")
    
    #Initialize epd instance and clear screen
    epd = epd5in65f.EPD()

    logging.info("init and Clear")

    epd.init()
    epd.Clear()

    #font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
    # Drawing on the Horizontal image
    #logging.info("1.Drawing on the Horizontal image...")
    #Himage = Image.new('RGB', (epd.width, epd.height), 0xffffff)  # 255: clear the frame
    #draw = ImageDraw.Draw(Himage)
    #draw.text((10, 0), 'hello world', font = font24, fill = 0)
    #draw.text((10, 160), u'微雪电子', font = font30, fill = epd.BLACK)
    #epd.display(epd.getbuffer(Himage))
    #time.sleep(3)
    
    # Display the image
    logging.info("3.read bmp file")
    Himage = Image.open(os.path.join(picdir, 'new.bmp'))
    epd.display(epd.getbuffer(Himage))

    #go to sleep mode
    logging.info("Goto Sleep...")
    epd.sleep()
    
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd5in65f.epdconfig.module_exit()
    exit()
