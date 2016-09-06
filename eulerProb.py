from mongoengine import *
from mongoengine.fields import *

class eulerProb(Document):
	num = IntField(required=True, primary_key=True, unique=True)
	title = StringField()
	text = StringField()
	probArgs = DictField()
	inputFile = FileField()
	url = StringField()
	html = FileField()

	baseURL = "https://projecteuler.net/problem=%d"

	def buildURL(self):
		self.url = self.baseURL %self.num