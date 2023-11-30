from qdrant_client import QdrantClient
from qdrant_client.http import models
from sentence_transformers import SentenceTransformer
# Initialize a pre-trained sentence transformer model
import pandas as pd
import os
# Load the CSV file
# file_path = '/'  # Replace with your file path
current_directory = os.path.dirname(os.path.abspath(__file__))

    # Construct the full path to other_file.py
file_path = os.path.join(current_directory, 'bigBasketProducts.csv')
data = pd.read_csv(file_path)

model = SentenceTransformer('all-MiniLM-L6-v2')
client = QdrantClient("localhost", port=6333)
query=input()
def search_in_qdrant(query):
    # Convert query to vector
    query_vector = model.encode([query])

    # Search in Qdrant
    search_result = client.search(collection_name="m_coll", query_vector=query_vector[0], limit=3)
    return search_result
results = search_in_qdrant(query)

context=data.loc[results[0].id-1,"product"]+"   "+data.loc[results[0].id-1,"description"]+data.loc[results[1].id-1,"product"]+" "+data.loc[results[1].id-1,"description"]+data.loc[results[2].id-1,"product"]+"   "+data.loc[results[2].id-1,"description"];

from openai import OpenAI

client = OpenAI(api_key="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")
print("in progress")
response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": f"Query: {query}\nText: {context}\nFormat the context according to the query as follows:\n",},
    
  ]
)
print("done")
print(response.choices[0].message.content)
