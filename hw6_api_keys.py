# OpenWeatherMap API Key
import os
from dotenv import load_dotenv

load_dotenv()
weather_api_key = os.environ.get('api')
