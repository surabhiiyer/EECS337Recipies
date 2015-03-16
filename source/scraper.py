import urllib2
import sys
from bs4 import BeautifulSoup

def scrapeIngredients(r_url):
	response = urllib2.urlopen(r_url)
	html_content = response.read()
	soup = BeautifulSoup(html_content)
 
	name_list = []
	amount_list = []

	ingredient_amount = soup.find_all("span",{"class":"ingredient-amount"})
	for a in ingredient_amount: 
		amount_list.append(a.string)
		for x in a.findNext("span",{"class":"ingredient-name"}): 
			name_list.append(x.string) 
	ingredient_dict = dict(zip(name_list, amount_list))
	return ingredient_dict	

def getDirections(r_url):
	response = urllib2.urlopen(r_url)
	html_content = response.read()
	soup = BeautifulSoup(html_content)

	#finding directions 
	all_directions = soup.find_all("span",{"class":"plaincharacterwrap break"})
	#directions list
	dir_list = [] 
	for d in all_directions: 
		dir_list.append(d.string)
	return dir_list



def getPrepTimeRating(r_url): 
	prepTime = 0.0
	readyTime = 0.0
	cookTime = 0.0
	rating = 0.0
	title = ''
	response = urllib2.urlopen(r_url)
	html_content = response.read()
	soup = BeautifulSoup(html_content)
	#Prep time 
	prep_time = soup.find("span",{"id":"prepMinsSpan"})
	if(prep_time):
		prepTime = prep_time.string

	#Ready-In
	ready_time = soup.find("span",{"id":"totalMinsSpan"})
	if(ready_time): 
		readyTime  = ready_time.string 

	#Cook time 
	cook_time = soup.find("span",{"id":"cookHoursSpan"})
	if(cook_time):
		cookTime = cook_time.string

	#Ratings 
	rating = soup.find("meta",{"itemprop":"ratingValue"})

	Title = soup.find("h1",id='itemTitle')
	title = Title.string

	print title
	# heading = ''
	# if(title != ''):
	# 	heading = heading + title + "."
	# if(prepTime != 0.0):
	# 	heading = heading + " Preparation time:" + str(prepTime ) + "."
	# if(cookTime != 0.0):
	# 	heading = heading + " Cooking time:" + str(cookTime) + "."
	# if(readyTime != 0.0):
	# 	heading = heading + " Ready in " + str(readyTime) + "."
	# print heading
	# if(rating != 0.0):
	# 	rating = 'Rating: ' + str(rating)
	# 	print rating

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



#scrape("http://allrecipes.com/Recipe/Todds-Famous-Blueberry-Pancakes/?prop24=hn_slide1_Todd%27s-Famous-Blueberry-Pancakes&evt19=1L")