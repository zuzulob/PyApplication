import os
import logging
from azure.storage.blob import BlobServiceClient
import azure.functions as func

def main(myblob: func.InputStream):
    logging.info(f"Python Blob trigger function processed blob \n"
                 f"Name: {myblob.name}\n"
                 f"Blob Size: {myblob.length} bytes")
 
    # Read the content of the blob
    blob_content = myblob.read()
    
    # Save the content to a file in the /tmp directory
    tmp_file_path = '/tmp/blob_content.txt'
    with open(tmp_file_path, 'wb') as f:
        f.write(blob_content)
    
    logging.info("Blob content saved to /tmp/blob_content.txt")

    # Upload the file to a different container
    try:
        upload_to_container(tmp_file_path, "csadest", "blob_content.txt")
        logging.info("File uploaded to destination container")
    except Exception as e:
        logging.error(f"Failed to upload file: {str(e)}")
    
    # Delete the file from /tmp
    try:
        os.remove(tmp_file_path)
        logging.info(f"Temporary file {tmp_file_path} deleted")
    except Exception as e:
        logging.error(f"Failed to delete temporary file: {str(e)}")

def upload_to_container(file_path, container_name, blob_name):
    connection_string = os.environ['AzureWebJobsStorage']
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

    with open(file_path, "rb") as data:
        blob_client.upload_blob(data, overwrite=True)
