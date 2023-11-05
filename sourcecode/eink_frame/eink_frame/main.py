from PIL import Image
from image_processing.image_processing import ImageProcessor


# Main function
if __name__ == "__main__":
    # Create an instance of the ImageProcessor class
    image_processor = ImageProcessor()

    #open image
    image = Image.open(r'F:\EPAPERPROJ\frame_proj\e-Paper\RaspberryPi\python\pic\dimi.JPEG')

    # Process the image using the ImageProcessor instance
    target_width = 600
    target_height = 448
    processed_image = image_processor.process_image(image, target_width, target_height)



