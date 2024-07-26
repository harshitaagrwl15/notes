import boto3
import json
import os

# Initialize the boto3 clients
codepipeline_client = boto3.client('codepipeline')
logs_client = boto3.client('logs')


# Get the pipeline state
response = codepipeline_client.get_pipeline_state(name=pipeline)

# Get the latest execution ID
latest_execution = response['stageStates'][0]['latestExecution']['pipelineExecutionId']

# Define the log group name
log_group_name = f'/aws/codepipeline/{pipeline_name}'

# Describe the log streams in the log group
log_streams = logs_client.describe_log_streams(logGroupName=log_group_name)

# Find the log stream for the latest execution
log_stream_name = None
for stream in log_streams['logStreams']:
    if latest_execution in stream['logStreamName']:
        log_stream_name = stream['logStreamName']
        break

if not log_stream_name:
    print("No log stream found for the latest execution")
    exit()

# Get the log events from the log stream
log_events = logs_client.get_log_events(logGroupName=log_group_name, logStreamName=log_stream_name)

# Extract the log messages
logs = []
for event in log_events['events']:
    logs.append(event['message'])

# Write logs to a JSON file
with open("pipeline_logs.json", "w") as logfile:
    json.dump(logs, logfile, indent=4)

print("Logs written to pipeline_logs.json")
