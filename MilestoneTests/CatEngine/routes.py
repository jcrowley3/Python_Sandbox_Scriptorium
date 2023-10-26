from fastapi import APIRouter
# from fastapi.exceptions import RequestValidationError
# from fastapi.responses import JSONResponse
from pydantic import BaseModel

class Cat(BaseModel):
    name: str
    age: int
    breed: str

router = APIRouter()

# @router.exception_handler(RequestValidationError)
# async def validation_exception_handler(request, exc):
#     return JSONResponse(
#         status_code=422,
#         content={"detail": exc.errors()}
#     )

@router.get("/cats")
def get_cats():
    return {"message": "List all cats"}

# alt GET using response_model
# @router.get("/cats", response_model=Cat)
# def get_cats():
#     return {"name": "Maru", "age": 3, "breed": "Scottish Fold"}

@router.post("/cats")
def create_cat():
    return {"message": "Create a new cat"}

# #  alt POST using model in function
# @router.get("/cats")
# def get_cats(request: Cat):
#     return {"name": "Maru", "age": 3, "breed": "Scottish Fold"}

@router.get("/cats/{cat_id}")
def get_cat_by_id(cat_id: int):
    return {"message": f"Get cat with ID {cat_id}"}

@router.put("/cats/{cat_id}")
def update_cat(cat_id: int):
    return {"message": f"Update cat with ID {cat_id}"}

@router.delete("/cats/{cat_id}")
def delete_cat(cat_id: int):
    return {"message": f"Delete cat with ID {cat_id}"}
