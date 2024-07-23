import json

def format_terraform_output(input_file, output_file):
    with open(input_file, 'r') as file:
        data = json.load(file)
    
    formatted_output = json.dumps(data, indent=4)
    
    with open(output_file, 'w') as file:
        file.write(formatted_output)
    
    print(f"Formatted output saved to {output_file}")

input_file = 'tfplan.json'
output_file = 'tfplan_pretty.json'
format_terraform_output(input_file, output_file)
