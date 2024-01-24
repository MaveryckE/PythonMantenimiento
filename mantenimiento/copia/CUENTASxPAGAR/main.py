from fastapi import FastAPI
from rutas.ruta import user
from rutas.apidos import mods
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user)
app.include_router(mods)
