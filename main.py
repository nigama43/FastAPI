import uvicorn
from fastapi import FastAPI
from src.controller.application import router as application_router
app = FastAPI(title="NT-Case Study",
              version="0.0.1"
              )
app.include_router(application_router)

if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8080)

