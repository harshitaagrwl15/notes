def create_terraform_backend_file(file_path):
    # Define the backend configuration
    backend_config = """
terraform {
  backend "s3" {
    bucket         = "my-tf-state-bucket"
    key            = "terraform/state"
    region         = "us-east-1"
    encrypt        = true
    dynamodb_table = "my-lock-table"
  }
}
"""

    # Write the backend configuration to the file
    with open(file_path, 'w') as file:
        file.write(backend_config.strip())

    print(f"Created Terraform backend file: '{file_path}'")
