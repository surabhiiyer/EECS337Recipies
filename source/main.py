#main file
import RecipeRepresentation
import ProjectDictionary
import HelperMethods
import scraper
import json
import userInput

if __name__ == "__main__":
	print ("\t\t\t\tRECIPE MANAGER: Your personal cooking guide.\n")
	recipeURL = input("Enter the URL of the recipe you want to explore: ")
	print("Please wait while I understand the recipe...\n")
	ingredientsDict = scraper.scrapeIngredients(recipeURL)
	directionsList = scraper.getDirections(recipeURL)
	#scraper.populateTools()
	print("Reading ingredients...\n")
	HelperMethods.identifyIngredients(ingredientsDict)
	HelperMethods.identifyTools(directionsList)
	HelperMethods.identifyCookingMethods(directionsList)
	print("Ready!!!\n")
	scraper.getPrepTimeRating(recipeURL)									
	print "\tIngredients:"
	for ingredient in HelperMethods.ingredientList:
		output = ''
		if(ingredient.m_IngQuantity != ''):
		 	output = output + ingredient.m_IngQuantity + ' '
		if(ingredient.m_IngMeasurement != ''):
		  	output = output + ingredient.m_IngMeasurement + ' '
		if(len(ingredient.m_IngDescriptor) == 0):
	 	 	output = output + ingredient.m_IngName + ' '
	 	else:
		    for descriptor in ingredient.m_IngDescriptor:
		    	if(descriptor != ''):
					output = output + descriptor + ','
	  		output = output[:len(output)-1] + ' ' + ingredient.m_IngName + ' '
	 	if(len(ingredient.m_IngPreparation)>0 or len(ingredient.m_IngPrepDescriptor)>0):
	 		output = output + '--> '
	 		if(len(ingredient.m_IngPrepDescriptor)>0):
	 			for prepDescriptor in ingredient.m_IngPrepDescriptor:
	 				if(prepDescriptor != ''):
	 					output = output + prepDescriptor + ','
	 			output = output[:len(output)-1] + ' '						  
	 	 	if(len(ingredient.m_IngPreparation)>0):
 				for prep in ingredient.m_IngPreparation:
 					if(prep != ''):
 						output = output + prep + ','
 				output = output[:len(output)-1] + ' '
 		print output
 	print "\n"										
	print "\tDirections: "
	step = 0
	for methodObj in HelperMethods.cookingMethodsList:
		if(len(methodObj.m_MethodName)>0 and len(methodObj.m_ingredientUsed)>0):
			step = step + 1
			output = str(step) + '. '
			for index in range(0,len(methodObj.m_MethodName)):
				output = output + methodObj.m_MethodName[index] + ' -> '
			output = output[:len(output)-3] + 'following ingredients: '	
			for ingObject in methodObj.m_ingredientUsed:
				output = output + ingObject.m_IngName + ','
			output = output[:len(output)-1] + '.'		
	  		if(len(methodObj.m_toolsUsed)>0):
	  			output = output + ' Use '
	  			for toolObject in methodObj.m_toolsUsed:
	  				output = output + toolObject.m_ToolName + ','
	  			output = output[:len(output)-1] + '.'
	  		if(methodObj.m_time > 0):
	  			output = output + 'Time for this step: ' + str(methodObj.m_time) + ' minutes.'	
	  		print output

	nameType_dict = HelperMethods.createDictionary()
	print "\n"
	print ("\tYou can also transform the recipe to your liking.\n")  		
	while(1):
		print("\tSelect a transformation:")
		print("1. To vegetarian/non-vegetarian/vegan")
		print("2. Change the Cuisine")
		print("3. Change the Cooking Method")
		print("4.To Exit")
		option = input("Enter your choice: ")
		
		if option == 1:
			# Veg, Non Veg and Vegan Transfromations 
			user_in = userInput.TrandformationVegNonVeg()
			choice = int(user_in)
			if choice == 1: 
				print "You typed 1. Transforming to Vegan\n"
				userInput.TransformToVegan(nameType_dict)
			elif choice == 2: 
				print "You typed 2. Transforming to Vegan\n"
				userInput.TransformToNonVegetarian(nameType_dict)
			elif choice == 3: 
				print "You typed 3. Transforming to Vegetarian\n"
				userInput.TransformToVegetarian(nameType_dict)
			else: 
				print "Please enter a valid input "

		#Cuisine Transformations 
		if option == 2: 
			user_in = userInput.TransformationCuisine()
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
				print "You typed 4. Transforming to East Asian\n"
				userInput.TransformToEastAsian(nameType_dict)
			elif choice == 5: 
				print "You typed 5. Transforming to French\n"
				userInput.TransformToFrench(nameType_dict)
			else: 
				print "Please enter the correct values"
		if option == 3:
			HelperMethods.transformCookingMethod()
			if(len(HelperMethods.transformMethodList)>0):
				json_data = open('vocabulary/methodTransformation.json')
				methodData = json.load(json_data)
				methodsSelected = dict()
				originalMethod = dict()
				for transformObject in HelperMethods.transformMethodList:
					output = "You can make the following changes to: " + transformObject.m_ingredient.m_IngName
					print output
					output = ''
					index = 0
					for method in transformObject.m_methodName:
						index = index + 1
						output = output + str(index) + "." + method + " " 
					output = output[:len(output)-1] + ". Select an option."
					option = input(output)
					methodName = transformObject.m_methodName[option - 1]
					methodsSelected[methodName] = transformObject.m_ingredient.m_IngName
					originalMethod[transformObject.m_ingredient.m_IngName] = transformObject.m_originalMethod
				for key in methodsSelected:
					ing = methodsSelected[key]
					output = key + " " +  ing + " ,instead of " +  originalMethod[ing] + ". New tools required: "
					toolsList = methodData['tools'][key]
					for tool in toolsList:
						output = output + tool + ', '
					output = output[:len(output)-2] + "."	
					print output
			else:
				print "Cannot find another cooking method for this recipe. Please try another transformation."
		if option == 4:
			print "\t\tBon Appetit!!!!"
			break				  							
