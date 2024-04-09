import pandas as pd
import streamlit as st
import pickle
from PIL import Image
img = Image.open("churn.png")
model = pickle.load(open("churning.pkl", "rb"))
st.header("Churning Predictor")
st.image(img)
st.subheader("Introduction")
st.text("Customer churn is the percentage of customers that stopped using your"
        " company's product\nor service during a certain time frame. Here in simple"
        " terms customer churn is considered\nas a situation where customers or subscribers"
        " stop using a company's products or services\nwithin a specific period."
        "\nThis webapp aims to be able to determine if a customer will leave the company's"
        " products\nand services or not.")
st.sidebar.header("Customer Metrics")
def report():
    REVENUE = st.sidebar.number_input("Enter Customer Monthly income")
    ORANGE = st.sidebar.number_input("Enter number of calls to Orange")
    ON_NET = st.sidebar.number_input("Enter number of Inter_expresso calls")
    MONTANT = st.sidebar.number_input("Enter Customer's Top up amount")
    FREQ_TOP_PACK = st.sidebar.number_input("How many time has the customer "
                                            "activated top packages?")
    FREQUENCE = st.sidebar.number_input("No of times Customer has made an income")
    FREQUENCE_RECH = st.sidebar.number_input("No of times Customer has refilled")
    REGULARITY = st.sidebar.number_input("No of times Customer has been active "
                                         "within the last 90 days")
    user_report = {
        "REVENUE" : REVENUE,
        "ORANGE": ORANGE,
        "ON_NET": ON_NET,
        "MONTANT": MONTANT,
        "FREQ_TOP_PACK": FREQ_TOP_PACK,
        "FREQUENCE": FREQUENCE,
        "FREQUENCE_RECH": FREQUENCE_RECH,
        "REGULARITY": REGULARITY}
    data = pd.DataFrame(user_report, index=[0])
    return data
insta = report()

st.subheader("Customer Summary")
st.write(insta)

if (st.button("Predict")):
    result = model.predict(insta)
    if (result == 0):
        st.write("This customer will leave the company.")
    else:
        st.write("This customer will not leave the company.")
