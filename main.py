from caesar_cipher import caesar_cipher
from indian_currency_formatter import format_indian_currency
from combine_lists import combine_position_value_lists
from minimize_loss import minimize_loss

# Test Caesar Cipher
msg = "Agetware Tech"
shift = 4
print("Encoded:", caesar_cipher(msg, shift))
print("Decoded:", caesar_cipher(caesar_cipher(msg, shift), shift, 'decode'))


# Test Currency Formatter
amount = 12345678.9012
print("Formatted INR:", format_indian_currency(amount))

# Test Combine Lists
list1 = [{"positions": [0, 4], "values": [1, 2]}]
list2 = [{"positions": [2, 5], "values": [3]}]
print("Combined List:", combine_position_value_lists(list1, list2))

# Test Minimize Loss
prices = [20, 15, 7, 2, 13]
result = minimize_loss(prices)
print(f"Buy in Year {result['buy_year']}, Sell in Year {result['sell_year']}, Loss: {result['loss']}")
