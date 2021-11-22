import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC


dataset = pd.read_excel('Internship Naming.xlsx', sheet_name='Duration')
dataset = dataset.dropna(axis=1, how='all')

corpus = []
for i in range(0, 47):
  review = re.sub('[^a-zA-Z]', ' ', dataset['Description'][i])
  review = review.lower()
  review = review.split()
  ps = PorterStemmer()
  all_stopwords = stopwords.words('english')
  all_stopwords.remove('not')
  review = [ps.stem(word) for word in review if not word in set(all_stopwords)]
  review = ' '.join(review)
  corpus.append(review)

cv = CountVectorizer()
X = cv.fit_transform(corpus).toarray()
y = dataset.iloc[:, -1].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

classifier = SVC(kernel = 'linear', random_state = 0)
classifier.fit(X_train, y_train)


def description_predict(new_description_p):
    new_description = new_description_p
    new_description = re.sub('[^a-zA-Z]', ' ', new_description)
    new_description = new_description.lower()
    new_description = new_description.split()
    ps = PorterStemmer()
    all_stopwords = stopwords.words('english')
    all_stopwords.remove('not')
    new_description = [ps.stem(word) for word in new_description if not word in set(all_stopwords)]
    new_description = ' '.join(new_description)
    new_corpus = [new_description]
    new_X_test = cv.transform(new_corpus).toarray()
    new_y_pred = classifier.predict(new_X_test)
    if new_y_pred == 1:
      category = '1'
    else:
      category = '0'


    new_description_c = new_description_p.lower()
    new_description_c.lower().replace(',','')
    new_description_c.replace('/',' ')
    new_description_c.replace('-',' ')

    if 'stipend' in new_description_c:
      if 'unpaid' in new_description_c:
          stipend = '0'
      else:
          stipend = '1'
    else:
      stipend = '0'

    

    if 'remote' in new_description_c or 'work from home' in new_description_c:
      workfromhome = '1'
    else:
      workfromhome = '0'



    if 'certificate' in new_description_c:
      certificate = '1'
    else:
      certificate = '0'


    if 'lor' in new_description_c or 'letter of recommendation' in new_description_c:
      lor = '1'
    else:
      lor = '0'
    


    if 'flexible' in new_description_c:
      flexible = '1'
    else:
      flexible = '0'



    Code_final = category + '' + workfromhome + '' + stipend + '' + certificate + '' + lor + '' + flexible

    return Code_final