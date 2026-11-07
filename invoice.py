def total(items):
    """Total price of all items, plus 10% tax."""
    subtotal = sum(price * qty for price, qty in items)
    return round(subtotal * 0.1, 2)
