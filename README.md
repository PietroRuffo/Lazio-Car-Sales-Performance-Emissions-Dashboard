# Lazio-Car-Sales-Performance-Emissions-Dashboard

This work, developed as the final project for [Data Engineering Zoomcamp 2024](https://github.com/DataTalksClub/data-engineering-zoomcamp), introduces an interactive [dashboard](https://lookerstudio.google.com/reporting/1fdade85-34b0-4e36-8552-6ea9ac601eb2/page/Az7uD) tailored for stakeholders in the [Lazio](https://en.wikipedia.org/wiki/Lazio#:~:text=Geography,-Relief%20map%20of&text=Lazio%20comprises%20a%20land%20area,Tyrrhenian%20Sea%20to%20the%20west.) car industry. It offers essential insights into car sales, registrations, and vehicle specifications, enabling informed decision-making.

Data Source: [Italian Ministry of Transport] (https://dati.mit.gov.it/catalog/dataset/dataset-parco-circolante-dei-veicoli/resource/0e49d85b-6836-492f-bafc-f612aa8ea23d)

*NB. Data refers to new cars only (second/third hand cars are excluded) and is updated to the end of 2019.*

Key Insights:
- **Total Cars Sold**: Provide an overview of the total number of cars sold within the specified perimiter.
- **Sales Performance by Automaker**: Identify top performers in the region through a clear bar chart.
- **Seasonal Sales Trends**: Uncover peak sales months with a line chart, allowing for optimized resource allocation and targeted marketing campaigns.
- **Environmental Impact Analysis**: Analyze the average CO2 emissions of different automakers' offerings to understand their environmental impact within Lazio.
- **Euro Class Distribution**: Gain insights into the distribution of cars by their Euro class compliance standards.

Flexible Exploration with Filters:
- Registration Year: Narrow your focus by selecting specific registration years (until 2019)
- Fuel Type: Filter results based on fuel type (gasoline, diesel, hybrid, etc.).
- City: Analyze data for specific cities within Lazio.

By combining data visualization and user-friendly filters, this dashboard empowers data-driven decision making for sales strategies, marketing initiatives, and potentially eco-conscious efforts within the Lazio car market.

Please visualize and use the dashboard at the following by clicking [here](https://lookerstudio.google.com/reporting/1fdade85-34b0-4e36-8552-6ea9ac601eb2/page/Az7uD)

![image](https://github.com/PietroRuffo/Lazio-Car-Sales-Performance-Emissions-Dashboard/assets/99428541/87031079-cb73-42eb-b96c-3b7fec91d5c8)


The following diagram indicates how the project was set up:

![image](https://github.com/PietroRuffo/Lazio-Car-Sales-Performance-Emissions-Dashboard/assets/99428541/9cd5b7c4-b638-4124-9a4f-0f75f8925533)


The diagram shows a **monthly** **batch** process that can be updated **manually**. It starts with CSV data from the Italian Ministry of Infrastructure and Transportation. This data is converted to Parquet format and transformed and then uploaded to a Google Cloud Platform (GCP) Bucket. After more transformations, it's stored in a BigQuery data warehouse. Inside the warehouse, DBT is used for further transformations. Finally, the cleaned data is used to create a dashboard in Looker Studio. All of this happens within Mage.ai running on a Docker container. GCP resources are set up in advance using Terraform.

Instructions:

1. Begin by installing Terraform and Docker.
2. Create a Google Cloud Platform (GCP) account if you haven't already.
3. Within GCP, create a project and generate/download a service account key in JSON format.
4. Clone the repository using the command:

    ```
    git clone https://github.com/PietroRuffo/Lazio-Car-Sales-Performance-Emissions-Dashboard de_final_project
    ```

5. Navigate to "C:\Users\...\de_final_project\terraform\keys" and move the downloaded JSON file here, renaming it as "my_cred.json".
6. Open "C:\Users\...\de_final_project\terraform\variables.tf" and update the project_id at line 9 and the bucket's name at line 34. Similarly, update "main.tf" at line 17 with the bucket's name.
7. Using the CLI, navigate to "C:\Users\...\de_final_project\terraform" and run:

    ```bash
    # Initialize state file (.tfstate)
    terraform init

    # Check changes to new infra plan
    terraform plan

    # Create new infra
    terraform apply
    ```


    
*!!! IF YOU ENCOUNTER ANY ISSUE IN SETTING UP GCP AND TERRAFORM PLEASE REFER TO THIS [LINK](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/01-docker-terraform/1_terraform_gcp) FOR FURTHER INSTRUCTIONS. DO ALSO CHECK [THIS](https://www.youtube.com/watch?v=Y2ux7gq3Z0o) FOR PROPER ACCOUNT KEY CONFIG IN TERRAFORM !!!*



8. Once GCP resources are created, navigate to "C:\Users\...de_final_project\lazio_car".

   ```
    cd "C:\Users\...\de_final_project\lazio_car"
    ```
9. Open Docker by double-clicking on the Docker desktop icon.
10. Run:

    ```bash
    docker compose up
    ```

11. Open an internet tab (e.g., Google Chrome) and go to: http://localhost:6789/
12. You should now see the list of pipelines. Click on "web_api_to_gcs".
13. In the left sidebar, click on "Edit pipeline" and scroll to the yellow block ("data_exporter_to_gcp_bucket"). Click the three dots on the upper right and select "Execute with all upstream blocks":


![image](https://github.com/PietroRuffo/Lazio-Car-Sales-Performance-Emissions-Dashboard/assets/99428541/067c0eab-cbaf-4bd9-aa4f-9ee7780cc840)


  - **data_exporter_to_gcp_bucket pipeline overview:**
    - Here's a brief overview of what each code block does:
    
      - **Loader Block 1 (Blue):**
        - Imports necessary libraries like Pandas, requests, etc.
        - Defines a function `load_data_from_api` which fetches data from an API, extracts it from a ZIP file, reads it into a DataFrame, and returns the DataFrame.
        - Defines a function `test_output` which tests if the DataFrame has a minimum number of rows and correct number of columns.
        
      - **Transformer Block 2 (Purple):**
        - Imports necessary libraries like Pandas, PyArrow, etc.
        - Defines a function `transform` which renames columns, drops rows with missing values, extracts registration year and month, drops 'registration_date' column, and redefines data types of columns.
        - Defines a function `test_output` which tests if the DataFrame has a minimum number of rows.
        
      - **Exporter Block 3 (Yellow):**
        - Imports necessary libraries like PyArrow and os.
        - Sets up Google Cloud service account credentials.
        - Defines variables for bucket, project, and table names.
        - Defines a function `export_data` decorated with `data_exporter` which exports data to Google Cloud Storage in Parquet format, **partitioned by registration year**.

14. Once execution is completed, return to the "Pipelines" section and repeat the same procedure for pipeline "gcs_to_bigquery". Simply scroll down to the last code block of each pipeline, click the three dots, and select "Execute with all upstream blocks".

    
![image](https://github.com/PietroRuffo/Lazio-Car-Sales-Performance-Emissions-Dashboard/assets/99428541/d2542a02-ac36-4780-9822-77f8cb705900)


- **data_exporter_to_gcp_bucket pipeline overview:**
 - Here's a brief overview of what each code block does:
  
    - **Loader Block 1 (Blue):**
      - This block is responsible for loading data from Google Cloud Storage using PyArrow library. 
      - It first checks if the required functions (`data_loader` and `test`) are defined in the global namespace. If not, it imports them.
      - It sets the Google Cloud credentials file path.
      - Defines a decorated function `load_data` to load data from Parquet files (the one we uploaded in the previous pipeline) located in a specified root path in Google Cloud Storage.
      - Defines another decorated function `test_output` to test the output of the data loading block.

    - **Transformer Block 2 (Purple):**
      - This block performs data transformation tasks on the loaded DataFrame.
      - It checks if the `transformer` and `test` functions are defined in the global namespace. If not, it imports them.
      - The `transform` function translates specific columns' values from Italian to English.
      - It returns the transformed DataFrame.
      - The `test_output` function asserts that the transformed DataFrame has at least 10,000 rows.

    - **Exporter Block 3 (Yellow):**
      - This block is a SQL query written to export data processed by the previous blocks to the BigQuery's dataset named "Lazio_vehicle".
        
15. Repeat what you did at step 14. with pipeline "lazio_car_dbt".

![image](https://github.com/PietroRuffo/Lazio-Car-Sales-Performance-Emissions-Dashboard/assets/99428541/4cb2e375-eb77-4870-a94c-99d1434ddab7)

- **lazio_car_dbt pipeline overview:**
  - Here's a brief overview of what each code block does:
  
    - **Sky Blue Block 1:**
      - Checks and imports necessary modules.
      - Defines a function to clone a repository and clear existing models.
      
    - **Pink Block 2:**
      - Imports modules for YAML handling and filesystem operations.
      - Defines a function to write a YAML configuration file with specific settings to connect DBT'S Mage integration to Bigquery.
      
    - **Orange Block 3 (DBT Model 1):**
      - Defines a DBT model to transform source data by renaming columns, applying filters (we are keeping only private cars, original dataset contains all vehicles), and aggregating sales data.
      
    - **Orange Block 4 (DBT Model 2):**
      - Defines another DBT model with materialization and partitioning by registration_year.





16. To create the dashboard on Looker, follow this quick tutorial: [Looker Dashboard Tutorial](https://www.youtube.com/watch?v=39nLTs74A3E&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=49)
