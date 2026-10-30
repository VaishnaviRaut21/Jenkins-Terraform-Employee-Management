terraform {
  required_providers {

    local = {
      source  = "hashicorp/local"
      version = "~> 2.5"
    }
  }
}

provider "local" {}

resource "local_file" "deployment_config" {

  filename = "${path.module}/deployment_config.txt"

  content = <<EOT
Employee Management System
==========================

Application: Flask
Database: SQLite
CI/CD: Jenkins
Infrastructure as Code: Terraform

Deployment Status: Provisioned
EOT
}

resource "local_file" "environment_config" {

  filename = "${path.module}/environment.txt"

  content = <<EOT
Environment: Development
Application: Employee Management System
Port: 5000
EOT
}