variable "credentials" {
  description = "My Credentials"
  default     = "./keys/my_cred.json"
}


variable "project" {
  description = "Final Project"
  default     = "de-final-project-417421"
}

variable "region" {
  description = "Region"
  #Update the below to your desired region
  default = "europe-west8"
}

variable "location" {

  description = "Project Location"
  #Update the below to your desired location
  default = "EUROPE-WEST8"
}

variable "bq_dataset_name" {
  description = "Vehicle BigQuery Dataset"
  #Update the below to what you want your dataset to be called
  default = "Lazio_vehicle"
}

variable "gcs_bucket_name" {
  description = "Vehicle Storage Bucket"
  #Update the below to a unique bucket name
  default = "de-final-project-417421-vehicle-bucket"
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}