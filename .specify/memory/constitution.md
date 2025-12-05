# Project Constitution: Integrated RAG Chatbot Development

## 1. Core Mandate

The primary goal of this project is to develop and embed a Retrieval-Augmented Generation (RAG) chatbot within a published book. This chatbot will serve as an intelligent assistant, capable of answering user questions directly related to the book's content, including queries based on user-selected text excerpts.

## 2. Key Technologies

The following technologies are central to the implementation of this project:
*   **Chatbot Framework**: OpenAI Agents/ChatKit SDKs
*   **Backend API**: FastAPI
*   **Vector Database**: Qdrant Cloud Free Tier
*   **Relational Database**: Neon Serverless Postgres

## 3. Core Functionality (Base Points - 100)

The base functionality, mandatory for achieving core points, includes:

*   **RAG Chatbot Integration**: Seamlessly embed the RAG chatbot within the published book.
*   **Content-Aware Question Answering**: The chatbot must accurately answer user questions about the book's content.
*   **Selected Text Query**: Enable users to select specific text within the book and pose questions based solely on that selection.

## 4. Bonus Functionality (Extra Points)

Additional features that can earn bonus points include:

### 4.1. Reusable Intelligence (50 Points)
*   **Claude Code Subagents**: Implement and utilize reusable intelligence via Claude Code Subagents.
*   **Agent Skills**: Develop and integrate Agent Skills within the book project to enhance chatbot capabilities.

### 4.2. User Authentication & Personalization (50 Points)
*   **Signup and Signin**: Implement user authentication using Better-Auth.com.
*   **User Profiling**: During signup, collect user's software and hardware background information.
*   **Personalized Content**: Utilize collected user background to personalize book content.

### 4.3. In-Chapter Content Personalization (50 Points)
*   **User-Driven Content Personalization**: Allow logged-in users to personalize content within chapters by pressing a dedicated button at the start of each chapter.

### 4.4. In-Chapter Content Translation (50 Points)
*   **Urdu Translation**: Enable logged-in users to translate chapter content into Urdu by pressing a dedicated button at the start of each chapter.

## 5. Constraints & Non-Goals

*   **Scope**: The project is strictly focused on the features and technologies outlined above. Any deviation requires explicit approval.
*   **Deliverable**: The primary deliverable is a published book with an integrated and functional RAG chatbot.
*   **Platform**: The implementation will leverage specified cloud services (Neon, Qdrant) and SDKs (OpenAI Agents/ChatKit).