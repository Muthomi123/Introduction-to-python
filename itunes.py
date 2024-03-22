import json
import requests
import sys

if len(sys.argv) != 2:
    print("Usage: python script.py <artist_name>")
    sys.exit(1)

# Retrieve the artist name from command line arguments
artist_name = sys.argv[1]

# Construct the API request URL
url = f"https://itunes.apple.com/search?entity=song&limit=1&term={artist_name}"

# Make the API request
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse and print the JSON response
    data = response.json()
    print(json.dumps(data, indent=2))
else:
    # Print an error message if the request was not successful
    print(f"Error: {response.status_code}")
    sys.exit(1)
