from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from os.path import exists , abspath
import sys

def generate_text_overlay(length_x , length_y , alpha = 55):
	if max(length_x , length_y) > 2000:
		amp_times = 4
	else:
		amp_times = 1

	try:
		font_kai = ImageFont.truetype("C:\Windows\Fonts\simkai.ttf", 60 * amp_times)
		font_eng = ImageFont.truetype("C:\Windows\Fonts\Arial.ttf", 30 * amp_times)
	except:
		raise NotImplementedError('Fonts simkai / Arial does not exists.')

	img = Image.new('RGBA', (length_x, length_y), (255,255,255,0))
	draw = ImageDraw.Draw(img)
	posx , posy = 0 , length_y * 0.2
	px_flag , py_flag = 0 , 0
	while True:
		draw.text((posx, posy), "夜sya乐谱研究会", font = font_kai ,fill=(0, 0, 0, alpha))
		draw.text((posx+( 105 * amp_times ), posy+( 65 * amp_times )), "https://yesya.net", font = font_eng ,fill=(0, 0, 0, alpha))
		posx = posx + ( 100  * amp_times )
		if posx >= length_x:
			px_flag = 1
			posx = posx % length_x
		posy = posy + ( 200 * amp_times )
		if posy >= length_y:
			py_flag = 1
			posy = posy % length_y
		if px_flag and py_flag:
			return img

def append_text_overlay(img_before):
	img_before = img_before.convert('RGBA')
	text_overlay = generate_text_overlay(img_before.size[0] , img_before.size[1])
	return Image.alpha_composite(img_before, text_overlay)

for index , filename in enumerate(sys.argv):
	if not index:
		continue
	if exists(filename):
		print("Working on" ,abspath(filename))
		try:
			img_before = Image.open(filename)
			img_output = append_text_overlay(img_before)
			img_output.save(filename,quality=95)
		except Exception as e:
			raise e
			print("File error.")
else:
	input("Press enter to continue.")