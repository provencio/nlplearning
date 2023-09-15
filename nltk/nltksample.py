import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from nltk import pos_tag

# Download necessary NLTK resources (might need to run this once)
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')

# Sample text for NLP tasks
text = """
The Boston Mountain region of the Ozarks is a breathtaking landscape 
located in the northwestern part of Arkansas. This area is renowned 
for its rugged beauty and natural splendor. Its distinctive features 
include steep, rocky hillsides covered in dense hardwood forests and 
picturesque valleys that cradle pristine rivers. The Boston Mountains 
offer a haven for outdoor enthusiasts, with hiking trails that wind 
through lush woodlands, providing stunning vistas of the surrounding 
landscape. This region is not only a paradise for nature lovers but 
also a place deeply rooted in history, where the legacy of early 
pioneers and their frontier spirit can still be felt today. Whether 
you're seeking outdoor adventure or a glimpse into the past, the Boston 
Mountain region of the Ozarks has something truly special to offer.
"""

# Tokenization: Split the text into words and sentences
words = word_tokenize(text)
sentences = sent_tokenize(text)

print("Tokenized Words:")
print(words)
print("\nTokenized Sentences:")
print(sentences)

# Stemming: Reduce words to their base form (stem)
stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in words]
print("\nStemmed Words:")
print(stemmed_words)

# Frequency Distribution: Calculate word frequencies
freq_dist = FreqDist(words)
print("\nWord Frequencies:")
print(freq_dist.most_common(5))  # Display the 5 most common words

# Stopword Removal: Remove common words (e.g., 'the', 'is', 'a')
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in words if word.lower() not in stop_words]
print("\nWords after Stopword Removal:")
print(filtered_words)

# Part-of-Speech Tagging: Tag words with their parts of speech
pos_tags = pos_tag(words)
print("\nPart-of-Speech Tags:")
print(pos_tags)
