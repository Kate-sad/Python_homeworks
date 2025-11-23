import pytest
from sqlalchemy import create_engine
from sqlalchemy.sql import text

connection_string = "postgresql://postgres:072025@localhost:5432/QA"


@pytest.fixture(scope="module")
def db():
    engine = create_engine(connection_string)
    conn = engine.connect()
    yield conn
    conn.close()


def test_add_subject(db):
    new_id = 1001

    insert_stmt = text("INSERT INTO subject (subject_id, subject_title) "
                       "VALUES (:id, :title)")
    db.execute(insert_stmt, {"id": new_id, "title": "Test"})

    select_stmt = text("SELECT * FROM subject WHERE subject_id = :id")
    subject = db.execute(select_stmt, {"id": new_id}).fetchone()
    assert subject.subject_title == "Test"

    db.execute(text("DELETE FROM subject WHERE subject_id = :id"),
               {"id": new_id})


def test_edit_subject(db):
    new_id = 1002

    db.execute(text("INSERT INTO subject (subject_id, subject_title) "
                    "VALUES (:id, :title)"),
               {"id": new_id, "title": "History2"})

    db.execute(text("UPDATE subject SET subject_title = :new_title "
                    "WHERE subject_id = :id"),
               {"new_title": "World History", "id": new_id})

    subject = db.execute(text("SELECT * FROM subject WHERE subject_id = :id"),
                         {"id": new_id}).fetchone()
    assert subject.subject_title == "World History"

    db.execute(text("DELETE FROM subject WHERE subject_id = :id"),
               {"id": new_id})


def test_delete_subject(db):
    new_id = 1003

    db.execute(text("INSERT INTO subject (subject_id, subject_title) "
                    "VALUES (:id, :title)"),
               {"id": new_id, "title": "Physics2"})

    db.execute(text("DELETE FROM subject WHERE subject_id = :id"),
               {"id": new_id})

    subject = db.execute(text("SELECT * FROM subject WHERE subject_id = :id"),
                         {"id": new_id}).fetchone()
    assert subject is None
