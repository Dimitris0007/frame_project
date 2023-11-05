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

from image_processing.image_processing import ImageProcessor

# Main function
if __name__ == "__main__":
    # Create an instance of the ImageProcessor class
    image_processor = ImageProcessor()

    # Get the user input for the filename
    user_input = input("Enter the filename (e.g., 'dimi.JPEG'): ")

    # Define the 'pic' folder path manually with single backslashes
    pic_folder = r'/home/pi/frame_project/pic/'

    # Combine the 'pic' folder path with the user input to create the full file path
    full_file_path = pic_folder + user_input

    # Open the image using the full file path
    image = Image.open(full_file_path)

    # Process the image using the ImageProcessor instance
    target_width = 600
    target_height = 448
    processed_image = image_processor.process_image(image, target_width, target_height)


    logging.basicConfig(level=logging.DEBUG)
    
    try:
        logging.info("epd5in65f Demo")
    
        #Initialize epd instance and clear screen
        epd = epd5in65f.EPD()

        logging.info("init and Clear")

        epd.init()
        epd.Clear()
    
        # Display the image
        logging.info("3.read bmp file")
        #Himage = Image.open(os.path.join(picdir, 'new.bmp'))
        epd.display(epd.getbuffer(processed_image))

        #go to sleep mode
        logging.info("Goto Sleep...")
        epd.sleep()
    
    except IOError as e:
        logging.info(e)
    
    except KeyboardInterrupt:    
        logging.info("ctrl + c:")
        epd5in65f.epdconfig.module_exit()
        exit()
