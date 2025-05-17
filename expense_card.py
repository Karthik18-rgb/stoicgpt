import streamlit as st

def render_expense_card(income, expenses):
    st.subheader("📊 Your Expense Overview")
    st.write(f"**Monthly Income:** ₹{income}")
    st.write("**Expenses:**")
    for category, amount in expenses.items():
        st.write(f"- {category}: ₹{amount}")
