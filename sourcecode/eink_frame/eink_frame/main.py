from PIL import Image, ImageOps
from image_processing.image_processing import ImageProcessor
import os


# Main function
if __name__ == "__main__":
    # Create an instance of the ImageProcessor class
    image_processor = ImageProcessor()

    # Get the user input for the filename
    user_input = input("Enter the filename (e.g., 'dimi.JPEG'): ")

    # Define the 'pic' folder path manually with single backslashes
    pic_folder = r'F:\EPAPERPROJ\frame_proj\e-Paper\RaspberryPi\python\pic'

    # Combine the 'pic' folder path with the user input to create the full file path
    full_file_path = os.path.join(pic_folder, user_input)

    # Open the image using the full file path
    image = Image.open(full_file_path)

    # Process the image using the ImageProcessor instance
    target_width = 600
    target_height = 448
    processed_image = image_processor.process_image(image, target_width, target_height)



