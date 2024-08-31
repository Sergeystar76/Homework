import requests
from PIL import Image, ImageFilter

r = requests.get('https://ria.ru/')
print(r.url)
print(r.headers)
query = {'order': 'sport'}
r_2 = requests.get('https://ria.ru/', params=query)
print(r_2.url)


pic = Image.open('girl.jpg')
pic.show()
print(pic.format, pic.size, pic.mode)
pic_res = pic.resize((300, 400))
pic_bw = pic_res.convert('L')
pic_end = pic_bw.filter(ImageFilter.GaussianBlur(2))
print(pic_end.format, pic_end.size, pic_end.mode)
pic_end.save('New girl.png')
pic_end.show()
