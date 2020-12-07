from Convert.converter import Converter

converter = Converter()

value_from_user = int(input("Enter elon coin amount: "))
usd = converter.to_usd(value_from_user)
print(f"{value_from_user} is equal to {usd} dollar")