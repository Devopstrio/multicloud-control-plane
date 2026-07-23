variable "project_id" {
  description = "Target GCP Project ID"
  type        = string
  default     = "devopstrio-multicloud-prod"
}

variable "region" {
  description = "Target GCP Region"
  type        = string
  default     = "us-central1"
}

variable "environment" {
  description = "Deployment Environment"
  type        = string
  default     = "production"
}
