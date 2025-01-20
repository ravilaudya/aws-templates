# Sync DynamoDB to Other DataSources


## Scripts

I use `awslocal` to deploy and test DynamoDB syncing using `localstack`.

### Create DynamoDB
```sh
aws dynamodb create-table \
    --table-name dynamo-sync-example \
    --key-schema AttributeName=id,KeyType=HASH \
    --attribute-definitions AttributeName=id,AttributeType=S \
    --billing-mode PAY_PER_REQUEST \
    --region us-west-2
```
### Populate DynamoDB

- Create a lambda to populate the DynamoDB with 20,000 entries
    ```sh
    rm -rf populate.zip
    zip populate.zip populate.py
    awslocal lambda create-function  \
        --function-name dynamo-populate \
        --runtime python3.12 \
        --zip-file fileb://populate.zip \
        --handler populate.handler \
        --role arn:aws:iam::000000000000:role/lambda-role \
        --timeout 300  \
        --region us-west-2
    ```
- Run Lambda to populate
    ```sh
    awslocal lambda invoke --function-name dynamo-populator \
        --cli-binary-format raw-in-base64-out \
        --region us-west-2  --payload '{"body": "test"}' output.txt
    ```

### Scan DynamoDB using Lambda
- Create a Lambda to scan the DynamoDB
    ```sh
    rm -rf scanner.zip
    zip scanner.zip scanner.py

    awslocal lambda create-function  \
        --function-name dynamo-scanner \
        --runtime python3.12 \
        --zip-file fileb://scanner.zip \
        --handler scanner.handler \
        --role arn:aws:iam::000000000000:role/lambda-role \
        --timeout 300  \
        --region us-west-2
    ```
- Run Lambda to scan DB
    ```sh
    awslocal lambda invoke --function-name dynamo-scanner \
        --cli-binary-format raw-in-base64-out \
        --region us-west-2 \
        --payload '{"body": "test"}' output.txt
    ```

### Check Logs
    ```sh
    awslocal logs describe-log-streams --log-group-name /aws/lambda/dynamo-scanner --region us-west-2
    awslocal logs get-log-events \
        --log-group-name /aws/lambda/dynamo-scanner \
        --region us-west-2 \
        --log-stream-name "<stream-id>"
    ```
