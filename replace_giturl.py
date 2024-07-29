import re

# Function to replace the base URL in all .tf files within a module
def replace_base_url_in_tf_files(directory, old_base_url, new_base_url):
    # Regular expression pattern to match the starting part of the URL
    pattern = re.compile(re.escape(old_base_url))

    # Iterate over all files in the specified directory
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.tf'):
                file_path = os.path.join(root, file)

                # Read the contents of the file
                with open(file_path, 'r') as f:
                    content = f.read()

                # Replace the old base URL with the new base URL
                updated_content = pattern.sub(new_base_url, content)

                # Write the updated contents back to the file
                with open(file_path, 'w') as f:
                    f.write(updated_content)

                print(f"Updated base URL in {file_path}")
