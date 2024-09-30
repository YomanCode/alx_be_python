a = input("Whats the weather like today? (sunny/rainy/cold): ").lower()

if a == "sunny":
    print("Wear a t-shirt and sunglasses")
elif a == "rainy":
    print("Don't forget your unmbrella and a raincoat")
elif a == "cold":
    print("Make sure to wear a warm coat and a scarf")
else:
    print("Sorry, I don't have recommendations for this weather.")
