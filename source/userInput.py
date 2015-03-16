import RecipeRepresentation
import ProjectDictionary
import HelperMethods
import scraper
import userInput
import main
import re
import nltk
import ProjectDictionary
import RecipeRepresentation
import json
import pdb

import random 


ingData = open('vocabulary/ingredientTypes2.json')
json_data = json.load(ingData)


def TransformationChoice():
	print "Enter your options",
	print "1. Transform to Indian"
	print "2. Transform to Mexican"
	choice_number = raw_input()
	return choice_number 


# French, Mexican, American Chinese, Indian, Itallian, Middle East 
def TranformToIndian(nameType_dict): 
	print "### Transfroming to Indian ####"
	flag = 0
	print len(nameType_dict)
	for old_ing,ing_type in nameType_dict.items(): 
		print(old_ing)
		#print(ing_type)
		if(ing_type == "spices"): 
			for i in json_data["spices"]["general"]: 
				if i == old_ing: 
	 				print "Not changed","\n"
	 				flag = 1
	 			if flag == 0: 
	 				new_type = random.choice(json_data["spices"]["indian"]);  
	 				print "changed to ", new_type,"\n"
	 	else: 
	 		print "Not changed","\n"

def TransformToMexican(nameType_dict):
	print "### Transfroming to Mexican ####"
	flag = 0
	count = 0 
	for old_ing,ing_type in nameType_dict.items(): 
		print count
		print old_ing 
		if(ing_type == "spices"): 
			for i in json_data["spices"]["general"]: 
				if i == old_ing: 
	 				print "Not changed","\n"
	 				flag = 1  
	 			if flag == 0: 
	 				new_type = random.choice(json_data["spices"]["mexican"])
	 				print "changed to ", new_type,"\n"
	 	elif(ing_type == "sauces"): 
	 		#new_type = random.choice(json_data["sauces"]["mexican"]) 
	 		new_type  = "salsa"
	 		print "changed to ", new_type,"\n"
	 	elif(ing_type == "roots" or ing_type == "roots" or ing_type == "tubers" or ing_type == "squash" or ing_type == "radish" or ing_type == "regular"): 
	 		new_type = random.choice(json_data["proteins"]["beans"])  
	 		print "changed to ", new_type,"\n"
	 	elif(ing_type == "breads"): 
	 		#new_type = random.choice(json_data["beans"])  
	 		print old_ing, "changed to ", "tortillas","\n"
	 	else: 
	 		print "Not changed","\n"
	 	count = count + 1

def TransformToLowFat(ingredientsDict):
	print "Transform to Low Fat"
	#Find all the ingredients that are fatty 



