import json

def format_terraform_output(input_file, output_file):
    with open(input_file, 'r') as file:
        data = json.load(file)
    
    formatted_output = json.dumps(data, indent=4)
    aws_credentials = session_data.get('aws_credentials', {})

# Fetch the required keys with default empty strings
aws_access_key_id = aws_credentials.get('aws_access_key_id', '')
aws_secret_access_key = aws_credentials.get('aws_secret_access_key', '')
aws_session_token = aws_credentials.get('aws_session_token', '')

# Check if the values are valid before setting environment variables
if aws_access_key_id:
    os.environ['AWS_ACCESS_KEY_ID'] = aws_access_key_id
else:
    print("Warning: 'aws_access_key_id' is missing or empty.")

if aws_secret_access_key:
    os.environ['AWS_SECRET_ACCESS_KEY'] = aws_secret_access_key
else:
    print("Warning: 'aws_secret_access_key' is missing or empty.")

if aws_session_token:
    os.environ['AWS_SESSION_TOKEN'] = aws_session_token
else:
    print("Warning: 'aws_session_token' is missing or empty.")

# Print environment variables
print(f"AWS_ACCESS_KEY_ID = {os.getenv('AWS_ACCESS_KEY_ID')}")
print(f"AWS_SECRET_ACCESS_KEY = {os.getenv('AWS_SECRET_ACCESS_KEY')}")
print(f"AWS_SESSION_TOKEN = {os.getenv('AWS_SESSION_TOKEN')}")
    with open(output_file, 'w') as file:
        file.write(formatted_output)
    
    print(f"Formatted output saved to {output_file}")

input_file = 'tfplan.json'
output_file = 'tfplan_pretty.json'
format_terraform_output(input_file, output_file)
