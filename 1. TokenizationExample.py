#If we want to use multi line comments then we have to use """ """

import nltk
from nltk.tokenize import sent_tokenize #responsible for converting the corpus into sentences 
from nltk.tokenize import word_tokenize #responsible for converting the corpus into words
from nltk.tokenize import wordpunct_tokenize #responsible for considering each punctuations into a separeate words
from nltk.tokenize import TreebankWordTokenizer #responsible for converting corpus into words 

nltk.download('punkt_tab')

corpus = """Unlock the world of data science with our Data Science Classroom Program. Master Python, machine learning, and visualization to excel in data-driven industries. Elevate your career with skill's that drive innovation and informed decision-making!"""
        
#printing the corpus before tokenizing 
print("\n Document = ",corpus)

#Tokenizing the above corpus into sentences then it will be
print("\n")
documents = sent_tokenize(corpus) #this will convert the corpus into documents 
for i,document in enumerate(documents):
    print(f"Document {i} = ",document)
    
#Tokenizing the above corpus into words using nltk
print("\n")
words = word_tokenize(corpus) #this will convert the corpus into words 
print("Words= ",words)
##Ouput:
# Words=  ['Unlock', 'the', 'world', 'of', 'data', 'science', 'with', 'our', 'Data', 'Science', 'Classroom',
#         'Program', '.', 'Master', 'Python', ',', 'machine', 'learning', ',', 'and', 'visualization', 'to', 
#         'excel', 'in', 'data-driven', 'industries', '.', 'Elevate', 'your', 'career', 'with', 'skill', 
#         "'s", 'that', 'drive', 'innovation', 'and', 'informed', 'decision-making', '!']
# Here in the above we can see that 's is considered to be a single word this can be remved using 
# wordpunkt.tokenize

#Making the punctuations also into a single words this can be done 
print("\n")
word_punct = wordpunct_tokenize(corpus)
print("WordPunkt = ",word_punct)
##output:
# WordPunkt =  ['Unlock', 'the', 'world', 'of', 'data', 'science', 'with', 'our', 'Data', 'Science', 
#               'Classroom', 'Program', '.', 'Master', 'Python', ',', 'machine', 'learning', ',', 
#               'and', 'visualization', 'to', 'excel', 'in', 'data', '-', 'driven', 'industries', '.', 
#               'Elevate', 'your', 'career', 'with', 'skill', "'", 's', 'that', 'drive', 'innovation', 
#               'and', 'informed', 'decision', '-', 'making', '!']
#here it is considering ' s both into a single word 

#Making use of tree bank word tokenizer
print("\n")
tokenizer = TreebankWordTokenizer()
treebanktokenizer = tokenizer.tokenize(corpus)
print("TreebankWordTokenizer = ",treebanktokenizer)
##output:
# TreebankWordTokenizer =  ['Unlock', 'the', 'world', 'of', 'data', 'science', 'with', 'our', 'Data', 
#                           'Science', 'Classroom', 'Program.', 'Master', 'Python', ',', 'machine', 
#                           'learning', ',', 'and', 'visualization', 'to', 'excel', 'in', 'data-driven', 
#                           'industries.', 'Elevate', 'your', 'career', 'with', 'skill', "'s", 'that', 
#                           'drive', 'innovation', 'and', 'informed', 'decision-making', '!']
#here the in between of sentences the full stop will not be considered as separate but at the end it will 
# be considered t be the end 

###### OUTPUT #####

# (myenv) D:\GENERATIVE AI>python TokenizationExample.py
# [nltk_data] Downloading package punkt_tab to
# [nltk_data]     C:\Users\LENOVO\AppData\Roaming\nltk_data...
# [nltk_data]   Package punkt_tab is already up-to-date!

#  Document =  Unlock the world of data science with our Data Science Classroom Program. Master Python, machine learning, and visualization to excel in data-driven industries. Elevate your career with skill's that drive innovation and informed decision-making!


# Document 0 =  Unlock the world of data science with our Data Science Classroom Program.
# Document 1 =  Master Python, machine learning, and visualization to excel in data-driven industries.
# Document 2 =  Elevate your career with skill's that drive innovation and informed decision-making!


# Words=  ['Unlock', 'the', 'world', 'of', 'data', 'science', 'with', 'our', 'Data', 'Science', 
# 'Classroom', 'Program', '.', 'Master', 'Python', ',', 'machine', 'learning', ',', 'and', 'visualization'
# , 'to', 'excel', 'in', 'data-driven', 'industries', '.', 'Elevate', 'your', 'career', 'with', 'skill', 
# "'s", 'that', 'drive', 'innovation', 'and', 'informed', 'decision-making', '!']


# WordPunkt =  ['Unlock', 'the', 'world', 'of', 'data', 'science', 'with', 'our', 'Data', 'Science', 
# 'Classroom', 'Program', '.', 'Master', 'Python', ',', 'machine', 'learning', ',', 'and', 'visualization'
# , 'to', 'excel', 'in', 'data', '-', 'driven', 'industries', '.', 'Elevate', 'your', 'career', 'with', 
# 'skill', "'", 's', 'that', 'drive', 'innovation', 'and', 'informed', 'decision', '-', 'making', '!']


# TreebankWordTokenizer =  ['Unlock', 'the', 'world', 'of', 'data', 'science', 'with', 'our', 'Data', 
# 'Science', 'Classroom', 'Program.', 'Master', 'Python', ',', 'machine', 'learning', ',', 'and', 
# 'visualization', 'to', 'excel', 'in', 'data-driven', 'industries.', 'Elevate', 'your', 'career', 'with',
# 'skill', "'s", 'that', 'drive', 'innovation', 'and', 'informed', 'decision-making', '!']
