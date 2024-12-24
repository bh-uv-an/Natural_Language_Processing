#WordNetLemmatizer 
#this lemmatizer is responsible for finding the root words also it only finds the meaningful word this 
# is lemmatizer

from nltk.stem import WordNetLemmatizer

words = ["eating","eats","eaten","writing","writes","programming","programs","history","finally","finalized"]

lemmatizer = WordNetLemmatizer()

for word in words:
    ele = lemmatizer.lemmatize(word,pos='v')  
    print(word + "----->" + ele)


# #Output:
# finalized----->finalized
# (myenv) PS D:\GENERATIVE AI> python 3.Lematization.py
# eating----->eat
# eats----->eat
# eaten----->eat
# writing----->write
# writes----->write
# programming----->program
# programs----->program
# history----->history
# finally----->finally
# finalized----->finalize