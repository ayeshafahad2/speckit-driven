import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Import models and Base from your application
from backend.src.database import Base, get_db
from backend.src.main import app as fastapi_app

# --- Database Fixtures ---
# Use a separate test database or an in-memory SQLite for tests
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="session")
def db_engine():
    """Provides a SQLAlchemy engine for the test database."""
    Base.metadata.create_all(bind=engine) # Create tables
    yield engine
    Base.metadata.drop_all(bind=engine) # Drop tables after tests

@pytest.fixture(scope="function")
def db_session(db_engine):
    """Provides a transactional session for each test."""
    connection = db_engine.connect()
    transaction = connection.begin()
    session = TestingSessionLocal(bind=connection)
    yield session
    session.close()
    transaction.rollback()
    connection.close()

# --- FastAPI Test Client Fixture ---
@pytest.fixture(scope="module")
def client(db_session):
    """Provides a test client for FastAPI application."""
    def override_get_db():
        yield db_session
    
    fastapi_app.dependency_overrides[get_db] = override_get_db
    with TestClient(fastapi_app) as c:
        yield c
    fastapi_app.dependency_overrides.clear()
