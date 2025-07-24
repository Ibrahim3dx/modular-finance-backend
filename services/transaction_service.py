from datetime import datetime

class TransactionService:
    @staticmethod
    def parse_transaction(text: str) -> dict:
        try:
            parts = text.strip().split()
            if len(parts) < 3:
                raise ValueError("Input too short")

            trans_type = parts[0].capitalize()  # Income / Expense
            category = parts[1]
            amount = float(parts[2])
            note = " ".join(parts[3:]) if len(parts) > 3 else ""

            if trans_type not in ["Income", "Expense"]:
                raise ValueError("Type must be 'Income' or 'Expense'")

            return {
                "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "type": trans_type,
                "category": category,
                "amount": amount,
                "note": note
            }

        except Exception as e:
            raise ValueError(f"Failed to parse transaction: {e}")
if __name__ == "__main__":
    sample = "Expense Coffee 10 Flat white"
    result = TransactionService.parse_transaction(sample)
    print(result)
