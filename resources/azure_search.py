#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Time    : 3/30/2023 2:26 PM
# @Author  : Owen_study
# @Email   : owen_study@126.com
# @File    : azure_search.py
# @Software: PyCharm
# ===============================================
import os
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient


index_name = "hotels-sample-index"
# Get the service endpoint and API key from the environment
endpoint = 'https://ebao-ods.search.windows.net'
# endpoint = os.environ["SEARCH_ENDPOINT"]
key = 'F5jn4xNZ2Eliwg05Jkvb8hCEMyYSiFEAnn5xEombJwAzSeCQcKBF'
# key = os.environ["SEARCH_API_KEY"]

# Create a client
credential = AzureKeyCredential(key)
client = SearchClient(endpoint=endpoint,
                      index_name=index_name,
                      credential=credential)
results = client.search(search_text="luxury")

for result in results:
    print(result.keys())
    # if "HotelId" in result.keys():
    #     print(result["HotelId"])
    # if "HotelName" in result.keys():
    #     print(result["HotelName"])
    print("{}: {})".format(result["HotelId"] , result["HotelName"]))

DOCUMENT = {
    'Category': 'Hotel',
    'HotelId': '1000',
    'Rating': 4.0,
    'Rooms': [],
    'HotelName': 'Azure Inn',
}

search_client = SearchClient(endpoint, index_name, AzureKeyCredential(key))

result = search_client.upload_documents(documents=[DOCUMENT])

print("Upload of new document succeeded: {}".format(result[0].succeeded))
if __name__ == '__main__':
    pass
