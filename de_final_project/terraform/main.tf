terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.20.0"
    }
  }
}

provider "google" {
  credentials = var.credentials
  project     = var.project
  region      = var.region
  zone        = "europe-west8-a"
}

resource "google_storage_bucket" "de-final-project-417421-vehicle-bucket" {
  name          = var.gcs_bucket_name
  location      = var.location
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}


resource "google_bigquery_dataset" "Lazio_vehicle" {
  dataset_id = var.bq_dataset_name
  location   = var.location
}