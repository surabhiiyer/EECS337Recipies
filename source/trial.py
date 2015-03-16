import re
import nltk
import ProjectDictionary
import RecipeRepresentation
import json

sentence = "salt and pepper"

from nltk.tokenize import TreebankWordTokenizer
wordTokenizer = TreebankWordTokenizer()

tokens = wordTokenizer.tokenize(sentence)

posTags = nltk.pos_tag(tokens)

print posTags