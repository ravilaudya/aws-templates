#!/bin/bash

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


# Invoke lambda function
# awslocal lambda invoke --function-name dynamo-populate \
#     --cli-binary-format raw-in-base64-out \
#     --region us-west-2 \
#     --payload '{"body": "test"}' output.txt

# List log streams
# awslocal logs describe-log-streams --log-group-name /aws/lambda/dynamo-populate --region us-west-2
