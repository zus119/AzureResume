import azure.functions as func
from azure.cosmos import CosmosClient, exceptions
import azure.cosmos.exceptions as exceptions
import os
import datetime
import json
import logging

app = func.FunctionApp()

@app.route(route="CosmosQueryFunction", auth_level=func.AuthLevel.FUNCTION)
def CosmosQueryFunction(req: func.HttpRequest) -> func.HttpResponse:
    url = os.environ['COSMOS_DB_URL']
    key = os.environ['COSMOS_DB_KEY']
    client = CosmosClient(url, credential={'masterKey': key})
    database_name = 'AzureResume'
    container_name = 'Counter'
    database = client.get_database_client(database_name)
    container = database.get_container_client(container_name)

    try:
        # Read the item
        item = container.read_item(item='1', partition_key='1')
        count = item.get('count', 0)  # Default to 0 if count is not present

        # Increment the count
        item['count'] = count + 1

        # Replace the item with the incremented count
        container.replace_item(item=item['id'], body=item)

        # Return the updated count in the response
        return func.HttpResponse(
        json.dumps({"count": item['count']}),  # Ensure this is a valid JSON structure
        status_code=200,
        headers={
            'Content-Type': 'application/json'
        }
    )
    except exceptions.CosmosHttpResponseError as e:
        return func.HttpResponse(f"Error interacting with Cosmos DB: {str(e)}", status_code=500)