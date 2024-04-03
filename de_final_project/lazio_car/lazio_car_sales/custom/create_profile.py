import ruamel.yaml
import os
from pathlib import Path

from mage_ai.settings.repo import get_repo_path

@custom
def load_profile(*args, **kwargs):
    local_dbt = get_repo_path() + '/dbt/lazio_car'
    local_dbt_path = Path(local_dbt)
    
    print('Writing demo profile...')
    
    yaml = ruamel.yaml.YAML()
    yaml.preserve_quotes = True
    yaml.explicit_start = True

    yml = yaml.load(f"""
    default:
      target: development  # The target environment, such as dev, staging, or prod - used when no other value is explicitly given
      outputs:
        development:
          type: bigquery
          method: service-account  # Use service account for authentication
          keyfile: "/home/src/my_cred.json"  # Path to your service account JSON key file
          project: de-final-project-417421  # Your GCP project ID
          dataset: prod_mage  # The dataset where dbt will create tables in BigQuery
          threads: 1  # Number of threads to use when executing dbt commands (optional)
          timeout_seconds: 300  # Timeout for individual queries in seconds (optional)
          location: europe-west8  # The location of your BigQuery dataset (optional)    
    """
    )

    with open(local_dbt + '/profiles.yml', 'w') as file:
        yaml.dump(yml, file)