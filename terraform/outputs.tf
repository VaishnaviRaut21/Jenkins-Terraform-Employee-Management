output "deployment_configuration" {

  value = local_file.deployment_config.filename
}


output "environment_configuration" {

  value = local_file.environment_config.filename
}