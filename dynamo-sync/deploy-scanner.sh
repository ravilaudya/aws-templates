#!/bin/bash

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


# Invoke lambda function
# awslocal lambda invoke --function-name dynamo-scanner \
#     --cli-binary-format raw-in-base64-out \
#     --region us-west-2 \
#     --payload '{"body": "test"}' output.txt

# List log streams
# awslocal logs describe-log-streams --log-group-name /aws/lambda/dynamo-scanner --region us-west-2
