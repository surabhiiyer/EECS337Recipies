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
		self.m_IngQuantity = ''
		self.m_IngMeasurement = ''
		self.m_IngDescriptor = []
		self.m_IngPreparation = []
		self.m_IngPrepDescriptor = []

class Tools:
	def __init__(self):
		self.m_ToolName = ''
		self.m_ToolQuantity = 0

class Methods:
	def __init__(self):
		self.m_MethodName = [] #Method name
		self.m_MethodType = '' #Cooking method type - Primary or Secondary
		self.m_ingredientUsed = [] #Ingredient on which the method has to be applied
		self.m_toolsUsed = []
		self.m_time = 0

class TransformMethods:
	def __init__(self):
		self.m_methodName = []
		self.m_ingredient = ''
		self.m_originalMethod = ''	
		
class Transformed_Indian: 
	def __init__(self): 
		self.m_IngName = ''

class Transformed_Italian: 
	def __init__(self): 
		self.m_IngName = ''

class Transformed_Mexican: 
	def __init__(self): 
		self.m_IngName = ''

class Transformed_Vegetarian:  
	def __init__(self): 
		self.m_IngName = ''

class Transformed_NonVegetarian:  
	def __init__(self): 
		self.m_IngName = ''

class Transformed_Vegan:  
	def __init__(self): 
		self.m_IngName = ''

class Transformed_EastAsian:  
	def __init__(self): 
		self.m_IngName = ''

class Transformed_French:  
	def __init__(self): 
		self.m_IngName = ''





