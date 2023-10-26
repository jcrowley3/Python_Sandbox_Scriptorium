from fastapi import APIRouter, Form
# from fastapi.exceptions import HTTPException
# from fastapi.responses import JSONResponse
from pydantic import BaseModel

class Dog(BaseModel):
    name: str
    age: int
    breed: str

router = APIRouter()

@router.get("/dogs", response_model=Dog)
def get_dogs():
    return {"message": "List of dogs"}

@router.post("/dogs")
def create_dog(request: Dog):
    return {"message": "Dog created"}

@router.get("/dogs")
def get_dogs():
    return {"message": "List of dogs"}

@router.post("/dogs")
def create_dog():
    return {"message": "Dog created"}

@router.get("/dogs/{dog_id}")
def get_dog_by_id(dog_id: int):
    return {"message": f"Get dog with ID {dog_id}"}

@router.put("/dogs/{dog_id}")
def update_dog(dog_id: int):
    return {"message": f"Dog {dog_id} updated"}

@router.put("/dogs/{dog_id}")
def update_dog(dog_id: int, name:str = Form(...), age: int = Form(...), breed: str = Form(...)):
    return {"message": f"Dog {dog_id} updated"}

@router.delete("/dogs/{dog_id}")
def delete_dog(dog_id: int):
    return {"message": f"Dog {dog_id} deleted"}

# @router.exception_handler(HTTPException)
# async def http_exception_handler(request, exc):
#     return JSONResponse(
#         status_code=exc.status_code,
#         content={"message": exc.detail}
#     )
