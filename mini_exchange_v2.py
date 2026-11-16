import random
import matplotlib.pyplot as plt

# --- UPGRADED MARKET SIMULATION ---
prices = [100.0]       # Track stock prices
volumes = [50.0]       # Track number of shares traded at each step
current_price = 100.0

for step in range(300):
    # Halfway through (step 150), simulate "good news" pushing the price up
    if step == 150:
        current_price += 8.0

    # Random market fluctuation
    market_push = random.uniform(-1.2, 1.2)
    current_price = round(current_price + market_push, 2)
    
    # Generate random trade volume between 10 and 200 shares
    trade_volume = random.randint(10, 200)
    
    # Save to our history logs
    prices.append(current_price)
    volumes.append(trade_volume)

# --- SHOW RESULTS ---
print("Advanced Simulation Complete!")
print("Starting Price: ₹100.00")
print("Final Stock Price: ₹", prices[-1])
print("Total Shares Traded Across All Steps:", sum(volumes))

# --- DRAW PROFESSIONAL DUAL CHARTS ---
plt.figure(figsize=(8, 6))

# Top Chart: Stock Price
plt.subplot(2, 1, 1)
plt.plot(prices, color='blue', linewidth=2)
plt.title("MiniExchange Pro: Price & Volume Tracker")
plt.ylabel("Price (₹)")
plt.grid(True)

# Bottom Chart: Trading Volume (Bar Chart)
plt.subplot(2, 1, 2)
plt.bar(range(len(volumes)), volumes, color='green', alpha=0.6)
plt.xlabel("Trade Steps")
plt.ylabel("Volume")
plt.grid(True)

plt.tight_layout()
plt.show()
