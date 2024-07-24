import os
import subprocess

def run_terraform_commands(base_path, folder_name):
    folder_path = os.path.join(base_path, folder_name)
    
    if not os.path.isdir(folder_path):
        print(f"The folder {folder_path} does not exist.")
        return
    os.chdir(folder_path)
    
    # Run terraform init
    init_command = ["terraform", "init"]
    subprocess.run(init_command)

    # Run terraform plan and save output to a file
    plan_command = ["terraform", "plan", "-no-color"]
    with open(f"{folder_name}.txt", "w") as output_file:
        subprocess.run(plan_command, stdout=output_file)

if __name__ == "__main__":
    # Set the default base path here
    base_path = "/home/harshitaagarwal/Desktop/learning"

    # Get the folder name from the user
    folder_name = input("Enter the Terraform folder name: ")

    # Run the Terraform commands
    run_terraform_commands(base_path, folder_name)
