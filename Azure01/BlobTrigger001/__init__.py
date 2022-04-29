import logging
from typing import Container

import azure.functions as func
from azure.storage.blob import BlobServiceClient,BlobClient

def main(myblob: func.InputStream):
    logging.info(f"Python blob trigger function processed blob \n"
                 f"Name: {myblob.name}\n"
                 f"Blob Size: {myblob.length} bytes")
    
    connection_string ="DefaultEndpointsProtocol=https;AccountName=tsworks;AccountKey=oj8UkuKB1oCLkhQXFFCGdM0ljUj6QR6b0h7yroBhyXYpCXEgsOTIk+6aO0wM+xCNcC69iUnWmX/+IRHPqVmW3g==;EndpointSuffix=core.windows.net"
    service = BlobServiceClient.from_connection_string(conn_str=connection_string)
    blob = service.get_blob_client(container="outbound",blob=myblob.name)
    blob.upload_blob(myblob)