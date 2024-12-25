import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

nltk.download('stopwords')
lemmatizer = WordNetLemmatizer()

## Speech Of DR APJ Abdul Kalam
paragraph = """I have three visions for India. In 3000 years of our history, people from all over 
               the world have come and invaded us, captured our lands, conquered our minds. 
               From Alexander onwards, the Greeks, the Turks, the Moguls, the Portuguese, the British,
               the French, the Dutch, all of them came and looted us, took over what was ours. 
               Yet we have not done this to any other nation. We have not conquered anyone. 
               We have not grabbed their land, their culture, 
               their history and tried to enforce our way of life on them. 
               Why? Because we respect the freedom of others.That is why my 
               first vision is that of freedom. I believe that India got its first vision of 
               this in 1857, when we started the War of Independence. It is this freedom that
               we must protect and nurture and build on. If we are not free, no one will respect us.
               My second vision for India’s development. For fifty years we have been a developing nation.
               It is time we see ourselves as a developed nation. We are among the top 5 nations of the world
               in terms of GDP. We have a 10 percent growth rate in most areas. Our poverty levels are falling.
               Our achievements are being globally recognised today. Yet we lack the self-confidence to
               see ourselves as a developed nation, self-reliant and self-assured. Isn’t this incorrect?
               I have a third vision. India must stand up to the world. Because I believe that unless India 
               stands up to the world, no one will respect us. Only strength respects strength. We must be 
               strong not only as a military power but also as an economic power. Both must go hand-in-hand. 
               My good fortune was to have worked with three great minds. Dr. Vikram Sarabhai of the Dept. of 
               space, Professor Satish Dhawan, who succeeded him and Dr. Brahm Prakash, father of nuclear material.
               I was lucky to have worked with all three of them closely and consider this the great opportunity of my life. 
               I see four milestones in my career"""
               
Tokenized_Sentence = sent_tokenize(paragraph)
# print(Tokenized_Sentence)

for i in range(len(Tokenized_Sentence)):
    word = word_tokenize(Tokenized_Sentence[i])
    word = [lemmatizer.lemmatize(words,pos='v') for words in word if words not in set(stopwords.words('english'))]
    Tokenized_Sentence[i] = ' '.join(word)

print("Tokenized and processed output is :")
for i in Tokenized_Sentence:
    print(i)
    
    
# OUTPUT:
#         (myenv) PS D:\GENERATIVE AI\Practice Set> python .\PrecticeSet2.py
# [nltk_data] Downloading package stopwords to
# [nltk_data]     C:\Users\LENOVO\AppData\Roaming\nltk_data...
# [nltk_data]   Package stopwords is already up-to-date!

# Tokenized and processed output is :
# I three visions India .
# In 3000 years history , people world come invade us , capture land , conquer mind .
# From Alexander onwards , Greeks , Turks , Moguls , Portuguese , British , French , Dutch , come loot us , take .
# Yet do nation .
# We conquer anyone .
# We grab land , culture , history try enforce way life .
# Why ?
# Because respect freedom others.That first vision freedom .
# I believe India get first vision 1857 , start War Independence .
# It freedom must protect nurture build .
# If free , one respect us .
# My second vision India ’ development .
# For fifty years develop nation .
# It time see develop nation .
# We among top 5 nations world term GDP .
# We 10 percent growth rate areas .
# Our poverty level fall .
# Our achievements globally recognise today .
# Yet lack self-confidence see develop nation , self-reliant self-assured .
# Isn ’ incorrect ?
# I third vision .
# India must stand world .
# Because I believe unless India stand world , one respect us .
# Only strength respect strength .
# We must strong military power also economic power .
# Both must go hand-in-hand .
# My good fortune work three great mind .
# Dr. Vikram Sarabhai Dept .
# space , Professor Satish Dhawan , succeed Dr. Brahm Prakash , father nuclear material .
# I lucky work three closely consider great opportunity life .
# I see four milestones career
# (myenv) PS D:\GENERATIVE AI\Practice Set>