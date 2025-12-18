import freecurrencyapi
import Key

client = freecurrencyapi.Client(Key.Code)

result = client.latest()

ConvertFrom = input("What currency do you wanna convert from?: ").upper()
ConvertTo = input("What currency do you wanna convert to?: ").upper()
Amount = float(input("How much do you wanna convert?: "))

Rate1 = result['data'][ConvertFrom]
Rate2 = result['data'][ConvertTo]

print(result)
print((Amount / Rate1)* Rate2)
