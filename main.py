"""
https://www.geeksforgeeks.org/fastapi-using-graphql/
"""

from ariadne import QueryType, gql, make_executable_schema
from ariadne.asgi import GraphQL
from fastapi import FastAPI

# Define a GraphQL query type
query = QueryType()


# Define a resolver for the "book" query
# Field name `book` should match the name defined in type Query {}
@query.field("book")
def resolve_book(*_):
    return {"title": "GraphQL Tutorial", "author": "GFG"}

# Define a resolver for the "books" query
@query.field("books")
def resolve_books(*_):
    return [
        {"title": "Book 1", "author": "Author 1"},
        {"title": "Book 2", "author": "Author 2"},
        {"title": "Book 3", "author": "Author 3"},
    ]

# Define the GraphQL schema using the gql function
type_defs = gql("""
	type Book {
		title: String
		author: String
	}

	type Query {
		book: Book
        books: [Book]
	}
""")

# Create the executable GraphQL schema
schema = make_executable_schema(type_defs, query)

# Create a FastAPI app
app = FastAPI()

# Create a GraphQL app using the Ariadne schema
graphql_app = GraphQL(schema, debug=True)

# Mount the GraphQL app on the "/graphql" route
app.mount("/graphql", graphql_app)

# app.add_route works too,
# but here graphql_app is a ASGI application, so mount is better
# app.add_route("/graphql", graphql_app)

# Run the FastAPI app
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
