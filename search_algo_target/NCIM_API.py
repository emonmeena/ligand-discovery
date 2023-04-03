import requests
import json

# Set the base URL for the API endpoints
base_url = 'https://api-evsrest.nci.nih.gov'

# Define the Concept-ID of interest
codeOrName = 'C0155685'  # Replace with the desired Concept-ID
terminology = "ncim"

# Define the API endpoint for retrieving drugs associated with the concept
endpoint = f'{base_url}/api/v1/concept/{terminology}/search'

# Send a GET request to the endpoint and retrieve the response

response = requests.get(endpoint)
response = response.json()

print(response)

# # Check if the response was successful (HTTP status code 200)
# if response.status_code == 200:
#     # Convert the response to JSON format
#     response_data = response.json()

#     # Extract the drug information from the response
#     drugs = []
#     for assoc in response_data['associatedConcepts']:
#         if assoc['concept']['semanticType'] == 'Clinical Drug':
#             drugs.append(assoc['concept']['preferredName'])

#     # Print the retrieved drug information
#     print(f'Drugs associated with Concept-ID {concept_id}:')
#     for drug in drugs:
#         print(f'- {drug}')
# else:
#     # Print an error message if the response was not successful
#     print(f'Error retrieving data. Status code: {response.status_code}')
