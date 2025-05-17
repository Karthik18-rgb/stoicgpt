import streamlit as st

def show_report_card(summary, net_savings):
    st.write("### Budget Report")
    for category, amount in summary.items():
        st.write(f"{category}: ₹{amount:.2f}")
    st.write(f"Net Savings: ₹{net_savings:.2f}")
