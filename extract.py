# author: ricardo lezama
import nltk 

def find_bigrams(t):
    list = []
    for a in t:
        token = nltk.word_tokenize(a)
        stop_words = set(stopwords.words('spanish')) 
        filtered_sentence = [w for w in token if not w in stop_words]         
        bigrams = ngrams(filtered_sentence,2)        
        for i, j in bigrams:
            if not re.match("[^a-zA-Z]", i) and not re.match("[^a-zA-Z]", j) :
                list.append("{0} {1}".format(i, j))
    return list 
