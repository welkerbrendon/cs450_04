import pandas as pd
import difflib
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn import preprocessing


voting_data = "https://archive.ics.uci.edu/ml/machine-learning-databases/voting-records/house-votes-84.data"

full_voting_data_array = pd.read_csv(voting_data).values
data = []
targets = []
for row in full_voting_data_array:
    row = row.tolist()
    targets.append(row.pop(0))
    data.append(row)


data_train, data_test, target_train, target_test = train_test_split(data, targets, test_size=.3)

classifier = tree.DecisionTreeClassifier()
model = classifier.fit(data_train, target_train)
targets_predicted = model.predict(data_test)

similarity_amount = difflib.SequenceMatcher(None, targets_predicted, target_test)
print(similarity_amount.ratio())