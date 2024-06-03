import requests
import time

def print_response_body(url):
    while True:
        response = requests.get(url)
        if response.status_code == 200:
            try:
                response_json = response.json()
                if "Body" in response_json and "stkCallback" in response_json["Body"]:
                    print("Response Body:", response_json)
                else:
                    print("Response does not contain expected JSON structure:", response_json)
            except ValueError:
                print("Failed to decode JSON response:", response.text)
        else:
            print("Failed to fetch callbacks. Status code:", response.status_code)
        time.sleep(1)  # Wait for 1 second before making the next request

if __name__ == "__main__":
    # Replace 'YOUR_CALLBACK_URL' with your actual callback URL
    callback_url = 'https://67b5-197-248-166-2.ngrok-free.app'
    print_response_body(callback_url)
