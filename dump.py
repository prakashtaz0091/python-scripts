from pymongo import MongoClient
from tqdm import tqdm
import json

# Connect to the cloud MongoDB
client = MongoClient("<mongodb cloud uri>")

# Select the database and collection
db = client['db_name']
collection = db['collection_name']

# Query to limit data (e.g., first 10000 documents)
limit = 1000000  # Set the limit for the number of documents to dump
documents = collection.find().limit(limit)

# Save the documents to a JSON file with a progress bar
with open('output_file_name.json', 'w') as file:
    # Use tqdm for the progress bar
    with tqdm(total=limit, desc="Dumping Data", unit="docs") as pbar:
        json.dump([doc for doc in tqdm(documents, total=limit, desc="Fetching Docs", unit="doc")], file, default=str)
        pbar.update(limit)

print("Limited data dumped successfully!")
