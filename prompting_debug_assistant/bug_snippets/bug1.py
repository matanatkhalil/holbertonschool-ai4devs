# Bug 1: Syntax error
def calculate_total(prices, tax_rate)
    subtotal = 0
    for price in prices:
        subtotal += price

    tax = subtotal * tax_rate
    total = subtotal + tax
    return total


def main():
    prices = [12.50, 8.00, 4.25]
    tax_rate = 0.10
    result = calculate_total(prices, tax_rate)
    print("Total:", result)


if __name__ == "__main__":
    main()
