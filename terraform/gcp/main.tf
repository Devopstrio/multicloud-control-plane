# GCP Multi-Cloud Landing Zone Hub Module
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
  project = var.project_id
  region  = var.region
}

resource "google_compute_network" "multicloud_vpc" {
  name                    = "devopstrio-multicloud-gcp-hub"
  auto_create_subnetworks = false
}

resource "google_compute_subnetwork" "hub_subnet" {
  name          = "devopstrio-gcp-subnet-1"
  ip_cidr_range = "10.150.0.0/16"
  region        = var.region
  network       = google_compute_network.multicloud_vpc.id
}
