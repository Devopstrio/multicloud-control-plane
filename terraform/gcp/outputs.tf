output "network_id" {
  description = "GCP Hub Network ID"
  value       = google_compute_network.multicloud_vpc.id
}

output "subnetwork_id" {
  description = "GCP Subnetwork ID"
  value       = google_compute_subnetwork.hub_subnet.id
}
