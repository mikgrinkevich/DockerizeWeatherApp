# DockerizeWeatherApp

pip freeze > requirements. txt

docker build -t weather-app .

docker run -e api=529f562f0c902bd2954ba4d2497a11a4 -e api_date=87N88F6TZNN8Y86FJGWRCJUVN -p 5000:5000 weather-app
