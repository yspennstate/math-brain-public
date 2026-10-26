from __future__ import annotations

import json

import pytest

from math_brain.models import Claim, ClaimKind, EdgeKind, GraphEdge
from math_brain.nightly import Queue, _main, digest, run
from math_brain.requests import RequestLedger
from math_brain.store import ResearchStore


def _store(path):
    with ResearchStore(path) as store:
        a = Claim("Every group of prime order is cyclic.", ClaimKind.THEOREM, id="claim_a")
        b = Claim("A cyclic group is abelian.", ClaimKind.THEOREM, id="claim_b")
        store.add_claim(a)
        store.add_claim(b)
    return a, b


def test_first_night_queues_proposals(tmp_path):
    _store(tmp_path / "s.sqlite")
    report = run(tmp_path / "s.sqlite", tmp_path / "q.jsonl", at="2026-10-01T03:00:00+00:00")
    assert report["changed"] and report["new"] and report["open"] == len(report["new"])
    kinds = {i.kind for i in Queue.load(tmp_path / "q.jsonl").items.values()}
    assert {"orphan_review", "missing_evidence"} <= kinds


def test_an_unchanged_store_leaves_the_queue_alone(tmp_path):
    _store(tmp_path / "s.sqlite")
    run(tmp_path / "s.sqlite", tmp_path / "q.jsonl", at="2026-10-01T03:00:00+00:00")
    size = (tmp_path / "q.jsonl").stat().st_size
    report = run(tmp_path / "s.sqlite", tmp_path / "q.jsonl", at="2026-10-02T03:00:00+00:00")
    assert not report["changed"] and report["new"] == []
    assert (tmp_path / "q.jsonl").stat().st_size == size
    assert "has not changed" in digest(Queue.load(tmp_path / "q.jsonl"), report)


def test_a_graph_change_retires_proposals_and_counts_nights(tmp_path):
    a, b = _store(tmp_path / "s.sqlite")
    run(tmp_path / "s.sqlite", tmp_path / "q.jsonl", at="2026-10-01T03:00:00+00:00")
    with ResearchStore(tmp_path / "s.sqlite") as store:
        store.add_edge(GraphEdge(b.id, a.id, EdgeKind.DEPENDS_ON, "b is used with a"))
    report = run(tmp_path / "s.sqlite", tmp_path / "q.jsonl", at="2026-10-02T03:00:00+00:00")
    assert report["changed"] and report["gone"]
    q = Queue.load(tmp_path / "q.jsonl")
    orphan = [i for i in q.items.values() if i.kind == "orphan_review"]
    assert orphan and all(not i.present and not i.open for i in orphan)
    missing = [i for i in q.items.values() if i.kind == "missing_evidence"]
    assert missing and all(i.nights_seen == 2 and i.open for i in missing)


def test_review_closes_a_proposal(tmp_path):
    _store(tmp_path / "s.sqlite")
    run(tmp_path / "s.sqlite", tmp_path / "q.jsonl")
    q = Queue.load(tmp_path / "q.jsonl")
    first = q.open_items()[0]
    q.review(first.id, "dismissed", "not worth an edge")
    again = Queue.load(tmp_path / "q.jsonl")
    assert first.id not in {i.id for i in again.open_items()}
    with pytest.raises(ValueError):
        again.review(first.id, "approved")
    with pytest.raises(KeyError):
        again.review("proposal_missing", "done")


def test_the_store_is_never_written(tmp_path):
    _store(tmp_path / "s.sqlite")
    with ResearchStore.open_read_only(tmp_path / "s.sqlite") as store:
        before = store.state_digest()
    run(tmp_path / "s.sqlite", tmp_path / "q.jsonl")
    with ResearchStore.open_read_only(tmp_path / "s.sqlite") as store:
        assert store.state_digest() == before


def test_requests_ride_along(tmp_path):
    _store(tmp_path / "s.sqlite")
    led = RequestLedger(tmp_path / "r.jsonl")
    led.ask("Is a group of prime order cyclic?", at="2026-01-01T00:00:00+00:00")
    report = run(tmp_path / "s.sqlite", tmp_path / "q.jsonl", requests_path=tmp_path / "r.jsonl")
    assert report["requests"]["stale"]
    assert "## Requests" in digest(Queue.load(tmp_path / "q.jsonl"), report)


def test_cli_run_writes_a_digest(tmp_path, capsys):
    _store(tmp_path / "s.sqlite")
    page = tmp_path / "dream" / "DIGEST.md"
    assert _main(["run", "--store", str(tmp_path / "s.sqlite"), "--queue", str(tmp_path / "q.jsonl"),
                  "--digest", str(page)]) == 0
    assert page.read_text(encoding="utf-8").startswith("# Nightly pass")
    rows = [json.loads(x) for x in (tmp_path / "q.jsonl").read_text(encoding="utf-8").splitlines()]
    assert rows[-1]["op"] == "night"
    capsys.readouterr()
    assert _main(["show", "--queue", str(tmp_path / "q.jsonl")]) == 0
    assert "proposal_" in capsys.readouterr().out


def test_request_links_reach_the_graph(tmp_path):
    a, _ = _store(tmp_path / "s.sqlite")
    led = RequestLedger(tmp_path / "r.jsonl")
    req = led.ask("Is a group of prime order cyclic?", at="2026-10-01T00:00:00+00:00")
    led.link(req.id, a.id, "produced", at="2026-10-01T01:00:00+00:00")
    plain = run(tmp_path / "s.sqlite", tmp_path / "q1.jsonl", requests_path=tmp_path / "r.jsonl")
    linked = run(tmp_path / "s.sqlite", tmp_path / "q2.jsonl", requests_path=tmp_path / "r.jsonl",
                 requests_in_graph=True)
    assert linked["nodes"] == plain["nodes"] + 1 and linked["edges"] == plain["edges"] + 1
    orphans = lambda q: {tuple(i.node_ids) for i in Queue.load(q).items.values() if i.kind == "orphan_review"}
    assert (a.id,) in orphans(tmp_path / "q1.jsonl") and (a.id,) not in orphans(tmp_path / "q2.jsonl")
    again = run(tmp_path / "s.sqlite", tmp_path / "q2.jsonl", requests_path=tmp_path / "r.jsonl",
                requests_in_graph=True)
    assert not again["changed"]


def test_digest_lists_open_requests_by_day(tmp_path):
    _store(tmp_path / "s.sqlite")
    led = RequestLedger(tmp_path / "r.jsonl")
    for i, day in enumerate(("2026-01-01", "2026-01-02", "2026-01-03")):
        led.ask(f"Open question number {i} about cyclic groups of prime order", at=f"{day}T00:00:00+00:00")
    report = run(tmp_path / "s.sqlite", tmp_path / "q.jsonl", requests_path=tmp_path / "r.jsonl")
    page = digest(Queue.load(tmp_path / "q.jsonl"), report, top=2)
    part = page.split("## Open requests by day", 1)[1]
    assert part.index("2026-01-03") < part.index("2026-01-02") and "2026-01-01" not in part
    assert "not started" in part and "and 1 more open" in part
