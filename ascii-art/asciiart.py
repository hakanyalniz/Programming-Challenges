'''Create a program that turns ordinary images to ASCII art'''
from PIL import Image, ImageDraw, ImageFont

ASCII_FONTS = [" " ,".", ";", "o", "O", "a", "A", "#"]
ASCII_NUMBERS = len(ASCII_FONTS)

def main():
    image = Image.open("./151.jpg")

    generate_ascii_image(resize_image(image))


def generate_ascii_image(originalImage):
    '''Given an image, loop through each pixel, get brightness, get correct ASCII font, 
    slowly build a new image with those font.'''

    originalWidth, originalHeight = originalImage.size
    ASCII_Image = Image.new("RGB", (originalWidth, originalHeight), "white")

    # Initialize ImageDraw, which we will use to draw ASCII
    draw = ImageDraw.Draw(ASCII_Image)
    # Specify the font and size
    font = ImageFont.truetype("arial.ttf", 8)

    # Loop through each pixel, get the pixel value
    for y in range(round(originalHeight)):
        for x in range(round(originalWidth)):
            pixel = originalImage.getpixel((x, y))
            # get brightness of pixel, then get the proper ASCII font for that brightness
            ASCII = generate_ascii_font(get_brightness(pixel))
            draw.text((x, y), ASCII, fill="black", font=font)
    
    ASCII_Image.show()


def resize_image(image):
    '''Resize image to half, then size it back up.'''

    originalWidth, originalHeight = image.size
    small_image = image.resize((originalWidth // 8, originalHeight // 8))
    return small_image.resize(image.size).convert("RGB")

def generate_ascii_font(brightness):
    '''Given brightness value, return an appropriate ASCII'''

    # Loop through each ascii font, since each brightness maps to each font
    # from 0 to the end, if we find the correct index, return that ascii
    # [" " ,".", ";", "o" ...
    #  0     1    2    3 
    # As in, each level of 0, 1, 2 and so on, corresponds to brightness level
    # and each of the ASCII index, match those levels
    # range gives 
    for index in range(ASCII_NUMBERS):
        if (brightness == index):
            return ASCII_FONTS[index]

def get_brightness(pixel):
    '''Return the rounded brightness of the pixel modulated to total number of available font.'''

    # Minus one, so it returns 0 to 7, instead of 0 to 8
    return round((sum(pixel[:3]) / 3) % (ASCII_NUMBERS - 1))

main()
