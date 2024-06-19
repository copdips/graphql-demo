import strawberry
from fastapi import FastAPI
from strawberry.asgi import GraphQL
from strawberry.fastapi import GraphQLRouter


@strawberry.type
class User:
    name: str
    age: int


@strawberry.type
class Query:
    @strawberry.field
    def user(self) -> User:
        return User(name="Patrick", age=100)


schema = strawberry.Schema(query=Query)

app = FastAPI()

"""
old version from fastapi:
https://fastapi.tiangolo.com/how-to/graphql/
graphql_app = GraphQL(schema)
app.add_route("/graphql", graphql_app)
app.add_websocket_route("/graphql", graphql_app)
"""

# latest version from strawberry:
# https://strawberry.rocks/docs/integrations/fastapi
graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")
