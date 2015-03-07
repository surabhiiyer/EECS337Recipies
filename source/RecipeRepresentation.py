#class to store basic information about a recipe
class Recipe:
	 def __init__(self):
	 	self.m_recipeName = ''
	 	self.m_recipeRating = 0.0
	 	self.m_cookingTime = 0.0
	 	self.m_prepTime = 0.0
	 	self.m_servings = 0

#associated with every recipe class are classes Ingredients, Tools and Methods 
class Ingredients:
	def __init__(self):
		self.m_IngName = ''
		self.m_IngType = ''
		self.m_IngQuantity = 0.0
		self.m_IngMeasurement = ''
		self.m_IngDescriptor = ''
		self.m_IngPreparation = ''
		self.m_IngPrepDescriptor = ''

class Tools:
	def __init__(self):
		self.m_ToolName = ''
		self.m_ToolQuantity = 0

class Methods:
	def __init__(self):
		self.m_MethodName = '' #Method name
		self.m_MethodType = '' #Cooking method type - Primary or Secondary
		self.m_ingredientUsed = [] #Ingredient on which the method has to be applied