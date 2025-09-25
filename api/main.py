import strawberry

from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

"""
Example query:
{
  hello,
  add(x:23, y:45)
}
"""

@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Hello World 123"

    @strawberry.field
    def add(self, x: int, y: int) -> int:
        return x + y


schema = strawberry.Schema(Query)

graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")