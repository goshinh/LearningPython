from PIL import Image
import requests
from io import BytesIO

# convert image's formam
im =Image.open('polygon.eps')
im.save('polygon.png')

# save internet picture to local
def save_url_img(img_url,localPath):
  respone = requests.get(img_url)
  img = Image.open(BytesIO(respone.content))
  img.save(localPath)

# example
img_url = 'https://ww1.prweb.com/prfiles/2017/02/05/14045030/portrait%20lower%20quality.jpg'
localPath = 'url_img2.png'
save_url_img(img_url,localPath)


