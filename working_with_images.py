from PIL import Image
mac = Image.open("Images/example.jpg")

# (0,0) is top left
mac.crop((0,0,100,100))

pencils = Image.open("Images/pencils.jpg")

# Top pencils
x = 0
y = 0
w = 1950 / 3
h = 1300 / 10
pencils.crop((x,y,w,h))

# Bottom pencils
x = 0
y = 1100
w = 1950 / 3
h = 1300
pencils.crop((x,y,w,h))

mac.size

halfway = 1993/2
x = halfway - 200
w = halfway + 200
y = 800
h = 1257

computer = mac.crop((x,y,w,h))

mac.paste(im = computer,box=(0,0))

mac.resize((3000,500))

mac.rotate(90)

# RGBA go 0-255
red = Image.open("Images/red_color.jpg")
blue = Image.open("Images/blue_color.png")

blue.putalpha(128)
red.putalpha(128)

blue.paste(im=red,box=(0,0),mask=red)

blue.show()

blue.save("Images/purple.png")

print("test")