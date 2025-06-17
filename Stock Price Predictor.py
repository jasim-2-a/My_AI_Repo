import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import joblib

# ========== SETTINGS ==========
TICKER = "AAPL"         # Change to any valid ticker (e.g. "GOOG", "MSFT")
FORECAST_DAYS = 5       # How many days ahead to predict
TRAIN_TEST_SPLIT = 0.2  # 20% test size
# ==============================


data = yf.download(TICKER, start="2015-01-01", end="2023-12-31")
data = data[["Open", "High", "Low", "Close", "Volume"]]
data.dropna(inplace=True)


data["Target"] = data["Close"].shift(-FORECAST_DAYS)
data.dropna(inplace=True)

X = data.drop("Target", axis=1).values
y = data["Target"].values


scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=TRAIN_TEST_SPLIT, shuffle=False)


model = LinearRegression()
model.fit(X_train, y_train)


predictions = model.predict(X_test)
mse = mean_squared_error(y_test, predictions)
print(f"🔍 Mean Squared Error: {mse:.2f}")


plt.figure(figsize=(14, 6))
plt.plot(y_test, label="Actual Price")
plt.plot(predictions, label="Predicted Price")
plt.title(f"{TICKER} Stock Price Prediction ({FORECAST_DAYS}-Day Ahead)")
plt.xlabel("Days")
plt.ylabel("Stock Price ($)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


joblib.dump(model, f"{TICKER}_lr_model.pkl")
joblib.dump(scaler, f"{TICKER}_scaler.pkl")


last_known = data.drop("Target", axis=1).tail(FORECAST_DAYS).values
last_known_scaled = scaler.transform(last_known)
future_preds = model.predict(last_known_scaled)

print(f"\n📈 Forecast for next {FORECAST_DAYS} days:")
for i, price in enumerate(future_preds, 1):
    print(f"Day {i}: ${price:.2f}")
