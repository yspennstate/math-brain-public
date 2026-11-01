"""The writable open refuses a database it must not initialize before writing anything to it.

Interactive audit IA-20260929-052554-02 (29 Sep 2026): the constructor turned on WAL, ran the
schema script and recorded version 1, and only then asked what version the file carried, so a newer
store it refused came back with WAL on, this build's tables added and a second version row. Each
refusal below is checked on the file itself afterwards - its bytes where the fixture is in
rollback-journal mode, its tables, version rows and journal mode otherwise - not on the exception
alone.
"""

from __future__ import annotations

import hashlib
import sqlite3
from pathlib import Path

import pytest

from math_brain.models import GraphNode, NodeKind
from math_brain.store import SCHEMA_SQL, STORE_SCHEMA_VERSION, ResearchStore, StoreSchemaError


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _state(path: Path) -> tuple:
    db = sqlite3.connect(path)
    try:
        tables = sorted(
            r[0] for r in db.execute("SELECT name FROM sqlite_master WHERE type = 'table'"))
        versions = (sorted(r[0] for r in db.execute("SELECT version FROM schema_meta"))
                    if "schema_meta" in tables else None)
        mode = db.execute("PRAGMA journal_mode").fetchone()[0]
    finally:
        db.close()
    return tables, versions, mode


def _fixture(path: Path, *statements: str) -> None:
    db = sqlite3.connect(path)
    try:
        for s in statements:
            db.execute(s)
        db.commit()
    finally:
        db.close()


FUTURE = STORE_SCHEMA_VERSION + 1


@pytest.mark.parametrize(
    "name, statements",
    [
        ("future version, schema_meta alone",
         ["CREATE TABLE schema_meta (version INTEGER PRIMARY KEY, applied_at TEXT)",
          f"INSERT INTO schema_meta(version) VALUES ({FUTURE})"]),
        ("future version sharing an old table name with other columns",
         ["CREATE TABLE schema_meta (version INTEGER PRIMARY KEY, applied_at TEXT)",
          f"INSERT INTO schema_meta(version) VALUES ({FUTURE})",
          "CREATE TABLE nodes (id TEXT PRIMARY KEY, payload BLOB NOT NULL)",
          "INSERT INTO nodes VALUES ('n1', x'00')"]),
        ("future version with tables this build does not know",
         ["CREATE TABLE schema_meta (version INTEGER PRIMARY KEY, applied_at TEXT)",
          f"INSERT INTO schema_meta(version) VALUES ({FUTURE})",
          "CREATE TABLE future_things (id TEXT PRIMARY KEY)"]),
        ("tables but no schema_meta",
         ["CREATE TABLE something_else (id INTEGER PRIMARY KEY, v TEXT)",
          "INSERT INTO something_else(v) VALUES ('kept')"]),
        ("a version that is not an integer",
         ["CREATE TABLE schema_meta (version TEXT, applied_at TEXT)",
          "INSERT INTO schema_meta(version) VALUES ('two')"]),
        ("no version row beside a table this build does not create",
         ["CREATE TABLE schema_meta (version INTEGER PRIMARY KEY, applied_at TEXT)",
          "CREATE TABLE future_things (id TEXT PRIMARY KEY)"]),
    ],
)
def test_refused_before_anything_is_written(
    tmp_path: Path, name: str, statements: list[str]
) -> None:
    path = tmp_path / "brain.sqlite3"
    _fixture(path, *statements)
    before_bytes, before_state = _sha(path), _state(path)
    assert before_state[2] == "delete"
    with pytest.raises(StoreSchemaError):
        ResearchStore(path)
    assert _sha(path) == before_bytes, name
    assert _state(path) == before_state, name
    assert not (tmp_path / "brain.sqlite3-wal").exists(), name


def test_future_version_in_wal_mode_keeps_its_tables_and_versions(tmp_path: Path) -> None:
    path = tmp_path / "brain.sqlite3"
    _fixture(path, "PRAGMA journal_mode = WAL",
             "CREATE TABLE schema_meta (version INTEGER PRIMARY KEY, applied_at TEXT)",
             f"INSERT INTO schema_meta(version) VALUES ({FUTURE})")
    before = _state(path)
    with pytest.raises(StoreSchemaError) as excinfo:
        ResearchStore(path)
    assert str(FUTURE) in str(excinfo.value)
    assert _state(path) == before == (["schema_meta"], [FUTURE], "wal")


def test_a_file_that_is_not_a_database_is_refused_unchanged(tmp_path: Path) -> None:
    path = tmp_path / "brain.sqlite3"
    path.write_bytes(b"this is not a SQLite database, it is a text file " * 40)
    before = _sha(path)
    with pytest.raises(StoreSchemaError):
        ResearchStore(path)
    assert _sha(path) == before


def test_a_new_path_and_an_empty_file_are_initialized(tmp_path: Path) -> None:
    for path in (tmp_path / "new" / "brain.sqlite3", tmp_path / "empty.sqlite3"):
        if path.name == "empty.sqlite3":
            path.write_bytes(b"")
        with ResearchStore(path) as store:
            store.add_node(GraphNode("n1", NodeKind.CLAIM, "A node", "The count is 1739."))
        tables, versions, mode = _state(path)
        assert "nodes" in tables and versions == [STORE_SCHEMA_VERSION] and mode == "wal"


def test_an_initialization_cut_off_before_the_version_row_is_finished(tmp_path: Path) -> None:
    # The schema script ran and the process died before the version row was committed: every
    # table is this build's own, schema_meta is empty. The next open completes the store.
    path = tmp_path / "brain.sqlite3"
    db = sqlite3.connect(path)
    db.executescript(SCHEMA_SQL)
    db.close()
    assert _state(path)[1] == []
    with ResearchStore(path) as store:
        store.add_node(GraphNode("n1", NodeKind.CLAIM, "A node", "The count is 1739."))
    assert _state(path)[1] == [STORE_SCHEMA_VERSION]


def test_an_existing_store_opens_with_its_rows(tmp_path: Path) -> None:
    path = tmp_path / "brain.sqlite3"
    with ResearchStore(path) as store:
        store.add_node(GraphNode("n1", NodeKind.CLAIM, "A node", "The count is 1739."))
        # an additive table another module keeps in the same store (provenance.py does this)
        store.connection.execute("CREATE TABLE claim_provenance (claim_id TEXT PRIMARY KEY)")
        store.connection.commit()
    with ResearchStore(path) as store:
        assert [n.id for n in store.iter_nodes()] == ["n1"]
    assert _state(path)[1] == [STORE_SCHEMA_VERSION]
