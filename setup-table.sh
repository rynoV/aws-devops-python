aws dynamodb create-table \
    --table-name todo_table\
    --attribute-definitions AttributeName=id,AttributeType=S AttributeName=name,AttributeType=S\
    --key-schema AttributeName=id,KeyType=HASH AttributeName=name,KeyType=RANGE\
    --billing-mode PAY_PER_REQUEST\
    --endpoint-url http://localhost:8000