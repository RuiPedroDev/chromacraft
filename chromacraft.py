from PIL import Image, ImageEnhance, ImageOps, ImageFilter
import argparse
import os

def change_image_properties(image_path, brightness=None, contrast=None, saturation=None, sharpness=None, invert=False, rotate=None, sepia=None, blur=None, glamour=None):
    image = Image.open(image_path)

    if brightness is not None:
        enhancer = ImageEnhance.Brightness(image)
        image = enhancer.enhance(brightness)

    if contrast is not None:
        enhancer = ImageEnhance.Contrast(image)
        image = enhancer.enhance(contrast)

    if saturation is not None:
        enhancer = ImageEnhance.Color(image)
        image = enhancer.enhance(saturation)

    if sharpness is not None:
        enhancer = ImageEnhance.Sharpness(image)
        image = enhancer.enhance(sharpness)

    if invert:
        image = image.convert("RGB")
        image = ImageOps.invert(image)

    if rotate is not None:
        image = image.rotate(rotate)

    if sepia is not None:
        image = image.convert("RGB")
        if(sepia < 1):
            sepia = 1
        image = apply_sepia_filter(image, -(sepia/10) + 1)

    if blur is not None:
        image = image.filter(ImageFilter.GaussianBlur(radius=blur))

    if glamour is not None:
        image = apply_glamour_filter(image, glamour)
    

    image_name, image_extension = os.path.splitext(image_path)
    new_image_path = f"{image_name}_modified{image_extension}"
    image.save(new_image_path)
    print(f"Modified image saved as {new_image_path}")
    image.show()

def apply_sepia_filter(image, intensity):
    sepia_filter = (0.393 + 0.607 * intensity, 0.769 - 0.769 * intensity, 0.189 - 0.189 * intensity, 0,
                   0.349 - 0.349 * intensity, 0.686 + 0.314 * intensity, 0.168 - 0.168 * intensity, 0,
                   0.272 - 0.272 * intensity, 0.534 - 0.534 * intensity, 0.131 + 0.869 * intensity, 0)
    return image.convert("RGB", sepia_filter)


def apply_glamour_filter(image, intensity):
    blurred = image.filter(ImageFilter.GaussianBlur(radius=intensity))
    final_image = Image.blend(image, blurred, 0.5)
    return final_image


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Image manipulation tool with Pillow')
    parser.add_argument('image_path', help='Path to the image file')
    parser.add_argument('--bright', type=float, help='Adjust brightness')
    parser.add_argument('--cont', type=float, help='Adjust contrast')
    parser.add_argument('--sat', type=float, help='Adjust saturation')
    parser.add_argument('--sharp', type=float, help='Adjust sharpness')
    parser.add_argument('--invert', action='store_true', help='Invert the image color')
    parser.add_argument('--rotate', type=float, help='Rotate the image by the specified degrees')
    parser.add_argument('--blur', type=float, help='Apply a Gaussian blur with the specified radius')
    parser.add_argument('--glamour', type=float, help='Apply a glamour filter with the specified intensity')
    parser.add_argument('--sepia', type=float, help='Apply a sepia filter with the specified intensity')

    args = parser.parse_args()
    change_image_properties(args.image_path, args.bright, args.cont, args.sat, args.sharp, args.invert, args.rotate,args.sepia, args.blur, args.glamour)