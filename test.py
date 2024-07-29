from jinja2 import Template

# Load the Jinja template file
with open('provider.jinja') as file:
    template_content = file.read()

# Create a Jinja2 Template object
template = Template(template_content)

# Define the values to replace in the template
context = {
    'aws_region': 'us-west-2',
    'aws_profile': 'my-aws-profile',
    'gcp_project': 'my-gcp-project',
    'gcp_region': 'us-central1',
    'azure_subscription_id': 'your-azure-subscription-id',
    'azure_client_id': 'your-azure-client-id',
    'azure_client_secret': 'your-azure-client-secret',
    'azure_tenant_id': 'your-azure-tenant-id'
}

# Render the template with the context values
rendered_content = template.render(context)

# Write the rendered content to the new file (provider.tf)
with open('provider.tf', 'w') as file:
    file.write(rendered_content)
