"""The delivery audit reads its store read-only and says what it did not measure.

Interactive audits IA-20260929-052554-01 and IA-20260929-MB-05 (29 Sep 2026): the audit opened the
store with the writable constructor, so a mistyped path produced a brand-new empty store and an
audit that "passed" over zero nodes; and its one statistic covered only positive values of two or
more digits without saying so. These run the real entry point on missing, unsupported, unreadable,
empty, out-of-scope and populated stores.
"""

from __future__ import annotations

import json
import sqlite3
from pathlib import Path

import pytest

from math_brain import delivery_audit
from math_brain.delivery_audit import ASSERTED, main
from math_brain.models import GraphNode, NodeKind
from math_brain.rendering import render_parts
from math_brain.store import STORE_SCHEMA_VERSION, ResearchStore

Cap = pytest.CaptureFixture[str]

FILLER = ("This sentence is provenance and context that states no result of its own, and it runs "
          "long on purpose so that whatever follows it lands past the injection budget. ") * 3


def _nodes() -> list[GraphNode]:
    return [
        GraphNode("n_early", NodeKind.CLAIM, "Early value", "The count is exactly 1739. " + FILLER),
        GraphNode("n_late", NodeKind.CLAIM, "Late value", FILLER + "The count is exactly 2048."),
        GraphNode("n_prose", NodeKind.CLAIM, "Prose",
                  "Every bounded martingale converges almost surely."),
        GraphNode("n_small", NodeKind.CLAIM, "Small value", "The index of the operator is 3."),
        GraphNode("n_neg_late", NodeKind.CLAIM, "Late negative", FILLER + "The constant is -0.25."),
    ]


def _store(path: Path, nodes: list[GraphNode]) -> Path:
    with ResearchStore(path) as store:
        for n in nodes:
            store.add_node(n)
        store.connection.commit()
    return path


def _rows(path: Path) -> tuple:
    db = sqlite3.connect(path)
    try:
        tables = sorted(
            r[0] for r in db.execute("SELECT name FROM sqlite_master WHERE type = 'table'"))
        versions = sorted(r[0] for r in db.execute("SELECT version FROM schema_meta"))
        nodes = db.execute("SELECT * FROM nodes ORDER BY id").fetchall()
    finally:
        db.close()
    return tables, versions, nodes


def _run_json(capsys: Cap, *argv: str) -> tuple[int, dict]:
    code = main([*argv, "--json"])
    return code, json.loads(capsys.readouterr().out)


def test_the_fixture_premise_late_values_are_past_the_budget() -> None:
    by_id = {n.id: n for n in _nodes()}
    _, early = render_parts(by_id["n_early"], max_text_chars=320, query="")
    _, late = render_parts(by_id["n_late"], max_text_chars=320, query="")
    _, neg = render_parts(by_id["n_neg_late"], max_text_chars=320, query="")
    assert "1739" in early and "2048" not in late and "0.25" not in neg


# Exit codes: 0 measured, 2 cannot open, 3 empty store, 4 nothing in scope. The text-mode tests
# use only arguments the audit has always taken, so the same tests run against the code before this
# change.


def test_missing_store_fails_and_creates_nothing(tmp_path: Path) -> None:
    path = tmp_path / "no_such_dir" / "brain.sqlite3"
    assert main(["--store", str(path)]) == 2
    assert not path.exists() and not path.parent.exists()


def test_missing_store_json_status(tmp_path: Path, capsys: Cap) -> None:
    path = tmp_path / "no_such_dir" / "brain.sqlite3"
    code, out = _run_json(capsys, "--store", str(path))
    assert code == 2 and out["status"] == "STORE_MISSING"
    assert not path.exists()


def test_newer_schema_fails_without_writing(tmp_path: Path, capsys: Cap) -> None:
    path = _store(tmp_path / "brain.sqlite3", _nodes()[:1])
    db = sqlite3.connect(path)
    db.execute("INSERT INTO schema_meta(version) VALUES (?)", (STORE_SCHEMA_VERSION + 1,))
    db.commit()
    db.close()
    before = _rows(path)
    assert main(["--store", str(path)]) == 2
    assert _rows(path) == before
    code, out = _run_json(capsys, "--store", str(path))
    assert code == 2 and out["status"] == "STORE_UNSUPPORTED"
    assert _rows(path) == before


@pytest.mark.parametrize("kind", ["not a database", "a directory"])
def test_unreadable_store_fails(tmp_path: Path, capsys: Cap, kind: str) -> None:
    path = tmp_path / "brain.sqlite3"
    if kind == "a directory":
        path.mkdir()
    else:
        path.write_bytes(b"plain text, not SQLite " * 50)
    before = path.read_bytes() if path.is_file() else None
    assert main(["--store", str(path)]) == 2
    if before is not None:
        assert path.read_bytes() == before
    code, out = _run_json(capsys, "--store", str(path))
    assert code == 2 and out["status"] in {"STORE_UNSUPPORTED", "STORE_UNREADABLE"}


def test_empty_store_is_reported_as_empty(tmp_path: Path, capsys: Cap) -> None:
    path = _store(tmp_path / "brain.sqlite3", [])
    assert main(["--store", str(path)]) == 3
    assert "EMPTY" in capsys.readouterr().out
    code, out = _run_json(capsys, "--store", str(path))
    assert code == 3 and out["status"] == "EMPTY_STORE"
    assert out["population"]["nodes"] == 0 and out["asserted"]["rate"] is None


def test_store_with_no_value_in_scope(tmp_path: Path, capsys: Cap) -> None:
    path = _store(tmp_path / "brain.sqlite3", [_nodes()[2]])
    assert main(["--store", str(path)]) == 4
    capsys.readouterr()
    code, out = _run_json(capsys, "--store", str(path))
    assert code == 4 and out["status"] == "NONE_IN_SCOPE"
    assert out["not_evaluated"] == 1 and out["asserted"]["carrying"] == 0


def test_populated_store_is_measured_and_left_as_it_was(tmp_path: Path, capsys: Cap) -> None:
    path = _store(tmp_path / "brain.sqlite3", _nodes())
    before = _rows(path)
    code, out = _run_json(capsys, "--store", str(path))
    assert code == 0 and out["status"] == "MEASURED"
    # the main rate: 1739 arrives, 2048 is cut
    assert (out["asserted"]["carrying"], out["asserted"]["intact"]) == (2, 1)
    # the broad line: 1739, 2048, 3 and -0.25 are stated; 1739 and 3 arrive
    assert (out["broad"]["carrying"], out["broad"]["intact"]) == (4, 2)
    forms = out["broad"]["values_by_form"]
    assert forms["integer, one digit"] == {"stated": 1, "delivered": 1}
    assert forms["decimal"] == {"stated": 1, "delivered": 0}
    assert forms["signed (any form)"] == {"stated": 1, "delivered": 0}
    assert out["not_evaluated"] == 1 and out["population"]["nodes"] == 5
    assert _rows(path) == before


def test_population_digest_names_the_population(tmp_path: Path, capsys: Cap) -> None:
    path = _store(tmp_path / "brain.sqlite3", _nodes()[:2])
    _, first = _run_json(capsys, "--store", str(path))
    _, again = _run_json(capsys, "--store", str(path))
    assert first["population"]["digest"] == again["population"]["digest"]
    with ResearchStore(path) as store:
        store.add_node(_nodes()[3])
        store.connection.commit()
    _, grown = _run_json(capsys, "--store", str(path))
    assert grown["population"]["digest"] != first["population"]["digest"]


def test_text_output_says_what_it_did_not_measure(tmp_path: Path, capsys: Cap) -> None:
    path = _store(tmp_path / "brain.sqlite3", _nodes())
    assert main(["--store", str(path)]) == 0
    text = capsys.readouterr().out
    assert "1/2 = 0.500" in text
    assert "scope:" in text and "not evaluated" in text and "2/4 = 0.500" in text


def test_the_asserted_pattern_is_unchanged() -> None:
    # Every earlier run's number was produced by this exact pattern; the broad line is separate.
    assert ASSERTED.pattern == (
        r"(?:\b(?:is|are|was|were|equals?|gives?|yields?|returns?)\s+"
        r"(?:exactly\s+|precisely\s+)?|=\s*)(\d{2,}(?:\.\d+)?)(?!\d)")


@pytest.mark.parametrize(
    "sentence, values",
    [
        ("The count is exactly 1739.", ["1739"]),
        ("The count is -1739.", ["-1739"]),
        ("The dimension is 3.", ["3"]),
        ("The probability is 0.25 here.", ["0.25"]),
        ("The error is 1e-10.", ["1e-10"]),
        ("The ratio equals 1/2.", ["1/2"]),
        ("The rate is 3 \u00d7 10^-4.", ["3 \u00d7 10^-4"]),
        ("The variance is at most 5.", ["5"]),
        ("so that \u03c3 \u2264 2", ["2"]),
        ("with x \u2212 y = \u22121", ["\u22121"]),
        ("and p >= 0.5 always", ["0.5"]),
        ("It was published in 2019 by the same group.", []),
        ("See arXiv:2103.01234 for details.", []),
        ("whenever x != 3 we stop", []),
        ("the map x -> 3 is constant", []),
        ("Theorem 3 holds for every n.", []),
        ("The winner is 3rd in the list.", []),
        ("The bound is O(n log n).", []),
    ],
)
def test_broad_pattern_contract(sentence: str, values: list[str]) -> None:
    assert delivery_audit.BROAD.findall(sentence) == values
