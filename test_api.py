import requests

BASE_URL = "http://127.0.0.1:5000"

def run_demo():
    print("--- 1. Registering University ---")
    uni_data = {
        "email": "admin@university.edu",
        "password": "password123",
        "role": "university",
        "uni_name": "State Tech University"
    }
    r = requests.post(f"{BASE_URL}/auth/register", json=uni_data)
    print(r.json())

    print("\n--- 2. Logging In ---")
    login_data = {"email": "admin@university.edu", "password": "password123"}
    r = requests.post(f"{BASE_URL}/auth/login", json=login_data)
    token = r.json().get('access_token')
    print(f"Logged in! JWT Token starts with: {token[:20]}...")

    # Now you can use this token to call protected routes!
    headers = {"Authorization": f"Bearer {token}"}
    print("\n--- 3. Testing Protected Route ---")
    # This assumes you have a request with ID 1 in your DB
    # r = requests.post(f"{BASE_URL}/university/verify-request/1", 
    #                   headers=headers, json={"status": "VERIFIED"})

if __name__ == "__main__":
    run_demo()