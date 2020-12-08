bash setup-table.sh > /dev/null 2>&1

sam local start-api --env-vars env.json --docker-network lambda