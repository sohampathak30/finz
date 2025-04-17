import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import date
from fpdf import FPDF

# --- Simulated Data ---
user_name = "Soham"
user_balance = 15000
monthly_expenses = [15000, 14500, 16000, 14000, 15500, 15000]
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
avg_expense = np.mean(monthly_expenses)
suggested_saving = avg_expense * 0.2
predicted_cashflow = avg_expense - suggested_saving
today = date.today()

# --- Page Setup ---
st.set_page_config(page_title="FinZ", layout="centered")

# --- Sidebar Navigation ---
page = st.sidebar.radio("Go to", ["Dashboard", "Insights", "Investments", "Notifications", "Export Report"])

# --- Profile Header ---
st.markdown("<h2 style='text-align:center; color:#90caf9;'>FinZ – Mobile Finance App</h2>", unsafe_allow_html=True)
st.markdown(
    f"<div style='text-align: center; margin-bottom: 1rem;'>"
    "<img src='https://cdn-icons-png.flaticon.com/512/149/149071.png' width='70' style='border-radius: 50%;'><br>"
    f"<h4 style='color:white;'>Welcome, {user_name}!</h4>"
    "</div>", unsafe_allow_html=True
)

# --- Dashboard Screen ---
if page == "Dashboard":
    st.subheader("Dashboard")

    st.markdown(f'''
        <div style="background: linear-gradient(135deg, #42a5f5, #478ed1); padding: 1rem; border-radius: 10px; margin-bottom: 10px;">
            <h4 style="margin:0; color:white;">Current Balance</h4>
            <p style="font-size: 1.5rem; color:white;">INR {user_balance}</p>
        </div>
    ''', unsafe_allow_html=True)

    st.markdown(f'''
        <div style="background: linear-gradient(135deg, #66bb6a, #43a047); padding: 1rem; border-radius: 10px; margin-bottom: 10px;">
            <h4 style="margin:0; color:white;">Saving Goal</h4>
            <p style="font-size: 1.5rem; color:white;">INR {suggested_saving:.2f}</p>
        </div>
    ''', unsafe_allow_html=True)

    st.markdown(f'''
        <div style="background: linear-gradient(135deg, #ffa726, #fb8c00); padding: 1rem; border-radius: 10px; margin-bottom: 10px;">
            <h4 style="margin:0; color:white;">Predicted Cashflow</h4>
            <p style="font-size: 1.5rem; color:white;">INR {predicted_cashflow:.2f}</p>
        </div>
    ''', unsafe_allow_html=True)

# --- Insights Screen ---
elif page == "Insights":
    st.subheader("Spending Insights")

    st.markdown("### 📊 Monthly Expense Trend")
    fig, ax = plt.subplots()
    ax.plot(months, monthly_expenses, marker='o', color='#90caf9')
    ax.set_facecolor('#1e1e1e')
    fig.patch.set_facecolor('#121212')
    ax.set_title("Monthly Expenses", color='white')
    ax.set_xlabel("Month", color='white')
    ax.set_ylabel("Expense (INR)", color='white')
    ax.tick_params(colors='white')
    st.pyplot(fig)

    st.markdown("### 📌 Category-wise Breakdown")
    category_data = {
        "Dining": 3000,
        "Transport": 2000,
        "Subscriptions": 2500,
        "Utilities": 1800,
        "Shopping": 2200
    }
    df = pd.DataFrame.from_dict(category_data, orient='index', columns=['Amount'])
    st.bar_chart(df)

# --- Investment Tips Screen ---
elif page == "Investments":
    st.subheader("💹 Investment Suggestions")
    st.success("Start a INR 500 SIP in Axis Bluechip – low risk, high consistency.")
    st.success("Try Green Investing – ESG score 82+, long-term stability.")
    st.success("Consider Gold ETF – Hedge against inflation.")
    st.success("Explore FinZ Smart Basket – diversified micro-investing.")

# --- Notifications Screen ---
elif page == "Notifications":
    st.subheader("🔔 Notifications")
    st.info("💡 Your rent is due in 3 days.")
    st.info("📈 You saved 92% of your goal last month.")
    st.info("🧾 2 new investment tips available.")

# --- PDF Report Export Screen ---
elif page == "Export Report":
    st.subheader("📥 Export Monthly Report")

    def generate_pdf():
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=16)
        pdf.cell(200, 10, txt="FinZ Monthly Report", ln=True, align='C')
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt=f"Name: {user_name}", ln=True)
        pdf.cell(200, 10, txt=f"Date: {today}", ln=True)
        pdf.cell(200, 10, txt=f"Average Expense: INR {avg_expense:.2f}", ln=True)
        pdf.cell(200, 10, txt=f"Suggested Saving: INR {suggested_saving:.2f}", ln=True)
        pdf.cell(200, 10, txt=f"Predicted Cashflow: INR {predicted_cashflow:.2f}", ln=True)
        file_path = "/tmp/FinZ_Report.pdf"
        pdf.output(file_path)
        return file_path

    if st.button("Generate PDF"):
        pdf_path = generate_pdf()
        with open(pdf_path, "rb") as f:
            st.download_button(label="Download Report", file_name="FinZ_Report.pdf", mime="application/pdf", data=f.read())

