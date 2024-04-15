print("LinkedIn Quick Responsive code")

import qrcode as qr
from PIL import Image   #The Python Imaging Library adds image processing capabilities to your Python interpreter

qr_code = qr.QRCode(box_size=10, border=4)

# Add data
qr_code.add_data('https://www.linkedin.com/in/isaar/')


qr_code.make(fit=True)

# Create an image
qr_image = qr_code.make_image(fill_color='Cyan', back_color='Blue')

# Resize image for better clarity
qr_image = qr_image.resize((300, 300), Image.LANCZOS)

# Save image
qr_image.save("Linkedin.png")









