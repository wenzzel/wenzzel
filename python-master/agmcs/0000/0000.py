from PIL import Image, ImageDraw, ImageFont
text = "55"
im = Image.open('./wenzzel/python-master/agmcs/0000/1.bmp')
w,h = im.size
font_size = h//4

draw = ImageDraw.Draw(im)
font = ImageFont.truetype ("./wenzzel/python-master/agmcs/0000/Arial.ttf",font_size)

text_w,text_h = draw.textsize(text,font=font) 
draw.text((w-text_w,0), text, fill=(255,0,0), font=font)

draw.ellipse((100, 100, 150, 200), fill=(255, 255, 0), outline=(0, 0, 0))


im.save('./wenzzel/python-master/agmcs/0000/heihei.bmp')
