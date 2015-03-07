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

regExTools = re.compile(r'(in\s{0,1}[a]{0,1}|take a) [a-z]+.([a-z]*) ([a-z]+)', re.IGNORECASE)

def identifyTools():
	f = open('vocabulary/tools.txt', 'r+')
	knownTools = []
	for line in f:
		knownTools.append(line)
	instructions = "Heat oil in large nonstick skillet on medium-high heat"
	toolsList = []
	for tool in knownTools:
		if tool in instructions:
			tool = RecipeRepresentation.Tools()
			tool.m_ToolName = toolName
	  		tool.m_ToolQuantity = 1
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
	  	if toolName not in knownTools:
	  		f.write(toolName+'\n')
	  		tool = RecipeRepresentation.Tools()
	  		tool.m_ToolName = toolName
	  		tool.m_ToolQuantity = 1
	  		toolsList.append(tool)	
	return toolsList

#list of cooking methods
cookingMethods = ['boil', 'bake', 'broil', 'blanch', 'braise', 'deep-fry', 'grill', 'pan-fry', 'roast','stir-fry', 'saute', 'simmer', 'steam', 'stew']
secondaryCookingMethods = ['add', 'chop', 'crush', 'mince', 'mix', 'grate', 'stir', 'shake',  'squeeze']
regExMethods = re.compile(r'([a-z]+) with ([a-z]+)', re.IGNORECASE)

def identifyCookingMethods():
	methodMap = dict()
	ingredients = ['cauliflower', 'melted butter', 'salt', 'black pepper']
	instructions = "Bake cauliflower onto prepared baking sheet. Brush each piece of cauliflower with melted butter. Season with salt and black pepper."
	sentences = sentenceTokenizer.tokenize(instructions)
	for sentence in sentences:
		for cookingMethod in cookingMethods:
			if cookingMethod in sentence.lower():
				for ingredient in ingredients:
					if ingredient in sentence:
						methodMap[cookingMethod] = ingredient
		searchResult = regExMethods.findall(sentence)
		print searchResult			
	print methodMap					



