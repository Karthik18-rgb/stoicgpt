import requests

def get_gpt_advice(income, expenses, api_key):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    # Format expenses for prompt
    expense_lines = "\n".join(f"{cat}: Rs. {amt}" for cat, amt in expenses.items())
    prompt = (
        f"You are a stoic financial advisor.\n"
        f"User's monthly income: Rs. {income}\n"
        f"User's monthly expenses:\n{expense_lines}\n\n"
        "Provide a brief, practical stoic advice to help manage their budget wisely."
    )

    data = {
        "model": "gpt-4o-mini",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7,
        "max_tokens": 250,
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        res_json = response.json()

        advice = res_json["choices"][0]["message"]["content"]
        # Replace ₹ with Rs. to avoid encoding issues in PDF
        advice = advice.replace("₹", "Rs.")
        return advice
    except Exception as e:
        return f"Failed to fetch advice: {e}"
