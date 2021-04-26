import qrcode
import image


qr = qrcode.QRCode(
    version=15, #15 means the version of the qr code, higher the number bigger the qr code image and complicated
    box_size=10, # size of the box
    border=5, #this is the white part of the qr code 
)

data = "https://github.com/arthcodes"
# add ur url here

qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill = "red", back_color = "white")
img.save("tesdadadadadadadt.png ")  #name of the file

