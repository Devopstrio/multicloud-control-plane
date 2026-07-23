output "resource_group_id" {
  description = "Azure Resource Group ID"
  value       = azurerm_resource_group.multicloud_rg.id
}

output "vnet_id" {
  description = "Azure Hub VNet ID"
  value       = azurerm_virtual_network.hub_vnet.id
}
