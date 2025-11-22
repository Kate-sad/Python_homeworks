import os
import requests


class ProjectsAPI:
    def __init__(self):
        self.base_url = os.getenv("API_BASE_URL")
        self.token = os.getenv("API_TOKEN")
        if not self.base_url:
            raise ValueError("API_BASE_URL is not set")
        if not self.token:
            raise ValueError("API_TOKEN is not set")
        self.headers = {"Authorization": f"Bearer {self.token}"}

    def create_project(self, payload):
        return requests.post(f"{self.base_url}/projects",
                             json=payload, headers=self.headers)

    def update_project(self, project_id, payload):
        return requests.put(f"{self.base_url}/projects/{project_id}",
                            json=payload, headers=self.headers)

    def get_project(self, project_id):
        return requests.get(f"{self.base_url}/projects/{project_id}",
                            headers=self.headers)
