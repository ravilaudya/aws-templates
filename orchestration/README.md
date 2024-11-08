### Event-Driven Orchestration Platform in AWS

Cloudformation Template for building Event-Driven Orchestration Platform in AWS. It creates the following AWS resources
- SNS
   - Sinlge SNS topic acting as the events publisher
- SQS
   - SQS queue subscribed to SNS
- Lambda
   - Lambda subscribed to SQS


![AWS Events Orchestration Platform](https://github.com/user-attachments/assets/a79d0e5a-4d23-47c4-9bf2-7c1d768a1ee1)




### Steps
- Use `sqs.cft.yaml` to create SNS topic
- Use `subscriber.cft.yaml` to create subscription

Can create multiple subscriptions as per need using same topic
