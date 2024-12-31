from locust import HttpUser, task, between
import random
import os

class VideoStorageUser(HttpUser):
    host = "http://34.47.196.178:3000"  # Base URL for the requests
    wait_time = between(1, 5)  # Simulated user will wait 1-5 seconds between tasks

    @task
    def signup_and_upload_video(self):
        # Step 1: Signup
        signup_payload = {
            "username": "testuser",
            "name": "Test User",
            "email": "testuser@example.com",
            "password": "password123",
            "contact": "1234567890"
        }
        signup_response = self.client.post("/signup", json=signup_payload)  # Changed to POST for signup submission
        if signup_response.status_code == 201:  # Assuming 201 means successful signup
            print("Signup successful")
