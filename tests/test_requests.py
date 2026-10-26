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
