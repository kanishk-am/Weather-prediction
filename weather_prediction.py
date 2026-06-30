import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn import tree
import matplotlib.pyplot as plt

# -------------------- DATASET --------------------
data = {
    "Outlook": ["Sunny", "Sunny", "Overcast", "Rainy", "Rainy", "Rainy", "Overcast", "Sunny", "Sunny", "Rainy"],
    "Temperature": ["Hot", "Hot", "Hot", "Mild", "Cool", "Cool", "Cool", "Mild", "Cool", "Mild"],
    "Humidity": ["High", "High", "High", "High", "Normal", "Normal", "Normal", "High", "Normal", "Normal"],
    "Wind": ["Weak", "Strong", "Weak", "Weak", "Weak", "Strong", "Strong", "Weak", "Weak", "Weak"],
    "Play": ["No", "No", "Yes", "Yes", "Yes", "No", "Yes", "No", "Yes", "Yes"]
}

df = pd.DataFrame(data)

# -------------------- ENCODING TEXT DATA --------------------
le_outlook = LabelEncoder()
le_temp = LabelEncoder()
le_humidity = LabelEncoder()
le_wind = LabelEncoder()
le_play = LabelEncoder()

df["Outlook"] = le_outlook.fit_transform(df["Outlook"])
df["Temperature"] = le_temp.fit_transform(df["Temperature"])
df["Humidity"] = le_humidity.fit_transform(df["Humidity"])
df["Wind"] = le_wind.fit_transform(df["Wind"])
df["Play"] = le_play.fit_transform(df["Play"])

# -------------------- FEATURES & TARGET --------------------
X = df[["Outlook", "Temperature", "Humidity", "Wind"]]
y = df["Play"]

# -------------------- MODEL TRAINING --------------------
model = DecisionTreeClassifier()
model.fit(X, y)

# -------------------- PREDICTION --------------------
# Example: Sunny, Hot, High humidity, Weak wind
sample = [[
    le_outlook.transform(["Sunny"])[0],
    le_temp.transform(["Hot"])[0],
    le_humidity.transform(["High"])[0],
    le_wind.transform(["Weak"])[0]
]]

prediction = model.predict(sample)

result = "YES ☀️ (Play)" if prediction[0] == 1 else "NO 🌧️ (Don't Play)"
print("Prediction:", result)

# -------------------- VISUALIZATION --------------------
plt.figure(figsize=(12,6))
tree.plot_tree(model,
               feature_names=["Outlook", "Temperature", "Humidity", "Wind"],
               class_names=["No", "Yes"],
               filled=True)

plt.title("Decision Tree - Weather Prediction")
plt.show()
