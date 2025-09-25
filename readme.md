## frontend

`frontend` is a React + Relay + TypeScript project template

## api

`api` is a python + FastAPI + Strawberry GraphQL server template

```
# to get the GQL schema
strawberry export-schema main > ../frontend/src/graphql_schema/local_schema.graphql

# then run this under frontend
npm run relay
```
