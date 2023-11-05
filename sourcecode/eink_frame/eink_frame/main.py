from PIL import Image, ImageOps
from image_processing.image_processing import ImageProcessor


# Main function
if __name__ == "__main__":
    # Create an instance of the ImageProcessor class
    image_processor = ImageProcessor()

    image_name = input("Enter an image name: ")
    
    base_file_path = r'F:\EPAPERPROJ\frame_proj\e-Paper\RaspberryPi\python\pic\\' 

    full_file_path = base_file_path + image_name

    #open image
    image = Image.open(full_file_path)

    # Process the image using the ImageProcessor instance
    target_width = 600
    target_height = 448
    processed_image = image_processor.process_image(image, target_width, target_height)



