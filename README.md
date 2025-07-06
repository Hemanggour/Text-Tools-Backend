# Project README

## Table of Contents

*   [Project Description](#project-description)
*   [Files](#files)
    *   [Core Project Files](#core-project-files)
    *   [API Related Files](#api-related-files)
    *   [Account Management Files](#account-management-files)
    *   [Testing Files](#testing-files)
    *   [AI Related Files](#ai-related-files)
*   [Installation](#installation)
*   [Features](#features)
*   [Usage](#usage)
*   [Dependencies](#dependencies)
*   [License](#license)

## Project Description

[Provide a brief description of your project here.]

## Files

This section describes the structure and purpose of the key files within this project.

### Core Project Files

*   **`README.md`**:
    *   **Role:** This file.

*   **`manage.py`**:
    *   **Role:** Main entry point for Django's command-line utility. Used for administrative tasks (database migrations, superuser creation, running the development server, etc.).
    *   **Key Functionality:** Sets the `DJANGO_SETTINGS_MODULE` environment variable and executes commands based on command-line arguments. Includes error handling for Django import failures.
    *   **Type:** Main entry point.

*   **`project/settings.py`**:
    *   **Role:** Central configuration file for the Django project. Defines various settings that control the behavior of the Django application.
    *   **Key Roles:** Sets up database connections (MySQL), authentication, installed applications, middleware, templates, static files, internationalization, and other project-specific configurations. Loads environment variables from a `.env` file for sensitive information. Defines custom settings like `MODEL_TEMPRATURE`, Google API key, Gemini model, and text-to-speech source URL.
    *   **Type:** Main configuration file.

*   **`project/urls.py`**:
    *   **Role:** Main entry point for URL routing in the Django project. Maps URLs to views.
    *   **Key Roles:** Defines URL patterns and their associated views or URLconfs. Includes Django admin site and includes URL patterns from other apps.
    *   **Type:** Main Entry Point

*   **`project/wsgi.py`**:
    *   **Role:** WSGI (Web Server Gateway Interface) configuration file. Handles incoming web requests and passes them to the Django application.
    *   **Key Roles:** Sets the Django settings module and creates the WSGI application instance.
    *   **Main Entry Point:** Yes, for web server interaction.

*   **`project/asgi.py`**:
    *   **Role:** ASGI (Asynchronous Server Gateway Interface) configuration for a Django project. Responsible for deploying the Django application to an ASGI-compatible server.
    *   **Main entry point for ASGI server deployment.**

*   **`requirements.txt`**:
    *   **Role:** Lists the Python packages required to run the project.
    *   **Key Roles:** Defines the project's software dependencies.
    *   **Type:** Helper file; used by `pip` to install dependencies.
    *   **Specific Dependencies:**
        *   `django`: A high-level Python web framework.
        *   `djangorestframework`: A toolkit for building Web APIs.
        *   `dotenv`: Allows loading environment variables from a `.env` file.
        *   `mysqlclient`: A Python library for connecting to MySQL databases.
        *   `langchain_google_genai`: For using Google's Generative AI models within the LangChain framework.
        *   `gradio_client`: For interacting with Gradio applications.
        *   `requests`: A library for making HTTP requests.

### API Related Files

*   **`api/urls.py`**:
    *   **Role:** Main entry point for API routing. Defines the URL patterns for various API endpoints.
    *   **Key Function:** Maps URL paths to specific view classes.
    *   **Components:** Uses `django.urls.path` to define the routes. Imports view classes from `api.views` (e.g., `SummarizeView`, `ParaphaseView`). Connects each URL path to a corresponding view class using `.as_view()`. Defines routes for summarizing text, paraphrasing, grammar checking, generating AI replies, and converting text to speech.

*   **`api/admin.py`**:
    *   **Role:** Configuration of Django's admin interface for the `api` app.
    *   **Key Role:**  Configuration of Django's admin interface.
    *   **Type:** Helper.

*   **`api/apps.py`**:
    *   **Role:** Defines the configuration for the Django app named "api."
    *   **Type:** Helper file, providing metadata about the Django application.

*   **`api/models.py`**:
    *   **Role:** Defines the data models for the Django application. This file is responsible for defining the structure of data that will be stored in the database.
    *   **Key Role:** Defines the database schema and the structure of the application's data.
    *   **Type:** Helper.

*   **`api/views.py`**:
    *   **Role:** Defines API views for various text-based AI functionalities. Acts as a **main entry point** for several REST API endpoints, handling requests and responses.
    *   **Key Functionality:**
        *   **SummarizeView:** Summarizes input text.
        *   **ParaphaseView:** Paraphrases input text.
        *   **AiReplyView:** Generates AI replies.
        *   **GrammarCheckView:** Performs grammar checks.
        *   **TextToSpeechView:** Converts text to speech, handling voice and emotion selection, and audio file generation.
    *   **Key Components:** Uses `rest_framework`, serializers, `ApiKeyAuthentication` and `IsAuthenticated`, interacts with AI classes (likely from `api.ai`), and uses `FileResponse` for audio files.
    *   **Main Entry Point:** Yes, for API interactions related to AI text functionalities.

### Account Management Files

*   **`account/admin.py`**:
    *   **Role:** Django admin configuration file for the `account` app. Registers Django models for management through the Django admin interface.
    *   **Key Features:** Imports the `admin` module.  Contains a comment indicating where model registration would occur. (Currently, no models are registered).
    *   **Type:** Helper file.

*   **`account/apps.py`**:
    *   **Role:** Defines the configuration for the "account" Django app.
    *   **Type:** Helper file.

*   **`account/authentication.py`**:
    *   **Role:** Defines a custom authentication class, `ApiKeyAuthentication`, for a Django REST Framework API. Authenticates requests based on an API key in the `X-API-KEY` header.
    *   **Key Role:** Implements API key-based authentication.
    *   **Type:** Helper.

*   **`account/models.py`**:
    *   **Role:** Defines the data models for user authentication and API key management.
        *   `UserManager`: Custom manager for the `UserModel`. Handles superuser creation and user retrieval by username.
        *   `UserModel`: Represents the user model, extending `AbstractBaseUser` and `PermissionsMixin`. Defines fields like email, staff status, and active status. `USERNAME_FIELD` is "email".
        *   `ApikeyModel`: Models the API key, linked to a user via a foreign key.
    *   **Key Roles:** Defines data structures for users and API keys, manages user creation.
    *   **Type:** Helper.

*   **`account/serializers.py`**:
    *   **Role:** Defines serializers for the `account` app, specifically for user authentication and API key management.
    *   **Key Components:**
        *   `UserSerializer`: Serializes user data (`UserModel`). Handles user creation, encrypting passwords.
        *   `ApikeySerializer`: Serializes API key data (`ApikeyModel`). Provides a static method `generate_api_key_for_user`.
    *   **Technical Summary:** Uses Django REST Framework's `serializers`. Handles password hashing and API key generation using the `secrets` module.
    *   **Type:** Helper.

*   **`account/tests.py`**:
    *   **Role:** Contains unit tests for the `account` application.
    *   **Key Elements:** Imports `TestCase` from `django.test`. Includes a placeholder for test cases.
    *   **Type:** Helper file.

*   **`account/urls.py`**:
    *   **Role:** Defines the URL patterns for the `account` app.
    *   **Key Role:** Serves as a main entry point for the `account` app's API endpoints.
    *   **Type:** Main entry point for URL routing.

*   **`account/views.py`**:
    *   **Role:** Defines API views for user authentication and account management. Handles user login, registration, API key generation/management, and logout.
    *   **Key Components:**
        *   **LoginView:** Handles user login.
        *   **RegisterView:** Handles user registration.
        *   **ApikeyView:** Manages API keys (GET, POST, PATCH).
        *   **LogoutView:** Handles user logout.
    *   **Dependencies:** Relies on `django.contrib.auth`, Django REST Framework (DRF), custom models/serializers from `account`, and DRF permissions.
    *   **Main Entry Point:** Yes, for account-related API interactions.

*   **`account\migrations\0001_initial.py`**:
    *   **Role:** Django database migration file. Defines the initial database schema for the `account` app.
    *   **Key Roles:**
        *   Creates `UserModel` and `ApikeyModel`.
        *   `UserModel` defines the structure for user accounts.
        *   `ApikeyModel` defines the structure for API keys.
    *   **Type:** Helper.

### Testing Files

*   **`api/tests.py`**:
    *   **Role:** Contains Django test cases for the `api` application.
    *   **Type:** Helper.

*   **`test_script\driver.py`**
    *   **Role:** Main entry point and driver script for testing the Text Tool API. It presents a menu-driven interface to the user.
    *   **Key Functionality:**
        *   Handles user input for API interactions (summarization, paraphrasing, grammar check, AI reply, text-to-speech).
        *   Manages the login and API key retrieval process using functions from the `test_file` module.
        *   Calls API functions from `test_file` based on user's menu selections.
        *   Manages user interaction, displaying results, and handling errors.
    *   **Main Entry Point:** Yes, the `main()` function is executed when the script is run.
    *   **Helper or Main:** Main

*   **`test_script\test_file.py`**
    *   **Role:** Defines functions to interact with a REST API for testing and integration. Provides functions for authentication, API key management, and calling AI-powered text processing APIs.
    *   **Key Roles:**
        *   **API Interaction:** Encapsulates API calls.
        *   **Authentication Management:** Manages login, CSRF token retrieval, and logout.
        *   **TTS handling:** handling the tts api that returns an audio file and stores it locally
    *   **Type:** Helper/Utility (not a main entry point).

### AI Related Files

*   **`api\ai\text_to_speech_ai.py`**
    *   **Role:** Implements a text-to-speech (TTS) service using a Gradio client. Allows generating audio from text input, with voice and emotion options. Includes functionality to delete the generated audio file.
    *   **Key Roles:**
        *   `TextToSpeech` class: Encapsulates TTS functionality. Handles interactions with the Gradio API.
    *   **Type:** Helper class.

*   **`api\ai\text_to_text_ai.py`**
    *   **Role:** Defines a class `TextToText` that uses Google's Gemini AI model (via `langchain_google_genai`) for text operations.
    *   **Key Roles:**
        *   `TextToText` class: Performs text summarization, paraphrasing, reply generation, and grammar checking.
        *   `ChatGoogleGenerativeAI`: Handles interaction with the Google Gemini model.
    *   **Type:** Helper (Provides AI-powered text manipulation functionalities).

## Installation

Provide instructions on how to install and set up the project.  This should include:

1.  **Prerequisites:**  List any software or tools that need to be installed (e.g., Python, a specific database like MySQL, etc.).
2.  **Cloning the repository:**  Instructions on how to clone the project repository.
3.  **Setting up a virtual environment:** Instructions on creating and activating a Python virtual environment.
4.  **Installing dependencies:** Instructions on installing the required Python packages using `pip` and the `requirements.txt` file.
5.  **Database setup:**  Instructions on how to set up and configure the database (e.g., creating a database, setting up database credentials).
6.  **Environment variables:** Instructions on setting up environment variables (e.g., API keys, database credentials) and the `.env` file.
7.  **Running migrations:**  How to run Django migrations to set up the database schema.
8.  **Creating a superuser:** How to create a Django superuser for administrative access.

## Features

Describe the key features of your project.  Be specific about what the project does.  Example:

*   User authentication (login, registration, logout).
*   API key generation and management.
*   Text summarization using AI.
*   Text paraphrasing using AI.
*   Grammar checking using AI.
*   AI-powered reply generation.
*   Text-to-speech conversion with voice and emotion selection.
*   Ability to download the generated audio files.

## Usage

Provide instructions on how to use the project. This should include:

1.  **Running the development server:**  How to start the Django development server.
2.  **API endpoints:**  Documentation for each API endpoint, including:
    *   The URL.
    *   The HTTP method (GET, POST, PUT, DELETE, etc.).
    *   Input parameters (e.g., in the request body).
    *   Expected output (e.g., in JSON format).
    *   Example requests and responses using `curl` or a tool like Postman.
3.  **Accessing the Django admin interface:**  How to access and use the Django admin interface.
4.  **Running the test script:** Instructions on running the test script and interacting with the API via a menu driven interface.

## Dependencies

List the project's dependencies, including their versions if possible.  You can often get this information from your `requirements.txt` file.

```
django==[version]
djangorestframework==[version]
dotenv==[version]
mysqlclient==[version]
langchain_google_genai==[version]
gradio_client==[version]
requests==[version]
# Add other dependencies and their versions here
```

## License

Specify the license under which the project is released (e.g., MIT, Apache 2.0, etc.).  Include a link to the full license text.  Example:

This project is licensed under the [MIT License](link_to_license_file).