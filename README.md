# Weather Prediction using Decision Tree Classifier

##  Project Overview

This project demonstrates how to use a **Decision Tree Classifier** to predict whether outdoor conditions are suitable for playing based on weather features. The model is trained on a small weather dataset and uses categorical data encoded into numerical values before training.

The project also visualizes the trained Decision Tree, making it easy to understand how decisions are made.

---

##  Features

* Uses a Decision Tree Classifier for prediction.
* Encodes categorical data using Label Encoding.
* Predicts whether to **Play** or **Don't Play** based on weather conditions.
* Visualizes the trained Decision Tree.
* Beginner-friendly implementation using Python and Scikit-learn.

---

##  Project Structure

```text
Weather-Prediction-Decision-Tree/
│
├── weather_prediction.py
├── README.md
└── requirements.txt
```

---

##  Technologies Used

* Python 3
* Pandas
* Scikit-learn
* Matplotlib

---

##  Dataset

The dataset contains weather-related attributes used to determine whether playing outdoors is recommended.

| Feature     | Description                |
| ----------- | -------------------------- |
| Outlook     | Sunny, Overcast, Rainy     |
| Temperature | Hot, Mild, Cool            |
| Humidity    | High, Normal               |
| Wind        | Weak, Strong               |
| Play        | Yes / No (Target Variable) |

### Sample Data

| Outlook  | Temperature | Humidity | Wind | Play |
| -------- | ----------- | -------- | ---- | ---- |
| Sunny    | Hot         | High     | Weak | No   |
| Overcast | Hot         | High     | Weak | Yes  |
| Rainy    | Cool        | Normal   | Weak | Yes  |

---

## Machine Learning Workflow

1. Create the weather dataset.
2. Encode categorical values using `LabelEncoder`.
3. Split the data into features and target.
4. Train a `DecisionTreeClassifier`.
5. Predict whether to play for a given weather condition.
6. Visualize the trained Decision Tree.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/Weather-Prediction-Decision-Tree.git
```

Navigate to the project folder:

```bash
cd Weather-Prediction-Decision-Tree
```

Install the required libraries:

```bash
pip install pandas matplotlib scikit-learn
```

Or install using:

```bash
pip install -r requirements.txt
```

---

## Running the Project

Run the Python script:

```bash
python weather_prediction.py
```

### Example Prediction

Input weather conditions:

* Outlook: Sunny
* Temperature: Hot
* Humidity: High
* Wind: Weak

Example output:

```text
Prediction: NO 🌧️ (Don't Play)
```

---

##  Output

The program provides:

* Weather prediction (Play / Don't Play)
* Visualization of the trained Decision Tree showing decision rules and class labels

---

##  Machine Learning Model

### Algorithm

* Decision Tree Classifier

### Data Preprocessing

* Label Encoding for categorical features

### Target Variable

* **Play**

  * Yes
  * No

---

##  Future Improvements

* Train on a larger real-world weather dataset.
* Allow users to enter weather conditions interactively.
* Evaluate the model using:

  * Accuracy
  * Precision
  * Recall
  * F1-Score
* Export and save the trained model using Joblib or Pickle.
* Build a web interface using Flask or Streamlit.

---

##  Requirements

```text
pandas
matplotlib
scikit-learn
```

Install all dependencies:

```bash
pip install pandas matplotlib scikit-learn
```

---

## Author

**KANISHK A M**

GitHub: https://github.com/kanishk-am

---
