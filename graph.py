import streamlit as st
import matplotlib.pyplot as plt

def plot_expense_graph(summary):
    fig, ax = plt.subplots()
    summary.plot(kind="bar", ax=ax)
    ax.set_ylabel("Amount (₹)")
    ax.set_title("Expenses by Category")
    st.pyplot(fig)
