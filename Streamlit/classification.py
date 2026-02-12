import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

st.title("Iris Flower Prediction App")

# ---------- Load Data ----------
@st.cache_data
def load_data():
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df["species"] = iris.target
    return df, iris.target_names

df, target_names = load_data()

# ---------- Train Model ----------
X = df.iloc[:, :-1]
y = df["species"]

model = RandomForestClassifier()
model.fit(X, y)

# ---------- Sidebar Inputs ----------
st.sidebar.header("Input Features")

sepal_length = st.sidebar.slider(
    "Sepal Length",
    float(df.iloc[:, 0].min()),
    float(df.iloc[:, 0].max())
)

sepal_width = st.sidebar.slider(
    "Sepal Width",
    float(df.iloc[:, 1].min()),
    float(df.iloc[:, 1].max())
)

petal_length = st.sidebar.slider(
    "Petal Length",
    float(df.iloc[:, 2].min()),
    float(df.iloc[:, 2].max())
)

petal_width = st.sidebar.slider(
    "Petal Width",
    float(df.iloc[:, 3].min()),
    float(df.iloc[:, 3].max())
)

# ---------- Prediction ----------
input_data = [[
    sepal_length,
    sepal_width,
    petal_length,
    petal_width
]]

prediction = model.predict(input_data)

st.subheader("Prediction")
st.write("Predicted species:", target_names[prediction][0])
