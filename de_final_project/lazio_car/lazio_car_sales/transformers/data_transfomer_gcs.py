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

    # Translating 'destination' labels from Italian to English
    df['destination'] = df['destination'].replace({
         'AUTOVEICOLO IN SERVIZIO PUBBLICO DI LINEA INTEGRATIVO': 'Supplementary Public Service Vehicle',
         'AUTOVEICOLO USO ESCLUSIVO DI POLIZIA': 'Police Exclusive Use Vehicle',
         'AUTOVETTURA PER TRASPORTO DI PERSONE': 'Car for Transporting People',
         'AUTOBUS PER TRASPORTO DI PERSONE': 'Bus for Transporting People',
         'AUTOCARRO PER TRASPORTO DI COSE': 'Truck for Transporting Goods',
         'AUTOCARAVAN': 'Motorhome',
         'AUTOVEICOLO PER USO SPECIALE': 'Special Purpose Vehicle',
         'TRAS.SPECIFICO PERSONE PART.CONDIZIONI': 'Specific Transport of People under Certain Conditions',
         'AUTOVEIC.TRASP.PROMISCUO PERSONE/COSE': 'Mixed Transport Vehicle for People/Goods',
         'TRATTORE STRADALE PER RIMORCHIO': 'Road Tractor for Trailer',
         'TRATTORE PER SEMIRIMORCHIO': 'Tractor for Semi-Trailer',
         'QUADRICICLO PER TRASPORTO DI PERSONE': 'Quadricycle for Transporting People',
         'QUADRICICLO PER TRASPORTO DI COSE': 'Quadricycle for Transporting Goods',
         'QUADRICICLO PER USO SPECIALE': 'Special Purpose Quadricycle',
         'QUADRICICLO TRASPORTO SPECIFICO': 'Specific Transport Quadricycle',
         'MOTOVEICOLO USO ESCLUSIVO DI POLIZIA': 'Police Exclusive Use Motorcycle',
         'TRICICLO PER TRASPORTO PROMISCUO': 'Mixed Transport Tricycle',
         'TRICICLO PER USO SPECIALE': 'Special Purpose Tricycle',
         'TRICICLO PER TRASPORTO SPECIFICO': 'Specific Transport Tricycle',
         'MOTOCICLO PER TRASPORTO PERSONE': 'Motorcycle for Transporting People',
         'TRICICLO PER TRASPORTO COSE': 'Tricycle for Transporting Goods',
         'TRICICLO PER TRASPORTO DI PERSONE': 'Tricycle for Transporting People'
    })


    # Translating 'fuel' labels from Italian to English
    df['fuel'] = df['fuel'].replace({
         'GASOLIO/METANO': 'Diesel/Methane',
         'GASOLIO/GPL': 'Diesel/LPG',
         'BENZINA': 'Petrol',
         'BENZINA/OLIO': 'Petrol/Oil',
         'BENZINA/WANK': 'Petrol/Wank',
         'ELETTRICA': 'Electric',
         'GASOLIO': 'Diesel',
         'GPL': 'LPG',
         'BENZINA/GPL': 'Petrol/LPG',
         'BENZINA/METANO': 'Petrol/Methane',
         'METANO': 'Methane',
         'MISCELA': 'Mixture',
         'PETROLIO': 'Petroleum',
         'IBRIDO BENZINA/ELETTRICO': 'Hybrid Petrol/Electric',
         'IBRIDO GASOLIO/ELETTRICO': 'Hybrid Diesel/Electric',
         'BENZINA/ETANOLO': 'Petrol/Ethanol'
    })


    # Translating 'usage' labels from Italian to English
    df['usage'] = df['usage'].replace({
        'PROPRIO': 'Own',
        'DI TERZI DA NOLEGGIO CON CONDUCENTE': 'Third-party with driver rental',
        'DI TERZI DA LOCARE SENZA CONDUCENTE': 'Third-party rental without driver',
        'DI TERZI': 'Third-party',
        'DI TERZI CON AUTORIZZAZIONE VINCOLATE': 'Third-party with constrained authorization',
        'DI TERZI CON AUTORIZZAZIONE LIBERA': 'Third-party with free authorization',
        'USO SPECIALE': 'Special use'
    })

    
    return df  


@test
def test_output(df, **args):

    assert len(df.index) >= 10000, 'The data does not have enough rows.'