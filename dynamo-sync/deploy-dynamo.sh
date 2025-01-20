#!/bin/bash

# Create Table
awslocal dynamodb create-table \
    --table-name dynamo-sync-example \
    --key-schema AttributeName=id,KeyType=HASH \
    --attribute-definitions AttributeName=id,AttributeType=S \
    --billing-mode PAY_PER_REQUEST \
    --region us-west-2

# List Items count
awslocal dynamodb describe-table \
    --table-name  dynamo-sync-example \
    --query 'Table.ItemCount' \
    --region us-west-2
