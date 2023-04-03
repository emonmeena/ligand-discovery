import requests
import json

# Set the API endpoint URL
url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"

# Set the parameters for the API request
params = {
    "db": "pubmed",
    "term": "cancer",
    "retmax": 10,
    "retmode": "json"
}

# Make the API request
response = requests.get(url, params=params)

# Parse the JSON response
data = json.loads(response.text)


print(data)
# Get the list of PubMed IDs from the response
pubmed_ids = data["esearchresult"]["idlist"]

# Print the list of PubMed IDs
print(pubmed_ids)
