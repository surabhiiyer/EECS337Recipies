# contains methods that assist in formulating recipes
import re
import nltk
import ProjectDictionary
import RecipeRepresentation

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
		for (data,tag) in posTags:
			if(tag == 'NN' or tag == 'NNS'):
				ingObject.m_IngName = data
			elif(tag == 'JJ'):
				ingObject.m_IngDescriptor.append(data)
			elif(tag == 'VB' or tag == 'VBD' or tag == 'VBP' or tag == 'VBN' or tag == 'VBG' or tag == 'VBZ'):
				ingObject.m_IngPreparation.append(data)
			elif(tag == 'RB'):
				ingObject.m_IngPrepDescriptor.append(data)	
		if(ingObject.m_IngName != ''):
			ingredientList.append(ingObject)	
		
	 						



