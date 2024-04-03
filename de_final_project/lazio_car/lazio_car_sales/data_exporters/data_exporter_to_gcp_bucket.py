import pyarrow as pa  # Importing pyarrow library for working with Arrow data
import pyarrow.parquet as pq  # Importing parquet module from pyarrow for Parquet file handling
import os  # Importing os module for interacting with the operating system

# Checking if 'data_exporter' is not in global namespace
if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter  # Importing data_exporter decorator

# Setting the path to the Google Cloud service account credentials
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/src/my_cred.json'

# Defining variables for bucket, project, and table names
bucket_name = 'de-final-project-417421-vehicle-bucket'
project_id = 'de-final-project-417421'
table_name = 'vehicle_Lazio'

# Constructing the root path using bucket and table names
root_path = f'{bucket_name}/{table_name}'

# Defining a function 'export_data' decorated with 'data_exporter':
#    Function to export data to Google Cloud Storage in Parquet format.
@data_exporter
def export_data(data, *args, **kwargs):
    # Converting the input data to an Arrow Table
    table = pa.Table.from_pandas(data)

    # Creating a GCS (Google Cloud Storage) filesystem object
    gcs = pa.fs.GcsFileSystem()

    # Writing the Arrow Table to a Parquet dataset in Google Cloud Storage
    pq.write_to_dataset(
        table,
        root_path=root_path,
        partition_cols=['registration_year'],  # Partitioning the dataset by registration year
        filesystem=gcs  # Specifying the GCS filesystem for writing
    )
