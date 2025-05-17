import os
from modules.budget_analyzer.backend.gpt_engine import openai_call

def get_budget_advice(summary_dict, net_savings):
    prompt = "Given the following budget summary and net savings, provide financial advice:\n"
    for category, amount in summary_dict.items():
        prompt += f"{category}: ₹{amount}\n"
    prompt += f"Net Savings: ₹{net_savings}\n"
    prompt += "Advice:"
    response = openai_call(prompt)
    return response
