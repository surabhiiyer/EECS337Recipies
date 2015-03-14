# contains methods that assist in formulating recipes
import re
import nltk
import ProjectDictionary
import RecipeRepresentation
import json

# to be used to tokenize words
from nltk.tokenize import TreebankWordTokenizer
wordTokenizer = TreebankWordTokenizer()

# to be used to tokenize sentences
sentenceTokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

#import all the stop words
from nltk.corpus import stopwords
stopWordsList = stopwords.words('english') 

regExTools = re.compile(r'(in a|take a) ([a-z]*) ([a-z]*)', re.IGNORECASE)
#regExTools = re.compile(r'(in\s{0,1}[a]{0,1}|take a) ([a-z]+).([a-z]*) ([a-z]+)', re.IGNORECASE)
#regExTools2 = re.compile(r'[in]to\s*[a-z]*\s*([a-z]*)', re.IGNORECASE)
ingredientList = []
cookingMethodsList = []
toolsList = []

#the pos tags do not treat these as nouns
exceptionNouns = ['chicken']

def identifyTools(directionsList):
	f = open('vocabulary/tools.txt', 'r+')
	knownTools = []
	for line in f:
		knownTools.append(line.replace('\n',''))
	for instructions in directionsList:
		for tool in knownTools:
			if tool in instructions:
				toolObj = RecipeRepresentation.Tools()
				toolObj.m_ToolName = tool
		  		toolObj.m_ToolQuantity = 1
		  		toolsList.append(toolObj)	
		#Gather knowledge about new tools
		findResults = regExTools.findall(instructions)
		for result in findResults:
		 	for index in range(0,len(result)):
		 		toolName = ''
		 		tokens = result[index]
		 		tokens = wordTokenizer.tokenize(tokens)
		 		posTag = nltk.pos_tag(tokens)
		 		for(data, tag) in posTag:
		 			if(tag == 'NN'):
		 				toolName += data				
				if toolName not in knownTools and toolName != '':
		  			f.write(toolName+'\n')
		  			knownTools.append(toolName)
		  			toolObj = RecipeRepresentation.Tools()
		  			toolObj.m_ToolName = toolName
		  			toolObj.m_ToolQuantity = 1
		  			toolsList.append(toolObj)
	f.close()	  			 			

regExMethods = re.compile(r'([a-z]+) with ([a-z]+)', re.IGNORECASE)

def identifyCookingMethods(directionsList):
	ingredients = []
	for ingredient in ingredientList:
		ingredients.append(ingredient.m_IngName)

	tools = []			
	for tool in toolsList:
		tools.append(tool.m_ToolName)

	fprimary = open('vocabulary/primaryMethods.txt', 'r+')
	primaryCookingMethods = []
	for line in fprimary:
		primaryCookingMethods.append(line.replace('\n',''))

	fsecondary = open('vocabulary/secondaryMethods.txt', 'r+')
	secondaryCookingMethods = []
	for line in fsecondary:
		secondaryCookingMethods.append(line.replace('\n',''))	
	
	for instructions in directionsList:	
		sentences = sentenceTokenizer.tokenize(instructions)
		for sentence in sentences:
			for cookingMethod in primaryCookingMethods:
				if cookingMethod in sentence.lower():
					methodObject = RecipeRepresentation.Methods()
					methodObject.m_MethodName = cookingMethod
					methodObject.m_MethodType = 'primary'
					for ingredient in ingredients:
						if ingredient in sentence:
							methodObject.m_ingredientUsed.append(ingredient)
					for tool in tools:
						if tool in sentence:
							methodObject.m_toolsUsed.append(tool)		
					cookingMethodsList.append(methodObject)		
			for cookingMethod in secondaryCookingMethods:
				if cookingMethod in sentence.lower():
					methodObject = RecipeRepresentation.Methods()
					methodObject.m_MethodName = cookingMethod
					methodObject.m_MethodType = 'secondary'
					for ingredient in ingredients:
						if ingredient in sentence:
							methodObject.m_ingredientUsed.append(ingredient)
					for tool in tools:
						if tool in sentence:
							methodObject.m_toolsUsed.append(tool)
					cookingMethodsList.append(methodObject)		
		searchResult = regExMethods.findall(instructions)
		for result in searchResult:
			if result[1] in ingredients and result[0] != '':
				methodObject = RecipeRepresentation.Methods()
				methodObject.m_MethodName = result[0].lower()
				methodObject.m_MethodType = 'secondary'
				methodObject.m_ingredientUsed.append(result[1])
				cookingMethodsList.append(methodObject)	

regexQuantity = re.compile(r'(\d+\/?\d?)\s*([a-z]*)', re.IGNORECASE)

def identifyIngredients(ingredientsDict):
	for key in  ingredientsDict:
	 	searchResult = regexQuantity.findall(ingredientsDict[key])
	 	ingObject = RecipeRepresentation.Ingredients()
	 	for result in searchResult:
	 		ingObject.m_IngQuantity = result[0]
	 		ingObject.m_IngMeasurement = result[1]
		tokens = wordTokenizer.tokenize(key.lower())
		posTags = nltk.pos_tag(tokens)
		name = ''
		descriptor = ''
		preparation = ''
		prepDescriptor = ''
		for (data,tag) in posTags:
			if(tag == 'NN' or tag == 'NNS' or data in exceptionNouns):
				name = name + data + ' ' 
			elif(tag == 'JJ' or data not in exceptionNouns):
				descriptor = descriptor + data + ','
			elif(tag == 'VB' or tag == 'VBD' or tag == 'VBP' or tag == 'VBN' or tag == 'VBG' or tag == 'VBZ' or data not in exceptionNouns):
				preparation = preparation + data + ','
			elif(tag == 'RB' or data not in exceptionNouns):
				prepDescriptor = prepDescriptor + data + ','
		ingObject.m_IngName = name[:len(name)-1]
		ingObject.m_IngDescriptor.append(descriptor[:len(descriptor)-1])
		ingObject.m_IngPreparation.append(preparation[:len(preparation)-1])
		ingObject.m_IngPrepDescriptor.append(prepDescriptor[:len(prepDescriptor)-1])			
		if(ingObject.m_IngName != ''):
			ingredientList.append(ingObject)


def identifyIngredientType():
	json_data = open('vocabulary/ingredientTypes.json')
	ingData = json.load(json_data)
	spices = ingData['spices']
	protPoultry = ingData['proteins']['poultry']
	protMeats = ingData['proteins']['meats']
	protEggs = ingData['proteins']['eggs']
	protSeafood = ingData['proteins']['seafood']
	protVeg = ingData['proteins']['vegetarian']
	protBeans = ingData['proteins']['beans']
	dairy = ingData['dairy']
	nuts = ingData['nuts']
	breads = ingData['breads']
	for ingObject in ingredientList:
		tokens = wordTokenizer.tokenize(ingObject.m_IngName)
		for token in tokens:
			if token in spices:
				ingObject.m_IngType = 'spices'
			elif token in dairy: 	
		 		ingObject.m_IngType = 'dairy'
		 	elif token in protPoultry:
		 		ingObject.m_IngType = 'poultry'
		 	elif token in protMeats:
		 		ingObject.m_IngType = 'meat'
		 	elif token in protEggs:
		 		ingObject.m_IngType = 'eggs'
		 	elif token in protSeafood:
		 		ingObject.m_IngType = 'seafood'
		 	elif token in protVeg:
		 		ingObject.m_IngType = 'vegetarian'					
		 	elif token in protBeans:
		 		ingObject.m_IngType = 'beans'
		 	elif token in nuts:
		 		ingObject.m_IngType = 'nuts'
		 	elif token in breads:	
		 		ingObject.m_IngType = 'breads'
		 	elif token == 'oil':
		 		ingObject.m_IngType = 'oil'
		 	else:
		 		ingObject.m_IngType = 'unknown'			
	json_data.close()	 		


transformMethodList = []

def transformCookingMethod():
	catTypes = ['bake','broil','barbecue','boil','deep-fry','pan-fry','grill','roast','poach','stir-fry',
	'stew','simmer']
	ruleTypes = ['bake','broil','barbecue','boil','deep-fry','pan-fry','grill','roast','poach','stir-fry',
	'stew','simmer']
	toolTypes = ['bake','broil','boil','deep-fry','pan-fry','roast','poach','stir-fry',
	'stew','simmer']
	json_data = open('vocabulary/methodTransformation.json')
	methodData = json.load(json_data)
	categories = methodData['categories']
	rules = methodData['rules']
	tools = methodData['tools']
	for methodObject in cookingMethodsList:
		if methodObject.m_MethodType == 'secondary':
			continue
		else:
			for ingredient in methodObject.m_ingredientUsed:
				for ingObject in ingredientList:
					if ingredient == ingObject.m_IngName:
						ingType = ingObject.m_IngType
						break
				if ingType == "unknown":
					continue
				else:
					
							


			


