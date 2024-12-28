import unittest
from unittest.mock import patch

import requests

from app import app, get_weather, calculate_statistics


class TestWeatherApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    @patch("app.requests.get")
    def test_get_weather_success(self, mock_get):
        mock_response = {
            "name": "London",
            "sys": {"country": "GB"},
            "main": {"temp": 15.3, "humidity": 80},
            "weather": [{"main": "Cloudy"}],
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        result = get_weather("London")
        self.assertEqual(result["city"], "London")
        self.assertEqual(result["country"], "GB")
        self.assertEqual(result["temperature"], 15.3)
        self.assertEqual(result["humidity"], 80)
        self.assertEqual(result["weather"], "Cloudy")

    @patch("app.requests.get")
    def test_get_weather_failure(self, mock_get):
        # Simulate an API failure with a response
        mock_get.side_effect = requests.RequestException("API failure")
        result = get_weather("InvalidCity")
        self.assertIsNone(result)

    def test_calculate_statistics(self):
        weather_data_list = [
            {"temperature": 15.0, "city": "CityA"},
            {"temperature": 10.0, "city": "CityB"},
            {"temperature": 20.0, "city": "CityC"},
        ]
        avg_temp, coldest_city = calculate_statistics(weather_data_list)
        self.assertAlmostEqual(avg_temp, 15.0)
        self.assertEqual(coldest_city["city"], "CityB")

    def test_index_route(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

        # Check for specific content in the HTML response
        self.assertIn(b"Weather Application", response.data)
        self.assertIn(b'<div class="container mt-5">', response.data)

    @patch("app.get_weather")
    def test_get_weather_data_route_single_city(self, mock_get_weather):
        mock_get_weather.return_value = {
            "city": "London",
            "country": "GB",
            "temperature": 15.3,
            "humidity": 80,
            "weather": "Cloudy",
        }

        response = self.client.post("/get_weather", data={"cities": "London"})
        self.assertEqual(response.status_code, 200)
        json_data = response.get_json()

        # Check that weather data is present
        self.assertEqual(len(json_data["weather_data"]), 1)
        self.assertEqual(json_data["weather_data"][0]["city"], "London")

        # Check that statistics are empty for a single city
        self.assertEqual(json_data["statistics"], {})

    @patch("app.get_weather")
    def test_get_weather_data_route_multiple_cities(self, mock_get_weather):
        mock_get_weather.side_effect = [
            {"city": "CityA", "temperature": 15.0, "country": "GB"},
            {"city": "CityB", "temperature": 10.0, "country": "US"},
        ]

        response = self.client.post("/get_weather", data={"cities": "CityA, CityB"})
        self.assertEqual(response.status_code, 200)
        json_data = response.get_json()
        self.assertEqual(len(json_data["weather_data"]), 2)
        self.assertIn("statistics", json_data)
        self.assertEqual(json_data["statistics"]["coldest_city"], "CityB")

    @patch("app.get_weather")
    def test_get_weather_data_route_no_data(self, mock_get_weather):
        mock_get_weather.return_value = None

        response = self.client.post("/get_weather", data={"cities": "InvalidCity"})
        self.assertEqual(response.status_code, 400)
        json_data = response.get_json()
        self.assertIn("error", json_data)


if __name__ == "__main__":
    unittest.main()
