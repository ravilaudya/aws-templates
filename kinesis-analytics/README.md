### Analytics Platform using Kinesis and S3

Cloudformation Template for Analytics Platform. It creates the following AWS resources for data ingestion, processing and storage.
- Kinesis Data Streams
   - Tool for Data ingestion from different sources
- Kinesis Firehose
   - Used as a data processing tool
- S3
   - Data Storage to store the stream data in raw format


### Steps
- Use `stack.cft.yaml` to create above resources
- Sending the event to Kinesis Data Streams
```
echo -n '{"id": 1, "value": 100, "timestamp": 1678901234}' | base64 
#### output 
eyJpZCI6IDEsICJ2YWx1ZSI6IDEwMCwgInRpbWVzdGFtcCI6IDE2Nzg5MDEyMzR9

### Put record into Kinesis data stream
aws kinesis put-record \
   --stream-name ravi-test-analytics-stream \
   --data 'eyJpZCI6IDEsICJ2YWx1ZSI6IDEwMCwgInRpbWVzdGFtcCI6IDE2Nzg5MDEyMzR9' \
   --partition-key "key1"

#### output
{
    "ShardId": "shardId-000000000001",
    "SequenceNumber": "49659171054654851540268694659818192826636083040645808146"
}

```

- Query S3 Bucket Objects
```
aws s3 ls s3://ravi-test-analytics-bucket --recursive
#### output
2024-12-31 15:45:08    48 raw-data/2024/12/31/23 test-analytics-stream-firehose-2-2024-12-31-23-40-05-0d33777b-662d-4d69-abeb-1c5024ac3cfe
```

- Architecture

![Screenshot 2024-12-31 at 4 00 56 PM](https://github.com/user-attachments/assets/6dea6c97-03d9-4a95-a031-421dd7c0c896)
