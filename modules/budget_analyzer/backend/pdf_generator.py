from fpdf import FPDF
import tempfile
import re

class PDF(FPDF):
    def header(self):
        self.set_font("Helvetica", "B", 16)
        self.cell(0, 10, "Stoic Budget Report", ln=True, align="C")

    def chapter_title(self, title):
        self.set_font("Helvetica", "B", 12)
        self.cell(0, 10, title, ln=True)
        self.ln(4)

    def chapter_body(self, body):
        self.set_font("Helvetica", "", 11)
        safe_body = sanitize_text(body)
        self.multi_cell(0, 10, safe_body)
        self.ln()

def sanitize_text(text):
    # Remove emojis and non-ASCII characters (to avoid PDF encoding errors)
    safe = re.sub(r'[^\x00-\x7F]+', '', text)
    return safe

def generate_pdf(budget_data, advice_text):
    pdf = PDF()
    pdf.add_page()

    # Income section
    pdf.chapter_title("Income:")
    income = budget_data.get("income", 0)
    pdf.chapter_body(f"Total Income: Rs. {income}")

    # Expenses section
    pdf.chapter_title("Expenses:")
    expenses = budget_data.get("expenses", {})
    if expenses:
        for category, amount in expenses.items():
            pdf.chapter_body(f"{category}: Rs. {amount}")
    else:
        pdf.chapter_body("No expenses provided.")

    # Advice section
    pdf.chapter_title("Stoic Budget Advice:")
    pdf.chapter_body(advice_text)

    # Save PDF to temp file and return file path
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    pdf.output(temp_file.name)
    temp_file.close()
    return temp_file.name
