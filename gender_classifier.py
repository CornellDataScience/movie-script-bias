from urllib.request import urlopen
import json
import random
from nltk.corpus import names
import nltk


class Gender_classifier():
    def __init__(self) -> None:
        self.gender_features = lambda word:  {'last_letter': word[-3:]}
        labeled_names = ([(name, 'male') for name in names.words('male.txt')] +
                         [(name, 'female') for name in names.words('female.txt')])

        random.shuffle(labeled_names)

        # we use the feature extractor to process the names data.
        featuresets = [(self.gender_features(n), gender)
                       for (n, gender) in labeled_names]

        # Divide the resulting list of feature
        # sets into a training set and a test set.
        train_set, test_set = featuresets[500:], featuresets[:500]

        # The training set is used to
        # train a new "naive Bayes" classifier.
        self.classifier = nltk.NaiveBayesClassifier.train(train_set)

    def nlp_classifier(self, name):
        return self.classifier.classify(self.gender_features(name))

    def api_classifier(self, name):
<<<<<<< HEAD
        url = "https://api.genderize.io?name=" + name
=======
        try:
            url = "https://api.genderize.io?name=" + name
        except:
            return("Undefined", 0)
>>>>>>> 78d729471d70fe8fb5f0ad00d647cf05fb24ef1d
        response = urlopen(url)
        decoded = response.read().decode('utf-8')
        data = json.loads(decoded)
        gender = data["gender"]
        prob = data["probability"]
        if gender == None:
            # if there's no gender could be assigned, return None
            print("None")
            return ("Undefined", prob)
        else:
            print(gender)
            return (gender, prob)

    def classify(self, name):
        gender, prob = self.api_classifier(name)
        if gender == "Undefined":
            return "Undefined"
        if prob <= 0.7:
            check = self.nlp_classifier(name)
            if check != gender:
                print("please check manually")
                return "Disagreed"
        return gender

# output should be 'male'
# print(nltk.classify.accuracy(classifier, train_set))
# print(nltk.classify.accuracy(classifier, test_set))
