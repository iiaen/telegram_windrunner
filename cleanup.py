import os

try:
    os.remove("openinsider.png")
except:
    print("openinsider.png", "does not exist")

try:
    os.remove("portfolio.png")
except:
    print("portfolio.png", "does not exist")

try:
    os.remove("candlestick.png")
except:
    print("candlestick.png", "does not exist")