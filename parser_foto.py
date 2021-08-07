from bs4 import *
import os
import requests as rq
from PIL import Image

r = rq.get(input("Дай ссылку: "))




# print(r.encoding)
r.encoding = 'cp1251'
s = BeautifulSoup(r.text, "html.parser")

myimg = s.find_all("img", src=True)
ancor = s.find_all("a", href=True)
titl = s.find("h1").text.replace('"', '-')
titl = titl.split()
titl='_'.join(titl)
# print(titl)
# print(myimg)
# print(ancor)
print(titl)
z=[]
for i in ancor:
	if ('jpeg' in i['href'] or 'jpg' in i['href']) and ('http' in i['href']):
		print(i['href'])
		z.append(i['href'])
	else:
		pass

for ii in myimg:
	if ('jpeg' in ii['src'] or 'jpg' in ii['src']) and ('http' in ii['src']):
		print(ii['src'])
		z.append(ii['src'])
	else:
		pass


if not os.path.isdir(titl): 
	os.mkdir(titl)

	iii=1
	for img_link in z:
			file_name = titl +"/"+ str(iii) + ".jpg"
			img_data = rq.get(img_link, stream=True).raw
			f= Image.open(img_data)
			w,h = f.size
			if w > 399 or h>599:
				f.thumbnail([2000, 2000], Image.ANTIALIAS)
				f.save(file_name)
				print(iii)
			iii +=1
else:
	print("Такая папка есть")
	input()

