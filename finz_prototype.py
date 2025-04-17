import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Dummy user balance and savings data
user_balance = 15000
monthly_expenses = [15000, 14500, 16000, 14000, 15500, 15000]
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
avg_expense = np.mean(monthly_expenses)
suggested_saving = avg_expense * 0.2
predicted_cashflow = avg_expense - suggested_saving

# App layout
st.set_page_config(page_title="FinZ Prototype", layout="centered")
st.title("FinZ – Your Gen Z Finance Buddy")

# Sidebar for navigation
page = st.sidebar.radio("Navigate", ["Dashboard", "Add Expense", "Insights", "Gamified Challenge"])

# Dashboard
if page == "Dashboard":
    st.subheader("Dashboard")
    st.metric(label="Current Balance", value=f"₹{user_balance}")
    st.metric(label="Suggested Saving Goal", value=f"₹{suggested_saving:.2f}")
    st.metric(label="Predicted Cashflow (Next Month)", value=f"₹{predicted_cashflow:.2f}")
    st.markdown("---")

# Add Expense
elif page == "Add Expense":
    st.subheader("Add an Expense")
    with st.form("expense_form"):
        desc = st.text_input("Description (e.g., Netflix, Uber)")
        amount = st.number_input("Amount (₹)", min_value=0)
        category = st.selectbox("Category", ["Dining", "Transport", "Subscriptions", "Utilities", "Shopping", "Rent", "Groceries"])
        submitted = st.form_submit_button("Add Expense")
        if submitted:
            st.success(f"Added: ₹{amount} for {desc} under {category}")

# Insights
elif page == "Insights":
    st.subheader("Spending Insights")
    category_data = {
        "Dining": 3000,
        "Transport": 2000,
        "Subscriptions": 2500,
        "Utilities": 1800,
        "Shopping": 2200
    }
    df = pd.DataFrame.from_dict(category_data, orient='index', columns=['Amount'])
    st.write("*Spending Breakdown*")
    st.bar_chart(df)

    st.write("*Monthly Expense Trend*")
    fig, ax = plt.subplots()
    ax.plot(months, monthly_expenses, marker='o', color='blue')
    ax.set_title("Monthly Expenses")
    ax.set_xlabel("Month")
    ax.set_ylabel("Expense (₹)")
    st.pyplot(fig)

# Challenge
elif page == "Gamified Challenge":
    st.subheader("Savings Challenge")
    st.markdown("*Challenge:* Save ₹5000 this month")
    actual_saved = st.slider("How much have you saved so far?", 0, 10000, 3000, step=500)

    if actual_saved >= 5000:
        st.success("Congrats! You've completed the challenge.")
    else:
        st.warning("Keep going! You're almost there.")

    st.progress(min(actual_saved / 5000, 1.0))