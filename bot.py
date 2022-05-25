'''
Made by Andrei.

@author - Ceban Andrei (ancrei.ceban@isa.utm.md)
'''

# Importing all needed libraries and modules.
import nltk
nltk.download('punkt')
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()
import numpy
import tflearn
from tensorflow.python.framework import ops
import json
import pickle


# The discord bot class.
class train_bot:
   # Load the json file
  with open("intents.json") as file:
    data = json.load(file)

  # Open up the saved data
  try:
    # For reseting the dataset we use "x"
    x 
    
    # Save the information and read in bytes
    with open("data.pickle", "rb") as f:
      words, labels, training, output = pickle.load(f)
  
  except:
    # Each entry in Doc's X corresponds to an entry in Doc's Y 
    words = []
    labels = []
    docs_x = []
    docs_y = []
    
    for intent in data["intents"]:
      for pattern in intent["patterns"]:
        # Get all the words in pattern, return a list
        wrds = nltk.word_tokenize(pattern)
        # Put all the words in the list
        words.extend(wrds)
        # Add to docs the pattern
        docs_x.append(wrds)
        docs_y.append(intent["tag"])
    
      # Get all the tags
      if intent["tag"] not in labels:
        labels.append(intent["tag"])
  
    # Remove any question marks, all duplicates and convert to a list
    
    words = [stemmer.stem(w.lower()) for w in words if w != "!"]
    words = sorted(list(set(words)))
  
  # Sort the labels
  labels = sorted(labels)

  # Put bags of words (list of zeros and ones)
  training = []
  output = []
  

  # List which will have a 0 in it for all of the classes, if that class exist we will put a 1 there
  out_empty = [0 for _ in range(len(labels))]
  
  # Create a bag of words
  for x,  doc in enumerate(docs_x):
    bag = []
  
    # Stem all of the words that are in our patterns
    wrds = [stemmer.stem(w) for w in doc]
  
    # Go through all the words and put 1 if words exist else 0
    for w in words:
      if w in wrds:
        bag.append(1)
      else:
        bag.append(0)
  
      ''' 
        Genereate the output, we're gonna look through this labels
        list here we're gonna see where the tag
        is in that list and then we're gonna set
        that value to one in our output row
      '''
    output_row = out_empty[:]
    output_row[labels.index(docs_y[x])] = 1
    training.append(bag)
    output.append(output_row)
  
  # Change output and training into NP arrays 
  training = numpy.array(training)
  output = numpy.array(output)

  # Write the variables in file to can save it
  with open("data.pickle", "wb") as f:
    pickle.dump((words, labels, training, output),f)



  # Make sure that we get rid of all like previous settings
  # and stuff it's resetting the underlying data graph or graph data 
  ops.reset_default_graph()
  
  # Define the input shape that we're expecting for our model so in this case we're getting the length of training zero because each training input is gonna be the same length 
  net = tflearn.input_data(shape=[None, len(training[0])])
  
  # Add this fully connected layer to our neural network which starts at this input data and we're gonna have 16 neurons for that hidden layer
  net = tflearn.fully_connected(net, 16)
  net = tflearn.fully_connected(net, 16)
  # Softmax is gonna go through and give us a probability for each neuron in this lair and that will be our output for the network 
  net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
  net = tflearn.regression(net)
  
  # Train the model
  model = tflearn.DNN(net)
  
  # Explanation
  """
  Am creat reteaua neuronala : 
  incepem cu o  multime de inputuri de neuroni
  - Avem multi neuroni (1 leier)
  - 16 neuroni care sunt conectati cu inputul (2 laier)
  - 16 neuroni care sunt conectati cu a 2 generatei (2 laier)
  - si apoi avem atiti neuroni cite retele avem facute (full conectate) - softmax (activation), si ne va da probabilitatea neuronilor
  
  Daca modelul  crede ca raspunsul trebuie sa fie un tag anumit atunci acest neuron o sa aiba cea mai mare probabilitate decit ceilalti
  - fiecare neuron reprezinta clase secifice (taguri)
  
  """
  
  # If we don't modify json file, then run this code
  
  model.load("model.tflearn")
  try:
      model.load("model.tflearn")
  except:
      model.fit(training, output, n_epoch=1000, batch_size=8, show_metric=True)
      model.save("model.tflearn")

  #If we modify json file, then run this code

  # model.fit(training, output, n_epoch=1000, batch_size=8, show_metric=True)
  # model.save("model.tflearn")

  # Turn the sentence in a bag of words, make predictions
  def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]
  
    # Get a list of tokenized words
    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]
  
    for se in s_words:
      for i, w in enumerate(words):
        if w == se:
          bag[i] = 1
  
    return numpy.array(bag)
