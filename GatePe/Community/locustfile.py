from locust import HttpUser, TaskSet, task, between
import random

# Survey api test 

class UserBehavior(TaskSet):
    @task(1)
    def get_survey(self):
        self.client.get("/survey/")

    @task(2)
    def create_survey(self):
        data = {
            "estate":3,
            "title":"jndfgjskfdg",
            "questions": [
                {"question": "What is your favorite color?", "type": "text"},
                {"question": "How satisfied are you with our service?", "type": "rating", "options": ["Very Satisfied", "Satisfied", "Neutral", "Dissatisfied", "Very Dissatisfied"]}
            ]
        }
        self.client.post("/survey/", json=data)

    @task(1)
    def update_survey(self):
        survey_id = random.randint(1, 100)  # Adjust this range based on your test data
        data = {
            "id": survey_id,
            "title": "Updated Survey Title",
            "questions": [
                {"question": "Updated question?", "type": "text"}
            ]
        }
        self.client.patch("/survey/", json=data)

    @task(1)
    def delete_notice(self):
        # Randomly select a booking ID from a set of existing IDs
        survey_id = random.randint(1, 100)  # Adjust this range based on your test data
        data = {
            "id": survey_id
        }
        response = self.client.delete("/survey/", json=data)
        self.client.delete("/survey/", json=data)

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 5)
