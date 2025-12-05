# API Contracts: Integrated RAG Chatbot Development

This document outlines the API contracts for the FastAPI backend, supporting the core and bonus functionalities of the "Integrated RAG Chatbot Development" project. Endpoints are designed following RESTful principles.

## 1. Authentication Endpoints (via Better-Auth.com Integration)

These endpoints facilitate user authentication and profile management, leveraging the `Better-Auth.com` service. The FastAPI backend will act as an intermediary, handling requests and interacting with Better-Auth.com as necessary.

### 1.1. User Registration
*   **Endpoint**: `POST /auth/signup`
*   **Description**: Registers a new user and collects their software and hardware background.
*   **Request Body**:
    ```json
    {
      "email": "user@example.com",
      "password": "strongpassword123",
      "software_background": "Experienced in Python, FastAPI, React",
      "hardware_background": "Familiar with NVIDIA GPUs, robotics kits"
    }
    ```
*   **Responses**:
    *   `201 Created`: User successfully registered.
    *   `400 Bad Request`: Invalid input or user already exists.
    *   `500 Internal Server Error`: Better-Auth.com integration error.

### 1.2. User Login
*   **Endpoint**: `POST /auth/login`
*   **Description**: Authenticates a user and issues a session token.
*   **Request Body**:
    ```json
    {
      "email": "user@example.com",
      "password": "strongpassword123"
    }
    ```
*   **Responses**:
    *   `200 OK`: User authenticated, returns session token.
    *   `401 Unauthorized`: Invalid credentials.
    *   `500 Internal Server Error`: Better-Auth.com integration error.

### 1.3. User Logout
*   **Endpoint**: `POST /auth/logout`
*   **Description**: Invalidates the current user session.
*   **Request Headers**: `Authorization: Bearer <session_token>`
*   **Responses**:
    *   `200 OK`: User logged out.
    *   `401 Unauthorized`: Invalid or missing token.

### 1.4. Get User Profile
*   **Endpoint**: `GET /auth/user_profile`
*   **Description**: Retrieves the profile details of the currently authenticated user.
*   **Request Headers**: `Authorization: Bearer <session_token>`
*   **Responses**:
    *   `200 OK`: Returns user profile including `software_background` and `hardware_background`.
    *   `401 Unauthorized`: Invalid or missing token.

### 1.5. Update User Profile
*   **Endpoint**: `PUT /auth/user_profile`
*   **Description**: Updates the profile details of the currently authenticated user.
*   **Request Headers**: `Authorization: Bearer <session_token>`
*   **Request Body**:
    ```json
    {
      "software_background": "Expert in Python, FastAPI, React.js, Robotics OS",
      "hardware_background": "Deep experience with NVIDIA Jetson, custom robotics hardware"
    }
    ```
*   **Responses**:
    *   `200 OK`: User profile updated.
    *   `400 Bad Request`: Invalid input.
    *   `401 Unauthorized`: Invalid or missing token.

## 2. Chatbot Interaction Endpoints

These endpoints manage chat sessions and message exchange with the RAG chatbot.

### 2.1. Start New Chat Session
*   **Endpoint**: `POST /chat/session`
*   **Description**: Initiates a new chat session.
*   **Request Headers**: `Authorization: Bearer <session_token>` (Optional, for logged-in users)
*   **Request Body**: (Optional)
    ```json
    {
      "initial_message": "Hello, tell me about Module 1.",
      "chapter_id": "uuid-of-chapter-if-contextualized"
    }
    ```
*   **Responses**:
    *   `201 Created`: Returns `session_id`.
    *   `401 Unauthorized`: For logged-in sessions with invalid token.

### 2.2. Send Chat Message
*   **Endpoint**: `POST /chat/session/{session_id}/message`
*   **Description**: Sends a user message to the RAG chatbot and receives a response.
*   **Request Path Parameters**: `session_id` (UUID)
*   **Request Headers**: `Authorization: Bearer <session_token>` (Optional)
*   **Request Body**:
    ```json
    {
      "user_message": "What is ROS 2?",
      "selected_text": "ROS 2 is the Robot Operating System." // Optional: user-selected text from the book
    }
    ```
*   **Responses**:
    *   `200 OK`: Returns chatbot response and sources.
    ```json
    {
      "chatbot_response": "ROS 2 is the second generation of the Robot Operating System, designed for distributed, real-time control...",
      "sources": [
        {
          "chapter_id": "uuid-of-chapter",
          "title": "Module 1: ROS 2 Introduction",
          "segment": "ROS 2 is the Robot Operating System..."
        }
      ]
    }
    ```
    *   `400 Bad Request`: Invalid input or session_id.
    *   `401 Unauthorized`: Invalid or missing token (if session is logged in).
    *   `404 Not Found`: Session not found.

### 2.3. Get Chat Session History
*   **Endpoint**: `GET /chat/session/{session_id}`
*   **Description**: Retrieves the message history for a given chat session.
*   **Request Path Parameters**: `session_id` (UUID)
*   **Request Headers**: `Authorization: Bearer <session_token>` (Optional)
*   **Responses**:
    *   `200 OK`: Returns an array of chat messages.
    *   `401 Unauthorized`: Invalid or missing token (if session is logged in).
    *   `404 Not Found`: Session not found.

### 2.4. End Chat Session
*   **Endpoint**: `POST /chat/session/{session_id}/end`
*   **Description**: Marks a chat session as inactive.
*   **Request Path Parameters**: `session_id` (UUID)
*   **Request Headers**: `Authorization: Bearer <session_token>` (Optional)
*   **Responses**:
    *   `200 OK`: Session ended.
    *   `401 Unauthorized`: Invalid or missing token (if session is logged in).
    *   `404 Not Found`: Session not found.

## 3. Book and Content Endpoints

These endpoints provide metadata about books and chapters. Actual book content (Markdown) is served by Docusaurus.

### 3.1. List All Books
*   **Endpoint**: `GET /books`
*   **Description**: Retrieves a list of all available books.
*   **Responses**:
    *   `200 OK`: Returns an array of book metadata.

### 3.2. Get Book Details
*   **Endpoint**: `GET /books/{book_id}`
*   **Description**: Retrieves detailed metadata for a specific book.
*   **Request Path Parameters**: `book_id` (UUID)
*   **Responses**:
    *   `200 OK`: Returns book metadata.
    *   `404 Not Found`: Book not found.

### 3.3. List Chapters for a Book
*   **Endpoint**: `GET /books/{book_id}/chapters`
*   **Description**: Retrieves a list of chapters belonging to a specific book.
*   **Request Path Parameters**: `book_id` (UUID)
*   **Responses**:
    *   `200 OK`: Returns an array of chapter metadata.
    *   `404 Not Found`: Book not found.

### 3.4. Get Chapter Details
*   **Endpoint**: `GET /chapters/{chapter_id}`
*   **Description**: Retrieves metadata for a specific chapter.
*   **Request Path Parameters**: `chapter_id` (UUID)
*   **Responses**:
    *   `200 OK`: Returns chapter metadata.
    *   `404 Not Found`: Chapter not found.

### 3.5. Index Chapter Content (Admin/Internal)
*   **Endpoint**: `POST /chapters/{chapter_id}/index`
*   **Description**: Triggers the process of extracting text segments from a chapter's content and indexing them into Qdrant. This would be an internal or admin-only API.
*   **Request Path Parameters**: `chapter_id` (UUID)
*   **Responses**:
    *   `202 Accepted`: Indexing process initiated.
    *   `401 Unauthorized`: Not an authorized admin user.
    *   `404 Not Found`: Chapter not found.

## 4. Personalization Endpoints

These endpoints manage user-specific content personalization.

### 4.1. Get User Personalization Settings
*   **Endpoint**: `GET /user/{user_id}/personalization`
*   **Description**: Retrieves all personalization settings for a specific user.
*   **Request Path Parameters**: `user_id` (UUID)
*   **Request Headers**: `Authorization: Bearer <session_token>`
*   **Responses**:
    *   `200 OK`: Returns an array of personalization settings.
    *   `401 Unauthorized`: Invalid or missing token.
    *   `403 Forbidden`: User not authorized to view settings for `user_id`.

### 4.2. Set/Update Personalization Setting
*   **Endpoint**: `PUT /user/{user_id}/personalization`
*   **Description**: Sets or updates a personalization setting for a user, optionally specific to a chapter.
*   **Request Path Parameters**: `user_id` (UUID)
*   **Request Headers**: `Authorization: Bearer <session_token>`
*   **Request Body**:
    ```json
    {
      "chapter_id": "uuid-of-chapter" (optional),
      "setting_key": "detail_level",
      "setting_value": "advanced"
    }
    ```
*   **Responses**:
    *   `200 OK`: Setting updated/created.
    *   `400 Bad Request`: Invalid input.
    *   `401 Unauthorized`: Invalid or missing token.
    *   `403 Forbidden`: User not authorized to modify settings for `user_id`.

### 4.3. Get Personalized Chapter Content
*   **Endpoint**: `GET /chapters/{chapter_id}/personalized_content`
*   **Description**: Retrieves the personalized version of a chapter's content based on the user's settings.
*   **Request Path Parameters**: `chapter_id` (UUID)
*   **Request Headers**: `Authorization: Bearer <session_token>`
*   **Responses**:
    *   `200 OK`: Returns the personalized chapter content (e.g., as HTML or Markdown).
    *   `401 Unauthorized`: Invalid or missing token.
    *   `404 Not Found`: Chapter not found.

## 5. Translation Endpoints

These endpoints provide content translation capabilities.

### 5.1. Get Translated Chapter Content
*   **Endpoint**: `GET /chapters/{chapter_id}/translated_content`
*   **Description**: Retrieves the translated version of a chapter's content into a specified target language.
*   **Request Path Parameters**: `chapter_id` (UUID)
*   **Request Headers**: `Authorization: Bearer <session_token>` (Optional, for logged-in user context)
*   **Request Query Parameters**: `target_language` (e.g., 'ur' for Urdu)
*   **Responses**:
    *   `200 OK`: Returns the translated chapter content (e.g., as HTML or Markdown).
    *   `400 Bad Request`: Invalid target language.
    *   `404 Not Found`: Chapter not found.
    *   `503 Service Unavailable`: Translation service error.
