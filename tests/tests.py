import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.models import Base
from database import get_db


@pytest.fixture(scope="function")
def db_session(tmpdir):
    db_file = tmpdir.join("test.db")
    DATABASE_URL = f"sqlite:///{db_file}"
    engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
    Base.metadata.create_all(bind=engine)
    print(engine)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    yield SessionLocal()
    engine.dispose()
    db_file.remove()


@pytest.fixture(scope="function")
def test_app(db_session):
    from app.main import app

    def override_get_db():
        yield db_session

    app.dependency_overrides = {
        get_db: override_get_db
    }

    yield TestClient(app)
