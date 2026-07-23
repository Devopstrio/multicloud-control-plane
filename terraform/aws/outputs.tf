output "vpc_id" {
  description = "AWS Landing Zone VPC ID"
  value       = aws_vpc.multicloud_hub_vpc.id
}

output "kms_key_arn" {
  description = "KMS Encryption Key ARN"
  value       = aws_kms_key.kms_governance_key.arn
}
