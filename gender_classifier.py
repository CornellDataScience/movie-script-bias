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

    def classify(self, name):
        return self.classifier.classify(self.gender_features(name))

# output should be 'male'
# print(nltk.classify.accuracy(classifier, train_set))
# print(nltk.classify.accuracy(classifier, test_set))
