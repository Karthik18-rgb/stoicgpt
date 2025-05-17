# For now, dummy in-memory db (extend later)
budget_records = []

def save_budget_record(record):
    budget_records.append(record)

def get_all_records():
    return budget_records
