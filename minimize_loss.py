def minimize_loss(prices):
    year_price_map = {price: i for i, price in enumerate(prices)}
    sorted_prices = sorted(prices, reverse=True)
    min_loss = float('inf')
    buy_year, sell_year = -1, -1
    for i in range(len(sorted_prices)):
        for j in range(i+1, len(sorted_prices)):
            buy_price = sorted_prices[i]
            sell_price = sorted_prices[j]
            if year_price_map[sell_price] > year_price_map[buy_price]:
                loss = buy_price - sell_price
                if 0 < loss < min_loss:
                    min_loss = loss
                    buy_year = year_price_map[buy_price] + 1
                    sell_year = year_price_map[sell_price] + 1
    return {"buy_year": buy_year, "sell_year": sell_year, "loss": min_loss}
