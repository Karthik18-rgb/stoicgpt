import streamlit as st

def render_input_form():
    with st.form("budget_form"):
        st.subheader("Enter Your Budget Details")

        income = st.number_input("Monthly Income (₹)", min_value=0, step=100)

        st.markdown("### Expenses")
        expenses = {}
        categories = ["Rent", "Food", "Utilities", "Transport", "Entertainment", "Others"]
        for category in categories:
            amount = st.number_input(f"{category} (₹)", min_value=0, step=100, key=category)
            expenses[category] = amount

        submit = st.form_submit_button("Analyze My Budget")

    if submit:
        return income, expenses
    return None, None
