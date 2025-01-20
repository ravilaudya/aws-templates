#!/bin/bash

awslocal logs delete-log-group --log-group-name /aws/lambda/dynamo-populate --region us-west-2

awslocal lambda delete-function --function-name dynamo-populate --region us-west-2
