#main file
import RecipeRepresentation
import ProjectDictionary
import HelperMethods
import scraper
import userInput

if __name__ == "__main__":
	print ("\t\t\t\tRECIPE MANAGER: Your personal cooking guide.\n")
	# print ("Enter the recipe you want to explore: ")
	# recipeName = raw_input()
	# recipeURL = ""
	#recipeURL = input("Enter the recipe you want to explore: ")
	recipeURL = "http://allrecipes.com/Recipe/Chilly-Day-Chili/Detail.aspx?event8=1&prop24=SR_Thumb&e11=chilli%20chicken&e8=Quick%20Search&event10=1&e7=Recipe&soid=sr_results_p1i1"
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
	
	## Take the user input and ask them for the transformation
	print("Ready!!!\n")
	
	## Harsh Code from here ###
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


	ing_nameList = []
	ing_typeList = []
					
	c = 0 	
	print "Ingredients:"
	for ingredient in HelperMethods.ingredientList:
	 	print ingredient.m_IngName + "("+ingredient.m_IngType+")"+ ":" + ingredient.m_IngQuantity + " " + ingredient.m_IngMeasurement
	 	ing_nameList.append(ingredient.m_IngName)
	 	ing_typeList.append(ingredient.m_IngType)
	 	for descriptor in ingredient.m_IngDescriptor:
	 		print descriptor
	 	for preparation in ingredient.m_IngPreparation:
	 		print preparation
	nameType_dict = dict(zip(ing_nameList,ing_typeList))
	print len(nameType_dict)

	print "Tools required: "
	for tool in HelperMethods.toolsList:
	  	print(tool.m_ToolName)	
	print "Methods: "
	for method in HelperMethods.cookingMethodsList:
	  	for ingredient in method.m_ingredientUsed:
	  		print(method.m_MethodName + " " + ingredient)
	  	for tool in method.m_toolsUsed:
	  		print(tool)	


	# CUISINE TRANSFORMATIONS :
	user_in = userInput.TransformationChoice()
	print "##### CHOICE ####",user_in
	choice = int(user_in)
	if choice == 1: 
		print "You tyed 1. Transforming to Indian"
		userInput.TranformToIndian(nameType_dict)
		# call a transformation function from the file userInput
	elif choice == 2: 
		print "You typed 2. Transforming to Mexican\n"
		userInput.TransformToMexican(nameType_dict)
	elif choice == 3: 
		print "You typed 3. Transforming to Italian\n"
		userInput.TransformToItalian(nameType_dict)
	elif choice == 4: 
		print "You typed 4. Transforming to Vegan\n"
		userInput.TransformToVegan(nameType_dict)
	elif choice == 5: 
		print "You typed 5. Transforming to Vegan\n"
		userInput.TransformToNonVegetarian(nameType_dict)
	elif choice == 6: 
		print "You typed 6. Transforming to Vegetarian\n"
		userInput.TransformToVegetarian(nameType_dict)
	else: 
		print "Please enter a valid input "
