import requests
import os

def download_file(url, save_path):
    """
    Download a file from the given URL and save it to the specified path.
    
    Args:
    url (str): The URL of the file to download.
    save_path (str): The path where the downloaded file will be saved.
    """
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Open the file in binary write mode and write the content
            with open(save_path, 'wb') as file:
                file.write(response.content)
            print("File downloaded successfully")
        else:
            print(f"Failed to download file. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage:
url = "https://example.com/samplefile.txt"
save_path = "samplefile.txt"
download_file(url, save_path)
