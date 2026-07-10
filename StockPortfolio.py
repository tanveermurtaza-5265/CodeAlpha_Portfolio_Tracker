# Stock Portfolio Tracker
# Developed for CodeAlpha Internship
# Dictionary containing stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGLE": 140,
    "AMZN": 160,
    "MSFT": 330
}
total_investment = 0
print("=" * 50)
print("      STOCK PORTFOLIO TRACKER")
print("=" * 50)
while True:
    stock = input("\nEnter Stock Name (AAPL/TSLA/GOOGLE/AMZN/MSFT): ").upper()
    if stock not in stock_prices:
        print("Stock not available.")
        continue
    quantity = int(input("Enter Quantity: "))
    investment = stock_prices[stock] * quantity
    total_investment += investment
    print("Investment in", stock, "=", investment)
    choice = input("Do you want to add another stock? (yes/no): ").lower()
    if choice == "no":
        break
print("\n==============================")
print("Total Investment =", total_investment)
print("==============================")
# Save result in text file
file = open("portfolio.txt", "w")
file.write("Total Investment = " + str(total_investment))
file.close()
print("Result saved successfully in portfolio.txt")