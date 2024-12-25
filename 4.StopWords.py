#Illustration of stopwords 
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

nltk.download('stopwords')
stemmer = PorterStemmer()

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
               
# Tokenizing the paragraph into sentence 
sentences = sent_tokenize(paragraph)

for sentnce in sentences:
    print(sentnce)
    
print("Length of the sentences ",len(sentences))

print("After tokenization of word =  ")
for i in range(len(sentences)):
    # This is word tokenizing Process
    print("\nStemming ")
    word = word_tokenize(sentences[i])
    print(word)
    
    print("\nTokenizing ")
    #Next will be the word stemming process where eating -> eat, drinking -> drink
    words = [stemmer.stem(wor) for wor in word if wor not in set(stopwords.words('english'))]
    print (words)
    
    #THis will Join the words 
    print("After Joining Each Word= ")
    sentences[i] = ' '.join(words)
    print(sentences[i])
    
#After processing the text printing it 
print(sentences)




#Output:


# (myenv) PS D:\GENERATIVE AI> git push origin dev
# Enumerating objects: 4, done.
# Counting objects: 100% (4/4), done.
# Delta compression using up to 8 threads
# Compressing objects: 100% (2/2), done.
# Writing objects: 100% (3/3), 305 bytes | 305.00 KiB/s, done.
# Total 3 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
# remote: Resolving deltas: 100% (1/1), completed with 1 local object.
# To https://github.com/bh-uv-an/Natural_Language_Processing.git
#    ffb5a8a..03842ce  dev -> dev
# (myenv) PS D:\GENERATIVE AI> python .\4.StopWords.py
# [nltk_data] Downloading package stopwords to
# [nltk_data]     C:\Users\LENOVO\AppData\Roaming\nltk_data...
# [nltk_data]   Package stopwords is already up-to-date!
# I have three visions for India.
# In 3000 years of our history, people from all over
#                the world have come and invaded us, captured our lands, conquered our minds.
# From Alexander onwards, the Greeks, the Turks, the Moguls, the Portuguese, the British,
#                the French, the Dutch, all of them came and looted us, took over what was ours.
# Yet we have not done this to any other nation.
# We have not conquered anyone.
# We have not grabbed their land, their culture,
#                their history and tried to enforce our way of life on them.
# Why?
# Because we respect the freedom of others.That is why my
#                first vision is that of freedom.
# I believe that India got its first vision of
#                this in 1857, when we started the War of Independence.
# It is this freedom that
#                we must protect and nurture and build on.
# If we are not free, no one will respect us.
# My second vision for India’s development.
# For fifty years we have been a developing nation.
# It is time we see ourselves as a developed nation.
# We are among the top 5 nations of the world
#                in terms of GDP.
# We have a 10 percent growth rate in most areas.
# Our poverty levels are falling.
# Our achievements are being globally recognised today.
# Yet we lack the self-confidence to
#                see ourselves as a developed nation, self-reliant and self-assured.
# Isn’t this incorrect?
# I have a third vision.
# India must stand up to the world.
# Because I believe that unless India
#                stands up to the world, no one will respect us.
# Only strength respects strength.
# We must be
#                strong not only as a military power but also as an economic power.
# Both must go hand-in-hand.
# My good fortune was to have worked with three great minds.
# Dr. Vikram Sarabhai of the Dept.
# of
#                space, Professor Satish Dhawan, who succeeded him and Dr. Brahm Prakash, father of nuclear material.
# I was lucky to have worked with all three of them closely and consider this the great opportunity of my life.
# I see four milestones in my career
# Length of the sentences  31
# After tokenization of word =

# Stemming
# ['I', 'have', 'three', 'visions', 'for', 'India', '.']

# Tokenizing
# ['i', 'three', 'vision', 'india', '.']
# After Joining Each Word=
# i three vision india .

# Stemming
# ['In', '3000', 'years', 'of', 'our', 'history', ',', 'people', 'from', 'all', 'over', 'the', 'world', 'have', 'come', 'and', 'invaded', 'us', ',', 'captured', 'our', 'lands', ',', 'conquered', 'our', 'minds', '.']

# Tokenizing
# ['in', '3000', 'year', 'histori', ',', 'peopl', 'world', 'come', 'invad', 'us', ',', 'captur', 'land', ',', 'conquer', 'mind', '.']
# After Joining Each Word=
# in 3000 year histori , peopl world come invad us , captur land , conquer mind .

# Stemming
# ['From', 'Alexander', 'onwards', ',', 'the', 'Greeks', ',', 'the', 'Turks', ',', 'the', 'Moguls', ',', 'the', 'Portuguese', ',', 'the', 'British', ',', 'the', 'French', ',', 'the', 'Dutch', ',', 'all', 'of', 'them', 'came', 'and', 'looted', 'us', ',', 'took', 'over', 'what', 'was', 'ours', '.']

# Tokenizing
# ['from', 'alexand', 'onward', ',', 'greek', ',', 'turk', ',', 'mogul', ',', 'portugues', ',', 'british', ',', 'french', ',', 'dutch', ',', 'came', 'loot', 'us', ',', 'took', '.']
# After Joining Each Word=
# from alexand onward , greek , turk , mogul , portugues , british , french , dutch , came loot us , took .

# Stemming
# ['Yet', 'we', 'have', 'not', 'done', 'this', 'to', 'any', 'other', 'nation', '.']

# Tokenizing
# ['yet', 'done', 'nation', '.']
# After Joining Each Word=
# yet done nation .

# Stemming
# ['We', 'have', 'not', 'conquered', 'anyone', '.']

# Tokenizing
# ['we', 'conquer', 'anyon', '.']
# After Joining Each Word=
# we conquer anyon .

# Stemming
# ['We', 'have', 'not', 'grabbed', 'their', 'land', ',', 'their', 'culture', ',', 'their', 'history', 'and', 'tried', 'to', 'enforce', 'our', 'way', 'of', 'life', 'on', 'them', '.']

# Tokenizing
# ['we', 'grab', 'land', ',', 'cultur', ',', 'histori', 'tri', 'enforc', 'way', 'life', '.']
# After Joining Each Word=
# we grab land , cultur , histori tri enforc way life .

# Stemming
# ['Why', '?']

# Tokenizing
# ['whi', '?']
# After Joining Each Word=
# whi ?

# Stemming
# ['Because', 'we', 'respect', 'the', 'freedom', 'of', 'others.That', 'is', 'why', 'my', 'first', 'vision', 'is', 'that', 'of', 'freedom', '.']

# Tokenizing
# ['becaus', 'respect', 'freedom', 'others.that', 'first', 'vision', 'freedom', '.']
# After Joining Each Word=
# becaus respect freedom others.that first vision freedom .

# Stemming
# ['I', 'believe', 'that', 'India', 'got', 'its', 'first', 'vision', 'of', 'this', 'in', '1857', ',', 'when', 'we', 'started', 'the', 'War', 'of', 'Independence', '.']

# Tokenizing
# ['i', 'believ', 'india', 'got', 'first', 'vision', '1857', ',', 'start', 'war', 'independ', '.']
# After Joining Each Word=
# i believ india got first vision 1857 , start war independ .

# Stemming
# ['It', 'is', 'this', 'freedom', 'that', 'we', 'must', 'protect', 'and', 'nurture', 'and', 'build', 'on', '.']

# Tokenizing
# ['it', 'freedom', 'must', 'protect', 'nurtur', 'build', '.']
# After Joining Each Word=
# it freedom must protect nurtur build .

# Stemming
# ['If', 'we', 'are', 'not', 'free', ',', 'no', 'one', 'will', 'respect', 'us', '.']

# Tokenizing
# ['if', 'free', ',', 'one', 'respect', 'us', '.']
# After Joining Each Word=
# if free , one respect us .

# Stemming
# ['My', 'second', 'vision', 'for', 'India', '’', 's', 'development', '.']

# Tokenizing
# ['my', 'second', 'vision', 'india', '’', 'develop', '.']
# After Joining Each Word=
# my second vision india ’ develop .

# Stemming
# ['For', 'fifty', 'years', 'we', 'have', 'been', 'a', 'developing', 'nation', '.']

# Tokenizing
# ['for', 'fifti', 'year', 'develop', 'nation', '.']
# After Joining Each Word=
# for fifti year develop nation .

# Stemming
# ['It', 'is', 'time', 'we', 'see', 'ourselves', 'as', 'a', 'developed', 'nation', '.']

# Tokenizing
# ['it', 'time', 'see', 'develop', 'nation', '.']
# After Joining Each Word=
# it time see develop nation .

# Stemming
# ['We', 'are', 'among', 'the', 'top', '5', 'nations', 'of', 'the', 'world', 'in', 'terms', 'of', 'GDP', '.']

# Tokenizing
# ['we', 'among', 'top', '5', 'nation', 'world', 'term', 'gdp', '.']
# After Joining Each Word=
# we among top 5 nation world term gdp .

# Stemming
# ['We', 'have', 'a', '10', 'percent', 'growth', 'rate', 'in', 'most', 'areas', '.']

# Tokenizing
# ['we', '10', 'percent', 'growth', 'rate', 'area', '.']
# After Joining Each Word=
# we 10 percent growth rate area .

# Stemming
# ['Our', 'poverty', 'levels', 'are', 'falling', '.']

# Tokenizing
# ['our', 'poverti', 'level', 'fall', '.']
# After Joining Each Word=
# our poverti level fall .

# Stemming
# ['Our', 'achievements', 'are', 'being', 'globally', 'recognised', 'today', '.']

# Tokenizing
# ['our', 'achiev', 'global', 'recognis', 'today', '.']
# After Joining Each Word=
# our achiev global recognis today .

# Stemming
# ['Yet', 'we', 'lack', 'the', 'self-confidence', 'to', 'see', 'ourselves', 'as', 'a', 'developed', 'nation', ',', 'self-reliant', 'and', 'self-assured', '.']

# Tokenizing
# ['yet', 'lack', 'self-confid', 'see', 'develop', 'nation', ',', 'self-reli', 'self-assur', '.']
# After Joining Each Word=
# yet lack self-confid see develop nation , self-reli self-assur .

# Stemming
# ['Isn', '’', 't', 'this', 'incorrect', '?']

# Tokenizing
# ['isn', '’', 'incorrect', '?']
# After Joining Each Word=
# isn ’ incorrect ?

# Stemming
# ['I', 'have', 'a', 'third', 'vision', '.']

# Tokenizing
# ['i', 'third', 'vision', '.']
# After Joining Each Word=
# i third vision .

# Stemming
# ['India', 'must', 'stand', 'up', 'to', 'the', 'world', '.']

# Tokenizing
# ['india', 'must', 'stand', 'world', '.']
# After Joining Each Word=
# india must stand world .

# Stemming
# ['Because', 'I', 'believe', 'that', 'unless', 'India', 'stands', 'up', 'to', 'the', 'world', ',', 'no', 'one', 'will', 'respect', 'us', '.']

# Tokenizing
# ['becaus', 'i', 'believ', 'unless', 'india', 'stand', 'world', ',', 'one', 'respect', 'us', '.']
# After Joining Each Word=
# becaus i believ unless india stand world , one respect us .

# Stemming
# ['Only', 'strength', 'respects', 'strength', '.']

# Tokenizing
# ['onli', 'strength', 'respect', 'strength', '.']
# After Joining Each Word=
# onli strength respect strength .

# Stemming
# ['We', 'must', 'be', 'strong', 'not', 'only', 'as', 'a', 'military', 'power', 'but', 'also', 'as', 'an', 'economic', 'power', '.']

# Tokenizing
# ['we', 'must', 'strong', 'militari', 'power', 'also', 'econom', 'power', '.']
# After Joining Each Word=
# we must strong militari power also econom power .

# Stemming
# ['Both', 'must', 'go', 'hand-in-hand', '.']

# Tokenizing
# ['both', 'must', 'go', 'hand-in-hand', '.']
# After Joining Each Word=
# both must go hand-in-hand .

# Stemming
# ['My', 'good', 'fortune', 'was', 'to', 'have', 'worked', 'with', 'three', 'great', 'minds', '.']

# Tokenizing
# ['my', 'good', 'fortun', 'work', 'three', 'great', 'mind', '.']
# After Joining Each Word=
# my good fortun work three great mind .

# Stemming
# ['Dr.', 'Vikram', 'Sarabhai', 'of', 'the', 'Dept', '.']

# Tokenizing
# ['dr.', 'vikram', 'sarabhai', 'dept', '.']
# After Joining Each Word=
# dr. vikram sarabhai dept .

# Stemming
# ['of', 'space', ',', 'Professor', 'Satish', 'Dhawan', ',', 'who', 'succeeded', 'him', 'and', 'Dr.', 'Brahm', 'Prakash', ',', 'father', 'of', 'nuclear', 'material', '.']

# Tokenizing
# ['space', ',', 'professor', 'satish', 'dhawan', ',', 'succeed', 'dr.', 'brahm', 'prakash', ',', 'father', 'nuclear', 'materi', '.']
# After Joining Each Word=
# space , professor satish dhawan , succeed dr. brahm prakash , father nuclear materi .

# Stemming
# ['I', 'was', 'lucky', 'to', 'have', 'worked', 'with', 'all', 'three', 'of', 'them', 'closely', 'and', 'consider', 'this', 'the', 'great', 'opportunity', 'of', 'my', 'life', '.']

# Tokenizing
# ['i', 'lucki', 'work', 'three', 'close', 'consid', 'great', 'opportun', 'life', '.']
# After Joining Each Word=
# i lucki work three close consid great opportun life .

# Stemming
# ['I', 'see', 'four', 'milestones', 'in', 'my', 'career']

# Tokenizing
# ['i', 'see', 'four', 'mileston', 'career']
# After Joining Each Word=
# i see four mileston career
# ['i three vision india .', 'in 3000 year histori , peopl world come invad us , captur land , conquer mind .', 'from alexand onward , greek , turk , mogul , portugues , british , french , dutch , came loot us , took .', 'yet done nation .', 'we conquer anyon .', 'we grab land , cultur , histori tri enforc way life .', 'whi ?', 'becaus respect freedom others.that first vision freedom .', 'i believ india got first vision 1857 , start war independ .', 'it freedom must protect nurtur build .', 'if free , one respect us .', 'my second vision india ’ develop .', 'for fifti year develop nation .', 'it time see develop nation .', 'we among top 5 nation world term gdp .', 'we 10 percent growth rate area .', 'our poverti level fall .', 'our achiev global recognis today .', 'yet lack self-confid see develop nation , self-reli self-assur .', 'isn ’ incorrect ?', 'i third vision .', 'india must stand world .', 'becaus i believ unless india stand world , one respect us .', 'onli strength respect strength .', 'we must strong militari power also econom power .', 'both must go hand-in-hand .', 'my good fortun work three great mind .', 'dr. vikram sarabhai dept .', 'space , professor satish dhawan , succeed dr. brahm prakash , father nuclear materi .', 'i lucki work three close consid great opportun life .', 'i see four mileston career']
# (myenv) PS D:\GENERATIVE AI>