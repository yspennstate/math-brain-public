"""A stored mistake or reflex is read back only when its payload still matches its row.

The audit B15-R79-MISTAKE-REFLEX-PAYLOAD-DIGEST-NOT-ENFORCED-20260929-01 found that get_mistake and
get_reflex rebuilt the record from payload_json and compared nothing: a payload changed under its
old digest column read back as the changed record, and a reflex's payload could disagree with its
reflex_sources rows. Each case below changes one thing in the database and expects the getter to
refuse it.
"""

import json
import sqlite3
from pathlib import Path

import pytest

from math_brain.mistakes import MistakeKind, MistakeRecord, ReflexRecord
from math_brain.models import Claim, ClaimKind
from math_brain.store import ResearchStore


def _records() -> tuple[Claim, MistakeRecord, MistakeRecord, ReflexRecord]:
    claim = Claim("For x != 0, x / x = 1.", ClaimKind.THEOREM, id="claim_division")
    first = MistakeRecord(
        claim_id=claim.id,
        kind=MistakeKind.DOMAIN,
        failing_step="Used the identity at x = 0.",
        cause="The domain restriction was omitted.",
        repair_steps=("State x != 0 before cancelling x.",),
        prevention_action="Before cancellation, prove the factor is nonzero.",
        id="mistake_division",
    )
    second = MistakeRecord(
        claim_id=claim.id,
        kind=MistakeKind.DOMAIN,
        failing_step="Cancelled a factor that vanishes on a branch.",
        cause="The zero set of the factor was not checked.",
        repair_steps=("Split the branch where the factor vanishes.",),
        prevention_action="Write the zero set of every cancelled factor.",
        id="mistake_branch",
    )
    reflex = ReflexRecord(
        activation_cues=("cancellation",),
        action_steps=("Name the cancelled factor and check its zero set.",),
        required_evidence=("a proof that the current branch excludes zero",),
        stop_condition="Do not cancel until the nonzero condition is proved.",
        source_mistake_ids=(first.id,),
        id="reflex_division",
    )
    return claim, first, second, reflex


def _store(path: Path) -> tuple[MistakeRecord, ReflexRecord]:
    claim, first, second, reflex = _records()
    with ResearchStore(path) as store:
        store.add_claim(claim)
        store.add_mistake(first)
        store.add_mistake(second)
        store.add_reflex(reflex)
    return first, reflex


def _edit_payload(path: Path, table: str, row_id: str, **changes: object) -> None:
    db = sqlite3.connect(path)
    try:
        payload = json.loads(
            db.execute(f"SELECT payload_json FROM {table} WHERE id = ?", (row_id,)).fetchone()[0]
        )
        payload.update(changes)
        db.execute(
            f"UPDATE {table} SET payload_json = ? WHERE id = ?",
            (json.dumps(payload, sort_keys=True), row_id),
        )
        db.commit()
    finally:
        db.close()


def _execute(path: Path, sql: str, params: tuple = ()) -> None:
    db = sqlite3.connect(path)
    try:
        db.execute("PRAGMA foreign_keys = OFF")
        db.execute(sql, params)
        db.commit()
    finally:
        db.close()


def test_untouched_records_round_trip(tmp_path: Path) -> None:
    path = tmp_path / "brain.sqlite3"
    first, reflex = _store(path)
    with ResearchStore(path) as store:
        assert store.get_mistake(first.id) == first
        assert store.get_reflex(reflex.id) == reflex
        assert store.get_mistake("absent") is None
        assert store.get_reflex("absent") is None


@pytest.mark.parametrize(
    "changes",
    [
        {"cause": "A different cause."},
        {"repair_steps": ["A different repair."]},
        {"id": "mistake_other"},
        {"claim_id": "claim_other"},
        {"created_at": "2020-01-01T00:00:00+00:00"},
    ],
    ids=["cause", "repair_steps", "id", "claim_id", "created_at"],
)
def test_a_changed_mistake_payload_is_refused(tmp_path: Path, changes: dict) -> None:
    path = tmp_path / "brain.sqlite3"
    first, _ = _store(path)
    _edit_payload(path, "mistakes", first.id, **changes)
    with ResearchStore(path) as store:
        with pytest.raises(ValueError, match="stored mistake columns do not match its payload"):
            store.get_mistake(first.id)


def test_a_changed_mistake_digest_column_is_refused(tmp_path: Path) -> None:
    path = tmp_path / "brain.sqlite3"
    first, _ = _store(path)
    _execute(path, "UPDATE mistakes SET digest = ? WHERE id = ?", ("sha256:" + "0" * 64, first.id))
    with ResearchStore(path) as store:
        with pytest.raises(ValueError, match="stored mistake columns do not match its payload"):
            store.get_mistake(first.id)


@pytest.mark.parametrize(
    "changes",
    [
        {"required_evidence": ["no evidence at all"]},
        {"stop_condition": "Cancel freely."},
        {"activation_cues": ["anything"]},
        {"created_at": "2020-01-01T00:00:00+00:00"},
    ],
    ids=["required_evidence", "stop_condition", "activation_cues", "created_at"],
)
def test_a_changed_reflex_payload_is_refused(tmp_path: Path, changes: dict) -> None:
    path = tmp_path / "brain.sqlite3"
    _, reflex = _store(path)
    _edit_payload(path, "reflexes", reflex.id, **changes)
    with ResearchStore(path) as store:
        with pytest.raises(ValueError, match="stored reflex columns do not match its payload"):
            store.get_reflex(reflex.id)


def test_reflex_sources_in_the_payload_must_match_the_source_rows(tmp_path: Path) -> None:
    # The payload names a second mistake and its digest column is rewritten to match, so only
    # the reflex_sources rows disagree.
    path = tmp_path / "brain.sqlite3"
    first, reflex = _store(path)
    changed = ReflexRecord(
        activation_cues=reflex.activation_cues,
        action_steps=reflex.action_steps,
        required_evidence=reflex.required_evidence,
        stop_condition=reflex.stop_condition,
        source_mistake_ids=(first.id, "mistake_branch"),
        id=reflex.id,
        created_at=reflex.created_at,
    )
    from dataclasses import asdict

    from math_brain.models import canonical_json

    _execute(
        path,
        "UPDATE reflexes SET payload_json = ?, digest = ? WHERE id = ?",
        (canonical_json(asdict(changed)), changed.digest(), reflex.id),
    )
    with ResearchStore(path) as store:
        with pytest.raises(ValueError, match="stored reflex sources do not match its payload"):
            store.get_reflex(reflex.id)


@pytest.mark.parametrize("change", ["replace", "delete", "add"])
def test_a_changed_source_row_is_refused(tmp_path: Path, change: str) -> None:
    path = tmp_path / "brain.sqlite3"
    first, reflex = _store(path)
    if change == "replace":
        _execute(
            path,
            "UPDATE reflex_sources SET mistake_id = ? WHERE reflex_id = ?",
            ("mistake_branch", reflex.id),
        )
    elif change == "delete":
        _execute(path, "DELETE FROM reflex_sources WHERE reflex_id = ?", (reflex.id,))
    else:
        _execute(
            path,
            "INSERT INTO reflex_sources(reflex_id, mistake_id) VALUES (?, ?)",
            (reflex.id, "mistake_branch"),
        )
    with ResearchStore(path) as store:
        with pytest.raises(ValueError, match="stored reflex sources do not match its payload"):
            store.get_reflex(reflex.id)


def test_the_state_digest_seals_identities_and_the_getters_seal_content(tmp_path: Path) -> None:
    # The limitation the state digest documents: a payload-only change leaves it unchanged, and
    # the getter is where that change is refused.
    path = tmp_path / "brain.sqlite3"
    first, _ = _store(path)
    with ResearchStore(path) as store:
        before = store.state_digest()
    _edit_payload(path, "mistakes", first.id, cause="A different cause.")
    with ResearchStore(path) as store:
        assert store.state_digest() == before
        with pytest.raises(ValueError):
            store.get_mistake(first.id)
