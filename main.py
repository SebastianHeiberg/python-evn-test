import requests

# URL of the webpage you want to fetch
url = 'https://www.kea.dk'

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200 indicates success)
if response.status_code == 200:
    # Print the content of the webpage
    print("Content of the webpage:")
    print(response.text)
else:
    # Print an error message if the request was not successful
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
