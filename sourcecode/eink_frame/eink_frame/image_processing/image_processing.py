from PIL import Image, ImageOps


def floyd_steinberg_dithering(image, palette):
    dithered_image = image.copy()
    width, height = dithered_image.size

    for y in range(1, height - 1):
        for x in range(1, width - 1):
            old_pixel = dithered_image.getpixel((x, y))
            new_pixel = find_closest_palette_color(old_pixel, palette)
            dithered_image.putpixel((x, y), new_pixel)

            quant_error = tuple(map(lambda a, b: a - b, old_pixel, new_pixel))

            for dx, dy, factor in ((1, 0, 7/(215/10)), (-1, 1, 2/(215/10)), (0, 1, 3/(215/10)), (1, 1, 1/(215/10))):
                neighbor_x, neighbor_y = x + dx, y + dy

                if 0 <= neighbor_x < width and 0 <= neighbor_y < height:
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

        if aspect_ratio < 1:
            image = image.rotate(90)
            image = ImageOps.fit(image, (target_width, target_height))

        # Resize the image using a recognized resampling filter (e.g., LANCZOS)
        image = image.resize((target_width, target_height), Image.LANCZOS)

            
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