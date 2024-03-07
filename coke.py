def main():
    # Initialize variables
    total_inserted = 0
    coke_price = 50

    # Prompt the user for coins until at least 50 cents are inserted
    while total_inserted < coke_price:
        try:
            coin = int(input("Insert a coin:"))
            if coin in [5, 10, 25]:
                total_inserted += coin
                print(f"Amount Due: {coke_price - total_inserted}")

            else:
                print(f"Amount Due: {coke_price}")
        except ValueError:
            pass

    # Calculate change owed
    change = total_inserted - coke_price
    print(f"Change Owed: {change}")

main()