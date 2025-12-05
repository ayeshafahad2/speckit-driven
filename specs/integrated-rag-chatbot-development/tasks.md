# Tasks: Integrated RAG Chatbot Development

**Input**: Design documents from `/specs/integrated-rag-chatbot-development/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification or if user requests TDD approach.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Web app**: `backend/src/`, `frontend/src/`
- Paths shown below assume this web app structure.

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure.

- [X] T001 Create backend directory structure backend/src/, backend/tests/
- [X] T002 Initialize Python project for backend in backend/ with `pyproject.toml` and `requirements.txt`
- [X] T003 Install core Python dependencies for backend in backend/requirements.txt
- [X] T004 Create initial FastAPI application instance in backend/src/main.py
- [X] T005 [P] Configure environment variables for backend in backend/.env.example
- [X] T006 [P] Configure CORS settings for FastAPI in backend/src/main.py
- [X] T007 Create initial Docusaurus frontend component for chatbot integration in frontend/src/components/Chatbot/index.tsx
- [X] T008 [P] Configure Docusaurus to allow integration with external API endpoints in `docusaurus.config.ts`
- [X] T009 [P] Update `.gitignore` for new backend/ and `.env` files

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented.

**⚠️ CRITICAL**: No user story work can begin until this phase is complete.

- [X] T010 Setup Neon Serverless Postgres database connection and ORM (e.g., SQLAlchemy) in backend/src/database.py
- [X] T011 [P] Implement base `User` model in backend/src/models/user.py
- [X] T012 [P] Implement base `Book` model in backend/src/models/book.py
- [X] T013 [P] Implement base `Chapter` model in backend/src/models/chapter.py
- [X] T014 [P] Setup Qdrant client connection in backend/src/vector_db.py
- [X] T015 Integrate Better-Auth.com SDK/client into backend/src/auth/better_auth_client.py
- [X] T016 Configure FastAPI authentication middleware for session management in backend/src/auth/middleware.py
- [X] T017 Setup basic testing framework (`pytest`) for backend in backend/tests/conftest.py
- [X] T018 Setup basic testing framework (`Jest`/`React Testing Library`) for frontend in `frontend/jest.config.js`
- [X] T019 Implement generic error handling and logging for backend in backend/src/utils/errors.py, backend/src/utils/logger.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel.

---

## Phase 3: User Story 1 - RAG Chatbot Core (Priority: P1) 🎯 MVP

**Goal**: Embed a RAG chatbot within the book interface.

**Independent Test**: Verify that a basic chat interface is displayed within the book's context and can send/receive predefined messages.

### Implementation for User Story 1

- [X] T020 [P] [US1] Create `ChatSession` model in backend/src/models/chat.py
- [X] T021 [P] [US1] Create `ChatMessage` model in backend/src/models/chat.py
- [X] T022 [P] [US1] Implement chat session management service in backend/src/services/chat_service.py
- [X] T023 [P] [US1] Implement FastAPI endpoint `POST /chat/session` in backend/src/api/chat.py
- [X] T024 [P] [US1] Implement FastAPI endpoint `GET /chat/session/{session_id}` in backend/src/api/chat.py
- [X] T025 [P] [US1] Implement FastAPI endpoint `POST /chat/session/{session_id}/end` in backend/src/api/chat.py
- [X] T026 [US1] Create base Chatbot UI component in frontend/src/components/Chatbot/ChatWindow.tsx
- [X] T027 [US1] Integrate Chatbot UI component into a Docusaurus page (e.g., `frontend/src/pages/chatbot.tsx`)
- [X] T028 [US1] Implement basic API calls from frontend to backend for chat session management in `frontend/src/hooks/useChatApi.ts`

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently.

---

## Phase 4: User Story 2 - Content-Aware Question Answering (Priority: P1)

**Goal**: Chatbot accurately answers questions about book content.

**Independent Test**: Given a question about the book, the chatbot provides a relevant answer grounded in the book's content.

### Implementation for User Story 2

- [X] T029 [P] [US2] Create `ContentEmbedding` model in backend/src/models/content.py
- [ ] T030 [P] [US2] Implement content ingestion service to parse Docusaurus Markdown and chunk text in backend/src/services/content_ingestion_service.py
- [ ] T031 [P] [US2] Implement embedding generation service (using OpenAI's embedding models) in backend/src/services/embedding_service.py
- [ ] T032 [P] [US2] Implement Qdrant indexing service in backend/src/services/qdrant_service.py
- [ ] T033 [US2] Implement FastAPI endpoint `POST /chapters/{chapter_id}/index` for content ingestion (admin/internal) in backend/src/api/content.py
- [ ] T034 [P] [US2] Implement Qdrant retrieval service in backend/src/services/qdrant_service.py
- [ ] T035 [P] [US2] Integrate OpenAI Agents/ChatKit SDK for RAG generation in backend/src/services/rag_service.py
- [ ] T036 [US2] Update chat service (`backend/src/services/chat_service.py`) to use RAG service for responses
- [ ] T037 [US2] Update FastAPI endpoint `POST /chat/session/{session_id}/message` to return RAG responses in backend/src/api/chat.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently.

---

## Phase 5: User Story 3 - User Selected Text Query (Priority: P1)

**Goal**: Chatbot answers questions based on user-selected text.

**Independent Test**: Users can select text, trigger a query, and the chatbot's response prioritizes that text.

### Implementation for User Story 3

- [ ] T038 [P] [US3] Frontend utility to capture user selected text from Docusaurus content in `frontend/src/utils/text_selection.ts`
- [ ] T039 [P] [US3] Frontend UI component for context menu on text selection (e.g., "Ask Chatbot") in `frontend/src/components/TextSelection/ContextMenu.tsx`
- [ ] T040 [US3] Update chat message endpoint (`POST /chat/session/{session_id}/message`) to accept `selected_text` in backend/src/api/chat.py
- [ ] T041 [US3] Modify RAG service (`backend/src/services/rag_service.py`) to prioritize `selected_text` in its retrieval and generation logic
- [ ] T042 [US3] Integrate text selection context menu with chatbot UI in `frontend/src/components/Chatbot/ChatWindow.tsx`

**Checkpoint**: All user stories up to US3 should now be independently functional.

---

## Phase 6: User Story 4 - User Authentication and Personalized Content (Priority: P2)

**Goal**: Secure user authentication and content personalization based on user background.

**Independent Test**: Users can sign up, log in, update profile, and see content dynamically personalized based on their background.

### Implementation for User Story 4

- [ ] T043 [P] [US4] Implement user registration endpoint (`POST /auth/signup`) in backend/src/api/auth.py
- [ ] T044 [P] [US4] Implement user login endpoint (`POST /auth/login`) in backend/src/api/auth.py
- [ ] T045 [P] [US4] Implement user logout endpoint (`POST /auth/logout`) in backend/src/api/auth.py
- [ ] T046 [P] [US4] Implement get user profile endpoint (`GET /auth/user_profile`) in backend/src/api/auth.py
- [ ] T047 [P] [US4] Implement update user profile endpoint (`PUT /auth/user_profile`) in backend/src/api/auth.py
- [ ] T048 [US4] Create frontend signup page in `frontend/src/pages/signup.tsx`
- [ ] T049 [US4] Create frontend login page in `frontend/src/pages/login.tsx`
- [ ] T050 [US4] Create frontend user profile page to display/update background in `frontend/src/pages/profile.tsx`
- [ ] T051 [US4] Implement API calls for auth from frontend to backend in `frontend/src/hooks/useAuthApi.ts`
- [ ] T052 [US4] Implement content personalization logic in backend/src/services/personalization_service.py
- [ ] T053 [US4] Develop frontend mechanism to fetch and display personalized content (e.g., via Docusaurus plugin or component wrapper) in `frontend/src/components/PersonalizedContent/index.tsx`

---

## Phase 7: User Story 5 - In-Chapter Content Personalization for Logged Users (Priority: P2)

**Goal**: Logged users can personalize chapter content with a button.

**Independent Test**: Logged-in user clicks a button in a chapter and sees the content change based on personalization settings.

### Implementation for User Story 5

- [ ] T054 [P] [US5] Implement `PersonalizationSetting` model in backend/src/models/personalization.py
- [ ] T055 [P] [US5] Implement FastAPI endpoint `PUT /user/{user_id}/personalization` for setting personalization in backend/src/api/personalization.py
- [ ] T056 [P] [US5] Implement FastAPI endpoint `GET /user/{user_id}/personalization` for retrieving settings in backend/src/api/personalization.py
- [ ] T057 [P] [US5] Implement FastAPI endpoint `GET /chapters/{chapter_id}/personalized_content` in backend/src/api/personalization.py
- [ ] T058 [US5] Create a Docusaurus component for "Personalize Chapter" button at start of chapters in `frontend/src/components/ChapterControls/PersonalizeButton.tsx`
- [ ] T059 [US5] Integrate "Personalize Chapter" button with chapter display in Docusaurus (e.g., via MDX or theme component swizzling) in `frontend/src/theme/DocItem/Content/index.js` (or similar)
- [ ] T060 [US5] Frontend logic to call personalization API and dynamically update chapter content in `frontend/src/hooks/usePersonalization.ts`

---

## Phase 8: User Story 6 - In-Chapter Content Translation to Urdu for Logged Users (Priority: P2)

**Goal**: Logged users can translate chapter content to Urdu with a button.

**Independent Test**: Logged-in user clicks a button in a chapter and sees the content translated to Urdu.

### Implementation for User Story 6

- [ ] T061 [P] [US6] Implement `TranslationCache` model in backend/src/models/translation.py
- [ ] T062 [P] [US6] Implement external translation service integration (e.g., Google Translate API) in backend/src/services/translation_service.py
- [ ] T063 [P] [US6] Implement FastAPI endpoint `GET /chapters/{chapter_id}/translated_content` in backend/src/api/translation.py
- [ ] T064 [US6] Create a Docusaurus component for "Translate to Urdu" button at start of chapters in `frontend/src/components/ChapterControls/TranslateButton.tsx`
- [ ] T065 [US6] Integrate "Translate to Urdu" button with chapter display in Docusaurus (e.g., via MDX or theme component swizzling) in `frontend/src/theme/DocItem/Content/index.js` (or similar)
- [ ] T066 [US6] Frontend logic to call translation API and dynamically update chapter content in `frontend/src/hooks/useTranslation.ts`

---

## Phase 9: User Story 7 - Reusable Intelligence via Claude Code Subagents and Agent Skills (Priority: P2)

**Goal**: Implement Claude Code Subagents/Agent Skills to enhance chatbot capabilities.

**Independent Test**: A specific chatbot query leverages a Claude Subagent/Skill and provides an enhanced or specialized response.

### Implementation for User Story 7

- [ ] T067 [P] [US7] Research specific use cases and integration patterns for Claude Code Subagents in Python (backend/src/services/claude_agent_integration.py)
- [ ] T068 [P] [US7] Develop a prototype Claude Code Subagent/Skill in backend/src/agents/claude_subagent.py
- [ ] T069 [US7] Integrate Claude Subagent/Skill output into the RAG service (`backend/src/services/rag_service.py`) for enhanced responses
- [ ] T070 [US7] Update chatbot interaction to potentially route specific queries to Claude Subagents in backend/src/services/chat_service.py

---

## Final Phase: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories.

- [ ] T071 [P] Implement Dockerfile for FastAPI backend deployment in backend/Dockerfile
- [ ] T072 [P] Configure CI/CD pipeline for backend (e.g., GitHub Actions) in `.github/workflows/backend_ci.yml`
- [ ] T073 [P] Configure CI/CD pipeline for frontend (e.g., GitHub Actions) in `.github/workflows/frontend_ci.yml`
- [ ] T074 Implement comprehensive end-to-end testing scenarios in `tests/e2e/`
- [ ] T075 Performance tuning for FastAPI endpoints and Qdrant queries
- [ ] T076 Security review of authentication, API endpoints, and data handling
- [ ] T077 Update project `README.md` with setup and deployment instructions
- [ ] T078 Finalize Docusaurus documentation for all new features

---

## Dependencies & Execution Order

### Phase Dependencies

-   **Setup (Phase 1)**: No dependencies - can start immediately.
-   **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories.
-   **User Stories (Phase 3-9)**: All depend on Foundational phase completion.
    -   User stories can then proceed in parallel (if staffed and dependencies are met).
    -   Or sequentially in priority order (P1 → P2).
-   **Polish (Final Phase)**: Depends on all desired user stories being complete.

### User Story Dependencies

-   **User Story 1 (RAG Chatbot Core)**: Can start after Foundational (Phase 2) - No dependencies on other stories.
-   **User Story 2 (Content-Aware QA)**: Depends on User Story 1 (RAG Chatbot Core) for the basic chat framework.
-   **User Story 3 (User Selected Text Query)**: Depends on User Story 2 (Content-Aware QA) for RAG capabilities.
-   **User Story 4 (User Authentication and Personalized Content)**: Can start after Foundational (Phase 2) - No dependencies on other user stories for its core functionality, but is a prerequisite for US5 and US6.
-   **User Story 5 (In-Chapter Content Personalization)**: Depends on User Story 4 (User Authentication and Personalized Content).
-   **User Story 6 (In-Chapter Content Translation)**: Depends on User Story 4 (User Authentication and Personalized Content).
-   **User Story 7 (Reusable Intelligence)**: Can be integrated incrementally after User Story 2, enhancing core RAG.

### Within Each User Story

-   Models before services.
-   Services before endpoints.
-   Core implementation before integration.
-   Story complete before moving to next priority.

### Parallel Opportunities

-   All Setup tasks marked `[P]` can run in parallel.
-   All Foundational tasks marked `[P]` can run in parallel (within Phase 2).
-   Once Foundational phase completes, User Stories can be worked on in parallel by different team members, respecting inter-story dependencies.
-   Within each User Story, tasks marked `[P]` can run in parallel.

---

## Parallel Example: User Story 1 (RAG Chatbot Core)

```bash
# Launch all model creation tasks for User Story 1 together:
- [ ] T020 [P] [US1] Create ChatSession model in backend/src/models/chat.py
- [ ] T021 [P] [US1] Create ChatMessage model in backend/src/models/chat.py

# Launch all backend endpoint creation tasks in parallel once services are ready:
- [ ] T023 [P] [US1] Implement FastAPI endpoint POST /chat/session in backend/src/api/chat.py
- [ ] T024 [P] [US1] Implement FastAPI endpoint GET /chat/session/{session_id} in backend/src/api/chat.py
- [ ] T025 [P] [US1] Implement FastAPI endpoint POST /chat/session/{session_id}/end in backend/src/api/chat.py
```

---

## Implementation Strategy

### MVP First (Core RAG Chatbot)

1.  Complete Phase 1: Setup
2.  Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3.  Complete Phase 3: User Story 1 (RAG Chatbot Core)
4.  Complete Phase 4: User Story 2 (Content-Aware QA)
5.  Complete Phase 5: User Story 3 (User Selected Text Query)
6.  **STOP and VALIDATE**: Test Core RAG Chatbot functionality independently.
7.  Deploy/demo if ready.

### Incremental Delivery (Adding Bonus Features)

1.  Complete Setup + Foundational → Foundation ready
2.  Add User Stories 1, 2, 3 → Core Chatbot MVP! → Test independently → Deploy/Demo
3.  Add User Story 4 (Authentication) → Test independently → Deploy/Demo
4.  Add User Story 5 (Personalization) → Test independently → Deploy/Demo
5.  Add User Story 6 (Translation) → Test independently → Deploy/Demo
6.  Add User Story 7 (Claude Intelligence) → Test independently → Deploy/Demo
7.  Each story adds value without breaking previous stories.

### Parallel Team Strategy

With multiple developers:

1.  Team completes Setup + Foundational together.
2.  Once Foundational is done:
    *   Developer A: User Story 1, 2, 3 (Core Chatbot)
    *   Developer B: User Story 4 (Authentication)
    *   Developer C: User Story 5 (Personalization)
    *   Developer D: User Story 6 (Translation)
    *   Developer E: User Story 7 (Claude Intelligence)
3.  Stories complete and integrate as per dependencies.

---

**Notes**

-   `[P]` tasks = different files, minimal dependencies within the immediate context.
-   `[Story]` label maps task to specific user story for traceability.
-   Each user story should be independently completable and testable where possible.
-   Tests are not explicitly included in the task list by default as per the prompt's instruction ("Tests are OPTIONAL: Only generate test tasks if explicitly requested in the feature specification or if user requests TDD approach"). If testing is required for specific tasks, it should be explicitly added.
-   Commit after each task or logical group.
-   Stop at any checkpoint to validate story independently.
-   Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence.
