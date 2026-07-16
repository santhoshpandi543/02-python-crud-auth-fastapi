from fastapi import FastAPI, HTTPException

# Our File
from app.routers import todos
from app.common.errors import centralized_exception_handler
from app.database import engine, Base

# To tell Sqlalchemy to build the tables in Postgre
Base.metadata.create_all(bind=engine)


def create_app() -> FastAPI:

    # app = FastAPI(dependencies=[Depends(get_db)])
    app = FastAPI(
        title="Todo App",
        # To link the centralized Http exception
        exception_handlers={HTTPException: centralized_exception_handler}
    )

    # To link the centralized Http exception this one another way 👇
    # app.add_exception_handler(HTTPException, handler=centralized_exception_handler)

    # To link the various routers [users, products, orders]
    app.include_router(todos.router)

    return app


app = create_app()
