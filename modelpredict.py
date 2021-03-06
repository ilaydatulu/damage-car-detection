from fastai.vision import *
from urllib.request import urlretrieve
from os import path
from random import choice

class ModelPredict():
	def __init__(self, filename):
		self.filename = filename

	def download_model(self):
		if path.exists('export.pkl') == False:
			url = 'https://drive.google.com/file/d/1AJiF7P7ER5iYfEH8vGFsX2YOnDMI6xci/view?usp=sharing'
			filename = 'export.pkl'
			urlretrieve(url,filename)

	def predict(self):
		self.download_model()
		learn = load_learner('')
		img = open_image(self.filename)
		pred_class , pred_idx, outputs = learn.predict(img)
		return str(pred_class)


if __name__=='__main__':
	m = ModelPredict('/content/drive/MyDrive/kalem/highlighter/download.jpg').predict()
	print(m)
