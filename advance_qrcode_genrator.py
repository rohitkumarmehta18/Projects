import qrcode
import qrcode as qr
from PIL import Image

qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=10,
                 border=4,)
qr.add_data("https://www.youtube.com/") #paste your text or link here
qr.make(fit=True)
img= qr.make_image(fill_color="blue",
                   back_color="white")
img.save("image_name.png")
