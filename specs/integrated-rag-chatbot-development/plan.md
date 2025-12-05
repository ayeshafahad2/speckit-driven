# Implementation Plan: Integrated RAG Chatbot Development

**Branch**: `integrated-rag-chatbot-development` | **Date**: 2025-12-04 | **Spec**: `specs/integrated-rag-chatbot-development/spec.md`
**Input**: Feature specification from `specs/integrated-rag-chatbot-development/spec.md`

## Summary

This plan details the implementation of a Retrieval-Augmented Generation (RAG) chatbot embedded within a published book. The chatbot will leverage OpenAI Agents/ChatKit SDKs, FastAPI for the backend, Qdrant Cloud for vector embeddings, and Neon Serverless Postgres for structured data. Core functionality includes content-aware Q&A and user-selected text querying. Bonus features cover reusable intelligence with Claude Code Subagents, user authentication with Better-Auth.com for personalized content, in-chapter personalization, and Urdu translation.

## Technical Context

**Language/Version**: Python 3.11 (for FastAPI and Claude components), TypeScript/JavaScript (for Docusaurus frontend and ChatKit SDK integration).  
**Primary Dependencies**: OpenAI Agents/ChatKit SDKs, FastAPI, Qdrant Client (e.g., `qdrant-client` for Python), Neon Serverless Postgres Client (e.g., `psycopg2-binary` or `asyncpg` for Python), Better-Auth.com SDK/API, Docusaurus for frontend integration.  
**Storage**: Qdrant (vector embeddings of book content), Neon Serverless Postgres (user profiles, personalization settings, content metadata, chatbot conversation history).  
**Testing**: `pytest` (for FastAPI backend), `Jest`/`React Testing Library` (for Docusaurus frontend).  
**Target Platform**: Web (Docusaurus frontend), Server (FastAPI backend deployed on a cloud platform like AWS/GCP/Azure, or serverless functions), Cloud Services (Qdrant Cloud, Neon Postgres).  
**Project Type**: Web application (frontend + backend).  
**Performance Goals**:
*   Chatbot responses for basic queries: 3-5 seconds (P95).
*   Content Retrieval Latency from Qdrant: Sub-100ms (P95).
*   FastAPI endpoints: Efficient response times (<200ms for critical APIs).  
**Constraints**:
*   Utilize Qdrant Cloud Free Tier.
*   Integrate specifically with Better-Auth.com for authentication.
*   Seamless embedding of chatbot within the existing Docusaurus-based published book.
*   Adherence to Docusaurus platform architecture and conventions for frontend components.
*   Bonus features (Claude Subagents, personalization, translation) must be implemented to earn additional points.  
**Scale/Scope**: Target: 500 peak concurrent users, 1 published book, approximately 16 chapters (4 modules x ~4 chapters each).

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **Gate 1 (Content Source)**: Does the plan originate from the "Physical AI & Humanoid Robotics" syllabus? **YES**, the RAG chatbot is specifically designed to interact with the book's content.
- **Gate 2 (Modular Focus)**: Does the plan focus on a specific, prioritized module? **YES**, the plan is entirely focused on the "Integrated RAG Chatbot Development" feature, which is a distinct module.
- **Gate 3 (Verification)**: Does the plan include steps for verifying technical information using authoritative sources (per Principle III)? **RESOLVED**: Phase 0 Research addressed this by identifying and documenting research tasks for new technologies. The `research.md` artifact serves as the record of this verification process.
- **Gate 4 (Platform)**: Does the plan's proposed structure and implementation align with the Docusaurus platform? **YES**, the frontend part of the chatbot and personalization/translation will integrate with Docusaurus.
- **Gate 5 (Spec-Driven)**: Is there a corresponding `spec.md` that this plan is based on? **YES**, this plan is based on `specs/integrated-rag-chatbot-development/spec.md`.

## Project Structure

### Documentation (this feature)

```text
specs/integrated-rag-chatbot-development/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
# Option 2: Web application (when "frontend" + "backend" detected)
backend/
├── src/
│   ├── api/             # FastAPI application, endpoints, and routing
│   ├── services/        # Business logic, interaction with databases/external APIs (Qdrant, OpenAI, Better-Auth)
│   ├── models/          # Pydantic models for request/response, database schemas (SQLAlchemy/Pydantic for Postgres)
│   └── utils/           # Helper functions, common utilities
└── tests/               # Unit, integration, and API tests for backend

frontend/ # Docusaurus project root is already the frontend. We will integrate into the existing Docusaurus structure.
├── src/
│   ├── components/      # React components for chatbot UI, personalization/translation buttons
│   ├── pages/           # Docusaurus pages (e.g., chatbot page, user profile page)
│   ├── hooks/           # Custom React hooks for API interaction, state management
│   └── utils/           # Frontend utility functions
└── docs/                # Book content (Markdown files) which chatbot will query

# Additional top-level files for setup/configuration
├── requirements.txt     # Python dependencies for backend
├── pyproject.toml       # Backend project configuration
├── Dockerfile           # For deploying the FastAPI backend
├── .env.example         # Environment variables for backend/frontend configuration
```

**Structure Decision**: The project will utilize a split "Web application" structure with a FastAPI backend and the existing Docusaurus frontend. Backend components will reside in a `backend/` directory at the repository root. Frontend components for the chatbot, personalization, and translation features will integrate directly into the existing Docusaurus `src/` and `docs/` structure, adhering to Docusaurus conventions.

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| N/A       | N/A        | N/A                                 |
