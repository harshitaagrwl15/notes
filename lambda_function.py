import json
import boto3

def lambda_handler(event, context):
    sns_topic_arn = "arn:aws:sns:us-west-2:600659917078:critical"
    event_details = {
        "EventName": event['detail']['EventName'],
        "EventID": event['detail']['EventID'],
        "DatabaseName": event['detail']['SourceIdentifier'],
        "DateAndTime": event['time'],
        "Message": event['detail']['Message']
    }

    sns_client = boto3.client('sns')
    sns_client.publish(
        TopicArn=sns_topic_arn,
        Message=json.dumps(event_details)
    )
