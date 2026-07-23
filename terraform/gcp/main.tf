# GCP Multi-Cloud Landing Zone Architecture Module
terraform {
  required_version = ">= 1.5.0"
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }
}

provider "google" {
  project = "devopstrio-multicloud-prod"
  region  = "us-central1"
}

resource "google_compute_network" "multicloud_vpc" {
  name                    = "devopstrio-multicloud-gcp-hub"
  auto_create_subnetworks = false
}
