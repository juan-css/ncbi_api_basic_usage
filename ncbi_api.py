# %%

import requests
import json

# These endpoints can be used to access the NCBI Datasets API (better with metadata)
# Recommended to use the NCBI datasets CLI tool to download the sequences of the metadata obtained from the API

# %%
#######################
url_taxonomy = "https://api.ncbi.nlm.nih.gov/datasets/v2alpha/taxonomy"

VIRUS_NAME = "dengue virus"
# VIRUS_NAME = "dengue type 1 d1 virus"
# VIRUS_NAME = "dengue virus type 1"
# VIRUS_NAME = "dengue virus type 2"
# VIRUS_NAME = "dengue virus type 3"
# VIRUS_NAME = "dengue virus type 4"
# VIRUS_NAME = "Dengue virus 1 Brazil/97-11/1997"

payload = json.dumps({
  "taxons": [
    VIRUS_NAME
  ]
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url_taxonomy, headers=headers, data=payload)

print(response.text)

response_data = response.json()

tax_id = response_data["taxonomy_nodes"][0]["taxonomy"]["tax_id"]
print("Tax ID: ", tax_id)


# %%
#######################
url_virus_genome = f"https://api.ncbi.nlm.nih.gov/datasets/v2alpha/virus/taxon/{tax_id}/genome"

payload = {}
headers = {}

response = requests.request("GET", url_virus_genome, headers=headers, data=payload)

print(response.text)

download_metadata_url = json.loads(response.text)

# Extract hydrated URL
url_get_data = download_metadata_url["hydrated"]["url"]
print("URL to downloado data: ", url_get_data)

# %%
#######################

# Access the URL to get the metadata

output_file = "dengue_virus_genome_api.zip"

response = requests.get(url_get_data, stream=True)

if response.status_code == 200:
    with open(output_file, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    print(f"Download complete: {output_file}")
else:
    print(f"Failed to download file. Status code: {response.status_code}")

# %%

