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
