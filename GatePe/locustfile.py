from locust import HttpUser, TaskSet, task, between
import random

# Bookings api test 

class UserBehavior(TaskSet):
    @task(1)
    def get_bookings(self):
        self.client.get("/bokingview")

    @task(2)
    def create_booking(self):
        data = {
            "property": 1,
            "facility": 1,
            "user": 1,
            "booking_time": "2023-07-26T14:00:00Z",
            "duration": 120,
            "payment_status": "Paid",
            "qr_code": "new_qr_code",
            "status": "Confirmed"
        }
        self.client.post("/bokingview", json=data)

    @task(1)
    def update_booking(self):
        # Randomly select a booking ID from a set of existing IDs
        booking_id = random.randint(1, 1000)  # Adjust this range based on your test data
        data = {
            "id": booking_id,
            "status": "Cancelled"
        }
        self.client.patch("/bokingview", json=data)

    @task(1)
    def delete_booking(self):
        # Randomly select a booking ID from a set of existing IDs
        booking_id = random.randint(1, 1000)  # Adjust this range based on your test data
        data = {
            "id": booking_id
        }
        self.client.delete("/bokingview", json=data)

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 5)
