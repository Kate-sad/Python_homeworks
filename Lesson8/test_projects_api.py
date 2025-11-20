import pytest
from projects_api import ProjectsAPI

api = ProjectsAPI()


@pytest.fixture
def new_project():
    payload = {"title": "Новый проект - моей компании",
               "users": {"ad5e8d07-208f-4420-846a-031234100d12": "admin"}
               }
    response = api.create_project(payload)
    assert response.status_code == 201
    return response.json()["id"]


# ---------- POST ----------
def test_create_project_positive():
    payload = {"title": "Новый проект - моей компании",
               "users": {"ad5e8d07-208f-4420-846a-031234100d12": "admin"}
               }
    response = api.create_project(payload)
    assert response.status_code == 201
    assert "id" in response.json()


def test_create_project_negative_missing_name():
    payload = {
               "users": {"ad5e8d07-208f-4420-846a-031234100d12": "admin"}
               }
    response = api.create_project(payload)
    assert response.status_code == 400


# ---------- PUT ----------
def test_update_project_positive(new_project):
    payload = {
        "deleted": True,
        "title": "Новый проект",
        "users": {"ad5e8d07-208f-4420-846a-031234100d12": "admin"}
    }
    response = api.update_project(new_project, payload)
    assert response.status_code == 200


def test_update_project_negative_invalid_id():
    payload = {"title": "Invalid Update"}
    response = api.update_project("999999", payload)
    assert response.status_code == 404


# ---------- GET ----------
def test_get_project_positive(new_project):
    response = api.get_project(new_project)
    assert response.status_code == 200
    assert response.json()["id"] == new_project


def test_get_project_negative_not_found():
    response = api.get_project("999999")
    assert response.status_code == 404
