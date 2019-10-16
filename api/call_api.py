#Use the request library to simplify making a REST API call from Python
import pip._vendor.requests

# We will need the json library to read the data passed back
# by the web service
import json
# We need the key to access our Computer Vision Service
SUSCRIPTION_KEY = '2e97d095564847e3a6954add736ad1a3'
# We need the address of our Computer Vision Service
vision_service_address = 'https://brazilsouth.api.cognitive.microsoft.com/vision/v1.0/'
# Add the name of the function we want to call to the address
address = vision_service_address + 'analyze'

# According to the documentation for the analyze image function
# There are three optional parameters: language, details and visualFeatures
parameters = {'visualFeatures':'Description,Color','language':'en'}

# Open the image file to get a file object containing the image to analyze
image_path = 'C:\dev\python-getting-started\\api\\testimages\\bear.png'
image_data = open(image_path, 'rb').read()

# According to the documentation for the analyze image function
# we need to specify the suscription key and the content type
# in the HTTP header. Content Type is application/octet-stream
headers = {'Content-Type':'application/octet-stream','Ocp-Apim-Suscription-Key': SUSCRIPTION_KEY}

# According to the documentation for the analyze image function
# we use HTTP POST to call this function
response = pip._vendor.requests.post(address, headers = headers, params = parameters, data = image_data)

# Raise an exception if the call returns an error code
response.raise_for_status()

# Display the JSON results returned
results = response.json()
print(json.dumps(results))

