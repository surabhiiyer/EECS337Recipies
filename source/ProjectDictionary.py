#file contains a dictionary of cooking utensils, ingredients, etc.
import urllib2
import re
from bs4 import BeautifulSoup

#create a dictionary of tool names from Wikipedia
def populateTools():
	f = open('vocabulary/tools.txt','w');
	html_source = urllib2.urlopen("http://en.wikipedia.org/wiki/Category:Cooking_utensils")
	wikiPage = BeautifulSoup(html_source)
	div = wikiPage.find('div', id='mw-pages')
	alphabeticalList = div.findAll('ul')
	firstItemSkipped = False;
	for listIndex in alphabeticalList:
		if(firstItemSkipped == False):
			firstItemSkipped = True
			continue;
		hyperlinks = listIndex.findAll('a')
		for hyperlink in hyperlinks:
			utensilName = hyperlink.string.lower()
			utensilName = re.sub(r'\(.*\)',r'',utensilName)
			f.write(utensilName+'\n')
	f.close()		

#create a dictionary of cooking methods from www.thedailymeal.com
# def populateCookingMethods():
# 	methods = []
# 	html_source = urllib2.urlopen("http://www.thedailymeal.com/15-basic-cooking-methods-you-need-know-slideshow")
# 	page = BeautifulSoup(html_source)
# 	listTag = page.findAll('li', class_='thumb')
# 	print listTag