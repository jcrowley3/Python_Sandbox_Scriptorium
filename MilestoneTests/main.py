import gevent.monkey
gevent.monkey.patch_all()
from gevent.pywsgi import WSGIServer
from fastapi import FastAPI
from DogEngine.routes import router as dogs_router
from CatEngine.routes import router as cats_router


app = FastAPI()

app.include_router(dogs_router, prefix="/api/v1")
app.include_router(cats_router, prefix="/api/v1")

if __name__ == "__main__":
    http_server = WSGIServer(("0.0.0.0", 8000), app)
    http_server.serve_forever()


# 0.0.0.0/api/v1/dogs/1
