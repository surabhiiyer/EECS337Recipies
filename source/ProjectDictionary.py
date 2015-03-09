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

def populateSpices():
	f = open('vocabulary/spices.txt','w')
	html_source = urllib2.urlopen("http://www.realsimple.com/food-recipes/shopping-storing/herbs-spices/basic-spice-checklist")
	spicesPage = BeautifulSoup(html_source)
	labels = spicesPage.findAll('label')
	for label in labels:
		tag = label.find('strong')
		if tag:
			f.write(tag.string.lower()+'\n')

	html_source = urllib2.urlopen("http://www.realsimple.com/food-recipes/shopping-storing/herbs-spices/gourmet-spice-checklist")
	spicesPage = BeautifulSoup(html_source)
	labels = spicesPage.findAll('label')
	for label in labels:
		tag = label.find('strong')
		if tag:
			f.write(tag.string.lower()+'\n')	
	f.close()			
				