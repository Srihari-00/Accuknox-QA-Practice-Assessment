import requests  # Library for handling HTTP requests

# Define the application URL to check
URL = "http://example.com"  # Replace with the actual application URL

try:
    # Send an HTTP GET request to the application
    response = requests.get(URL)

    # Check if the application is responding with a success status code
    if response.status_code == 200:
        print("Application is UP")  # Application is functioning normally
    else:
        print(f"Application is DOWN (Status Code: {response.status_code})")  # Error status returned
except requests.exceptions.RequestException as e:
    # Handle cases where the application cannot be reached
    print(f"Application is DOWN (Error: {e})")
