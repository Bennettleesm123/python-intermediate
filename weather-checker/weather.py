"""
WEATHER-CHECKER — SIMPLE EXPLANATION

WHAT THIS PROGRAM DOES:
Fetches the current weather for a city from the OpenWeatherMap API and prints it.

BEFORE RUNNING:
1) Get a free API key at openweathermap.org.
2) Set it in your terminal:  export API_KEY=your_key_here
3) Run:  python weather.py "London"

HOW IT WORKS (step-by-step):
1) Reads my API key from the environment (os.environ["API_KEY"]).
2) Builds a URL with the city name and my key.
3) Sends a GET request using requests.get(...).
4) Converts the response to JSON and prints temperature + description.

WHAT I SHOULD NOTICE:
- If I forget the API key, it prints a helpful message.
- If the city is invalid, the API returns an error string that gets printed.
"""


import sys, os, requests

def get_weather(city):
    key=os.environ.get("API_KEY")
    if not key:
        print("Please set API_KEY env var.")
        return
    url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric"
    r=requests.get(url)
    if r.status_code!=200:
        print("Error:",r.text); return
    data=r.json()
    print(f"{city}: {data['main']['temp']}°C, {data['weather'][0]['description']}")

if __name__=="__main__":
    if len(sys.argv)<2:
        print("Usage: python weather.py <city>")
    else:
        get_weather(sys.argv[1])
