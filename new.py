import os
import re

def find_and_replace_repos_in_tf_files(base_dir, old_prefix, new_prefix):
    # Regex to find the module source paths
    module_source_pattern = re.compile(r'source\s*=\s*["\'](.*?)["\']')

    # Walk through the base directory to find .tf files
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.tf'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    content = f.read()

                # Find all source paths in the current .tf file
                for match in module_source_pattern.finditer(content):
                    source_path = match.group(1)
                    
                    # Compute the absolute path to the module directory
                    module_dir = os.path.abspath(os.path.join(root, source_path))
                    
                    # Check if the module directory exists
                    if os.path.isdir(module_dir):
                        print(f"Updating repo URLs in module directory: {module_dir}")

                        # Perform the operation in the module directory
                        perform_operations_in_directory(module_dir, old_prefix, new_prefix)
                    else:
                        print(f"Module directory does not exist: {module_dir}")

def perform_operations_in_directory(directory, old_prefix, new_prefix):
    # Define regex patterns for matching the repo URLs
    repo_pattern = re.compile(r'source\s*=\s*["\'](' + re.escape(old_prefix) + r')(.*?)["\']')

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.tf'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    content = f.read()
                
                # Replace the repo URL prefix
                updated_content = repo_pattern.sub(lambda m: f'source = "{new_prefix}{m.group(2)}"', content)
                
                # Write the updated content back to the file
                with open(file_path, 'w') as f:
                    f.write(updated_content)

def main():
    base_dir = '/home/harshitaagarwal/Desktop/learning/testing/account'
    old_prefix = 'git::ssh://abcsdfgh@git-codecommit.com/vi/repos/'
    new_prefix = 'git::ssh://HARSHITA@github.com'

    find_and_replace_repos_in_tf_files(base_dir, old_prefix, new_prefix)

if __name__ == "__main__":
    main()
