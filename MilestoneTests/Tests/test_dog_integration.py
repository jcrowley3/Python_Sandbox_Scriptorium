# import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
# import MilestoneTests.DogEngine as dog
from MilestoneTests.DogEngine.routes import router as dogs_router

app = FastAPI()
app.include_router(dogs_router)
client = TestClient(app)

def err_msg(response):
    return f"Response[{response.status_code}]: {response.text} "

def test_get_dogs_integration():
    response = client.get("/dogs")
    assert response.status_code == 200, err_msg(response)
    assert response.json() == {"message": "List of dogs"}

def test_create_dog_integration():
    response = client.post("/dogs")
    assert response.status_code == 200
    assert response.json() == {"message": "Dog created"}

def test_update_dog_integration():
    dog_id = 1
    response = client.put(f"/dogs/{dog_id}")
    assert response.status_code == 200
    assert response.json() == {"message": f"Dog {dog_id} updated"}

# make a PUT test that also includes a request body
def test_update_dog_info_integration():
    dog_id = 1
    response = client.put(f"/dogs/{dog_id}", data={"name": "Fido", "age": 3, "breed": "Golden Retriever"})
    assert response.status_code == 200
    assert response.json() == {"message": f"Dog {dog_id} updated"}

def test_delete_dog_integration():
    dog_id = 1
    response = client.delete(f"/dogs/{dog_id}")
    assert response.status_code == 200
    assert response.json() == {"message": f"Dog {dog_id} deleted"}
