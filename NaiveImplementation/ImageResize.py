from PIL import Image

#Images preprocessed to be of same size 256X256

for i in range(1,16):
   im = Image.open("VanGogh/img"+str(i)+".jpg")
   new_width = 256 
   new_height = 256
   im = im.resize((new_width, new_height), Image.ANTIALIAS)
   im.save("VanGogh/img"+str(i)+".jpg")

