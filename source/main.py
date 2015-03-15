#main file
import RecipeRepresentation
import ProjectDictionary
import HelperMethods
import scraper


if __name__ == "__main__":
	print ("\t\t\t\tRECIPE MANAGER: Your personal cooking guide.\n")
	recipeURL = input("Enter the recipe you want to explore: ")
	print("Please wait while I understand the recipe...\n")
	ingredientsDict = scraper.scrapeIngredients(recipeURL)
	directionsList = scraper.getDirections(recipeURL)
	#ProjectDictionary.populateTools()
	print("Reading ingredients...\n")
	HelperMethods.identifyIngredients(ingredientsDict)
	HelperMethods.identifyTools(directionsList)
	HelperMethods.identifyCookingMethods(directionsList)
	HelperMethods.identifyIngredientType()
	HelperMethods.ingredientList
	HelperMethods.cookingMethodsList
	print("Ready!!!\n")

	for ingredient in HelperMethods.ingredientList:
		output = '-->'
		toolName = ''
		for method in HelperMethods.cookingMethodsList:
			if ingredient.m_IngName in method.m_ingredientUsed:
				output += method.m_MethodName + ' '
				for tool in method.m_toolsUsed:
					toolName = tool + ','
		if ingredient.m_IngQuantity != '':
			output += ingredient.m_IngQuantity + ' '
		if ingredient.m_IngMeasurement != '':
			output += ingredient.m_IngMeasurement + ' '
		for prepDescriptor in ingredient.m_IngPrepDescriptor:
			output += prepDescriptor + ','	
		#output = output[:,len(output)-1] + ' '	
		for prep in ingredient.m_IngPreparation:
			output += prep + ','
		#output = output[:,len(output)-1] + ' '	
		for desc in ingredient.m_IngDescriptor:
			output += desc + ','
		#output = output[:,len(output)-1]
		output += ingredient.m_IngName 
		if toolName != '':
			#toolName = toolName[:,len(toolName)-1]
			output += ' in/on a '+toolName
		print output	


									
	print "Ingredients:"
	for ingredient in HelperMethods.ingredientList:
	 	print ingredient.m_IngName + "("+ingredient.m_IngType+")"+ ":" + ingredient.m_IngQuantity + " " + ingredient.m_IngMeasurement
	 	for descriptor in ingredient.m_IngDescriptor:
	 		print descriptor
	 	for preparation in ingredient.m_IngPreparation:
	 		print preparation
	print "Tools required: "
	for tool in HelperMethods.toolsList:
	  	print(tool.m_ToolName)	
	print "Methods: "
	for method in HelperMethods.cookingMethodsList:
	  	for ingredient in method.m_ingredientUsed:
	  		print(method.m_MethodName + " " + ingredient)
	  	for tool in method.m_toolsUsed:
	  		print(tool)	
