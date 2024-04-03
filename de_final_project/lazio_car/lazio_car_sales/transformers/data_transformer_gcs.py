# Check if the 'transformer' function is not defined in the global namespace. If not, import it from the mage_ai.data_preparation.decorators module.
if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer

# Check if the 'test' function is not defined in the global namespace. If not, import it from the mage_ai.data_preparation.decorators module.
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

# Import necessary libraries
import pandas as pd  # Data manipulation library
from datetime import datetime  # Date and time operations
import pyarrow as pa  # Arrow memory format library
import pyarrow.parquet as pq  # Parquet file format library

@transformer
def transform(df, *args, **kwargs):
    
    # Rename columns for clarity
    df.columns = ['vehicle_type', 'destination', 'usage', 'city', 'automaker', 'fuel', 'registration_date', 'euro_class', 'co2_emission', 'vehicle_mass']

    # Drop rows with missing values
    df.dropna(inplace=True)


    # Extract registration year and month from registration date
    df['registration_year'] = df['registration_date'].apply(lambda x: x[-4:])
    df['registration_month'] = df['registration_date'].apply(lambda x: x[3:5])

    # Drop 'registration_date' column as it's no longer needed
    df.drop(columns=['registration_date'], inplace=True)


    # Redefine dtypes
    df = df.astype({
        'vehicle_type': str,
        'destination': str,
        'usage': str,
        'city': str,
        'automaker': str,
        'fuel': str,
        'registration_year': int,
        'registration_month': int,
        'euro_class' : str,
        'co2_emission':int, 
        'vehicle_mass':int
    })

    return df  


@test
def test_output(df, **args):

    assert len(df.index) >= 10000, 'The data does not have enough rows.'