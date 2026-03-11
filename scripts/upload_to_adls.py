from azure.storage.blob import BlobServiceClient
import os

connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")

container_name = "raw-data"

blob_service_client = BlobServiceClient.from_connection_string(connection_string)

def upload_file(local_file, blob_name):

    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

    with open(local_file, "rb") as data:
        blob_client.upload_blob(data, overwrite=True)

    print("Uploaded:", blob_name)