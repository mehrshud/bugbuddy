
# Import necessary libraries
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
import pickle
import os

class MachineLearningModel:
    def __init__(self):
        self.model = LogisticRegression()

    def train(self, X, y):
        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train the model
        self.model.fit(X_train, y_train)

        # Make predictions
        predictions = self.model.predict(X_test)

        # Print the accuracy of the model
        print('Model Accuracy:', metrics.accuracy_score(y_test, predictions))

        # Save the model to a file
        with open('model.pkl', 'wb') as file:
            pickle.dump(self.model, file)

    def load(self):
        # Load the model from a file
        if os.path.exists('model.pkl'):
            with open('model.pkl', 'rb') as file:
                self.model = pickle.load(file)
        else:
            print('No model file found.'
                  '
Please train a model first.'
                  '
Use the train method to train a model.')
