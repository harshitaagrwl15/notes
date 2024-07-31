import os
import re

def find_and_replace_repos_in_tf_files(base_dir, old_prefix, new_prefix):
    # Regex to find the module source paths
    module_source_pattern = re.compile(r'source\s*=\s*["\'](git::ssh://[^/]+/[^/]+/(.*?))(\?.*?)?["\']')
    relative_source_pattern = re.compile(r'source\s*=\s*["\'](\.\./.*)["\']')

    # Walk through the base directory to find .tf files
    for root, dirs, files in os.walk(base_dir):
        # Skip the .terraform directory
        dirs[:] = [d for d in dirs if d != '.terraform']

        for file in files:
            if file.endswith('.tf'):
                file_path = os.path.join(root, file)
                
                # Skip files in .terraform directory
                if '.terraform' in file_path.split(os.sep):
                    continue

                with open(file_path, 'r') as f:
                    content = f.read()

                # Replace the old repo URL with the new one directly in the content
                updated_content = re.sub(r'source\s*=\s*["\']' + re.escape(old_prefix), f'source = "{new_prefix}', content)

                # Write the updated content back to the file
                with open(file_path, 'w', newline='') as f:
                    f.write(updated_content)
                print(f"Updated repo URLs in file: {file_path}")

                # Find all source paths in the current .tf file
                for match in module_source_pattern.finditer(content):
                    full_source_path = match.group(1)
                    relative_source_path = match.group(2)
                    
                    # Compute the absolute path to the module directory
                    module_dir = os.path.abspath(os.path.join(base_dir, relative_source_path))
                    
                    # Check if the module directory exists
                    if os.path.isdir(module_dir):
                        print(f"Recursively updating repo URLs in module directory: {module_dir}")

                        # Recursively perform the operation in the module directory
                        find_and_replace_repos_in_tf_files(module_dir, old_prefix, new_prefix)
                    else:
                        print(f"Module directory does not exist: {module_dir}")

                # Handle relative paths
                for match in relative_source_pattern.finditer(content):
                    relative_source_path = match.group(1)
                    
                    # Compute the absolute path to the module directory
                    module_dir = os.path.abspath(os.path.join(root, relative_source_path))
                    
                    # Check if the module directory exists
                    if os.path.isdir(module_dir):
                        print(f"Recursively updating repo URLs in module directory: {module_dir}")

                        # Recursively perform the operation in the module directory
                        find_and_replace_repos_in_tf_files(module_dir, old_prefix, new_prefix)
                    else:
                        print(f"Module directory does not exist: {module_dir}")

def main():
    base_dir = '/home/harshitaagarwal/Desktop/SE/services-estimator-devops-master/terraform/configuration/runway-iam'
    old_prefix = 'git::ssh://git@github.azc.ext.hp.com/runway/'
    new_prefix = 'git::ssh://harshit.ext.hp.com/AGARWAL/'

    find_and_replace_repos_in_tf_files(base_dir, old_prefix, new_prefix)

if __name__ == "__main__":
    main()
