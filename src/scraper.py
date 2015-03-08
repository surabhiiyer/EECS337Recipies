import urllib2
import sys
from bs4 import BeautifulSoup

def scrape(r_url): 
	response = urllib2.urlopen(r_url)
	html_content = response.read()
	soup = BeautifulSoup(html_content)

	#Print ingredients 
	name_list = []
	amount_list = []

	# Finding ingredient names 
	# ingredients = soup.find_all("span",{"class":"ingredient-name"})
	# for i in ingredients:
	# 	ingredient_name = i.string 
	#  	name_list.append(ingredient_name) 

	# # Finding all the quantities 
	# ingredient_amount = soup.find_all("span",{"class":"ingredient-amount"})
	# for a in ingredient_amount: 
	# 	amount = a.string 
	# 	amount_list.append(amount)

	# # Creating dictionary 
	# ingredient_dict = dict(zip(name_list, amount_list))

	# print ingredient_dict

	print "Printing ingredients: "
	ingredient_amount = soup.find_all("span",{"class":"ingredient-amount"})
	for a in ingredient_amount: 
		amount_list.append(a.string)
		for x in a.findNext("span",{"class":"ingredient-name"}): 
			name_list.append(x.string)

	# Creating dictionary 
	ingredient_dict = dict(zip(name_list, amount_list))
	print ingredient_dict

	#finding directions 
	all_directions = soup.find_all("span",{"class":"plaincharacterwrap break"})
	#directions list
	dir_list = [] 
	print "printing directions"
	for d in all_directions: 
		dir_list.append(d.string)

	print "Directions:"
	print dir_list

	#Prep time 
	prep_time = soup.find("span",{"id":"prepMinsSpan"})
	if(prep_time):
		prepTime = prep_time.string
		print "Prep Time", prepTime 
	else: 
		print "Prep Time not available on the html page"

	#Ready-In
	ready_in = soup.find("span",{"id":"totalMinsSpan"})
	if(ready_in): 
		readyIn  = ready_in.string 
		print "Read In", readyIn
	else:
		print "Ready In time not available on the html page"

	#Cook time 
	cook_time = soup.find("span",{"id":"cookHoursSpan"})
	if(cook_time):
		cookTime = cook_time.string
		print "cook_time", cookTime
	else: 
		print "Cook Time not found in the html page"
	#Ratings 
	rating_value = soup.find("meta",{"itemprop":"ratingValue"})
	r_val = rating_value
	print "Ratings: ", r_val



scrape("http://allrecipes.com/Recipe/Todds-Famous-Blueberry-Pancakes/?prop24=hn_slide1_Todd%27s-Famous-Blueberry-Pancakes&evt19=1L")