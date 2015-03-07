#main file
import RecipeRepresentation
import ProjectDictionary
import HelperMethods


if __name__ == "__main__":
	ProjectDictionary.populateTools()
	toolsList = HelperMethods.identifyTools()
	print "Tools required: "
	for tool in toolsList:
		print(tool.m_ToolName)
	#ProjectDictionary.populateCookingMethods()
	#HelperMethods.identifyCookingMethods()
	#print utensils