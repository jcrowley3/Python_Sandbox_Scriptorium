import pytest
# import MilestoneTests.DogEngine as dog
from MilestoneTests.DogEngine.routes import get_dogs, create_dog, update_dog, delete_dog

# @pytest.mark.asyncio
def test_get_dogs():
    response = get_dogs()
    assert response == {"message": "List of dogs"}

# @pytest.mark.asyncio
def test_create_dog():
    response = create_dog()
    assert response == {"message": "Dog created"}

# @pytest.mark.asyncio
def test_update_dog():
    dog_id = 1
    response = update_dog(dog_id)
    assert response == {"message": f"Dog {dog_id} updated"}

# @pytest.mark.asyncio
def test_delete_dog():
    dog_id = 1
    response = delete_dog(dog_id)
    assert response == {"message": f"Dog {dog_id} deleted"}
