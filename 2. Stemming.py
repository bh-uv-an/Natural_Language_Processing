# Stemming is the process of reducing a word to its stem this is the process of stemming 

## Reviews----> eating, eat,eaten [going,gone,goes]--->go

import nltk
from nltk.stem import PorterStemmer
from nltk.stem import RegexpStemmer
from nltk.stem import SnowballStemmer

words=["eating","eats","eaten","writing","writes","programming","programs","history","finally","finalized"]

for word in words:
    print(word)

#Illustartion of porter Stemmer 
print("\n")
ps = PorterStemmer()
for word in words:
    print(word+"---->"+ps.stem(word))
    
#Illustration of regular expression
print("\n")
rs = RegexpStemmer('ing$|e$|s$|',min=4)
for word in words:
    print(word +"--->"+ rs.stem(word))
    
#Illustartion of snow ball stemmer 
print("\n")
sb = SnowballStemmer(language='english')
for word in words:
    print(word+" ---> "+sb.stem(word))
    
    
# OUTPUT:
# (myenv) D:\GENERATIVE AI>python "2. Stemming.py"
# eating
# eats
# eaten
# writing
# writes
# programming
# programs
# history
# finally
# finalized


# eating---->eat
# eats---->eat
# eaten---->eaten
# writing---->write
# writes---->write
# programming---->program
# programs---->program
# history---->histori
# finally---->final
# finalized---->final


# eating--->eat
# eats--->eat
# eaten--->eaten
# writing--->writ
# writes--->write
# programming--->programm
# programs--->program
# history--->history
# finally--->finally
# finalized--->finalized


# eating ---> eat
# eats ---> eat
# eaten ---> eaten
# writing ---> write
# writes ---> write
# programming ---> program
# programs ---> program
# history ---> histori
# finally ---> final
# finalized ---> final