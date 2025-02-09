import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function to fetch data from OpenWeatherMap API
def fetch_weather_data(cities, api_key):
    #list that contains name, temperature, humidity and wind speed of each given cities
    data = []
    for city in cities:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            city_data = response.json()
            data.append({
                'City': city,
                'Temperature (°C)': city_data['main']['temp'],
                'Humidity (%)': city_data['main']['humidity'],
                'Wind Speed (m/s)': city_data['wind']['speed']
            })
            #if any input is given wrong then the error msessage will appear
        else:
            print(f"Failed to fetch data for {city}. Error: {response.status_code}")
            #all the collected lists are framed as dataframe and returned ti the main funtion
    return pd.DataFrame(data)

# Visualization functions for bar plot
def plot_bar(df, x_col, y_col, title, ylabel):
    plt.figure(figsize=(8, 6))
    sns.barplot(x=x_col, y=y_col, data=df, palette='viridis')
    plt.title(title)
    plt.xlabel(x_col)
    plt.ylabel(ylabel)
    plt.show()
    
# Visualization functions for scatter plot
def plot_scatter(df, x_col, y_col, hue_col, title):
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=x_col, y=y_col, hue=hue_col, data=df, s=100, palette='coolwarm')
    plt.title(title)
    plt.show()

# Visualization functions for correlation
def plot_correlation_heatmap(df):
    plt.figure(figsize=(8, 6))
    sns.heatmap(df.corr(), annot=True, cmap='YlGnBu')
    plt.title("Correlation Heatmap")
    plt.show()

# Main program
if __name__ == "__main__":
    # User inputs
    #Enter the name of city names that the user want to visualize
    cities = input("Enter city names separated by commas: ").split(',')
    #everybody have their own API key as private should enter here
    api_key = input("Enter your OpenWeatherMap API key: ")

    # Fetch data from the API
    weather_df = fetch_weather_data(cities, api_key)

    # Display the DataFrame
    print("\nWeather Data:")
    print(weather_df)

    # Visualize data
    plot_bar(weather_df, 'City', 'Temperature (°C)', 'Temperature in Different Cities', 'Temperature (°C)')
    plot_scatter(weather_df, 'Temperature (°C)', 'Humidity (%)', 'City', 'Temperature vs Humidity')
    plot_correlation_heatmap(weather_df)
