import pandas as pd
from nltk.stem import SnowballStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

#initializing all default values 
stemmer = SnowballStemmer('english')

# Read the CSV file without predefined column names to inspect the structure
data = pd.read_csv(r'D:\GENERATIVE AI\spam.csv', sep=',', quotechar='"', encoding='ISO-8859-1', usecols=[0, 1],names=["label", "message"])


# Display the first few rows to inspect the structure
print(data.head())

#data clenaing and pre processing 
for i in range(len(data)):
    # print(data['message'].iloc[i])
    tokenized_word = word_tokenize(data['message'].iloc[i])
    print(tokenized_word)

    
