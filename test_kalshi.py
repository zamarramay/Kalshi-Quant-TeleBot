from src.kalshi_api import KalshiAPI

k = KalshiAPI()

print("Exchange status:")
print(k.get_exchange_status())

print("\nBalance:")
print(k.get_account_balance())
