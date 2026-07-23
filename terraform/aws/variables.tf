variable "aws_region" {
  description = "Target AWS Region"
  type        = string
  default     = "us-east-1"
}

variable "environment" {
  description = "Target Deployment Environment"
  type        = string
  default     = "production"
}

variable "vpc_cidr" {
  description = "VPC CIDR Block"
  type        = string
  default     = "10.100.0.0/16"
}

variable "public_subnet_cidr" {
  description = "Public Subnet CIDR Block"
  type        = string
  default     = "10.100.1.0/24"
}
