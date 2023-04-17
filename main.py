from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import StandardScaler
import numpy as np

# Define the questions to ask the user
questions = [
    "Are you often the life of the party?",
    "Do you enjoy being the center of attention?",
    "Do you prefer to be alone rather than in large groups?",
    "Do you enjoy taking risks and trying new things?",
    "Do you have a strong sense of right and wrong?",
    "Do you tend to be more organized or spontaneous?",
    "Do you prefer to follow established rules and procedures, or do you prefer to be more flexible and adaptable?",
    "Do you tend to be more introverted or extroverted?",
    "Do you tend to be more sensitive and emotional, or more logical and detached?",
    "Do you tend to be more ambitious and driven, or more laid back and easy-going?"
]

# Ask the user each question and store their responses
responses = []
for question in questions:
    while True:
        response = input(question + " (y/n) ")
        if response in ['y', 'n']:
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
    responses.append(response == "y")

# Preprocess the data
scaler = StandardScaler()
responses = scaler.fit_transform([responses])

# Use a machine learning model to predict the user's personality type based on their responses
model = RandomForestClassifier()
scores = cross_val_score(model, X_train, y_train, cv=5)
model.fit(X_train, y_train)
predictions = model.predict_proba(responses)

# Output the prediction and an explanation of the personality traits associated with that type
if predictions.any():
    labels = ['Introverted', 'Extroverted']
    idx = np.argsort(predictions)[::-1]
    for i in range(len(labels)):
        print(f"{labels[idx[i]]}: {predictions[0][idx[i]]:.2f}")
else:
    print("Unable to determine personality type.")

