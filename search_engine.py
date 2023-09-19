#-------------------------------------------------------------------------
# AUTHOR: Grecia Alvarado
# FILENAME: search_engine.py
# SPECIFICATION: Create a tf-idf matrix. Incomplete because i'm prepping for interviews and am short on time
# FOR: CS 4250- Assignment #1
# TIME SPENT: 2hr
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard arrays

#importing some Python libraries
import csv
import math

documents = []
labels = []

#reading the data in a csv file
with open('collection.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
         if i > 0:  # skipping the header
            documents.append (row[0])
            labels.append(row[1])

#Conduct stopword removal.
#--> add your Python code here
stopWords = {'I', 'and', 'She', 'They', 'her', 'their'}
docs = []
for document in documents:
  sentence = document.split()
  adjusted_sentence = [word for word in sentence if word.lower() not in stopWords]
  docs.append(''.join(adjusted_sentence))

#Conduct stemming.
#--> add your Python code here
steeming = {
  "cats": "cat",
  "dogs": "dog",
  "loves": "love",
}
fixed_docs = []
for doc in docs:
  sentence = doc.split()
  stemmed = [steeming.get(word,word) for word in sentence]
  fixed_docs.append(''.join(stemmed))

#Identify the index terms.
#--> add your Python code here
#unique_terms = {}
terms = set()
for doc in fixed_docs:
  words = doc.split()
  for word in words:
    if word not in terms:
      terms.add(word)

#Build the tf-idf term weights matrix.
#--> add your Python code here
tf_matrix = []
idf_matrix = []
for doc in fixed_docs:
  doc_terms = {}
  words = doc.split()
  word_count = 0
  for word in words:
    if word in doc_terms.keys():
      doc_terms[word] += 1
    else:
      doc_terms[word] = 1
    word_count += 1
  
  tf_row = []
  for word in doc_terms:
    tf = doc_terms[word] / word_count
    tf_row.append(tf)

  tf_matrix.append(tf_row)

print(tf_matrix)

    

docMatrix = []

#Calculate the document scores (ranking) using document weigths (tf-idf) calculated before and query weights (binary - have or not the term).
#--> add your Python code here
docScores = []

#Calculate and print the precision and recall of the model by considering that the search engine will return all documents with scores >= 0.1.
#--> add your Python code here