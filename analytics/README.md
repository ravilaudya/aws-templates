### Analytics Platform using Timestream in AWS

Cloudformation Template for Analytics Platform for E-Commerce Application. It creates the following AWS resources
- SQS
   - FIFO SQS queue to receive the events from sources
   - DLQ for events that are failed publishing to Timestream
- Lambda
   - Event processor lambda to process events, publish to Timestream
- Timestream
   - Events Database & Table


### Steps
- Use `stack.cft.yaml` to create above resources
- Sending the event to SQS in the following format triggers the processing flow
```
{
  "order_id": "test-order-1",
  "customer_id": "test-customer-1",
  "event_type": "order_placed",
  "metric_value": 1
}
```

- Query Timestream
```
--- Fetch all metrics in last 15 minutes

SELECT * FROM "events-db"."events-metrics" WHERE time between ago(15m) and now() ORDER BY time DESC LIMIT 10
```

- Architecture

  ![aws-analytics-timestream](https://github.com/user-attachments/assets/7a1e7999-a9e7-460b-9cfa-c1cd83724fd4)
