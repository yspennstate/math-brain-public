from __future__ import annotations

import json
from datetime import UTC, datetime

import pytest

from math_brain.requests import LedgerError, RequestLedger, _main, normalize, redact, request_id


def test_same_ask_typed_twice_is_one_node(tmp_path):
    led = RequestLedger(tmp_path / "r.jsonl")
    a = led.ask("Is the mixing time polynomial?", at="2026-10-01T00:00:00+00:00")
    b = led.ask("is the  MIXING time polynomial", at="2026-10-03T00:00:00+00:00")
    assert a.id == b.id == request_id("is the mixing time polynomial")
    assert b.times_asked == 2
    assert b.first_asked.startswith("2026-10-01") and b.last_asked.startswith("2026-10-03")


def test_state_survives_reload(tmp_path):
    path = tmp_path / "r.jsonl"
    led = RequestLedger(path)
    rid = led.ask("Check Lemma 3").id
    led.link(rid, "claim_abc", "answered_by")
    again = RequestLedger(path)
    assert again.get(rid).status == "answered"
    assert again.for_node("claim_abc")[0][0] == "answered_by"


def test_reasking_an_answered_request_reopens_it(tmp_path):
    led = RequestLedger(tmp_path / "r.jsonl")
    rid = led.ask("Bound the spectral gap").id
    led.link(rid, "claim_1", "answered_by")
    assert led.ask("bound the spectral gap").status == "open"


def test_similar_finds_an_earlier_wording(tmp_path):
    led = RequestLedger(tmp_path / "r.jsonl")
    led.ask("Prove the spectral gap of the Glauber dynamics is bounded below")
    led.ask("Find a counterexample for the Ising perceptron capacity")
    hits = led.similar("spectral gap Glauber dynamics lower bound")
    assert hits and "Glauber" in hits[0][1].text
    assert all("perceptron" not in r.text for _, r in hits)


def test_threads_follow_both_ways(tmp_path):
    led = RequestLedger(tmp_path / "r.jsonl")
    a = led.ask("first", at="2026-10-01T00:00:00+00:00").id
    b = led.ask("second", follows=a, at="2026-10-02T00:00:00+00:00").id
    c = led.ask("third", follows=b, at="2026-10-03T00:00:00+00:00").id
    assert [r.id for r in led.thread(a)] == [a, b, c]
    assert [r.id for r in led.thread(c)] == [a, b, c]


def test_bad_input_is_refused(tmp_path):
    led = RequestLedger(tmp_path / "r.jsonl")
    with pytest.raises(LedgerError):
        led.ask("  ?! ")
    rid = led.ask("x y").id
    with pytest.raises(LedgerError):
        led.link(rid, "claim_1", "proves")
    with pytest.raises(LedgerError):
        led.link(rid, "claim_1", "follows")
    with pytest.raises(LedgerError):
        led.set_status("req_missing", "dropped")


def test_redaction_drops_addresses_and_home_paths():
    text = redact(r"see C:\Users\someone\notes.tex and /home/someone/x, mail a.b@example.org")
    assert "someone" not in text and "example.org" not in text
    assert normalize(text).count("home") == 2
    shouted = redact("SEE /USERS/SOMEONE/NOTES.TEX AND /Home/someone/x")  # a path typed in capitals is a path
    assert "someone" not in shouted.lower() and shouted.count("<home>") == 2


def test_a_torn_last_line_is_skipped(tmp_path):
    path = tmp_path / "r.jsonl"
    led = RequestLedger(path)
    led.ask("keep me")
    with path.open("a", encoding="utf-8") as fh:
        fh.write('{"op": "ask", "id": "req_x", "te')
    assert len(RequestLedger(path).requests) == 1


def test_consolidate_answers_reopens_and_lists_stale(tmp_path):
    led = RequestLedger(tmp_path / "r.jsonl")
    done = led.ask("will be verified", at="2026-10-01T00:00:00+00:00").id
    led.link(done, "claim_ok", "produced", at="2026-10-01T00:00:00+00:00")
    wrong = led.ask("answered wrongly", at="2026-10-01T00:00:00+00:00").id
    led.link(wrong, "claim_bad", "answered_by", at="2026-10-01T00:00:00+00:00")
    old = led.ask("nobody touched this", at="2026-09-01T00:00:00+00:00").id
    status = {"claim_ok": "verified", "claim_bad": "refuted"}
    out = led.consolidate(status_of=status.__getitem__, today=datetime(2026, 10, 20, tzinfo=UTC))
    assert out["answered"] == [done] and led.get(done).status == "answered"
    assert out["reopened"] == [wrong] and led.get(wrong).status == "open"
    assert old in out["stale"] and led.get(old).status == "open"


def test_cli_round_trip(tmp_path, capsys):
    path = str(tmp_path / "r.jsonl")
    assert _main(["--ledger", path, "ask", "Is the bound sharp?"]) == 0
    rid = capsys.readouterr().out.split()[0]
    assert _main(["--ledger", path, "link", rid, "claim_9", "answered_by"]) == 0
    assert _main(["--ledger", path, "node", "claim_9"]) == 0
    assert rid in capsys.readouterr().out
    rows = [json.loads(x) for x in open(path, encoding="utf-8")]
    assert [r["op"] for r in rows] == ["ask", "link"]


def test_consolidate_reports_a_status_it_cannot_read(tmp_path):
    led = RequestLedger(tmp_path / "r.jsonl")
    rid = led.ask("needs a status").id
    led.link(rid, "claim_x", "produced")

    def refuse(node):
        raise RuntimeError("persisted status must be recomputed")

    out = led.consolidate(status_of=refuse)
    assert out["answered"] == [] and led.get(rid).status == "open"
    assert out["unresolved"] and "claim_x" in out["unresolved"][0]


def test_consolidate_against_a_real_store(tmp_path):
    from math_brain.models import Claim, ClaimKind
    from math_brain.store import ResearchStore

    with ResearchStore(tmp_path / "brain.sqlite") as store:
        claim = Claim("Every group of prime order is cyclic.", ClaimKind.THEOREM)
        store.add_claim(claim)
        led = RequestLedger(tmp_path / "r.jsonl")
        rid = led.ask("Is a group of prime order cyclic?").id
        led.link(rid, claim.id, "produced")
        led.link(rid, "claim_never_written", "asks_about")
        led.link(rid, "claim_never_written", "produced")
        out = led.consolidate(status_of=store.current_status)
    assert led.get(rid).status == "open" and out["answered"] == []
    assert [u.split()[1].rstrip(":") for u in out["unresolved"]] == ["claim_never_written"]


def test_graph_is_deterministic_and_bridges_cards_to_requests(tmp_path):
    led = RequestLedger(tmp_path / "g.jsonl")
    a = led.ask("Is every group of prime order cyclic?", at="2026-10-03T09:00:00+00:00")
    b = led.ask("And is it abelian as well?", at="2026-10-04T09:00:00+00:00", follows=a.id)
    led.link(a.id, "claim_ab12", "produced", at="2026-10-03T10:00:00+00:00")
    led.link(a.id, "claim_ab12", "produced", at="2026-10-03T11:00:00+00:00")
    nodes, edges = led.graph()
    again_nodes, again_edges = RequestLedger(tmp_path / "g.jsonl").graph()
    assert [n.digest() for n in nodes] == [n.digest() for n in again_nodes]
    assert [e.digest() for e in edges] == [e.digest() for e in again_edges]
    proxy = {n.metadata["external_id"]: n.id for n in nodes}
    assert set(proxy) == {a.id, b.id}
    pairs = {(e.source_id, e.target_id) for e in edges}
    assert pairs == {("claim_ab12", proxy[a.id]), (proxy[b.id], proxy[a.id])}
    assert all(e.kind.value == "bridges_to" for e in edges)


def test_made_since_finds_the_card_made_after_the_ask(tmp_path):
    from math_brain.models import GraphNode, NodeKind

    led = RequestLedger(tmp_path / "m.jsonl")
    rid = led.ask("Is every group of prime order cyclic?", at="2026-10-03T09:00:00+00:00").id
    before = GraphNode("claim_old", NodeKind.CLAIM, "Every group of prime order is cyclic.",
                       created_at="2026-10-02T09:00:00+00:00")
    after = GraphNode("claim_new", NodeKind.CLAIM, "A group of prime order is cyclic, by Lagrange.",
                      created_at="2026-10-03T12:00:00")
    other = GraphNode("claim_walk", NodeKind.CLAIM, "The lamplighter walk on Z mixes slowly.",
                      created_at="2026-10-03T12:00:00+00:00")
    assert [n.id for _, n in led.made_since(rid, [before, after, other])] == ["claim_new"]
    led.link(rid, "claim_new", "produced")
    assert led.made_since(rid, [before, after, other]) == []
    with pytest.raises(LedgerError):
        led.made_since("req_nope", [after])


def test_cli_made_lists_and_links_store_nodes(tmp_path, capsys):
    from math_brain.models import Claim, ClaimKind
    from math_brain.store import ResearchStore

    ledger = str(tmp_path / "r.jsonl")
    rid = RequestLedger(ledger).ask("Is every group of prime order cyclic?", at="2026-01-01T00:00:00+00:00").id
    with ResearchStore(tmp_path / "b.sqlite") as store:
        claim = Claim("Every group of prime order is cyclic.", ClaimKind.THEOREM)
        store.add_claim(claim)
        store.add_claim(Claim("The lamplighter walk mixes in order n squared steps.", ClaimKind.THEOREM))
    assert _main(["--ledger", ledger, "made", rid, "--store", str(tmp_path / "b.sqlite"), "--link"]) == 0
    out = capsys.readouterr().out
    assert claim.id in out and "lamplighter" not in out and "(linked)" in out
    assert RequestLedger(ledger).get(rid).linked("produced") == [claim.id]


def test_import_prompts_keeps_real_asks_once(tmp_path):
    led = RequestLedger(tmp_path / "i.jsonl")
    rows = [
        {"ts": "2026-10-01T09:00:00Z", "text": "Is the mixing time of the lamplighter walk polynomial?", "origin": "owner"},
        {"ts": "2026-10-02T09:00:00Z", "text": "is the mixing time of the lamplighter walk polynomial"},
        {"ts": "2026-10-02T09:05:00Z", "text": "ok do it", "origin": "owner"},
        {"ts": "2026-10-02T10:00:00Z", "text": "Loop tick: check the mixing bound again", "origin": "automation"},
        {"ts": "not a time", "text": "Does the walk on the torus mix in n squared steps?"},
    ]
    got = led.import_prompts(rows)
    assert got == {"added": 1, "again": 1, "already": 0, "automation": 1, "short": 1, "unreadable": 1}
    (req,) = led.requests.values()
    assert req.times_asked == 2 and req.role == "researcher" and req.first_asked == "2026-10-01T09:00:00+00:00"
    again = RequestLedger(tmp_path / "i.jsonl").import_prompts(rows)
    assert again["added"] == again["again"] == 0 and again["already"] == 2
    assert RequestLedger(tmp_path / "i.jsonl").get(req.id).times_asked == 2
    auto = led.import_prompts(rows, automation=True)
    assert auto["added"] == 1 and len(led.requests) == 2


def test_cli_import_reads_a_prompt_archive(tmp_path, capsys):
    archive = tmp_path / "PROMPTS.jsonl"
    archive.write_text(json.dumps({"ts": "2026-10-01T09:00:00", "text": "Is every group of prime order cyclic?"})
                       + "\n{torn\n", encoding="utf-8")
    ledger = str(tmp_path / "r.jsonl")
    assert _main(["--ledger", ledger, "import", str(archive)]) == 0
    assert json.loads(capsys.readouterr().out)["added"] == 1
    assert len(RequestLedger(ledger).open_requests()) == 1


def test_backlog_groups_open_requests_by_day(tmp_path):
    led = RequestLedger(tmp_path / "r.jsonl")
    a = led.ask("Is the mixing time of the lamplighter walk polynomial?", at="2026-03-01T09:00:00+00:00")
    led.ask("Is the mixing time of the lamplighter walk polynomial?", at="2026-03-04T09:00:00+00:00")
    b = led.ask("Does every planar graph have a proper four colouring?", at="2026-03-01T15:00:00+00:00")
    c = led.ask("Is the spectral gap of the Glauber dynamics bounded below?", at="2026-03-03T09:00:00+00:00")
    led.link(c.id, "claim_x", "produced", at="2026-03-05T09:00:00+00:00")
    d = led.ask("Is every group of prime order cyclic?", at="2026-03-02T09:00:00+00:00")
    led.set_status(d.id, "answered")
    days = led.backlog(today=datetime(2026, 3, 10, 9, tzinfo=UTC))
    assert [day for day, _ in days] == ["2026-03-03", "2026-03-01"]
    first = days[1][1]
    assert [e["id"] for e in first] == [a.id, b.id]  # the request asked twice comes first
    assert first[0]["times_asked"] == 2 and first[0]["idle_days"] == 6 and first[0]["produced"] == 0
    assert days[0][1][0]["idle_days"] == 5 and days[0][1][0]["produced"] == 1
    recent = led.backlog(today=datetime(2026, 3, 10, 9, tzinfo=UTC), days=8)
    assert [day for day, _ in recent] == ["2026-03-03"]


def test_cli_backlog(tmp_path, capsys):
    path = tmp_path / "r.jsonl"
    RequestLedger(path).ask("Is the mixing time of the lamplighter walk polynomial?", at="2026-03-01T09:00:00+00:00")
    assert _main(["--ledger", str(path), "backlog"]) == 0
    out = capsys.readouterr().out
    assert out.startswith("2026-03-01 (1 open)") and "nothing produced" in out
