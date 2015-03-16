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


def TrandformationVegNonVeg(): 
	print "Enter your options: ", 
	print "1. Transform to Vegan"
	print "2. Transform to Non Vegetarian"
	print "3. Transform to Vegetarian"
	choice_number = raw_input()
	return choice_number 

def TransformationCuisine():
	print "Enter your options",
	print "1. Transform to Indian"
	print "2. Transform to Mexican"
	print "3. Transform to Italian"
	choice_number = raw_input()
	return choice_number 

# French, Mexican, American Chinese, Indian, Itallian, Middle East 
def TranformToIndian(nameType_dict): 
	ingObject = RecipeRepresentation.Transformed_Indian()
	print "### Transfroming to Indian ####"
	flag = 0
	count = 0 
	print len(nameType_dict)
	for old_ing,ing_type in nameType_dict.items(): 
		print count
		print(old_ing)
		#print(ing_type)
		if(ing_type == "spices"): 
			for i in json_data["spices"]["general"]: 
				if i == old_ing: 
					ingObject.m_IngName = i 
	 				print "Not changed","\n"
	 				flag = 1
	 			if flag == 0: 
	 				new_type = random.choice(json_data["spices"]["indian"]);  
	 				ingObject.m_IngName = new_type
	 				print "changed to ", new_type,"\n"
	 	else:
	 		ingObject.m_IngName = old_ing
	 		print "Not changed","\n"
	 	count = count+1
	 	new_ing_list.append(ingObject.m_IngName)

def TransformToMexican(nameType_dict):
	print "### Transfroming to Mexican ####"
	ingObject = RecipeRepresentation.Transformed_Mexican()
	flag = 0
	count = 0
	new_ing_list = [] 
	for old_ing,ing_type in nameType_dict.items(): 
		print count
		print old_ing 
		if(ing_type == "spices"): 
			for i in json_data["spices"]["general"]: 
				if i == old_ing: 
	 				print "Not changed","\n"
	 				ingObject.m_IngName = i 
	 				flag = 1  
	 			if flag == 0: 
	 				new_type = random.choice(json_data["spices"]["mexican"])
	 				ingObject.m_IngName = new_type
	 				print "changed to ", new_type,"\n"
	 	elif(ing_type == "sauces"): 
	 		new_type = random.choice(json_data["sauces"]["mexican"]) 
	 		ingObject.m_IngName = new_type
	 		print "changed to ", new_type,"\n"
	 	elif(ing_type == "roots" or ing_type == "roots" or ing_type == "tubers" or ing_type == "squash" or ing_type == "radish" or ing_type == "regular"): 
	 		new_type = random.choice(json_data["proteins"]["beans"])  
	 		ingObject.m_IngName = new_type
	 		print "changed to ", new_type,"\n"
	 	elif(ing_type == "breads"): 
	 		#new_type = random.choice(json_data["beans"])  
	 		ingObject.m_IngName = "tortillas"
	 		print old_ing, "changed to ", "tortillas","\n"
	 	elif(ing_type == "herbs"): 
	 		new_type = random.choice(json_data["MexicanHerbs"])  
	 		ingObject.m_IngName = new_type
	 		print old_ing, "changed to ", new_type,"\n"
	 	else:
	 		ingObject.m_IngName = old_ing;
	 		print "Not changed","\n"
	 	count = count + 1
	 	new_ing_list.append(ingObject.m_IngName)
	# print "#############"
	# print new_ing_list 

def TransformToItalian(nameType_dict):
	print "### Transfroming to Mexican ####"
	flag = 0
	count = 0 
	new_ing_list = []
	ingObject = RecipeRepresentation.Transformed_Italian()
	for old_ing,ing_type in nameType_dict.items(): 
		print count
		print old_ing 
		if(ing_type == "spices"): 
			for i in json_data["spices"]["general"]: 
				if i == old_ing: 
					ingObject.m_IngName = i 
	 				print "Not changed","\n"
	 				flag = 1  
	 			if flag == 0: 
	 				new_type = random.choice(json_data["spices"]["italian"])
	 				ingObject.m_IngName = new_type
	 				print "changed to ", new_type,"\n"
	 	elif(ing_type == "sauces"): 
	 		new_type = random.choice(json_data["sauces"]["italian"]) 
	 		ingObject.m_IngName = new_type
	 		print "changed to ", new_type,"\n"
	 	elif(ing_type == "roots" or ing_type == "tubers" or ing_type == "squash" or ing_type == "radish" or ing_type == "regular"): 
	 		new_type = random.choice(json_data["proteins"]["beans"])  
	 		ingObject.m_IngName = new_type
	 		print "changed to ", new_type,"\n"
	 	elif(ing_type == "breads"): 
	 		new_type = random.choice(json_data["italianBreads"]) 
	 		ingObject.m_IngName = new_type 
	 		print old_ing, "changed to ", new_type,"\n"
	 	elif(ing_type == "herbs"): 
	 		new_type = random.choice(json_data["italianHerbs"])  
	 		ingObject.m_IngName = new_type
	 		print old_ing, "changed to ", new_type,"\n"
	 	else:
	 		ingObject.m_IngName = old_ing
	 		print "Not changed","\n"
	 	count = count + 1
	 	new_ing_list.append(ingObject.m_IngName)
def TransformToLowFat(ingredientsDict):
	print "Transform to Low Fat"
	#Find all the ingredients that are fatty 

def TransformToVegetarian(nameType_dict):
	#Find any meat and egg components of the recipe and add vegetables in place of them
	ingObject = RecipeRepresentation.Transformed_Vegetarian()
	print "### Transforming to Vegetarian ###"
	# ing = old_ing
	for ing, ing_type in nameType_dict.items():
		print ing
		if(ing_type == "meats" or ing_type == "poultry" or ing_type == "eggs" or ing_type == "seafood"):
			new_type=random.choice(json_data["vegetables"]["regular"])
			ingObject.m_IngName = new_type
			print "Changed to ",new_type,"\n"
		else:
			print "Not changed"

def TransformToVegan(nameType_dict):
	#Find meat, eggs, and dairy components and replace them with appropriate ingredients
	print "### Transforming to Vegan ###"
	ingObject = RecipeRepresentation.Transformed_Vegan() 
	new_ing_list = [] 
	count = 0 
	for ing, ing_type in nameType_dict.items():
		print ing
		print count 
		if(ing_type == "meats" or ing_type == "poultry" or ing_type == "eggs" or ing_type == "seafood"):
			new_type=random.choice(json_data["vegetables"]["regular"])
			ingObject.m_IngName = new_type
			print "Changed to ",new_type,"\n"
		elif(ing_type == "dairy"):
			new_type = "soy milk"
			ingObject.m_IngName = new_type
			print "Changed to ", new_type
		else:
			ingObject.m_IngName = ing
			print "Not changed"
		count = count + 1 
		new_ing_list.append(ingObject.m_IngName)

def TransformToNonVegetarian(nameType_dict):
	#Find vegetarian products and replace with meat or eggs
	print "### Transforming to Non Vegetarian ###"
	ingObject = RecipeRepresentation.Transformed_NonVegetarian()
	new_ing_list = [] 
	count = 0
	for ing, ing_type in nameType_dict.items():
		print ing
		print count
		if (ing_type == "regular" or ing_type == "onions" or ing_type == "roots" or ing_type == "radish" or ing_type == "squash" or ing_type == "tubers"):
			list_picker=["meats","eggs","poultry","seafood"]
			picked=random.choice(list_picker)
			new_type=random.choice(json_data["proteins"][picked])
			ingObject.m_IngName = new_type
			print "Changed to ",new_type,"\n"
		else:
			ingObject.m_IngName = ing
			print "Not changed."
		count = count + 1
		new_ing_list.append(ingObject.m_IngName)



