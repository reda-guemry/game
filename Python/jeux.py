from PIL import Image

background = Image.open("Python/img/background.png")

icon = Image.open("Python/img/icon.png")

background.paste(icon, (150, 200), icon) 

background.save("Python/img/map_final.png")

background.show()





