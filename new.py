import os
import re

def find_and_replace_repos_in_tf_files(base_dir, old_prefix, new_prefix):
    # Regex to find the module source paths
    module_source_pattern = re.compile(r'source\s*=\s*["\'](git::ssh://[^/]+/[^/]+/(.*?))(\?.*?)?["\']')

    # Walk through the base directory to find .tf files
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.tf'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    content = f.read()

                # Replace the old repo URL with the new one directly in the content
                updated_content = re.sub(r'source\s*=\s*["\']' + re.escape(old_prefix), f'source = "{new_prefix}', content)
                
                # Write the updated content back to the file
                with open(file_path, 'w', newline='') as f:
                    f.write(updated_content)
                print(f"Updated repo URLs in file: {file_path}")

def main():
    base_dir = '/home/harshitaagarwal/Desktop/SE/services-estimator-devops-master/terraform/configuration/runway-iam'
    old_prefix = 'git::ssh://git@github.azc.ext.hp.com/runway/'
    new_prefix = 'git::ssh://harshit.ext.hp.com/AGARWAL/'

    find_and_replace_repos_in_tf_files(base_dir, old_prefix, new_prefix)

if __name__ == "__main__":
    main()
