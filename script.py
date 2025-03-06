# Install necessary libraries if not available
!pip install numpy pandas matplotlib scipy

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm

# Set seed for reproducibility
np.random.seed(42)

# Historical revenue data for CMA CGM (in billion USD) - Actual Data
extended_historical_revenues_full = {
    "2010": 10.2, "2011": 11.5, "2012": 12.0, "2013": 13.5, "2014": 14.8,  # Estimated values
    "2015": 15.7, "2016": 16.0, "2017": 21.1, "2018": 34.0, "2019": 38.9,
    "2020": 55.5, "2021": 74.5, "2022": 62.3, "2023": 47.0, "2024": 55.5
}

# Convert extended historical data to DataFrame
df_extended = pd.DataFrame(list(extended_historical_revenues_full.items()), columns=["Year", "Revenue"])
df_extended["Revenue"] = df_extended["Revenue"].astype(float)

# Define forecast parameters
years_ahead = 6  # Projecting from 2025 to 2030
current_revenue = df_extended["Revenue"].iloc[-1]  # Last known revenue (2024)
years = np.arange(2025, 2025 + years_ahead)

# Define growth rate distributions (Annual % Growth)
pessimistic_growth = norm.rvs(loc=-5, scale=2, size=years_ahead)  # -5% mean decline
neutral_growth = norm.rvs(loc=2, scale=1.5, size=years_ahead)  # 2% moderate growth
optimistic_growth = norm.rvs(loc=8, scale=3, size=years_ahead)  # 8% strong growth

# Generate revenue projections
pessimistic_forecast = [current_revenue]
neutral_forecast = [current_revenue]
optimistic_forecast = [current_revenue]

for i in range(years_ahead):
    pessimistic_forecast.append(pessimistic_forecast[-1] * (1 + pessimistic_growth[i] / 100))
    neutral_forecast.append(neutral_forecast[-1] * (1 + neutral_growth[i] / 100))
    optimistic_forecast.append(optimistic_forecast[-1] * (1 + optimistic_growth[i] / 100))

# Create DataFrame for projections
forecast_df = pd.DataFrame({
    "Year": np.append([2024], years),
    "Pessimistic": pessimistic_forecast,
    "Neutral": neutral_forecast,
    "Optimistic": optimistic_forecast
})

# Merge historical and forecasted data
full_forecast_df_extended = df_extended.copy()
for scenario in ["Pessimistic", "Neutral", "Optimistic"]:
    full_forecast_df_extended[scenario] = np.nan  # Initialize columns

# Fill the historical "Neutral" scenario with actual revenue data
full_forecast_df_extended.loc[full_forecast_df_extended["Year"] <= 2024, "Neutral"] = full_forecast_df_extended["Revenue"]

# Merge forecasted values
forecast_df_aligned = forecast_df.set_index("Year")
full_forecast_df_extended.set_index("Year", inplace=True)

for scenario in ["Pessimistic", "Neutral", "Optimistic"]:
    full_forecast_df_extended[scenario] = full_forecast_df_extended[scenario].combine_first(forecast_df_aligned[scenario])

full_forecast_df_extended.reset_index(inplace=True)

# Ensure "Year" column is formatted correctly for plotting
full_forecast_df_extended["Year"] = full_forecast_df_extended["Year"].astype(int)

# Plot the extended revenue forecast including historical data from 2010 to 2030 with projections
plt.figure(figsize=(10, 5))
plt.plot(full_forecast_df_extended["Year"], full_forecast_df_extended["Pessimistic"], label="Pessimistic Scenario", linestyle="--", color="red")
plt.plot(full_forecast_df_extended["Year"], full_forecast_df_extended["Neutral"], label="Neutral Scenario", linestyle="-", color="blue")
plt.plot(full_forecast_df_extended["Year"], full_forecast_df_extended["Optimistic"], label="Optimistic Scenario", linestyle=":", color="green")

# Highlight the transition from historical data to projections at 2025
plt.axvline(x=2024.5, color='black', linestyle="--", alpha=0.6)  # Visual separation

# Correct x-axis labels to ensure they display as integers
plt.xticks(full_forecast_df_extended["Year"], rotation=45)  # Rotate for better readability

plt.xlabel("Year")
plt.ylabel("Revenue (Billion USD)")
plt.title("CMA CGM Revenue Forecast (2010-2030) with Projections")
plt.legend()
plt.grid(True)
plt.show()

# Display updated forecast data
full_forecast_df_extended
