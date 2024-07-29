from locust import HttpUser, TaskSet, task, between
import random

# user api test

class UserBehavior(TaskSet):
    def on_start(self):
        """ Called when a Locust user starts running """
        self.create_user()  # Create a user at the beginning of the test

    def create_user(self):
        """ Helper function to create a user """
        self.client.post("/users/", json={
            "username": "testuser",
            "password": "testpassword",
            "email": "testuser@example.com",
            "phone_number": "1234567890",
            "role": "Resident",
            "estate": 1
        })

    @task(1)
    def get_users(self):
        self.client.get("/users/")

    @task(2)
    def update_user(self):
        # Randomly select a user ID from a set of existing IDs
        user_id = random.randint(1, 1000)  # Adjust this range based on your test data
        self.client.patch("/users/", json={
            "id": user_id,
            "phone_number": "0987654321"
        })

    @task(2)
    def delete_user(self):
        # Randomly select a user ID from a set of existing IDs
        user_id = random.randint(1, 1000)  # Adjust this range based on your test data
        self.client.delete("/users/", json={"id": user_id})

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 5)
