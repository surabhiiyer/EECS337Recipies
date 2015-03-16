# contains methods that assist in formulating recipes
import re
import nltk
import ProjectDictionary
import RecipeRepresentation
import json
import pdb

# to be used to tokenize words
from nltk.tokenize import TreebankWordTokenizer
wordTokenizer = TreebankWordTokenizer()

# to be used to tokenize sentences
sentenceTokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

#import all the stop words
from nltk.corpus import stopwords
stopWordsList = stopwords.words('english') 

ingredientList = []
cookingMethodsList = []
toolsList = []

def removeDuplicates():
	for ingObject in ingredientList:
		name = ingObject.m_IngName
		descrptorList = ingObject.m_IngDescriptor
		for index in range(0,len(descrptorList)):
			if name == descrptorList[index]:
				ingObject.m_IngDescriptor[index] = ''

		prepList = ingObject.m_IngPreparation
		for index in range(0,len(prepList)):
			if name == prepList[index]:
				ingObject.m_IngPreparation[index] = ''
		
		prepDescList = ingObject.m_IngPrepDescriptor
		for index in range(0,len(prepDescList)):
			if name == prepDescList[index]:
				ingObject.m_IngPrepDescriptor[index] = ''

regexQuantity = re.compile(r'(\d+\/?\d?)\s*([a-z]*)', re.IGNORECASE)
# Method to extract indredient names, quantities, descriptors, etc
def identifyIngredients(ingredientsDict):
	categories = ['spices','proteins','dairy','nuts','breads','grains','vegetables','peppers','sauce','oil','fruits']
	proteinCatgs = ['poultry','meats','eggs','seafood','vegetarian','beans']
	vegeCatgs = ['regular', 'onions', 'roots', 'radish', 'squash', 'tubers']
	ingData = open('vocabulary/ingredientTypes.json')
	json_data = json.load(ingData)
	for key in  ingredientsDict:
		breakFlag = 0
		ingObject = RecipeRepresentation.Ingredients()
		for category in categories:
			if(category == 'proteins'):
				for proteinType in proteinCatgs:
					proteinList = json_data[category][proteinType]
					for protein in proteinList:
						if protein in key.lower():
							ingObject.m_IngName = protein
							ingObject.m_IngType = proteinType
							breakFlag = 1
							break
					if breakFlag == 1:
						break			
			elif(category == 'vegetables'):
				for vegeType in vegeCatgs:
					vegeList = json_data[category][vegeType]		
					for vege in vegeList:
						if vege in key.lower():
							ingObject.m_IngName = vege
							ingObject.m_IngType = vegeType
							breakFlag = 1
							break
					if breakFlag == 1:
						break
			else:
				ingCategory = json_data[category]
				for ing in ingCategory:
					if ing in key.lower():
						ingObject.m_IngName = ing
						ingObject.m_IngType = category
						breakFlag = 1
			if breakFlag == 1:
				break
		searchResult = regexQuantity.findall(ingredientsDict[key])
	 	for result in searchResult:
	 		ingObject.m_IngQuantity = result[0]
	 		ingObject.m_IngMeasurement = result[1]
		tokens = wordTokenizer.tokenize(key.lower())
		posTags = nltk.pos_tag(tokens)
		name = ''
		descriptor = []
		preparation = []
		prepDescriptor = []
		for (data,tag) in posTags:
			if(tag == 'NN' or tag == 'NNS'):
				name = name + data + ' ' 
			elif(tag == 'JJ'):
				descriptor.append(data)
			elif(tag == 'VB' or tag == 'VBD' or tag == 'VBP' or tag == 'VBN' or tag == 'VBG' or tag == 'VBZ'):
				preparation.append(data)
			elif(tag == 'RB'):
				prepDescriptor.append(data)
		if(breakFlag == 0):		
			ingObject.m_IngName = name[:len(name)-1]
		ingObject.m_IngDescriptor = descriptor
		ingObject.m_IngPreparation = preparation
		ingObject.m_IngPrepDescriptor = prepDescriptor			
		if(ingObject.m_IngName != ''):
			ingredientList.append(ingObject)
	ingData.close()	
	removeDuplicates()	

regExTools = re.compile(r'(in a|take a) ([a-z]*) ([a-z]*)', re.IGNORECASE)
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

	fprimary = open('vocabulary/primaryMethods.txt', 'r')
	primaryCookingMethods = []
	for line in fprimary:
		primaryCookingMethods.append(line.replace('\n',''))

	fsecondary = open('vocabulary/secondaryMethods.txt', 'r+')
	secondaryCookingMethods = []
	for line in fsecondary:
		secondaryCookingMethods.append(line.replace('\n',''))

	for instructions in directionsList:
		sentences = sentenceTokenizer.tokenize(instructions)
		#for sentence in sentences:

# def identifyCookingMethods(directionsList):
# 	ingredients = []
# 	for ingredient in ingredientList:
# 		ingredients.append(ingredient.m_IngName)

# 	tools = []			
# 	for tool in toolsList:
# 		tools.append(tool.m_ToolName)

# 	fprimary = open('vocabulary/primaryMethods.txt', 'r')
# 	primaryCookingMethods = []
# 	for line in fprimary:
# 		primaryCookingMethods.append(line.replace('\n',''))

# 	fsecondary = open('vocabulary/secondaryMethods.txt', 'r+')
# 	secondaryCookingMethods = []
# 	for line in fsecondary:
# 		secondaryCookingMethods.append(line.replace('\n',''))	
	
# 	for instructions in directionsList:	
# 		sentences = sentenceTokenizer.tokenize(instructions)
# 		for sentence in sentences:
# 			#pdb.set_trace()
# 			for cookingMethod in primaryCookingMethods:
# 				if cookingMethod in sentence.lower():
# 					methodObject = RecipeRepresentation.Methods()
# 					methodObject.m_MethodName = cookingMethod
# 					methodObject.m_MethodType = 'primary'
# 					for ingredient in ingredients:
# 						if ingredient in sentence.lower():
# 							methodObject.m_ingredientUsed.append(ingredient)
# 					for tool in tools:
# 						if tool in sentence:
# 							methodObject.m_toolsUsed.append(tool)		
# 					cookingMethodsList.append(methodObject)		
# 			for cookingMethod in secondaryCookingMethods:
# 				if cookingMethod in sentence.lower():
# 					methodObject = RecipeRepresentation.Methods()
# 					methodObject.m_MethodName = cookingMethod
# 					methodObject.m_MethodType = 'secondary'
# 					for ingredient in ingredients:
# 						if ingredient in sentence:
# 							methodObject.m_ingredientUsed.append(ingredient)
# 					for tool in tools:
# 						if tool in sentence:
# 							methodObject.m_toolsUsed.append(tool)
# 					cookingMethodsList.append(methodObject)		
# 		searchResult = regExMethods.findall(instructions)
# 		for result in searchResult:
# 			if result[1] in ingredients and result[0] != '':
# 				methodObject = RecipeRepresentation.Methods()
# 				methodObject.m_MethodName = result[0].lower()
# 				methodObject.m_MethodType = 'secondary'
# 				methodObject.m_ingredientUsed.append(result[1])
# 				cookingMethodsList.append(methodObject)	


 		

# def transformCookingMethod():
# 	catTypes = ['bake','broil','barbecue','boil','deep-fry','pan-fry','grill','roast','poach','stir-fry',
# 	'stew','simmer']
# 	ruleTypes = ['bake','broil','barbecue','boil','deep-fry','pan-fry','grill','roast','poach','stir-fry',
# 	'stew','simmer']
# 	toolTypes = ['bake','broil','boil','deep-fry','pan-fry','roast','poach','stir-fry',
# 	'stew','simmer']
# 	json_data = open('vocabulary/methodTransformation.json')
# 	methodData = json.load(json_data)
# 	categories = methodData['categories']
# 	rules = methodData['rules']
# 	tools = methodData['tools']
# 	for methodObject in cookingMethodsList:
# 		if methodObject.m_MethodType == 'secondary':
# 			continue
# 		else:
# 			for rule in ruleTypes:
# 				transformList = methodData['rules'][methodObject.m_MethodName]
# 				for ingredient in methodObject.m_ingredientUsed:
# 					for ingObject in ingredientList:
# 		 				if ingObject.m_IngName == ingredient:
# 							ingType = ingObject.m_IngType
# 							for transform in transformList:
# 								catList = methodData['categories'][transform]
# 								if ingType in catList
# 									m_MethodName.m_optionalMethods.append(transform)