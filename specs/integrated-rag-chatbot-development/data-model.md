# Data Model: Integrated RAG Chatbot Development

This document outlines the data model for the "Integrated RAG Chatbot Development" project, based on the requirements defined in `spec.md`. It identifies key entities, their attributes, and relationships, which will be stored primarily in Neon Serverless Postgres and Qdrant.

## 1. Entities

### 1.1. User (Stored in Neon Serverless Postgres)
Represents a user of the system, including authentication and personalization data.

*   **Attributes**:
    *   `user_id`: UUID (Primary Key) - Unique identifier for the user.
    *   `email`: VARCHAR(255), UNIQUE, NOT NULL - User's email address for authentication.
    *   `password_hash`: VARCHAR(255), NOT NULL - Hashed password for security.
    *   `software_background`: TEXT - Information about user's software experience (collected during signup).
    *   `hardware_background`: TEXT - Information about user's hardware experience (collected during signup).
    *   `created_at`: TIMESTAMP, NOT NULL - Timestamp of user creation.
    *   `updated_at`: TIMESTAMP, NOT NULL - Last update timestamp.

*   **Relationships**:
    *   One-to-many with `Chat_Session`
    *   One-to-many with `Personalization_Setting`

### 1.2. Book (Metadata Stored in Neon Serverless Postgres)
Represents a published book within the system.

*   **Attributes**:
    *   `book_id`: UUID (Primary Key) - Unique identifier for the book.
    *   `title`: VARCHAR(255), NOT NULL - Title of the book.
    *   `author`: VARCHAR(255) - Author of the book.
    *   `description`: TEXT - Brief description of the book.
    *   `cover_image_url`: VARCHAR(255) - URL to the book's cover image.
    *   `total_modules`: INTEGER - Total number of modules in the book.
    *   `total_chapters`: INTEGER - Total number of chapters in the book.
    *   `published_date`: DATE - Publication date.
    *   `created_at`: TIMESTAMP, NOT NULL.
    *   `updated_at`: TIMESTAMP, NOT NULL.

*   **Relationships**:
    *   One-to-many with `Chapter`

### 1.3. Chapter (Content Metadata Stored in Neon Serverless Postgres)
Represents a chapter within a book. The actual content is primarily within the Docusaurus Markdown files, but metadata is stored here.

*   **Attributes**:
    *   `chapter_id`: UUID (Primary Key) - Unique identifier for the chapter.
    *   `book_id`: UUID (Foreign Key) - Links to the parent book.
    *   `module_number`: INTEGER - The module number the chapter belongs to.
    *   `chapter_number`: INTEGER - The order of the chapter within its module.
    *   `title`: VARCHAR(255), NOT NULL - Title of the chapter.
    *   `docusaurus_path`: VARCHAR(255), UNIQUE, NOT NULL - Path to the Docusaurus Markdown file for this chapter.
    *   `last_indexed_at`: TIMESTAMP - Timestamp when the chapter's content was last indexed for embeddings.
    *   `created_at`: TIMESTAMP, NOT NULL.
    *   `updated_at`: TIMESTAMP, NOT NULL.

*   **Relationships**:
    *   Many-to-one with `Book`
    *   One-to-many with `Content_Embedding`
    *   One-to-many with `Personalization_Setting` (if chapter-specific)
    *   One-to-many with `Translation_Cache`

### 1.4. Content_Embedding (Stored in Qdrant)
Represents a chunk of book content and its vector embedding, used for RAG.

*   **Attributes**:
    *   `embedding_id`: UUID (Primary Key in Qdrant, can be implicit or generated) - Unique ID for the vector.
    *   `chapter_id`: UUID (Metadata in Qdrant, FK equivalent) - Links to the source chapter in Neon Postgres.
    *   `book_id`: UUID (Metadata in Qdrant, FK equivalent) - Links to the source book.
    *   `text_segment`: TEXT - The original chunk of text that was embedded.
    *   `embedding_vector`: VECTOR (FLOAT ARRAY) - The high-dimensional vector representation of `text_segment`.
    *   `segment_order`: INTEGER - Order of the segment within the chapter (for reconstruction).
    *   `metadata`: JSONB (Qdrant payload) - Additional context like page number, section, etc.

*   **Relationships**:
    *   Many-to-one with `Chapter` (via `chapter_id` metadata)

### 1.5. Chat_Session (Stored in Neon Serverless Postgres)
Represents a single conversational session with the RAG chatbot.

*   **Attributes**:
    *   `session_id`: UUID (Primary Key) - Unique identifier for the chat session.
    *   `user_id`: UUID (Foreign Key, NULLABLE) - Links to the `User` if logged in, otherwise NULL for anonymous.
    *   `start_time`: TIMESTAMP, NOT NULL - Time the session started.
    *   `end_time`: TIMESTAMP - Time the session ended.
    *   `is_active`: BOOLEAN, NOT NULL - Indicates if the session is currently active.
    *   `current_context_chapter_id`: UUID (Foreign Key, NULLABLE) - If chat is focused on a specific chapter.

*   **Relationships**:
    *   Many-to-one with `User`
    *   One-to-many with `Chat_Message`

### 1.6. Chat_Message (Stored in Neon Serverless Postgres)
Represents an individual message within a chat session.

*   **Attributes**:
    *   `message_id`: UUID (Primary Key) - Unique identifier for the message.
    *   `session_id`: UUID (Foreign Key) - Links to the parent `Chat_Session`.
    *   `sender_type`: VARCHAR(50), NOT NULL - 'user', 'chatbot', 'agent'.
    *   `content`: TEXT, NOT NULL - The message text.
    *   `timestamp`: TIMESTAMP, NOT NULL - Time the message was sent.
    *   `context_selected_text`: TEXT - If the message was a user query based on selected text, this stores the selected text.
    *   `retrieved_sources`: JSONB - References to `Content_Embedding` IDs or chapter sections used by the chatbot.

*   **Relationships**:
    *   Many-to-one with `Chat_Session`

### 1.7. Personalization_Setting (Stored in Neon Serverless Postgres)
Stores user-specific preferences for content personalization.

*   **Attributes**:
    *   `setting_id`: UUID (Primary Key).
    *   `user_id`: UUID (Foreign Key) - Links to the `User`.
    *   `chapter_id`: UUID (Foreign Key, NULLABLE) - If the setting is chapter-specific, otherwise NULL for global.
    *   `setting_key`: VARCHAR(100), NOT NULL - Key for the personalization setting (e.g., 'detail_level', 'example_style').
    *   `setting_value`: TEXT, NOT NULL - The value of the setting (e.g., 'advanced', 'practical').
    *   `created_at`: TIMESTAMP, NOT NULL.
    *   `updated_at`: TIMESTAMP, NOT NULL.

*   **Relationships**:
    *   Many-to-one with `User`
    *   Many-to-one with `Chapter` (optional)

### 1.8. Translation_Cache (Stored in Neon Serverless Postgres)
Caches translated chapter content to improve performance and reduce repeated API calls.

*   **Attributes**:
    *   `cache_id`: UUID (Primary Key).
    *   `chapter_id`: UUID (Foreign Key) - Links to the original `Chapter`.
    *   `original_content_hash`: VARCHAR(255), NOT NULL - Hash of the original chapter content to detect changes.
    *   `language`: VARCHAR(10), NOT NULL - e.g., 'ur' for Urdu.
    *   `translated_content`: TEXT, NOT NULL - The full translated chapter content.
    *   `translation_time`: TIMESTAMP, NOT NULL - When the translation was performed/cached.
    *   `created_at`: TIMESTAMP, NOT NULL.
    *   `updated_at`: TIMESTAMP, NOT NULL.

*   **Relationships**:
    *   Many-to-one with `Chapter`

## 2. Relationships Summary

*   `User` 1:N `Chat_Session`
*   `User` 1:N `Personalization_Setting`
*   `Book` 1:N `Chapter`
*   `Chapter` 1:N `Content_Embedding` (via Qdrant metadata)
*   `Chapter` 1:N `Personalization_Setting` (chapter-specific)
*   `Chapter` 1:N `Translation_Cache`
*   `Chat_Session` 1:N `Chat_Message`

## 3. Validation Rules and State Transitions

*   **User**: Email must be unique. Password must meet complexity requirements (handled by Better-Auth.com).
*   **Book/Chapter**: `book_id`, `chapter_id`, `title`, `docusaurus_path` must be unique and NOT NULL where specified. `chapter_order` should be unique within a `book_id`.
*   **Chat_Session**: `is_active` managed by session lifecycle.
*   **Content_Embedding**: `text_segment` must be processed before embedding. `embedding_vector` must be valid vector format.
*   **Authentication**: Handled by Better-Auth.com. Session management for logged-in users.
*   **Personalization/Translation**: Settings are applied per user, and optionally per chapter. Content hashes ensure cache validity.
