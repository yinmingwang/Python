from PIL import Image
im = Image.open("lady.jpg")
print im.format, im.size, im.mode
box = (100, 100, 200, 200)
region = im.crop(box)
region = region.transpose(Image.ROTATE_180)
im.paste(region, box)
out = im.transpose(Image.FLIP_LEFT_RIGHT) 
out.show()
