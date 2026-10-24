"""The QA sampler never erases a round; the verdict converter only corrects what was sampled.

Scheduled audit account01/B16 (29 Sep 2026), B16-R13-QA-SAMPLE-RERUN-ERASES-COVERAGE-011:
rerunning a round overwrote its review file, so nodes it had covered became eligible again; an
unreadable review file was skipped silently; apply_verdicts accepted verdicts for nodes the review
never contained.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import pytest

from math_brain.models import GraphNode, NodeKind
from math_brain.store import ResearchStore

TOOLS = Path(__file__).resolve().parents[1] / "tools"


def _tool(name: str):
    spec = importlib.util.spec_from_file_location(f"tool_{name}", TOOLS / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _store(path: Path, count: int = 40) -> Path:
    with ResearchStore(path) as store:
        for i in range(count):
            store.add_node(GraphNode(f"n{i:03d}", NodeKind.CLAIM, f"Claim {i}",
                                     f"Statement number {i} of the fixture."))
        store.connection.commit()
    return path


@pytest.fixture
def sampler(tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
    qa = _tool("qa_sample")
    monkeypatch.setattr(qa, "STORE", _store(tmp_path / "brain.sqlite3"))
    monkeypatch.setattr(qa, "OUT", tmp_path / "qa")
    return qa


def _items(qa, round_no: int) -> list[str]:
    data = json.loads((qa.OUT / f"review_{round_no:03d}.json").read_text(encoding="utf-8"))
    return [item["node_id"] for item in data["items"]]


def test_a_same_rerun_changes_nothing(sampler) -> None:
    assert sampler.main(10, round_no=1) == 0
    before = (sampler.OUT / "review_001.json").read_bytes()
    assert sampler.main(10, round_no=1) == 0
    assert (sampler.OUT / "review_001.json").read_bytes() == before


def test_a_different_rerun_is_refused_and_the_round_kept(sampler) -> None:
    assert sampler.main(10, round_no=1) == 0
    before = (sampler.OUT / "review_001.json").read_bytes()
    assert sampler.main(5, round_no=1) == 2
    assert (sampler.OUT / "review_001.json").read_bytes() == before


def test_rounds_do_not_overlap(sampler) -> None:
    for r in (1, 2, 3):
        assert sampler.main(10, round_no=r) == 0
    seen = [nid for r in (1, 2, 3) for nid in _items(sampler, r)]
    assert len(seen) == 30 and len(set(seen)) == 30


def test_an_unreadable_review_is_an_error(sampler) -> None:
    sampler.OUT.mkdir(parents=True)
    (sampler.OUT / "review_009.json").write_text("{not json", encoding="utf-8")
    assert sampler.main(10, round_no=1) == 2
    assert not (sampler.OUT / "review_001.json").exists()


def test_verdicts_outside_the_review_are_refused(sampler, tmp_path: Path,
                                                 monkeypatch: pytest.MonkeyPatch) -> None:
    assert sampler.main(5, round_no=1) == 0
    review = sampler.OUT / "review_001.json"
    apply = _tool("apply_verdicts")
    monkeypatch.setattr(apply, "STORE", sampler.STORE)
    monkeypatch.setattr(apply, "INBOX", tmp_path / "inbox")
    (tmp_path / "inbox").mkdir()
    inside = _items(sampler, 1)[0]
    outside = next(f"n{i:03d}" for i in range(40) if f"n{i:03d}" not in _items(sampler, 1))
    verdicts = tmp_path / "verdicts.json"
    verdicts.write_text(json.dumps([{"node_id": inside, "verdict": "correct"},
                                    {"node_id": outside, "verdict": "wrong", "fix": "x" * 80}]),
                        encoding="utf-8")
    assert apply.main(str(verdicts), str(review), "t") == 2
    assert list((tmp_path / "inbox").iterdir()) == []
    verdicts.write_text(json.dumps([{"node_id": inside, "verdict": "correct"}]), encoding="utf-8")
    assert apply.main(str(verdicts), str(review), "t") == 0
    assert (tmp_path / "inbox" / "bundle_t.part").exists()


def test_a_correction_names_the_review_it_came_from(tmp_path: Path,
                                                   monkeypatch: pytest.MonkeyPatch) -> None:
    # account01/B18, B18-R13-QA-CORRECTION-BUNDLE-UNBOUND-TO-REVIEW-GENERATION-20260929: every
    # correction said "round 3" and one fixed revision string, whatever review it came from.
    import hashlib
    store = tmp_path / "brain.sqlite3"
    with ResearchStore(store) as s:
        s.add_node(GraphNode("n1", NodeKind.CLAIM, "Banach fixed point theorem",
                             "A contraction on a complete metric space has a unique fixed point.",
                             metadata={"logical_id": "math:wiki:banach-fixed-point",
                                       "claim_kind": "theorem", "proof_text": "Iterate."}))
        s.connection.commit()
    apply = _tool("apply_verdicts")
    monkeypatch.setattr(apply, "STORE", store)
    monkeypatch.setattr(apply, "INBOX", tmp_path / "inbox")
    (tmp_path / "inbox").mkdir()
    fix = ("A contraction T on a nonempty complete metric space has exactly one fixed point, "
           "the limit of the iterates from any start.")
    verdicts = tmp_path / "verdicts.json"
    verdicts.write_text(json.dumps([{"node_id": "n1", "verdict": "imprecise", "fix": fix}]),
                        encoding="utf-8")
    seen = {}
    for round_no, note in ((1, "first"), (2, "second")):
        review = tmp_path / f"review_{round_no:03d}.json"
        review.write_text(json.dumps({"note": note, "items": [{"node_id": "n1"}]}),
                          encoding="utf-8")
        assert apply.main(str(verdicts), str(review), f"r{round_no}") == 0
        part = tmp_path / "inbox" / f"bundle_r{round_no}.part"
        bundle = json.loads(part.read_text(encoding="utf-8"))
        entry = bundle["entries"][0]
        review_sha = hashlib.sha256(review.read_bytes()).hexdigest()[:16]
        verdict_sha = hashlib.sha256(verdicts.read_bytes()).hexdigest()[:16]
        assert entry["domain"] == f"QA-corrected (round {round_no}, audit-driven)"
        assert entry["source"]["revision"].endswith(
            f"-r{round_no}-review-{review_sha}-verdicts-{verdict_sha}")
        seen[round_no] = entry["source"]["revision"]
    assert seen[1] != seen[2]
