from fastapi.responses import JSONResponse
from fastapi import Request, HTTPException

async def centralized_exception_handler(request: Request, exc: HTTPException):

    try:
        body_data = await request.json()
    except Exception:
        body_data = {}

    error_response = {
        "status_code": exc.status_code,
        "message": exc.detail,
        "metadata": {
            "method": request.method,
            "path": request.url.path,
            "content": {
                "body": body_data,
                "query": dict(request.query_params),
                "params": request.path_params,
            },
        },
    }

    return JSONResponse(status_code=exc.status_code, content=error_response)
