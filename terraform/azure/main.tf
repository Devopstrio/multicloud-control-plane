# Azure Multi-Cloud Landing Zone Architecture Module
terraform {
  required_version = ">= 1.5.0"
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"
    }
  }
}

provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "multicloud_rg" {
  name     = "rg-devopstrio-multicloud-hub"
  location = "eastus"

  tags = {
    Env = "production"
  }
}
