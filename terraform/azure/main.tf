# Azure Multi-Cloud Landing Zone Hub Module
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
  name     = var.resource_group_name
  location = var.location

  tags = {
    Env         = var.environment
    ManagedBy   = "Terraform"
    ControlPlane = "MultiCloudHub"
  }
}

resource "azurerm_virtual_network" "hub_vnet" {
  name                = "vnet-devopstrio-azure-hub"
  address_space       = ["10.200.0.0/16"]
  location            = azurerm_resource_group.multicloud_rg.location
  resource_group_name = azurerm_resource_group.multicloud_rg.name

  tags = {
    Env = var.environment
  }
}
