import streamlit as st
import qrcode
from io import BytesIO
from modules.budget_analyzer.backend.pdf_generator import generate_pdf
from modules.budget_analyzer.backend.gpt_predictor import get_gpt_advice

st.set_page_config(page_title="Stoic Budget", page_icon="💰")

st.title("Stoic Budget")

# API key input
api_key = st.text_input("Enter your OpenRouter API Key", type="password")
if not api_key:
    st.warning("Please enter your OpenRouter API Key.")
    st.stop()

# UPI payment simulation
UPI_ID = "thakurjamuns@okicici"
PAY_AMOUNT = 1

# Generate UPI QR code dynamically
upi_uri = f"upi://pay?pa={UPI_ID}&pn=StoicBudget&am={PAY_AMOUNT}&cu=INR"
qr = qrcode.make(upi_uri)
buf = BytesIO()
qr.save(buf)
buf.seek(0)

st.image(buf, caption=f"Pay ₹{PAY_AMOUNT} via UPI to unlock budget analysis", use_container_width=True)

payment_done = st.checkbox("I have completed the payment")

if payment_done:
    st.success("Payment verified! You can now input your budget.")

    with st.form("budget_form"):
        income = st.number_input("Monthly Income (₹)", min_value=0, step=1000)
        st.write("Enter your expenses by category:")
        expenses = {}
        expense_categories = ["Rent", "Food", "Transport", "Entertainment", "Others"]
        for cat in expense_categories:
            expenses[cat] = st.number_input(f"{cat} Expense (₹)", min_value=0, step=100)

        submitted = st.form_submit_button("Analyze & Generate PDF")

    if submitted:
        with st.spinner("Analyzing budget..."):
            advice = get_gpt_advice(income, expenses, api_key)

        if advice.startswith("Failed"):
            st.error(advice)
        else:
            st.markdown("### Stoic Budget Advice")
            st.write(advice)

            # Generate PDF
            pdf_path = generate_pdf({"income": income, "expenses": expenses}, advice)

            # Show download button
            with open(pdf_path, "rb") as f:
                pdf_bytes = f.read()

            st.download_button(
                label="Download Budget Analysis PDF",
                data=pdf_bytes,
                file_name="Stoic_Budget_Report.pdf",
                mime="application/pdf"
            )
else:
    st.info("Please complete the payment above to use the app.")

