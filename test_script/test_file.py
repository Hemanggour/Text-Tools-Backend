import os

import requests

BASE_URL = "http://127.0.0.1:8000"
SESSION = requests.Session()
CSRF_TOKEN = None


def login(email, password):
    global CSRF_TOKEN
    response = SESSION.post(
        f"{BASE_URL}/account/login/", data={"email": email, "password": password}
    )
    print("Login:", response.status_code)
    if response.ok:
        # Extract CSRF token from cookies
        CSRF_TOKEN = SESSION.cookies.get("csrftoken")
        return response.json()
    print("Error in login!!", response.text)
    return None


def register(email, password):
    response = SESSION.post(
        f"{BASE_URL}/account/register/", data={"email": email, "password": password}
    )
    print("Register:", response.status_code)
    if response.ok:
        return response.json()
    print("Error in register!!", response.text)
    return None


def get_api_key():
    response = SESSION.get(f"{BASE_URL}/account/api-key/")
    print("Get API Key:", response.status_code)
    if response.ok:
        return response.json()
    print("Error in get api!!", response.text)
    return None


def generate_api_key():
    headers = {"X-CSRFToken": CSRF_TOKEN}
    response = SESSION.post(f"{BASE_URL}/account/api-key/", headers=headers)
    print("Generate API Key:", response.status_code)
    if response.ok:
        return response.json()
    print("Error in generate api!!", response.text)
    return None


def refresh_api_key():
    headers = {"X-CSRFToken": CSRF_TOKEN}
    response = SESSION.patch(f"{BASE_URL}/account/api-key/", headers=headers)
    print("Refresh API Key:", response.status_code)
    if response.ok:
        return response.json()
    print("Error in refresh api!!", response.text)
    return None


def logout():
    headers = {"X-CSRFToken": CSRF_TOKEN}
    response = SESSION.post(f"{BASE_URL}/account/logout/", headers=headers)
    print("Logout:", response.status_code)
    if response.ok:
        return "Logged out!!"
    print("Error in logout!!", response.text)
    return None


def paraphase_api(api_key, query):
    response = requests.post(
        headers={"X-API-KEY": api_key},
        url=f"{BASE_URL}/api/paraphase/",
        json={"query_text": query},
    )
    print("paraphase api:", response.status_code)
    if response.ok:
        return response.json()
    print("Error in paraphase api!!", response.text)
    return None


def grammar_check_api(api_key, query):
    response = requests.post(
        headers={"X-API-KEY": api_key},
        url=f"{BASE_URL}/api/grammer-check/",
        json={"query_text": query},
    )
    print("grammar check api:", response.status_code)
    if response.ok:
        return response.json()
    print("Error in grammar check api!!", response.text)
    return None


def summarize_api(api_key, query):
    response = requests.post(
        headers={"X-API-KEY": api_key},
        url=f"{BASE_URL}/api/summarize/",
        json={"query_text": query},
    )
    print("summarize api:", response.status_code)
    if response.ok:
        return response.json()
    print("Error in summarize api!!", response.text)
    return None


def ai_reply_api(api_key, query):
    response = requests.post(
        headers={"X-API-KEY": api_key},
        url=f"{BASE_URL}/api/ai-reply/",
        json={"query_text": query},
    )
    print("ai reply api:", response.status_code)
    if response.ok:
        return response.json()
    print("Error in ai reply api!!", response.text)
    return None


def text_to_speech_api(
    api_key, query, voice=None, emotion=None, save_dir="audio_responses"
):
    """
    Sends text to a TTS API, receives audio (MP3), saves it locally, and returns the filename.
    """
    os.makedirs(save_dir, exist_ok=True)

    query = {
        "query_text": query,
    }
    if voice:
        query.update({"voice": voice})
    if emotion:
        query.update({"emotion": emotion})

    response = requests.post(
        url=f"{BASE_URL}/api/tts/",
        headers={"X-API-KEY": api_key},
        json=query,
        stream=True,
    )

    print("audio api:", response.status_code)

    if response.ok:
        # Extract filename from Content-Disposition header if available
        content_disposition = response.headers.get("Content-Disposition", "")
        filename = "output.mp3"
        if "filename=" in content_disposition:
            filename = content_disposition.split("filename=")[1].strip('";')

        file_path = os.path.join(save_dir, filename)

        # Save audio file
        with open(file_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

        print(f"Audio saved to: {file_path}")
        return file_path

    print("Error in audio api!!", response.text)
    return None
