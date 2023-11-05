from PIL import Image


def floyd_steinberg_dithering(image, palette):
    # Create a copy of the original image
    dithered_image = image.copy()

    width, height = dithered_image.size

    for y in range(1, height - 1):
        for x in range(1, width - 1):
            old_pixel = dithered_image.getpixel((x, y))
            new_pixel = find_closest_palette_color(old_pixel, palette)
            dithered_image.putpixel((x, y), new_pixel)

            quant_error = tuple(map(lambda a, b: a - b, old_pixel, new_pixel))

            for dx, dy, factor in ((1, 0, 7/16), (-1, 1, 3/16), (0, 1, 5/16), (1, 1, 1/16)):
                neighbor_x, neighbor_y = x + dx, y + dy
                neighbor_pixel = dithered_image.getpixel((neighbor_x, neighbor_y))
                adjusted_pixel = tuple(
                    int(neighbor_channel + quant_error_channel * factor)
                    for neighbor_channel, quant_error_channel in zip(neighbor_pixel, quant_error)
                )
                dithered_image.putpixel((neighbor_x, neighbor_y), adjusted_pixel)

    return dithered_image

def find_closest_palette_color(pixel, palette):
    return min(palette, key=lambda color: sum((a - b) ** 2 for a, b in zip(pixel, color)))

class ImageProcessor:
    def __init__(self, palette=None):
        self.palette = palette or [
            (0, 0, 0),      # Black
            (255, 255, 255),# White
            (0, 255, 0),    # Green
            (0, 0, 255),    # Blue
            (255, 0, 0),    # Red
            (255, 255, 0),  # Yellow
            (255, 128, 0)   # Orange 
            # Add more colors as needed
        ]
        

    def resize_image(self, image, target_width, target_height):
        # Check the aspect ratio of the image
        width, height = image.size
        aspect_ratio = width / height

        # If the image is vertical, rotate it 90 degrees
        if aspect_ratio < 1:
            image = image.rotate(90, expand=True)

        # Resize the image while maintaining its aspect ratio
        image.thumbnail((target_width, target_height))

        return image

    def apply_dithering(self, image, palette):
        # Call the Floyd-Steinberg dithering function
        dithered_image = floyd_steinberg_dithering(image, palette)
        return dithered_image

    def process_image(self, image, target_width, target_height):
        # Resize and dither the image
        resized_image = self.resize_image(image, target_width, target_height)
        dithered_image = self.apply_dithering(resized_image, self.palette)

        dithered_image.save(r'F:\EPAPERPROJ\frame_proj\e-Paper\RaspberryPi\python\pic\new.bmp', 'BMP')

        return dithered_image