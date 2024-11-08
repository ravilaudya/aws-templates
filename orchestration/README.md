### Event-Driven Orchestration Platform in AWS

Cloudformation Template for building Event-Driven Orchestration Platform in AWS. It creates the following AWS resources
- SNS
   - Sinlge SNS topic acting as the events publisher
- SQS
   - SQS queue subscribed to SNS
- Lambda
   - Lambda subscribed to SQS

