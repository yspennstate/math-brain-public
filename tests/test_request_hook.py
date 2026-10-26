from __future__ import annotations

import io
import json

from math_brain import request_hook
from math_brain.requests import RequestLedger


def _ledger(tmp_path):
    led = RequestLedger(tmp_path / "r.jsonl")
    req = led.ask("Is every group of prime order cyclic?", at="2026-10-03T09:00:00+00:00")
    led.link(req.id, "claim_ab12", "produced")
    led.set_status(req.id, "answered", "yes, by Lagrange")
    return req


def test_an_earlier_request_is_shown(tmp_path):
    req = _ledger(tmp_path)
    out = request_hook.run({"prompt": "is every group of prime order cyclic"},
                           {"MATH_BRAIN_REQUESTS": str(tmp_path / "r.jsonl")})
    assert req.id in out and "claim_ab12" in out and "answered" in out and "2026-10-03" in out


def test_silent_without_a_ledger_or_a_match(tmp_path):
    _ledger(tmp_path)
    assert request_hook.run({"prompt": "is every group of prime order cyclic"}, {}) == ""
    env = {"MATH_BRAIN_REQUESTS": str(tmp_path / "r.jsonl")}
    assert request_hook.run({"prompt": "bound the mixing time of the lamplighter walk"}, env) == ""
    assert request_hook.run({"prompt": "ok go on"}, env) == ""


def test_recording_happens_after_the_lookup(tmp_path):
    env = {"MATH_BRAIN_REQUESTS": str(tmp_path / "r.jsonl"), "MATH_BRAIN_REQUESTS_RECORD": "1"}
    assert request_hook.run({"prompt": "bound the mixing time of the lamplighter walk"}, env) == ""
    led = RequestLedger(tmp_path / "r.jsonl")
    assert len(led.requests) == 1
    again = request_hook.run({"prompt": "bound the mixing time of the lamplighter walk on Z"}, env)
    assert next(iter(led.requests)) in again


def test_codex_envelope_and_errors_are_silent(tmp_path, monkeypatch, capsys):
    _ledger(tmp_path)
    monkeypatch.setenv("MATH_BRAIN_REQUESTS", str(tmp_path / "r.jsonl"))
    monkeypatch.setattr("sys.stdin", io.StringIO(json.dumps({"prompt": "is every group of prime order cyclic"})))
    assert request_hook.main(["--codex"]) == 0
    env = json.loads(capsys.readouterr().out)
    assert "claim_ab12" in env["hookSpecificOutput"]["additionalContext"]
    monkeypatch.setattr("sys.stdin", io.StringIO("not json"))
    assert request_hook.main([]) == 0
    assert capsys.readouterr().out == ""
