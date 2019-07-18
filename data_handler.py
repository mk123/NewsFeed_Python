import json
class DataHandler:
	"""docstring for DataHandler"""
	def __init__(self, file_name):
		file = open(file_name, 'r')
		self.data = json.load(file)

	def get_categories_list(self):
		names = []
		for element in self.data["news_data"]:
			names.append(element["category_name"])
		return names

	def get_news_for_category(self,category_name):
		news = []
		for element in self.data["news_data"]:
			if element["category_name"] == category_name:
				news = element["news"]
				break
		return news

# x = DataHandler("data.json")
# print(x.get_categories_list())
# print(x.get_news_for_category(x.get_categories_list()[0]))
		
		