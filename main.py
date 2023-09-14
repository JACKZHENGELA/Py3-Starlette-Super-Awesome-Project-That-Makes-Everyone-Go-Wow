from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route

import uvicorn

async def homepage(request):
    return JSONResponse({"Hello": "World"})

app = Starlette(
    debug=True,
    routes=[
        Route('/', homepage)
    ]
)

uvicorn.run(app, port=8080)