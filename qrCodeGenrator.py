import qrcode as qr
img =qr.make("https://www.youtube.com/") #paste your text or link here
img.save("image_name.png")
