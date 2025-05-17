import requests
import os
import re

def sanitize_input(text):
    # Remove emojis and non-ASCII characters that might break the request
    return re.sub(r'[^\x00-\x7F]+', '', text)

def get_gpt_advice(income, expenses, api_key):
    try:
        total_expenses = sum(expenses.values())
        savings = income - total_expenses
        prompt = (
            f"Give simple and practical Stoic budgeting advice for someone with ₹{income} income "
            f"and ₹{total_expenses} in expenses, who has saved ₹{savings} this month. "
            f"Use plain language."
        )
        prompt = sanitize_input(prompt)

        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        }

        payload = {
            "model": "mistral:instruct",
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }

        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=payload
        )
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]

    except Exception as e:
        # In case of any failure, return default advice
        print(f"⚠️ Failed to fetch advice: {e}")
        return (
            "Live below your means. Track every rupee. Avoid impulsive purchases. "
            "Spend on needs, not wants. Build discipline through financial awareness. "
            "Even a small saving is a victory in self-mastery."
        )
