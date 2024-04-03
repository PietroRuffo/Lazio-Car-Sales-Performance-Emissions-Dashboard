if 'data_loader' not in globals():
    # If 'data_loader' is not found in the global namespace, import it from the specified module.
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    # If 'test' is not found in the global namespace, import it from the specified module.
    from mage_ai.data_preparation.decorators import test

import pyarrow as pa
import pyarrow.parquet as pq
import os

# Set the path to the Google Cloud credentials file.
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/src/my_cred.json'

# Decorated function to load data.
@data_loader
def load_data(*args, **kwargs):
    """
    Template code for loading data from any source.

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your data loading logic here
    bucket_name = 'de-final-project-417421-vehicle-bucket'
    project_id = 'de-final-project-417421'
    table_name = 'vehicle_Lazio'

    # Define the root path for data loading.
    root_path = f'{bucket_name}/{table_name}'

    # Create a Google Cloud Storage filesystem instance using pyarrow.
    gcs = pa.fs.GcsFileSystem()  # PyArrow will automatically connect with the credentials set above.

    # Load data from Parquet files in the specified root path.
    arrow_df = pq.ParquetDataset(root_path, filesystem=gcs)
    df = arrow_df.read_pandas().to_pandas()
    return df

# Decorated function to test the output of the block.
@test
def test_output(df, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    # Check if the output is not None.
    assert df is not None, 'The output is undefined'