## Group DevOps project description - Group Kangaroo
Members: Tim, Samuel, Lovisa

Ideas:
Idea 1:
Web application where one or more buttons will show current weather for a specific coordinate.

Idea 2:
Web application where you can insert own coordinates and get the current weather.

Idea 3: 
Web application where you can choose a city in a dropdown list and see the current weather for chosen city.

Description:
SMHI's API will be used to collect weather data from a specific location. 
When the app is run several tests in GitHub Actions will run and test the data and code.
This will later be sent to a docker image and sent to Azure.

Tests: 
Validation that data comes from correct coordinates.
Validation that timeframe is correct.
Validation that syntax is working in code.
