"""The review recorder: an agent's read lands as discovery evidence the hook can show, never as authority."""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

from math_brain.models import Claim, ClaimKind, EvidenceKind, NodeKind, EdgeKind, RecordStatus
from math_brain.store import ResearchStore
from math_brain.verification import decide_promotion

TOOL = Path(__file__).resolve().parents[1] / "tools" / "record_review.py"


def _load_tool():
    spec = importlib.util.spec_from_file_location("record_review", TOOL)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


@pytest.fixture()
def store(tmp_path: Path):
    with ResearchStore(tmp_path / "brain.sqlite3") as s:
        claim = Claim("If a_{m+n} <= a_m + a_n for all m, n then a_n/n converges to inf a_n/n", ClaimKind.LEMMA)
        s.add_claim(claim)
        yield s, claim


def test_agent_read_is_discovery_evidence_and_moves_no_status(store):
    s, claim = store
    rr = _load_tool()
    eid = rr.record_agent_read(s, claim.id, "agent-x", "sound", "read against Steele ch. 1", "statement and proof", ())
    assert eid
    rows = s.evidence_for(claim.id)
    assert len(rows) == 1 and rows[0].kind is EvidenceKind.DISCOVERY_REPORT and rows[0].passed
    assert rows[0].summary.startswith("read by agent-x: sound")
    node = s.get_node(eid)
    assert node is not None and node.kind is NodeKind.EVIDENCE
    edges = [e for e in s.iter_edges() if e.target_id == eid]
    assert edges and edges[0].kind is EdgeKind.SEMANTIC_ASSOCIATION
    # discovery evidence never promotes: the store's own policy says so
    decision = decide_promotion(claim, rows, target=RecordStatus.PROVISIONAL)
    assert not decision.allowed


def test_agent_read_is_idempotent(store):
    s, claim = store
    rr = _load_tool()
    first = rr.record_agent_read(s, claim.id, "agent-x", "sound", "read against Steele ch. 1", "statement", ())
    second = rr.record_agent_read(s, claim.id, "agent-x", "sound", "read against Steele ch. 1", "statement", ())
    assert first and second is None
    assert len(s.evidence_for(claim.id)) == 1


def test_unsound_read_is_recorded_as_not_passed(store):
    s, claim = store
    rr = _load_tool()
    rr.record_agent_read(s, claim.id, "agent-y", "gap", "the proof sketch skips the r < m remainder term", "proof", ("the statement itself was not disputed",))
    rows = s.evidence_for(claim.id)
    assert len(rows) == 1 and not rows[0].passed
    assert "remainder" in rows[0].summary and rows[0].limitations[-1].startswith("the statement itself")


def test_human_role_refuses_without_a_key(store, monkeypatch, tmp_path):
    s, claim = store
    rr = _load_tool()
    monkeypatch.setattr(rr, "HUMAN_KEY", tmp_path / "missing.key")
    with pytest.raises(SystemExit):
        rr.record_human_read(s, claim.id, "a human", "sound", "read", "statement", ())
    assert s.evidence_for(claim.id) == []
