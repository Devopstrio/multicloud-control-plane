variable "location" {
  description = "Target Azure Region"
  type        = string
  default     = "eastus"
}

variable "resource_group_name" {
  description = "Resource Group Name"
  type        = string
  default     = "rg-devopstrio-multicloud-hub"
}

variable "environment" {
  description = "Deployment Environment"
  type        = string
  default     = "production"
}
