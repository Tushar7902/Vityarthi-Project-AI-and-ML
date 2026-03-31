import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
import joblib

data = pd.read_csv("../data/data.csv")

le_backlog = LabelEncoder()
le_difficulty = LabelEncoder()
le_mood = LabelEncoder()
le_subject = LabelEncoder()

data['backlog_level'] = le_backlog.fit_transform(data['backlog_level'])
data['subject_difficulty'] = le_difficulty.fit_transform(data['subject_difficulty'])
data['mood'] = le_mood.fit_transform(data['mood'])
data['priority_subject'] = le_subject.fit_transform(data['priority_subject'])
X = data[['hours_available', 'backlog_level', 'subject_difficulty', 'mood']]
y = data['priority_subject']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = DecisionTreeClassifier(max_depth=5, random_state=42)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"Model Accuracy: {accuracy*100:.2f}%")

joblib.dump(model, "model.pkl")
joblib.dump(le_backlog, "le_backlog.pkl")
joblib.dump(le_difficulty, "le_difficulty.pkl")
joblib.dump(le_mood, "le_mood.pkl")
joblib.dump(le_subject, "le_subject.pkl")

print("The program executed successfully")
