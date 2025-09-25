# Overview

This project demonstrates a Web project of React frontend + Python backend communicating via GraphQL

## frontend

`/frontend` is a React + Relay + TypeScript project template

## api

`/api` is a python + FastAPI + Strawberry GraphQL server template


## Syncing GraphQL schema

```
# to get the GQL schema
strawberry export-schema main > ../frontend/src/graphql_schema/local_schema.graphql

# then run this under frontend
npm run relay
```

# How to hack this project

## Develop Environment

### Starting Development Environment

**Method 1: Start Separately (Recommended)**

1. Start Backend API:
   ```bash
   cd api
   uvicorn main:app --reload --port 9000
   ```

2. Start Frontend Dev Server:
   ```bash
   cd frontend
   npm run dev
   ```
### Access URLs

- **Frontend Dev Server**: http://localhost:5173
- **Backend API**: http://localhost:9000/graphql

### Hot Reload Features

✅ **Frontend Hot Reload**: Changes to files under `frontend/src/` automatically refresh the browser
✅ **Backend Hot Reload**: Changes to files under `api/` automatically restart uvicorn
✅ **API Proxy**: Frontend automatically proxies `/graphql` path to backend API

### Development Workflow

1. Modify frontend code → Browser auto-refreshes
2. Modify backend code → API auto-restarts
3. No need to manually restart any services

## Production Environment

Production environment still uses a single port:

