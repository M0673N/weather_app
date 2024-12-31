# Weather App
Simple weather app. Allows you to check the weather conditions in different cities. 
The aim of the project is to practice teamwork and DevOps practices.

# Live at: [weather-app-u0jr.onrender.com](https://weather-app-u0jr.onrender.com/)

## Requirements
- **Python 3**: [Download Python 3.10](https://www.python.org/downloads/release/python-3100/)

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