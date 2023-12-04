resource "aws_db_event_subscription" "default" {
  name      = "critical"
  sns_topic = "arn:aws:sns:us-west-2:600659917078:critical"

  source_type = "db-instance"

  event_categories = [
    "availability",
    "deletion",
    "failover",
    "failure",
    "low storage",
    "maintenance",
    "notification",
    "read replica",
    "recovery",
    "restoration"
  ]
}

resource "aws_lambda_function" "rds_event_lambda" {
  function_name = "rds-event-lambda"
  runtime       = "python3.8" # Replace with your desired runtime
  handler       = "lambda_function.lambda_handler"
  filename      = "lambda.zip"
  role          = aws_iam_role.lambda_execution_role.arn
  environment {
    variables = {
      RDSEventID= "\nRDS-EVENT-0011,RDS-EVENT-0028,RDS-EVENT-0029,RDS-EVENT-0014,RDS-EVENT-0010,RDS-EVENT-0067,RDS-EVENT-0078,RDS-EVENT-0049,RDS-EVENT-0031,RDS-EVENT-0035,RDS-EVENT-0036,RDS-EVENT-0026,RDS-EVENT-0055,RDS-EVENT-0056,RDS-EVENT-0087,RDS-EVENT-0158,RDS-EVENT-0154,RDS-EVENT-0037,RDS-EVENT-0038,RDS-EVENT-0006,RDS-EVENT-0004,RDS-EVENT-0022,RDS-EVENT-0003,RDS-EVENT-0092,RDS-EVENT-0155",
      RDSIdentifier= "database-1"
      SNSTopic="arn:aws:sns:us-west-2:600659917078:critical"
    }
  }
}

resource "aws_iam_role_policy_attachment" "lambda_execution_role_policy" {
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
  role       = aws_iam_role.lambda_execution_role.name
} 

resource "aws_iam_role" "lambda_execution_role" {
  name = "lambda_execution_role"

  assume_role_policy = <<POLICY
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
POLICY
}

resource "aws_cloudwatch_event_rule" "rds_event_rule" {
  name        = "critical-event-rule"
  description = "Rule for specific RDS events"

  event_pattern = <<PATTERN
{
  "source": ["aws.rds"],
  "detail-type": ["RDS DB Instance Event"],
  "detail": {
    "EventID": [
      "RDS-EVENT-001",
      "RDS-EVENT-002",
      "RDS-EVENT-003"
    ]
  }
}
PATTERN
}

resource "aws_cloudwatch_event_target" "rds_event_target" {
  rule      = aws_cloudwatch_event_rule.rds_event_rule.name
  arn       = aws_lambda_function.rds_event_lambda.arn
}
resource "aws_lambda_permission" "allow_cloudwatch" {
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.rds_event_lambda.function_name
  principal     = "events.amazonaws.com"
  source_arn    = aws_cloudwatch_event_rule.rds_event_rule.arn
}
