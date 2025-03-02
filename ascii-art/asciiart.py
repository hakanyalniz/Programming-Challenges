'''Create a program that turns ordinary images to ASCII art'''
from PIL import Image, ImageDraw, ImageFont

ASCII_FONTS = ["#", "@", "%", "A", "a", "O", "o", ";", ".", " "]
ASCII_NUMBERS = len(ASCII_FONTS)    

def main():
    # image = Image.open("./test.png")
    image = Image.open("./test.png")

    generate_ascii_image(resize_image(image))


def generate_ascii_image(originalImage):
    '''Given an image, loop through each pixel, get brightness, get correct ASCII font, 
    slowly build a new image with those font.'''

    originalWidth, originalHeight = originalImage.size
    # The original image was resized to become small by factor of 8, we take that size
    # and increase it by 8 to get original size
    ASCII_Image = Image.new("RGB", (originalWidth * 8, originalHeight * 8), "white")

    # Initialize ImageDraw, which we will use to draw ASCII
    draw = ImageDraw.Draw(ASCII_Image)
    # Specify the font and size
    font = ImageFont.truetype("./dejavu-sans-mono/DejaVuSansMono.ttf", 14)

    # Loop through each pixel, get the pixel value
    for y in range(originalHeight):
        # ASCII_ROW = ""
        for x in range(originalWidth):
            pixel = originalImage.getpixel((x, y))
            r, g, b = pixel[:3]  # Extract RGB values (ignore alpha if present)

            # get brightness of pixel, then get the proper ASCII font for that brightness
            ASCII = generate_ascii_font(get_brightness(pixel))
            draw.text((x * 8, y * 8), ASCII, fill=(r, g, b), font=font)
            # ASCII_ROW += ASCII

        # draw.text((0, y * 8), ASCII_ROW, fill="black", font=font)
            
    ASCII_Image.show()
    ASCII_Image.save("ascii_image.png")


def resize_image(image):
    '''Resize image to half'''

    originalWidth, originalHeight = image.size
    small_image = image.resize((originalWidth // 8, originalHeight // 8))
    return small_image.convert("RGB")


def generate_ascii_font(brightness):
    '''Given brightness value, return an appropriate ASCII'''

    # each brightness maps to each font
    # from 0 to the end, return that ascii
    # [" " ,".", ";", "o" ...
    #  0     1    2    3 
    # As in, each level of 0, 1, 2 and so on, corresponds to brightness level
    # and each of the ASCII index, match those levels
    return ASCII_FONTS[brightness]


def get_brightness(pixel):
    import math

    '''Return the rounded brightness of the pixel modulated to total number of available font.'''

    # Calculate average brightness of the pixel (R + G + B) / 3
    brightness = sum(pixel[:3]) / 3

    # Minus one, so it returns 0 to 7, instead of 0 to 8
    # Map brightness (0 to 255) to the ASCII font range (0 to ASCII_NUMBERS-1)
    return math.floor(brightness * (ASCII_NUMBERS - 1) // 255)


main()
