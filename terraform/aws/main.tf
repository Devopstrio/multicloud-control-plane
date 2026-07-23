# AWS Multi-Cloud Landing Zone Hub Module
terraform {
  required_version = ">= 1.5.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

# Network Hub VPC
resource "aws_vpc" "multicloud_hub_vpc" {
  cidr_block           = var.vpc_cidr
  enable_dns_hostnames = true
  enable_dns_support   = true

  tags = {
    Name        = "devopstrio-multicloud-aws-hub"
    Env         = var.environment
    ManagedBy   = "Terraform"
    ControlPlane = "MultiCloudHub"
  }
}

resource "aws_subnet" "public_subnet_1" {
  vpc_id                  = aws_vpc.multicloud_hub_vpc.id
  cidr_block              = var.public_subnet_cidr
  map_public_ip_on_launch = false
  availability_zone       = "${var.aws_region}a"

  tags = {
    Name = "devopstrio-aws-hub-public-1"
    Env  = var.environment
  }
}

resource "aws_kms_key" "kms_governance_key" {
  description             = "Multi-Cloud Control Plane Encryption Key"
  deletion_window_in_days = 30
  enable_key_rotation     = true

  tags = {
    Env = var.environment
  }
}
