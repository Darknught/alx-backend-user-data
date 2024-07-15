# Simple API

Simple HTTP API for playing with `User` model.


## Files

### `models/`

- `base.py`: base of all models of the API - handle serialization to file
- `user.py`: user model

### `api/v1`

- `app.py`: entry point of the API
- `views/index.py`: basic endpoints of the API: `/status` and `/stats`
- `views/users.py`: all users endpoints


## Setup

```
$ pip3 install -r requirements.txt
```


## Run

```
$ API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
```


## Routes

- `GET /api/v1/status`: returns the status of the API
- `GET /api/v1/stats`: returns some stats of the API
- `GET /api/v1/users`: returns the list of users
- `GET /api/v1/users/:id`: returns an user based on the ID
- `DELETE /api/v1/users/:id`: deletes an user based on the ID
- `POST /api/v1/users`: creates a new user (JSON parameters: `email`, `password`, `last_name` (optional) and `first_name` (optional))
- `PUT /api/v1/users/:id`: updates an user based on the ID (JSON parameters: `last_name` and `first_name`)


## Components

### Auth Class (auth.py)

The `Auth` class provides methods to require authentication, check authorization headers, and validate user credentials. 

#### Methods:

- `require_auth(path: str, excluded_paths: List[str]) -> bool`: Determines if a path requires authentication.
- `authorization_header(request=None) -> str`: Retrieves the Authorization header from the request.
- `current_user(request=None) -> TypeVar('User')`: Retrieves the current user based on the request.

### BasicAuth Class (basic_auth.py)

The `BasicAuth` class inherits from `Auth` and implements methods specific to Basic Authentication.

#### Methods:

- `extract_base64_authorization_header(self, authorization_header: str) -> str`: Extracts the Base64 part of the Authorization header.
- `decode_base64_authorization_header(self, base64_authorization_header: str) -> str`: Decodes the Base64 string.
- `extract_user_credentials(self, decoded_base64_authorization_header: str) -> (str, str)`: Extracts the user email and password from the decoded Base64 string.
- `user_object_from_credentials(self, user_email: str, user_pwd: str) -> TypeVar('User')`: Returns the User instance based on email and password.
- `current_user(self, request=None) -> TypeVar('User')`: Retrieves the User instance for a request by using the provided credentials.

### Flask Application (app.py)

The Flask application integrates the authentication system and handles various routes and error handling.

#### Key Features:

- Registers the blueprint `app_views`.
- Configures CORS.
- Handles errors for `404 Not Found`, `401 Unauthorized`, and `403 Forbidden`.
- Implements a `before_request` method to enforce authentication on protected routes.

### User Model (user.py)

The `User` model defines user-related attributes and methods, including searching for users by email and validating passwords.

## Basic Authentication

Basic Authentication is a simple authentication scheme built into the HTTP protocol. It involves sending credentials (username and password) encoded in Base64 as part of the HTTP request's Authorization header.

### Process:

1. **Client Request**: The client sends a request with an Authorization header containing the credentials encoded in Base64.
2. **Server Validation**: The server decodes the credentials and validates them against the stored user data.
3. **Response**: If the credentials are valid, the server grants access; otherwise, it responds with an error (e.g., `401 Unauthorized`).

### Example:

1. **Client Request**:

2. **Server Decodes**:
- `dXNlcm5hbWU6cGFzc3dvcmQ=` decodes to `username:password`.

3. **Server Validates**:
- Checks if the username and password match any stored user credentials.

4. **Server Response**:
- If valid, returns the requested resource.
- If invalid, returns `401 Unauthorized`.


## Session Authentication
Session Authentication involves creating a session for the user and maintaining it through cookies. It provides a more secure and scalable way to manage user authentication.

### Process:
- Login: The user sends credentials, and the server creates a session, returning a session ID.
- Session Storage: The session ID is stored on the client (typically in cookies) and on the server (in memory or a database).
- Authenticated Requests: The client includes the session ID in subsequent requests.
- Session Validation: The server validates the session ID and retrieves the associated user.
- Logout: The session is destroyed, removing the session ID from the client and server.

### Example Endpoints:
- POST /api/v1/auth_session/login: Authenticates a user and creates a session.
- GET /api/v1/users/me: Retrieves the authenticated user's details.
- DELETE /api/v1/auth_session/logout: Logs out the user and destroys the session.


### SessionAuth Class (session_auth.py)
The `SessionAuth` class inherits from `Auth` and implements methods for session-based authentication

### Methods:
- `create_session(self, user_id=None) -> str`: Creates a session for a user
- `user_id_for_session_id(self, session_id=None) -> str`: Retrieves a user ID based on the session ID.
- `destroy_session(self, request=None) -> bool`: Destroys a session based on the request.

### SessionExpAuth Class (session_exp_auth.py)
The SessionExpAuth class inherits from SessionAuth and adds session expiration functionality.

### Methods:
- `create_session(self, user_id=None) -> str`: Creates a session with an expiration time.
- `user_id_for_session_id(self, session_id=None) -> str`: Retrieves a user ID based on the session ID, considering session expiration.


## Setting Up the Project

### Prerequisites

- Python 3.x
- Flask

### Installation

1. Clone the repository:
2. Install the required dependencies:


### Running the Application

1. Set environment variables for the host and port:
2. Run the Flask application:
3. The application will be accessible at `http://0.0.0.0:5000`.

## Testing the Endpoints

Use `curl` or a tool like Postman to test the endpoints:

## Conclusion

This project demonstrates implementing Basic Authentication in a Flask API. It covers creating authentication classes, integrating them into the Flask application, and handling user credentials securely. The provided structure and methods ensure a robust and scalable authentication system suitable for various projects.

