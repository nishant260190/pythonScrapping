import pytesseract
import sys
import os

print(os.path.exists('/Users/nishantgoel/downloads/112.png'))
try:
    import Image
except ImportError:
    from PIL import Image
from subprocess import check_output


def resolve(path):
	print("Resampling the Image")
	check_output(['/usr/local/bin/convert', path, '-resample', '600', 'xyz.png'])
	return pytesseract.image_to_string(Image.open(path))

if __name__=="__main__":
	print('Resolving Captcha')
	captcha_text = resolve('/Users/nishantgoel/downloads/112.png')
	print('Extracted Text',captcha_text)
