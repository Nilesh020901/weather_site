from django.shortcuts import render
import json
import urllib.request
import urllib.parse

def index(request):
    if request.method == 'POST':
        city = request.POST['city'].strip()  # Remove leading and trailing spaces from the city name
        
        # Base URL for the OpenWeatherMap API
        base_url = 'http://api.openweathermap.org/data/2.5/weather'
        
        # Parameters for the API request
        params = {
            'q': city,  # City name entered by the user
            'appid': '34390a97d43446de8bbca2d7560942a2'  # Your API key
        }
        
        # Encode the parameters and create the complete URL
        url = f"{base_url}?{urllib.parse.urlencode(params)}"
        
        try:
            # Fetch the JSON data from the API
            source = urllib.request.urlopen(url).read()
            
            # Convert JSON data to a dictionary
            list_of_data = json.loads(source)
            
            # Extract required information and create a data dictionary
            data = {
                "country_code": str(list_of_data['sys']['country']),
                "coordinate": str(list_of_data['coord']['lon']) + ' ' + str(list_of_data['coord']['lat']),
                "temp": str(list_of_data['main']['temp']) + ' K',  # Temperature with unit K
                "pressure": str(list_of_data['main']['pressure']),
                "humidity": str(list_of_data['main']['humidity']),
            }
            print(data)
        except Exception as e:
            # Handle any errors (e.g., invalid city name or API issues)
            data = {"error": f"Could not retrieve weather data: {e}"}
    else:
        data = {}  # Empty data if the request method is not POST
    
    # Render the template with the data
    return render(request, "weather/index.html", data)
