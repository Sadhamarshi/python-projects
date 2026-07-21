class Expense:
    def __init__(self, title, amount, category):
        self.title = title
        self.amount = amount
        self.category = category

    def __str__(self):
        return (
            f"Title    : {self.title}\n"
            f"Amount   : ₹{self.amount:.2f}\n"
            f"Category : {self.category}"
        )