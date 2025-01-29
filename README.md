# Weather App
Simple weather app. Allows you to check the weather conditions in different cities.
The aim of the project is to practice teamwork and DevOps practices.

![weather app](https://github.com/user-attachments/assets/620f6cac-4274-44fd-ae32-57cb8f90a7e6)

# Live at: [m0673n-weather-app.onrender.com](https://m0673n-weather-app.onrender.com/)

## Requirements
- **Python 3**: [Download Python 3.10](https://www.python.org/downloads/release/python-3100/)
- **<a name="env">`.env` file</a>**: Before running the application, ensure you have an `.env` file in your project directory with the following variable:
```
API_KEY=your_api_key
```
Replace `your_api_key` with your actual API key obtained from the weather service provider.

## Cloning and Running the Project
- **Windows**:
```
git clone https://github.com/M0673N/weather_app.git &&
cd ./weather_app/ &&
python -m venv .venv &&
source .venv/Scripts/activate &&
python -m pip install --upgrade pip &&
pip install -r requirements.txt &&
echo "Server has been started on http://127.0.0.1:5000" &&
python app.py
```
- **Linux and macOS**:
```
git clone https://github.com/M0673N/weather_app.git &&
cd ./weather_app/ &&
python3 -m venv .venv &&
source .venv/Scripts/activate &&
python3 -m pip install --upgrade pip &&
pip3 install -r requirements.txt &&
echo "Server has been started on http://127.0.0.1:5000" &&
python3 app.py
```

## Runing the Tests
- **Windows**:
```
python -m unittest test_app.py
```
- **Linux and macOS**:
```
python3 -m unittest test_app.py
```

## Runing with Docker
- Don't forget the [.env](#env) file.
```
docker run -P -d --name weather_app --env-file .env m0673n/weather_app
```