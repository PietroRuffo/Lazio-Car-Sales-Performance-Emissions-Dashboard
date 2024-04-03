# Import necessary libraries
import io  # Input/output operations
import pandas as pd  # Data manipulation library
import requests  # HTTP requests library
import zipfile  # ZIP file manipulation library

# Decorator to load data from an API
@data_loader
def load_data_from_api(*args, **kwargs):
    # Columns to read from the CSV
    columns_to_read = [ 1, 2, 3, 4, 5, 7, 9, 10, 11, 12] 

    # List of regions from which data will be fetched
    regions = ['Lazio']

    # Iterate over each region to fetch data
    for region in regions:
        # Construct the URL for fetching data for the specific region
        url = f'https://dati.mit.gov.it/hfs/parco_circolante_{region}.csv.zip'
        
        # Define the filename for the CSV file after extraction
        filename = f'Circolante_{region}.csv' 
        
        # Make a request to fetch the ZIP file containing the CSV
        r = requests.get(url)
        
        # Extract the ZIP file:

        z = zipfile.ZipFile(io.BytesIO(r.content))
        # Breaking down line 29:
          #Extracts the contents of the received ZIP archive:
          # - Converts the raw bytes content of the HTTP response into a file-like object using io.BytesIO().
          # - Creates a ZipFile object using zipfile.ZipFile(), representing the contents of the ZIP archive.
          # This object can be used to interact with the contents of the ZIP archive.
        z.extractall()  # Extract all files from the ZIP archive
        
        # Read the CSV into a DataFrame, selecting specific columns
        df = pd.read_csv(filename, sep=',', usecols=columns_to_read, low_memory=False)

    # Return the DataFrame containing the data
    return df

# Decorator for testing row count
@test
def test_output(df, *args) -> None:
    # Check if the DataFrame has at least 10000 rows
    assert len(df.index) >= 1000000, 'The data does not have enough rows.'
    assert len(df.columns) == 10, 'Number of total columns is not correct'