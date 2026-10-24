"""An expansion sidecar reaches ranking only with the store generation it was built from (1000-page report D10-T05)."""
from __future__ import annotations

import pickle
import sqlite3

import pytest

from math_brain import retrieval as R

STORE_NEWEST = "2026-09-25T10:32:26.065029+00:00"


def _store(tmp_path, newest=STORE_NEWEST):
    path = tmp_path / "brain.sqlite3"
    db = sqlite3.connect(path)
    db.execute("CREATE TABLE nodes (id TEXT PRIMARY KEY, created_at TEXT NOT NULL)")
    db.executemany("INSERT INTO nodes VALUES (?, ?)",
                   [("n-old", "2026-09-01T08:00:00+00:00"), ("n-new", newest)])
    db.commit()
    db.close()
    return path


def _sidecar(store_path, generation, expansion=None):
    path = str(store_path) + ".expansion.pkl"
    payload = {"version": "expansion.v1", "expansion": expansion or {"n-old": "halfspace walsh coefficient"}}
    if generation is not None:
        payload["generation"] = generation
    with open(path, "wb") as fh:
        pickle.dump(payload, fh)
    return path


@pytest.fixture(autouse=True)
def _clean():
    R.EXPANSION.clear()
    R.EXPANSION_STATUS.clear()
    yield
    R.EXPANSION.clear()
    R.EXPANSION_STATUS.clear()


def test_same_generation_is_admitted(tmp_path):
    side = _sidecar(_store(tmp_path), STORE_NEWEST)
    assert R.load_expansion(side) == 1
    assert R.EXPANSION == {"n-old": "halfspace walsh coefficient"}
    assert R.EXPANSION_STATUS["admitted"] is True and R.EXPANSION_STATUS["lag_s"] == 0


def test_a_lag_inside_the_rebuild_window_is_admitted(tmp_path):
    side = _sidecar(_store(tmp_path), "2026-09-25T10:22:26.065029+00:00")
    assert R.load_expansion(side) == 1
    assert R.EXPANSION_STATUS["admitted"] is True
    assert R.EXPANSION_STATUS["lag_s"] == pytest.approx(600.0)


def test_a_sidecar_from_an_older_generation_is_refused(tmp_path):
    side = _sidecar(_store(tmp_path), "2026-09-22T10:32:26+00:00")
    assert R.load_expansion(side) == 0
    assert R.EXPANSION == {}
    assert R.EXPANSION_STATUS["admitted"] is False
    assert "lags" in R.EXPANSION_STATUS["reason"]


def test_a_sidecar_newer_than_the_store_is_refused(tmp_path):
    side = _sidecar(_store(tmp_path), "2026-09-29T19:17:11+00:00")
    assert R.load_expansion(side) == 0
    assert R.EXPANSION == {}
    assert "newer than the store" in R.EXPANSION_STATUS["reason"]


def test_a_refusal_drops_terms_an_earlier_load_admitted(tmp_path):
    store = _store(tmp_path)
    side = _sidecar(store, STORE_NEWEST, {"n-old": "first words"})
    assert R.load_expansion(side) == 1
    _sidecar(store, "2026-09-20T00:00:00+00:00", {"n-old": "stale words"})
    assert R.load_expansion(side) == 0
    assert R.EXPANSION == {}


def test_the_limit_is_a_dial(tmp_path, monkeypatch):
    side = _sidecar(_store(tmp_path), "2026-09-25T09:32:26.065029+00:00")
    monkeypatch.setattr(R, "EXPANSION_MAX_LAG_S", 1800.0)
    assert R.load_expansion(side) == 0
    monkeypatch.setattr(R, "EXPANSION_MAX_LAG_S", 7200.0)
    assert R.load_expansion(side) == 1


def test_a_sidecar_without_a_generation_is_admitted_as_unchecked(tmp_path):
    side = _sidecar(_store(tmp_path), None)
    assert R.load_expansion(side) == 1
    assert R.EXPANSION_STATUS["admitted"] is True
    assert R.EXPANSION_STATUS["reason"].startswith("unchecked")


def test_without_a_store_beside_it_the_sidecar_is_unchecked(tmp_path):
    side = tmp_path / "loose.expansion.pkl"
    with open(side, "wb") as fh:
        pickle.dump({"generation": STORE_NEWEST, "expansion": {"a": "b c"}}, fh)
    assert R.load_expansion(side) == 1
    assert R.EXPANSION_STATUS["store_generation"] is None
    assert R.EXPANSION_STATUS["reason"].startswith("unchecked")


def test_an_explicit_store_generation_is_used(tmp_path):
    side = _sidecar(_store(tmp_path), STORE_NEWEST)
    assert R.load_expansion(side, store_generation="2026-10-05T00:00:00+00:00") == 0
    assert R.load_expansion(side, store_generation=STORE_NEWEST) == 1


def test_different_unreadable_stamps_are_refused(tmp_path):
    side = _sidecar(_store(tmp_path), "build seven")
    assert R.load_expansion(side, store_generation="build eight") == 0
    assert R.EXPANSION_STATUS["reason"] == "unreadable generation stamp"
    assert R.load_expansion(side, store_generation="build seven") == 1


def test_an_unreadable_file_leaves_the_loaded_terms_alone(tmp_path):
    side = _sidecar(_store(tmp_path), STORE_NEWEST)
    assert R.load_expansion(side) == 1
    assert R.load_expansion(tmp_path / "missing.expansion.pkl") == 0
    assert R.EXPANSION == {"n-old": "halfspace walsh coefficient"}
