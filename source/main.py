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
	HelperMethods.ingredientList
	HelperMethods.cookingMethodsList
	print("Ready!!!\n")
	print "Ingredients:"
	for ingredient in HelperMethods.ingredientList:
	 	print ingredient.m_IngName + ":" + ingredient.m_IngQuantity + " " + ingredient.m_IngMeasurement
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
